# use Chat GPT4

import PyPDF2

def remove_duplicate_pages(pdf_files):
    output = PyPDF2.PdfWriter()
    seen_texts = set()
    
    for pdf_file in pdf_files:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text = page.extract_text()
            if text not in seen_texts:
                seen_texts.add(text)
                output.add_page(page)

    with open("merged_without_duplicates.pdf", "wb") as f_out:
        output.write(f_out)
route = "/Users/idaejong/Desktop/oneday/1DayCoding/pdf samples/"
# PDF 파일 경로 리스트
pdf_files = ['1강통증질환 1차.pdf', '1강통증질환 2차.pdf', '1강통증질환 강의록.pdf,1강통증질환강의 2차(수강생용).pdf']
lists =[route + filename for filename in pdf_files]



remove_duplicate_pages(lists)
