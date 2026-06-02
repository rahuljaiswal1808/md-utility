import os
import sys
import click
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


PAGE_CSS_TEMPLATE = "@page {{ margin: {margin}; size: {paper_format} {orientation}; }}\n"

BASE_CSS = """
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 14px;
    line-height: 1.6;
    color: #24292e;
    max-width: 860px;
    margin: 0 auto;
    padding: 0 20px;
}

h1, h2, h3, h4, h5, h6 {
    margin-top: 24px;
    margin-bottom: 16px;
    font-weight: 600;
    line-height: 1.25;
    color: #1b1f23;
}

h1 { font-size: 2em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
h2 { font-size: 1.5em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }

a { color: #0366d6; text-decoration: none; }

code {
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 85%;
    background-color: #f6f8fa;
    padding: 0.2em 0.4em;
    border-radius: 3px;
}

pre {
    background-color: #f6f8fa;
    padding: 16px;
    border-radius: 6px;
    overflow-x: auto;
    line-height: 1.45;
}

pre code {
    background: none;
    padding: 0;
    font-size: 100%;
}

blockquote {
    margin: 0;
    padding: 0 1em;
    color: #6a737d;
    border-left: 4px solid #dfe2e5;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 16px;
}

th, td {
    border: 1px solid #dfe2e5;
    padding: 6px 13px;
}

th { background-color: #f6f8fa; font-weight: 600; }
tr:nth-child(even) { background-color: #f6f8fa; }

img { max-width: 100%; }

hr { border: none; border-top: 1px solid #eaecef; margin: 24px 0; }
"""


@click.command("to-pdf")
@click.argument("input", type=click.Path(exists=True, dir_okay=False))
@click.option("-o", "--output", "output", default=None, help="Output PDF file path.")
@click.option("--style", "style", default=None, type=click.Path(exists=True, dir_okay=False), help="Path to a custom CSS file.")
@click.option("--paper-format", default="A4", show_default=True, help="Paper size: A3, A4, A5, Letter, Legal.")
@click.option("--landscape", is_flag=True, default=False, help="Use landscape orientation.")
@click.option("--margin", default="20mm", show_default=True, help="Page margin, e.g. 20mm or 1cm.")
def to_pdf(input, output, style, paper_format, landscape, margin):
    """Convert a Markdown file to PDF."""
    if not input.lower().endswith(".md"):
        click.echo(f"Error: input file must be a .md file: {input}", err=True)
        sys.exit(1)

    if output is None:
        base = os.path.splitext(input)[0]
        output = base + ".pdf"

    orientation = "landscape" if landscape else "portrait"

    if style:
        with open(style) as f:
            css_content = PAGE_CSS_TEMPLATE.format(
                margin=margin, paper_format=paper_format, orientation=orientation
            ) + f.read()
    else:
        css_content = PAGE_CSS_TEMPLATE.format(
            margin=margin, paper_format=paper_format, orientation=orientation
        ) + BASE_CSS

    with open(input, encoding="utf-8") as f:
        md_content = f.read()

    md = markdown.Markdown(extensions=["extra", "codehilite", "toc", "tables"])
    body_html = md.convert(md_content)

    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body>{body_html}</body>
</html>"""

    click.echo(f"Converting {input} → {output}")

    font_config = FontConfiguration()
    css = CSS(string=css_content, font_config=font_config)
    HTML(string=html, base_url=os.path.dirname(os.path.abspath(input))).write_pdf(
        output,
        stylesheets=[css],
        font_config=font_config,
    )

    click.echo(f"Done! PDF saved to: {output}")
