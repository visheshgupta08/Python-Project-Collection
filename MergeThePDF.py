import os
from pypdf import PdfMerger  # PDF jodne waali main machine import kari

def merge_all_pdfs(folder_name, output_filename):
    # 1. Merger machine ko chalu kiya
    merger = PdfMerger()
    
    # 2. Check kiya ki kya folder sach mein hai ya nahi
    if not os.path.exists(folder_name):
        print(f"Oops! '{folder_name}' naam ka koi folder nahi mila. ")
        return

    # 3. Folder ki saari files ki list nikali
    files = os.listdir(folder_name)
    
    # Sort kar liya taaki files line se judhein (jaise 1.pdf, 2.pdf)
    files.sort()

    pdf_count = 0
    print("PDFs ko merge karne ka kaam shuru ho gaya hai...\n")

    # 4. Loop chalakar ek-ek file ko check karenge
    for file in files:
        if file.endswith(".pdf"):
            # Agar file ka naam output file jaisa hi hai, toh use skip kar do (infinite loop se bachne ke liye)
            if file == output_filename:
                continue
                
            file_path = f"{folder_name}/{file}"
            print(f"Adding: {file} ")
            
            #  JADU: merger.append() se file machine ke andar jodne ke liye chali gayi
            merger.append(file_path)
            pdf_count += 1

    # 5. Agar koi PDF mili, toh use naye naam se save kar do
    if pdf_count > 0:
        output_path = f"{folder_name}/{output_filename}"
        
        # merger.write() se asli file disk par banti hai
        merger.write(output_path)
        merger.close() # Machine ko band karna zaroori hai memory khali karne ke liye
        
        print(f"\nMubarak ho! Total {pdf_count} PDFs merge ho gayi hain.")
        print(f"Aapki final file yahan hai: {output_path} ")
    else:
        print("Folder mein koi bhi .pdf file nahi mili! ")

# --- FUNCTION CALL (Ise chalakar dekho) ---
# Pehle ek folder banao 'my_pdfs' naam ka aur usme 2 dummy pdf files daal do
merge_all_pdfs("my_pdfs", "result_merged.pdf")



# Harry sir ka tarika
'''from PyPDF2 import PdfWriter
import os 

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf") and file != "merged-pdf.pdf"]


if len(files) > 0:
    print("PDFs ko merge karne ka kaam shuru ho gaya hai...\n")
    
    for pdf in files:
        print(f"Adding file: {pdf}")
        merger.append(pdf)
    
    merger.write("merged-pdf.pdf")
    
    
    merger.close()
    
    print("\nSaari PDF files successfully merge ho gayi hain.")
else:
    print("Oops! Is folder mein koi bhi .pdf file nahi mili.")
 '''