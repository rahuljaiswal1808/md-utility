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

### `mdu to-docx` — Convert Markdown to DOCX

```bash
mdu to-docx <input.md> [OPTIONS]
```

**Options:**

| Option | Default | Description |
|---|---|---|
| `-o, --output <path>` | `<input>.docx` | Output DOCX file path |
| `--reference-doc <file.docx>` | Word default | Reference .docx to inherit styles from |

**Examples:**

```bash
# Basic conversion — outputs README.docx in the same directory
mdu to-docx README.md

# Custom output path
mdu to-docx README.md -o docs/output.docx

# Apply styles from an existing Word document
mdu to-docx README.md --reference-doc my-template.docx
```
