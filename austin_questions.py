
"""Evaluation questions for Austin Eats AI."""

QUESTIONS = [
    {
        "question": "What restaurants are in South Congress?",
        "expects": "All five South Congress restaurants",
    },
    {
        "question": "Recommend restaurants in North Austin.",
        "expects": "Only North Austin restaurants",
    },
    {
        "question": "Which South Congress restaurants cost $20 or less per person?",
        "expects": "Only restaurants with an upper estimated price of $20 or less",
    },
    {
        "question": "Recommend restaurants in Downtown Austin for under $30 per person.",
        "expects": "Only Downtown restaurants within the stated budget",
    },
    {
        "question": "Recommend casual restaurants in East Austin.",
        "expects": "Only East Austin restaurants categorized as casual",
    },
    {
        "question": "Find fine-dining restaurants in West Austin.",
        "expects": "Only West Austin restaurants categorized as fine dining",
    },
    {
        "question": "Recommend a restaurant in Austin that serves food made from moon rocks.",
        "expects": "No unsupported restaurant recommendations",
    },
]

OUT_OF_SCOPE = [
    "What is the capital of Mongolia?",
    "How do I change the oil in a diesel engine?",
    "Who won the 1994 World Cup?",
    "What is the recommended dosage of ibuprofen for a headache?",
    "How do I write a for loop in Rust?",
]


def answered() -> list[dict]:
    return [q for q in QUESTIONS if q.get("question", "").strip()]
