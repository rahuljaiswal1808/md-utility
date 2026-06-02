#!/usr/bin/env node

import { program } from 'commander';
import { convert } from './commands/convert.js';

program
  .name('md-utility')
  .description('A CLI utility for working with Markdown files')
  .version('1.0.0');

program
  .command('to-pdf <input>')
  .description('Convert a Markdown file to PDF')
  .option('-o, --output <path>', 'Output PDF file path')
  .option('--style <css>', 'Path to a custom CSS file for styling')
  .option('--highlight-style <style>', 'Code highlight style (e.g. github, monokai)', 'github')
  .option('--paper-format <format>', 'Paper format: A3, A4, A5, Letter, Legal, Tabloid', 'A4')
  .option('--landscape', 'Use landscape orientation')
  .option('--margin <margin>', 'Page margin (e.g. 20mm, 1cm)', '20mm')
  .action(convert);

program.parse();
