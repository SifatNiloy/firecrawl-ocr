from firecrawl import FirecrawlApp
import json
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    # api_key = "fc-04ba0293f30a4e41972053d02f6f7815"
    # app = FirecrawlApp(api_key=api_key)
    api_key = os.getenv("FIRECRAWL_API_KEY")
    if not api_key:
        print("Error: FIRECRAWL_API_KEY not found in environment variables.")
        return
    app = FirecrawlApp(api_key=api_key)

    # direct_url = "https://fatimekerimli.wordpress.com/wp-content/uploads/2018/12/ernest_hemingway-the_old_man_and_the_sea.pdf"
    # direct_url = "https://www.gutenberg.org/files/29785/29785-pdf.pdf"
    # direct_url = "https://www.isinj.com/mt-usamo/Functional%20Equations%20and%20How%20To%20Solve%20Them%20-%20Christopher%20G.%20Small.pdf"
    # direct_url = "https://ocw.mit.edu/courses/res-18-001-calculus-fall-2023/mitres_18_001_f17_ch10.pdf"
    # direct_url = "https://arxiv.org/pdf/2106.14881"
    # direct_url = "https://www.hyvonline.com/papers/mcom-2-sem-statistical-analysis-216-may-2019.pdf"
    direct_url = "https://www.thephysicsteacher.ie/Formulae%20and%20Tables%20Book.pdf"


    # file_id = "1YFxvTdoN7JyqIgJKN611J93jBSYlALxL"
    # direct_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    try:
        result = app.extract(
            urls=[direct_url],
            prompt="Extract all readable text from the document using OCR if necessary."
        )
        print("Extraction result:")
        print(json.dumps(result.data, indent=4))

        if "textContent" in result.data and result.data["textContent"]:
            print("\nExtracted Text Content:\n")
            print(result.data["textContent"])
        else:
            print("\nNo textContent extracted.")
    except Exception as e:
        print("Error during extraction:", e)

if __name__ == "__main__":
    main()
