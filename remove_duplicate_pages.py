import PyPDF2
import os

def remove_duplicate_pages(pdf_folder, output_folder):
    output = PyPDF2.PdfWriter()
    seen_texts = set()
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    
    for pdf_file in pdf_files:
        full_path = os.path.join(pdf_folder, pdf_file)
        reader = PyPDF2.PdfReader(full_path)
        for page in reader.pages:
            text = page.extract_text()
            if text not in seen_texts:
                seen_texts.add(text)
                output.add_page(page)

    # 결과 파일을 지정된 출력 폴더에 저장
    output_path = os.path.join(output_folder, "merged_without_duplicates.pdf")
    with open(output_path, "wb") as f_out:
        output.write(f_out)

def delete_pdf_files(pdf_folder):
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    for pdf_file in pdf_files:
        os.remove(os.path.join(pdf_folder, pdf_file))

# 원본 PDF 파일이 있는 폴더
pdf_folder = "/Users/idaejong/Desktop/oneday/1DayCoding/pdf samples/"

# 결과 PDF 파일을 저장할 폴더
output_folder = "/Users/idaejong/Desktop/oneday/1DayCoding/daon/"

remove_duplicate_pages(pdf_folder, output_folder)

# 모든 PDF 파일을 삭제
delete_pdf_files(pdf_folder)

print("""
      -----------------------------
      PDF processing is complete!
      -----------------------------
      All original PDF files have been delete.
      -----------------------------
      """)
