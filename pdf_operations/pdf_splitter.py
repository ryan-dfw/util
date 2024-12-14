import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf):
    breakpoints = []
    output_dir = os.path.dirname(input_pdf)

    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)

    print(f"The PDF has {total_pages} pages.")

    while True:
        try:
            bp = input("Enter a page number to split after or press Enter to finish: ").strip()
            if bp == "":
                break
            bp = int(bp)
            if bp < 1 or bp >= total_pages:
                print(f"Please enter a number between 1 and {total_pages - 1}.")
            else:
                breakpoints.append(bp)
        except ValueError:
            print("Invalid input. Please enter a number or press Enter to finish.")

    breakpoints = sorted(set(breakpoints))

    start_page = 0
    part = 1
    for bp in breakpoints + [total_pages]:
        writer = PdfWriter()
        for i in range(start_page, bp):
            writer.add_page(reader.pages[i])

        output_filename = os.path.join(output_dir, f"splitPDF_{part}.pdf")
        with open(output_filename, "wb") as output_file:
            writer.write(output_file)

        print(f"Created: {output_filename}")
        start_page = bp
        part += 1

    print("PDF split successfully!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Split a PDF into smaller parts interactively.")
    parser.add_argument("input_pdf", nargs="?", help="Path to the input PDF file.")

    args = parser.parse_args()

    if not args.input_pdf:
        args.input_pdf = input("Enter the path to the PDF file: ").strip()

    split_pdf(args.input_pdf)