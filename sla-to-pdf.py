import os
import scribus

if scribus.haveDoc() :
    filename = os.path.splitext(scribus.getDocName())[0]
    pdf = scribus.PDFfile()
    pdf.file = filename+".pdf"
    pdf.save()
else :
    print("No file open")
