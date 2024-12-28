from pdf2image import convert_from_path
import os


def convert_pdf_to_grayscale(input_pdf, output_pdf):
    """
    Convert a PDF file to grayscale.

    Parameters:
    input_pdf (str): Path to the input PDF file
    output_pdf (str): Path where the grayscale PDF will be saved
    """
    try:
        print(f"Converting {input_pdf} to images...")
        pages = convert_from_path(input_pdf)

        grayscale_pages = []
        for i, page in enumerate(pages):
            print(f"Converting page {i+1} to grayscale...")
            grayscale_page = page.convert(
                "L"
            )  # 'L' mode means single channel grayscale
            grayscale_pages.append(grayscale_page)

        print("Saving grayscale PDF...")
        grayscale_pages[0].save(
            output_pdf,
            "PDF",
            resolution=100.0,
            save_all=True,
            append_images=grayscale_pages[1:],
        )
        print(f"Grayscale PDF saved as: {output_pdf}")

    except Exception as e:
        print(f"An error occurred while processing {input_pdf}: {str(e)}")


def process_folder():
    """
    Process all PDF files from the input folder and save grayscale versions to the output folder
    """
    input_folder = "input"
    output_folder = "output"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in the input folder!")
        return

    print(f"Found {len(pdf_files)} PDF files to process")

    for pdf_file in pdf_files:
        input_path = os.path.join(input_folder, pdf_file)
        output_path = os.path.join(output_folder, pdf_file)

        print(f"\nProcessing: {pdf_file}")
        convert_pdf_to_grayscale(input_path, output_path)


if __name__ == "__main__":
    process_folder()
