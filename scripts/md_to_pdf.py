#!/usr/bin/env python3
"""Convert THESIS.md + refs/references.md to a print CSS HTML file, then PDF via Chrome."""
from __future__ import annotations

import html
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_PATH = ROOT / "THESIS.md"
REFS_PATH = ROOT / "refs" / "references.md"
PDF_PATH = ROOT / "THESIS.pdf"
HTML_PATH = ROOT / "THESIS.html"


def inline_format(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2">\1</a>',
        text,
    )
    return text


def latex_to_plain(body: str) -> str:
    body = body.replace("\n", " ")
    repl = [
        (r"\\qquad", "    "),
        (r"\\mathrm\{primary\}", "primary"),
        (r"\\mathbf\{1\}", "1"),
        (r"\\mathbb\{R\}", "ℝ"),
        (r"\\partial_t", "∂t"),
        (r"\\partial_x", "∂x"),
        (r"\\dot\{\s*T\s*\}", "Ṫ"),
        (r"\\dot T", "Ṫ"),
        (r"\\geqslant", "≥"),
        (r"\\geq", "≥"),
        (r"\\ge", "≥"),
        (r"\\leq", "≤"),
        (r"\\le", "≤"),
        (r"\\neq", "≠"),
        (r"\\in", "∈"),
        (r"\\ldots", "…"),
        (r"\\dots", "…"),
        (r"\\infty", "∞"),
        (r"\\inf", "inf"),
        (r"\\max", "max"),
        (r"\\sum", "Σ"),
        (r"\\varphi", "φ"),
        (r"\\Phi", "Φ"),
        (r"\\sigma", "σ"),
        (r"\\lambda", "λ"),
        (r"\\theta", "θ"),
        (r"\\alpha", "α"),
        (r"\\tau", "τ"),
        (r"\\pi", "π"),
        (r"\\mu", "μ"),
        (r"\\bigl", ""),
        (r"\\bigr", ""),
        (r"\\, ", " "),
        (r"\\,", " "),
    ]
    for pat, sub in repl:
        body = re.sub(pat, sub, body)
    body = body.replace(r"\{", "{").replace(r"\}", "}")
    body = re.sub(r"_\{([^}]+)\}", r"_\1", body)
    body = re.sub(r"\^\{([^}]+)\}", r"^\1", body)
    body = re.sub(r"\s+", " ", body).strip()
    return body


def convert_math(text: str) -> str:
    def disp(m: re.Match[str]) -> str:
        return "\n\n**" + latex_to_plain(m.group(1)) + "**\n\n"

    def inl(m: re.Match[str]) -> str:
        return latex_to_plain(m.group(1))

    text = re.sub(r"\$\$([\s\S]+?)\$\$", disp, text)
    text = re.sub(r"\\\[([\s\S]+?)\\\]", disp, text)
    text = re.sub(r"\\\((.+?)\\\)", inl, text)
    return text


