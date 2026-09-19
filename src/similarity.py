from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_keyword_similarity(resume_text, job_text):
    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(
        [resume_text, job_text]
    )

    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]

    return similarity * 100


def calculate_semantic_similarity(resume_text, job_text):

    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode(
        [resume_text, job_text]
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return similarity * 100




def find_relevant_passages(
    resume_text: str,
    job_text: str,
    top_n: int = 3
) -> list[tuple[str, float]]:

    import spacy
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    nlp = spacy.load("en_core_web_sm")

    doc = nlp(resume_text)

    passages = [
        sentence.text.strip()
        for sentence in doc.sents
        if sentence.text.strip()
    ]

    if not passages:
        return []

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(
        passages + [job_text]
    )

    job_vector = vectors[-1]
    passage_vectors = vectors[:-1]

    scores = cosine_similarity(
        passage_vectors,
        job_vector
    ).flatten()

    ranked = sorted(
        zip(passages, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        (passage, score * 100)
        for passage, score in ranked[:top_n]
    ]

