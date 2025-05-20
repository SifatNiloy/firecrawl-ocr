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
    direct_url = "https://sci-hub.se/https://doi.org/10.1103/RevModPhys.29.325"


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
