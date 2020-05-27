import PyPDF2
import sys

# reading and writing to pdf file

with open('./pdfs/dummy.pdf', 'rb') as dummy_file:
    # print(dummy_file)
    reader = PyPDF2.PdfFileReader(dummy_file)
    # print(reader.numPages)
    # print(reader.documentInfo)

    page = reader.getPage(0)
    # print(page)
    page.rotateCounterClockwise(90)

    # writing to a pdf file
    # allows you to write the obeject in memory
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

# merging pdfs
inputs = sys.argv[1:]


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        pdf = './pdfs/' + pdf
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_merger(inputs)