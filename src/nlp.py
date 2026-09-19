import re
import spacy
nlp = spacy.load("en_core_web_sm")

def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def process_text(text: str):
    cleaned_text = clean_text(text)

    return nlp(cleaned_text)