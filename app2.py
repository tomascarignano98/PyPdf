# combining multiple pdfs into a single pdf
import PyPDF2

merger = PyPDF2.PdfFileMerger()
files = ["deep_learning.pdf", "math_symbols.pdf"]
# in a real-world app, isntead of har-coding this array, we can
# iterate over all the pdfs in a directory. I tried to do this, but
# the resulting combined.pdf wouldn't open, because it was "damaged."
for file in files:
    merger.append(file)
merger.write("combined.pdf")
