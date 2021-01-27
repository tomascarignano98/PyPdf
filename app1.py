import PyPDF2

with open("deep_learning.pdf", "rb") as file:  # file stream object
    reader = PyPDF2.PdfFileReader(file)  # pdf file reader object
    page = reader.getPage(0)  # page object
    page.rotateClockwise(90)
    # this does not modify the original pdf. this is only rotating the page object in memory.
    # So we need to write this to a separate pdf file.
    # this creates a writer object in emmory, not a file.
    writer = PyPDF2.PdfFileWriter()
    # writer.addpage(page) this adds the page object at the end of this pdf in memory.
    writer.insertPage(page, -1)
    # finally, we need to write this pdf in memory, to a file in disk.
    with open("new_pdf.pdf", "wb") as ouptut:
        writer.write(ouptut)
