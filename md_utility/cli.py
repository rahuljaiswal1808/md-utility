import click
from md_utility.commands.convert import to_pdf
from md_utility.commands.to_docx import to_docx


@click.group()
@click.version_option("1.0.0", prog_name="mdu")
def main():
    """A CLI utility for working with Markdown files."""


main.add_command(to_pdf)
main.add_command(to_docx)
