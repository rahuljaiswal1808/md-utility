# md-utility (`mdu`)

A CLI utility for working with Markdown files.

## Installation

```bash
pip install -e .
```

## Commands

### `mdu to-pdf` — Convert Markdown to PDF

```bash
mdu to-pdf <input.md> [OPTIONS]
```

**Options:**

| Option | Default | Description |
|---|---|---|
| `-o, --output <path>` | `<input>.pdf` | Output PDF file path |
| `--paper-format <format>` | `A4` | Paper size: A3, A4, A5, Letter, Legal |
| `--landscape` | off | Use landscape orientation |
| `--margin <value>` | `20mm` | Page margin, e.g. `15mm`, `1cm` |
| `--style <file.css>` | built-in | Path to a custom CSS file |

**Examples:**

```bash
# Basic conversion — outputs README.pdf in the same directory
mdu to-pdf README.md

# Custom output path
mdu to-pdf README.md -o docs/output.pdf

# Letter size, landscape, tighter margins
mdu to-pdf README.md --paper-format Letter --landscape --margin 15mm

# Custom stylesheet
mdu to-pdf README.md --style my-theme.css
```
