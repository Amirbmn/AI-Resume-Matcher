from pathlib import Path
import fitz


def extract_text_from_pdf(file_path: str) -> str:
    

    try:
        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text.strip()

    except Exception as error:
        raise ValueError(f"Could not read PDF: {error}") from error


def extract_text_from_txt(file_path: str) -> str:
   

    try:
        return Path(file_path).read_text(
            encoding="utf-8"
        ).strip()

    except Exception as error:
        raise ValueError(f"Could not read TXT file: {error}") from error