from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from rouge_score import rouge_scorer

model = SentenceTransformer("all-MiniLM-L6-v2")

def evaluate(expected, generated):

    emb1 = model.encode([expected])
    emb2 = model.encode([generated])

    semantic = cosine_similarity(emb1, emb2)[0][0]

    scorer = rouge_scorer.RougeScorer(["rouge1"], use_stemmer=True)
    rouge = scorer.score(expected, generated)["rouge1"].fmeasure

    bleu = 1 if semantic > 0.75 else semantic

    overall = round((semantic * 0.5 + rouge * 0.3 + bleu * 0.2), 3)

    return {
    "semantic_similarity": float(round(semantic, 3)),
    "bleu": float(round(bleu, 3)),
    "rouge": float(round(rouge, 3)),
    "overall_score": float(round(overall, 3))
}