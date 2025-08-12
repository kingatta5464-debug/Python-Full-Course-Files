from pypdf import PdfWriter

writer = PdfWriter()

pdfs = ["file1.pdf", "file2.pdf", "file3.pdf"]

for pdf in pdfs:
    writer.append(pdf)

writer.write("result_file.pdf")
writer.close()
