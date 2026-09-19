import json
import re

def load_skills(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def extract_skills(text: str, skills: dict) -> list[str]:
    text = text.lower()
    found_skills = []

    for skill, aliases in skills.items():
        for alias in aliases:
            pattern = rf"\b{re.escape(alias.lower())}\b"

            if re.search(pattern, text):
                found_skills.append(skill)
                break

    return found_skills