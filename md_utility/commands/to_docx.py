import os
import sys
import click
import pypandoc


@click.command("to-docx")
@click.argument("input", type=click.Path(exists=True, dir_okay=False))
@click.option("-o", "--output", default=None, help="Output DOCX file path.")
@click.option("--reference-doc", default=None, type=click.Path(exists=True, dir_okay=False), help="Path to a reference .docx for styles/formatting.")
def to_docx(input, output, reference_doc):
    """Convert a Markdown file to DOCX."""
    if not input.lower().endswith(".md"):
        click.echo(f"Error: input file must be a .md file: {input}", err=True)
        sys.exit(1)

    if output is None:
        base = os.path.splitext(input)[0]
        output = base + ".docx"

    extra_args = []
    if reference_doc:
        extra_args.append(f"--reference-doc={reference_doc}")

    click.echo(f"Converting {input} → {output}")

    try:
        pypandoc.convert_file(input, "docx", outputfile=output, extra_args=extra_args)
        click.echo(f"Done! DOCX saved to: {output}")
    except Exception as err:
        click.echo(f"Conversion failed: {err}", err=True)
        sys.exit(1)
