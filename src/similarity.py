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