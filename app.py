import streamlit as st

from src.extractor import (
    extract_text_from_pdf,
    extract_text_from_txt,
)

from src.nlp import process_text

from src.skills import (
    load_skills,
    extract_skills,
)

from src.matcher import (
    calculate_skill_score,
    calculate_overall_score,
    extract_experience_years,
    calculate_experience_score,
    generate_recommendations,
    calculate_education_score,
    calculate_role_score,
)

from src.similarity import (
    calculate_keyword_similarity,
    calculate_semantic_similarity,
    find_relevant_passages,
)


st.title("AI Resume–Job Matcher")

st.write(
    "Stage 4: Resume–Job matching and skill-gap analysis"
)


uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "txt"],
)


job_description = st.text_area(
    "Paste the job description",
    height=300,
)


if uploaded_file is not None:

    if uploaded_file.type == "application/pdf":

        with open("temp_resume.pdf", "wb") as file:
            file.write(uploaded_file.getbuffer())

        text = extract_text_from_pdf(
            "temp_resume.pdf"
        )

    else:

        text = uploaded_file.getvalue().decode(
            "utf-8"
        )


    st.subheader("Extracted Text")

    st.text_area(
        "Resume",
        text,
        height=300,
    )


    doc = process_text(text)

    st.subheader("Resume Sentences")

    for sentence in doc.sents:
        st.write(sentence.text)


    st.subheader("Named Entities")

    for entity in doc.ents:

        st.write(
            f"{entity.text} → {entity.label_}"
        )


    skills = load_skills(
        "data/skills.json"
    )

    found_skills = extract_skills(
        text,
        skills,
    )

    st.subheader("Resume Skills")

    st.write(found_skills)


    if job_description.strip():

        job_skills = extract_skills(
            job_description,
            skills,
        )

        st.subheader("Job Skills")

        st.write(job_skills)


        matching_skills = [
            skill
            for skill in found_skills
            if skill in job_skills
        ]

        missing_skills = [
            skill
            for skill in job_skills
            if skill not in found_skills
        ]


        st.subheader("Matching Skills")

        st.write(matching_skills)


        st.subheader("Missing Skills")

        st.write(missing_skills)


        # Skill score

        skill_score = calculate_skill_score(
            found_skills,
            job_skills,
        )

        st.subheader("Skill Match Score")

        st.metric(
            "Skill Match",
            f"{skill_score:.1f}%",
        )


        # Keyword similarity

        keyword_score = calculate_keyword_similarity(
            text,
            job_description,
        )

        st.subheader("Keyword Similarity")

        st.metric(
            "Keyword Match",
            f"{keyword_score:.1f}%",
        )


        # Semantic similarity

        semantic_score = calculate_semantic_similarity(
            text,
            job_description,
        )

        st.subheader("Semantic Similarity")

        st.metric(
            "Semantic Match",
            f"{semantic_score:.1f}%",
        )


        # Experience

        candidate_years = extract_experience_years(
            text
        )

        required_years = extract_experience_years(
            job_description
        )

        experience_score = calculate_experience_score(
            candidate_years,
            required_years,
        )

        st.subheader("Experience")

        st.write(
            f"Candidate experience: "
            f"{candidate_years} years"
        )

        st.write(
            f"Required experience: "
            f"{required_years} years"
        )

        st.metric(
            "Experience Match",
            f"{experience_score:.1f}%",
        )


        # Education

        education_score = calculate_education_score(
            text,
            job_description,
        )

        st.subheader("Education Match")

        st.metric(
            "Education Match",
            f"{education_score:.1f}%",
        )


        # Role

        role_score = calculate_role_score(
            text,
            job_description,
        )

        st.subheader("Role Match")

        st.metric(
            "Role Match",
            f"{role_score:.1f}%",
        )


        # Overall score

        overall_score = calculate_overall_score(
            skill_score,
            semantic_score,
            keyword_score,
            experience_score,
            education_score,
            role_score,
        )


        # Score breakdown

        st.subheader("Match Score Breakdown")

        st.write(
            f"Skill Match (30%): "
            f"{skill_score:.1f}%"
        )

        st.write(
            f"Semantic Match (25%): "
            f"{semantic_score:.1f}%"
        )

        st.write(
            f"Keyword Match (15%): "
            f"{keyword_score:.1f}%"
        )

        st.write(
            f"Experience Match (15%): "
            f"{experience_score:.1f}%"
        )

        st.write(
            f"Education Match (10%): "
            f"{education_score:.1f}%"
        )

        st.write(
            f"Role Match (5%): "
            f"{role_score:.1f}%"
        )


        # Overall match

        st.subheader("Overall Match")

        st.metric(
            "Resume–Job Match",
            f"{overall_score:.1f}%",
        )


        # Recommendations

        st.subheader(
            "Resume Recommendations"
        )

        recommendations = generate_recommendations(
            missing_skills
        )

        for recommendation in recommendations:

            st.write(
                f"• {recommendation}"
            )


        # Relevant passages

        relevant_passages = find_relevant_passages(
            text,
            job_description,
        )

        st.subheader(
            "Relevant Resume Passages"
        )

        for passage, score in relevant_passages:

            st.write(passage)

            st.caption(
                f"Relevance: {score:.1f}%"
            )
