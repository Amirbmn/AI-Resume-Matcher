def calculate_skill_score(
    resume_skills: list[str],
    job_skills: list[str]
) -> float:
    if not job_skills:
        return 0.0

    matching_skills = set(resume_skills) & set(job_skills)

    return len(matching_skills) / len(job_skills) * 100




def calculate_experience_score(
    candidate_years: float,
    required_years: float
) -> float:

    if required_years <= 0:
        return 100.0

    score = (candidate_years / required_years) * 100

    return min(score, 100.0)


def calculate_overall_score(
    skill_score: float,
    semantic_score: float,
    keyword_score: float,
    experience_score: float
) -> float:

    return (
        skill_score * 0.40
        + semantic_score * 0.30
        + keyword_score * 0.15
        + experience_score * 0.15
    )

import re


def extract_experience_years(text: str) -> float:
    pattern = r"(\d+(?:\.\d+)?)\+?\s*(?:years?|yrs?)"

    matches = re.findall(pattern, text.lower())

    if not matches:
        return 0.0

    return max(float(match) for match in matches)


def generate_recommendations(missing_skills: list[str]) -> list[str]:
    recommendations = []

    for skill in missing_skills:
        recommendations.append(
            f"Consider adding {skill} to your resume if you have relevant experience."
        )

    if not recommendations:
        recommendations.append(
            "Your resume covers all detected job skills."
        )

    return recommendations




def calculate_education_score(
    resume_text: str,
    job_text: str
) -> float:

    resume_text = resume_text.lower()
    job_text = job_text.lower()

    education_keywords = [
        "computer science",
        "computer engineering",
        "software engineering",
        "information technology",
        "information systems",
    ]

    required_education = [
        keyword
        for keyword in education_keywords
        if keyword in job_text
    ]

    if not required_education:
        return 100.0

    matching_education = [
        keyword
        for keyword in required_education
        if keyword in resume_text
    ]

    if matching_education:
        return 100.0

    return 0.0

