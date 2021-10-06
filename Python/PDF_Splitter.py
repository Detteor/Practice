from PyPDF2 import PdfFileWriter, PdfFileReader
import glob
from pathlib import Path
import os

paths = glob.glob(r'Q:\GEO_PROJECT\sp_TEST\01_to_09_00\*\Page*.pdf')

for path in paths:
    print('Splitting: ' + str(path))
    f = open(path, "rb")
    inputpdf = PdfFileReader(f)
    parent_path = Path(path).parents[0]
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(str(parent_path) + "\\document-page%s.pdf" % (i+1), "wb") as outputStream:
            output.write(outputStream)
    f.close()
    os.remove(path)