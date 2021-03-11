"""Export notebook to pdf using custom template."""

from nbconvert import PDFExporter
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('input', type=str, help='Input file')
    parser.add_argument('--output', '-o', type=str, help='Output file')

    args = parser.parse_args()

    pdfexp = PDFExporter(template_file="hidecode.tpl")

    pdf_data, _ = pdfexp.from_filename(args.input)

    output_file = args.output_file or f"{args.input}.rstrip('.ipynb').pdf"

    with open(output_file, "wb") as f:
        f.write(pdf_data)
