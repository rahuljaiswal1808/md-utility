import { mdToPdf } from 'md-to-pdf';
import { existsSync, readFileSync } from 'fs';
import { resolve, dirname, basename, extname } from 'path';

export async function convert(input, options) {
  const inputPath = resolve(input);

  if (!existsSync(inputPath)) {
    console.error(`Error: File not found: ${inputPath}`);
    process.exit(1);
  }

  if (extname(inputPath).toLowerCase() !== '.md') {
    console.error(`Error: Input file must be a Markdown file (.md): ${inputPath}`);
    process.exit(1);
  }

  const outputPath = options.output
    ? resolve(options.output)
    : resolve(dirname(inputPath), basename(inputPath, '.md') + '.pdf');

  const config = {
    dest: outputPath,
    launch_options: {
      args: ['--no-sandbox', '--disable-setuid-sandbox'],
    },
    pdf_options: {
      format: options.paperFormat,
      landscape: options.landscape || false,
      margin: {
        top: options.margin,
        right: options.margin,
        bottom: options.margin,
        left: options.margin,
      },
    },
    highlight_style: options.highlightStyle,
  };

  if (options.style) {
    const stylePath = resolve(options.style);
    if (!existsSync(stylePath)) {
      console.error(`Error: CSS file not found: ${stylePath}`);
      process.exit(1);
    }
    config.css = readFileSync(stylePath, 'utf8');
  }

  console.log(`Converting ${inputPath} → ${outputPath}`);

  try {
    await mdToPdf({ path: inputPath }, config);
    console.log(`Done! PDF saved to: ${outputPath}`);
  } catch (err) {
    console.error(`Conversion failed: ${err.message}`);
    process.exit(1);
  }
}
