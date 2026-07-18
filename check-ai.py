import os
import sys

# Sửa lỗi DLL load failed cho PyMuPDF trên Windows và lỗi hiển thị ký tự Unicode
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    os.add_dll_directory(os.path.dirname(sys.executable))
    import importlib.util
    spec = importlib.util.find_spec("pymupdf")
    if spec and spec.submodule_search_locations:
        for loc in spec.submodule_search_locations:
            if os.path.isdir(loc):
                os.add_dll_directory(loc)

import fitz  # Thư viện PyMuPDF dùng để đọc và ghi file PDF
import re
import time

# ==========================================
# CẤU HÌNH MÀU SẮC ĐỂ HIGHLIGHT TRONG PDF
# ==========================================
COLOR_PLAGIARISM = (1, 0, 0)      # Màu Đỏ cho đạo văn (Red)
COLOR_AI_CONTENT = (1, 0.8, 0)    # Màu Vàng cam cho AI sinh ra (Orange)
COLOR_BOTH = (0.5, 0, 0.5)        # Màu Tím nếu dính cả hai (Purple)

def extract_sentences(text):
    """
    Tách đoạn văn bản dài thành các câu nhỏ để kiểm tra chi tiết.
    """
    # Xóa các ký tự xuống dòng thừa của PDF
    text = text.replace('\n', ' ')
    # Tách câu dựa trên dấu chấm, chấm hỏi, chấm than
    sentences = re.split(r'(?<=[.!?]) +', text)
    return [s.strip() for s in sentences if len(s.strip()) > 10]

def api_check_sentence(sentence):
    """
    MÔ PHỎNG API KIỂM TRA (GIỐNG TURNITIN / GPTZERO).
    Trong thực tế, bạn sẽ dùng thư viện 'requests' để gửi câu này 
    lên API của Copyleaks, GPTZero, hoặc OpenAI để nhận kết quả.
    
    Ở đây, tôi tạo logic mô phỏng: 
    - Đánh dấu AI với các câu mang văn phong đặc trưng của ChatGPT.
    - Đánh dấu đạo văn ngẫu nhiên để demo tính năng tô màu.
    """
    # Mô phỏng độ trễ của mạng
    time.sleep(0.05) 
    
    is_ai = False
    is_plagiarized = False
    
    # Những cụm từ ChatGPT rất hay dùng (có xuất hiện trong bài của bạn)
    ai_keywords = [
        "In today's highly competitive market",
        "Furthermore",
        "Taking everything into account",
        "delve into",
        "crucial",
        "underscores"
    ]
    
    if any(keyword.lower() in sentence.lower() for keyword in ai_keywords):
        is_ai = True
        
    # Mô phỏng một vài câu copy từ nguồn khác (giả định)
    if "The dataset consists of 180,519 records" in sentence or "A total of 80% of the data" in sentence:
        is_plagiarized = True
        
    return {
        "is_ai": is_ai,
        "is_plagiarized": is_plagiarized
    }

def analyze_and_highlight_pdf(input_pdf_path, output_pdf_path):
    """
    Hàm chính: Đọc PDF, kiểm tra từng câu, tính % và tô màu.
    """
    print(f"Đang mở file: {input_pdf_path}...")
    try:
        doc = fitz.open(input_pdf_path)
    except Exception as e:
        print(f"Lỗi khi mở file: {e}")
        return

    total_sentences = 0
    ai_sentences_count = 0
    plagiarized_sentences_count = 0

    print("Đang quét nội dung và phân tích...")
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        
        sentences = extract_sentences(text)
        
        for sentence in sentences:
            total_sentences += 1
            
            # GỌI API KIỂM TRA
            result = api_check_sentence(sentence)
            
            # Đếm thống kê
            if result['is_ai']: ai_sentences_count += 1
            if result['is_plagiarized']: plagiarized_sentences_count += 1
            
            # TÔ MÀU NẾU PHÁT HIỆN LỖI
            if result['is_ai'] or result['is_plagiarized']:
                # Tìm tọa độ của câu này trên trang PDF
                text_instances = page.search_for(sentence)
                
                for inst in text_instances:
                    highlight = page.add_highlight_annot(inst)
                    
                    if result['is_ai'] and result['is_plagiarized']:
                        highlight.set_colors(stroke=COLOR_BOTH)
                        highlight.set_info(content="Phát hiện AI và Đạo văn")
                    elif result['is_ai']:
                        highlight.set_colors(stroke=COLOR_AI_CONTENT)
                        highlight.set_info(content="Văn bản do AI tạo ra (AI Generated)")
                    elif result['is_plagiarized']:
                        highlight.set_colors(stroke=COLOR_PLAGIARISM)
                        highlight.set_info(content="Phát hiện Đạo văn (Plagiarized)")
                    
                    highlight.update()

    # TÍNH TOÁN PHẦN TRĂM
    if total_sentences > 0:
        ai_percentage = (ai_sentences_count / total_sentences) * 100
        plagiarism_percentage = (plagiarized_sentences_count / total_sentences) * 100
    else:
        ai_percentage = 0
        plagiarism_percentage = 0

    # Lưu file mới
    doc.save(output_pdf_path)
    doc.close()

    # IN KẾT QUẢ GIỐNG TURNITIN
    print("\n" + "="*50)
    print("BÁO CÁO KẾT QUẢ KIỂM TRA (TƯƠNG TỰ TURNITIN)")
    print("="*50)
    print(f"Tổng số câu đã kiểm tra: {total_sentences}")
    print(f"Tỷ lệ văn bản do AI viết: {ai_percentage:.2f}% (Tô màu Vàng)")
    print(f"Tỷ lệ Đạo văn (Similarity): {plagiarism_percentage:.2f}% (Tô màu Đỏ)")
    print("="*50)
    print(f"Đã lưu file báo cáo đã highlight tại: {output_pdf_path}")
    print("Mở file này bằng Foxit Reader, Adobe Acrobat hoặc trình duyệt để xem các đoạn bị bôi màu.")

if __name__ == "__main__":
    # Đặt tên file của bạn ở đây
    INPUT_FILE = "ADY201m_AI2008_Group_7_Article (3).pdf" 
    OUTPUT_FILE = "checked_result.pdf"
 
    analyze_and_highlight_pdf(INPUT_FILE, OUTPUT_FILE)