from os import listdir
from os.path import isfile, join
from PyPDF2 import PdfFileReader, PdfFileWriter

# Get a list of all PDF files in the current directory
pdf_files = [f for f in listdir('.') if isfile(join('.', f)) and f.endswith('.pdf')]

# Loop through each PDF file
for pdf_file in pdf_files:
    # Open the PDF file
    input_pdf = PdfFileReader(open(pdf_file, 'rb'))
    
    # Create a new PDF writer for the cropped pages
    output_pdf = PdfFileWriter()
    
    # Loop through each page of the PDF file
    for page_num in range(input_pdf.getNumPages()):
        # Get the current page
        page = input_pdf.getPage(page_num)
        media_box = page.mediaBox
        page_width = media_box.getUpperRight_x() - media_box.getLowerLeft_x()
        page_height = media_box.getUpperRight_y() - media_box.getLowerLeft_y()

        # Define the crop box
        crop_box = (17, 15, page_width-17, page_height-14)
        
        # Apply the crop box to the page
        page.cropBox.lowerLeft = crop_box[:2]
        page.cropBox.upperRight = crop_box[2:]
        
        # Add the cropped page to the output PDF writer
        output_pdf.addPage(page)
    
    # Save the cropped pages as a new PDF file with the same name as the original file
    output_file_name = f'{pdf_file}'
    with open(output_file_name, 'wb') as output_file:
        output_pdf.write(output_file)
