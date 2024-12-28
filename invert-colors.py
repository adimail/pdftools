from pdf2image import convert_from_path
from PIL import Image, ImageOps
import os


def invert_pdf_colors(input_pdf, output_pdf):
    """
    Invert colors in a PDF file (e.g., black on white becomes white on black).

    Parameters:
    input_pdf (str): Path to the input PDF file
    output_pdf (str): Path where the inverted PDF will be saved
    """
    try:
        print(f"Converting {input_pdf} to images...")
        pages = convert_from_path(input_pdf)

        inverted_pages = []
        for i, page in enumerate(pages):
            print(f"Inverting colors of page {i+1}...")

            # Convert to RGB mode if not already (some PDFs might be in RGBA)
            if page.mode == "RGBA":
                page = page.convert("RGB")

            inverted_page = ImageOps.invert(page)
            inverted_pages.append(inverted_page)

        print("Saving inverted PDF...")
        inverted_pages[0].save(
            output_pdf,
            "PDF",
            resolution=100.0,
            save_all=True,
            append_images=inverted_pages[1:],
        )
        print(f"Inverted PDF saved as: {output_pdf}")

    except Exception as e:
        print(f"An error occurred while processing {input_pdf}: {str(e)}")


def process_folder():
    """
    Process all PDF files from the input folder and save color-inverted versions to the output folder
    """
    input_folder = "output"
    output_folder = "inverted"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in the input folder!")
        return

    print(f"Found {len(pdf_files)} PDF files to process")

    for pdf_file in pdf_files:
        input_path = os.path.join(input_folder, pdf_file)
        filename, ext = os.path.splitext(pdf_file)
        output_filename = f"{filename}_inverted{ext}"
        output_path = os.path.join(output_folder, output_filename)

        print(f"\nProcessing: {pdf_file}")
        invert_pdf_colors(input_path, output_path)


if __name__ == "__main__":
    process_folder()
