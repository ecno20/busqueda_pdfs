import os
import re
from PyPDF2 import PdfFileReader

def search_text_in_pdf(file_path, search_text):
    """Search for a specific text in a PDF file."""
    with open(file_path, 'rb') as file:
        reader = PdfFileReader(file)
        num_pages = reader.getNumPages()
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text = page.extract_text()
            if text and re.search(search_text, text, re.IGNORECASE):
                return True
    return False

def search_pdf_in_folder(folder_path, search_text):
    """Search for PDFs in a folder and check if they contain specific text."""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                file_path = os.path.join(root, file)
                if search_text_in_pdf(file_path, search_text):
                    print(f'Found "{search_text}" in: {file_path}')
                    return file_path
    print(f'The text "{search_text}" was not found in any PDF files in the folder.')
    return None

if __name__ == "__main__":
    folder_path = input("Introduzca la dirección de la carpeta de busqueda: ")
    search_text = input("Introduzca el texto que desea buscar: ")
    search_pdf_in_folder(folder_path, search_text)