def md_to_html_body(src: str) -> str:
    src = convert_math(src)
    lines = src.splitlines()
    out: list[str] = []
    i = 0
    in_code = False
    in_table = False
    table_rows: list[str] = []
    para: list[str] = []

    def flush_para() -> None:
        nonlocal para
        if para:
            out.append("<p>" + inline_format(" ".join(para)) + "</p>")
            para = []

    def flush_table() -> None:
        nonlocal in_table, table_rows
        if not table_rows:
            in_table = False
            return
        rows = []
        for raw in table_rows:
            cells = [c.strip() for c in raw.strip().strip("|").split("|")]
            rows.append(cells)
        if len(rows) >= 2 and all(re.match(r"^:?-+:?$", c or "") for c in rows[1]):
            header, body = rows[0], rows[2:]
        else:
            header, body = None, rows
        html_rows = ["<table>"]
        if header:
            html_rows.append(
                "<thead><tr>"
                + "".join(f"<th>{inline_format(c)}</th>" for c in header)
                + "</tr></thead>"
            )
        html_rows.append("<tbody>")
        for r in body:
            html_rows.append(
                "<tr>" + "".join(f"<td>{inline_format(c)}</td>" for c in r) + "</tr>"
            )
        html_rows.append("</tbody></table>")
        out.extend(html_rows)
        table_rows = []
        in_table = False

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            flush_para()
            flush_table()
            in_code = not in_code
            if in_code:
                out.append("<pre><code>")
            else:
                out.append("</code></pre>")
            i += 1
            continue
        if in_code:
            out.append(html.escape(line))
            i += 1
            continue
        if line.startswith("|"):
            flush_para()
            in_table = True
            table_rows.append(line)
            i += 1
            continue
        if in_table:
            flush_table()
        if line.startswith("---") and set(line.strip()) <= {"-", " "}:
            flush_para()
            out.append("<hr/>")
            i += 1
            continue
        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            flush_para()
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline_format(heading.group(2))}</h{level}>")
            i += 1
            continue
        ol = re.match(r"^(\d+)\.\s+(.*)$", line)
        if ol:
            flush_para()
            items = [ol.group(2)]
            i += 1
            while i < len(lines):
                m = re.match(r"^\d+\.\s+(.*)$", lines[i])
                if not m:
                    break
                items.append(m.group(1))
                i += 1
            out.append(
                "<ol>" + "".join(f"<li>{inline_format(x)}</li>" for x in items) + "</ol>"
            )
            continue
        ul = re.match(r"^[-*]\s+(.*)$", line)
        if ul:
            flush_para()
            items = [ul.group(1)]
            i += 1
            while i < len(lines):
                m = re.match(r"^[-*]\s+(.*)$", lines[i])
                if not m:
                    break
                items.append(m.group(1))
                i += 1
            out.append(
                "<ul>" + "".join(f"<li>{inline_format(x)}</li>" for x in items) + "</ul>"
            )
            continue
        if not line.strip():
            flush_para()
            i += 1
            continue
        para.append(line.strip())
        i += 1
    flush_para()
    flush_table()
    return "\n".join(out)


CSS = """
@page { size: A4; margin: 22mm 20mm 24mm 20mm; }
html, body { font-family: "Liberation Serif", "Times New Roman", Times, serif;
  font-size: 11pt; line-height: 1.38; color: #111; }
h1 { font-size: 16pt; line-height: 1.25; margin: 0 0 12pt; }
h2 { font-size: 13pt; margin: 16pt 0 8pt; page-break-after: avoid; }
h3 { font-size: 11.5pt; margin: 12pt 0 6pt; page-break-after: avoid; }
p { margin: 0 0 8pt; text-align: justify; hyphens: auto; }
code { font-family: "Liberation Mono", Consolas, monospace; font-size: 9.5pt; }
pre { background: #f4f4f4; padding: 8pt; font-size: 9pt; white-space: pre-wrap; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0 12pt;
  font-size: 9.5pt; page-break-inside: avoid; }
th, td { border: 1px solid #444; padding: 3pt 5pt; vertical-align: top; }
th { background: #eee; text-align: left; }
hr { border: 0; border-top: 1px solid #888; margin: 14pt 0; }
a { color: #000; text-decoration: none; }
.banner { font-size: 9.5pt; color: #333; margin-bottom: 10pt; }
.math-display { margin: 10pt 0; text-align: center; }
"""

HTML_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>Thesis #5 — Metastasis as Stochastic Spreading on Anatomical Graphs</title>
<style>__CSS__</style>
</head>
<body>
<div class="banner">Thesis #5 working manuscript · computational research only · not a medical device · no document DOI</div>
__BODY__
</body>
</html>
"""


def main() -> None:
    thesis = MD_PATH.read_text(encoding="utf-8")
    refs = REFS_PATH.read_text(encoding="utf-8")
    # Drop the refs file's own H1; the thesis already points to it.
    refs_body = re.sub(r"^# .*\n+", "", refs, count=1)
    body = md_to_html_body(thesis) + "\n" + md_to_html_body("## References\n\n" + refs_body)
    html_doc = HTML_TMPL.replace("__CSS__", CSS).replace("__BODY__", body)
    HTML_PATH.write_text(html_doc, encoding="utf-8")

    chrome = "google-chrome"
    cmd = [
        "timeout",
        "-k",
        "2",
        "20",
        chrome,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-first-run",
        "--disable-background-networking",
        "--disable-sync",
        "--disable-extensions",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_PATH}",
        HTML_PATH.resolve().as_uri(),
    ]
    subprocess.run(cmd, check=False)
    HTML_PATH.unlink(missing_ok=True)
    if not PDF_PATH.exists() or PDF_PATH.stat().st_size < 1000:
        raise SystemExit("PDF was not produced")


if __name__ == "__main__":
    main()
