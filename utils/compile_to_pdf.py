"""Export notebook to pdf using custom template."""

import argparse
from pathlib import Path

from nbconvert import PDFExporter

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("input", type=str, help="Input file")
    parser.add_argument("--output", "-o", type=str, help="Output file")

    args = parser.parse_args()

    pdfexp = PDFExporter(
        template_file=str((Path(__file__).parent / "hidecode.tpl").resolve())
    )

    pdf_data, _ = pdfexp.from_filename(args.input)

    output_file = args.output or f"{args.input.rstrip('.ipynb')}.pdf"

    with open(output_file, "wb") as f:
        f.write(pdf_data)
