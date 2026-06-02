import click
from md_utility.commands.convert import to_pdf


@click.group()
@click.version_option("1.0.0", prog_name="mdu")
def main():
    """A CLI utility for working with Markdown files."""


main.add_command(to_pdf)
