# def judge(question: str, expects: str, answer: str, results) -> bool:
#     if not expects:
#         return False
#     return expects.strip().lower() in (answer or "").lower()

# def judge(question: str, expects: str, answer: str, results) -> bool:
#     print("\nQUESTION:", question)
#     print("EXPECTS:", repr(expects))
#     print("ANSWER :", repr(answer))

#     if not expects:
#         return False

#     return expects.strip().lower() in (answer or "").lower()


# def retrieval_hit(expects: str, results) -> bool:
#     if not expects:
#         return False

#     needle = expects.strip().lower()
#     return any(
#         needle in (r.text or "").lower()
#         for r in results
#     )


import csv
import re
from pathlib import Path

DATASET = (
    Path(__file__).resolve().parent
    / "corpora"
    / "austin_restaurants"
    / "documents"
    / "austin_restaurants_by_neighborhood.csv"
)


def load_restaurants():
    with DATASET.open(encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def max_price(price_tier):
    """Return the upper price estimate, or None if unavailable."""
    match = re.search(r"\$(\d+)\s*-\s*\$(\d+)", price_tier)
    if match:
        return int(match.group(2))

    return None


def mentioned_restaurants(answer, restaurants):
    """Find restaurant names mentioned in an answer."""
    answer_lower = (answer or "").casefold()
    return [
        row
        for row in restaurants
        if row["Restaurant Name"].casefold() in answer_lower
    ]


def judge(question: str, expects: str, answer: str, results) -> bool:
    if not answer or not expects:
        return False

    # Original city_guides questions use factual answer matching.
    # Austin restaurant questions use the dataset-aware checks below.
    city_guide_questions = (
        "marchwood",
        "limited mobility",
        "halden bay",
        "kestrelford",
        "brightwater",
    )

    if any(term in question.casefold() for term in city_guide_questions):
        return expects.strip().casefold() in answer.casefold()

    restaurants = load_restaurants()
    mentioned = mentioned_restaurants(answer, restaurants)
    q = question.casefold()

    if "moon rocks" in q:
        return (
            not mentioned
            and any(
                phrase in answer.casefold()
                for phrase in (
                    "don't have enough information",
                    "do not have enough information",
                    "no information",
                    "do not mention",
                    "don't mention",
                    "cannot recommend",
                    "can't recommend",
                )
            )
        )

    if not mentioned:
        return False

    if "south congress" in q:
        eligible = [
            r for r in restaurants
            if r["Area"].casefold() == "south congress"
        ]

        if "$20" in q:
            eligible = [
                r for r in eligible
                if max_price(r["Price Tier"]) is not None
                and max_price(r["Price Tier"]) <= 20
            ]
        else:
            # The first question explicitly asks for all five.
            if len(mentioned) != len(eligible):
                return False

    elif "north austin" in q:
        eligible = [
            r for r in restaurants
            if r["Area"].casefold() == "north austin"
        ]

    elif "downtown" in q:
        eligible = [
            r for r in restaurants
            if r["Area"].casefold() == "downtown"
            and max_price(r["Price Tier"]) is not None
            and max_price(r["Price Tier"]) <= 30
        ]

    elif "east austin" in q:
        eligible = [
            r for r in restaurants
            if r["Area"].casefold() == "east austin"
            and "casual" in r["Price Tier"].casefold()
        ]

    elif "west austin" in q:
        eligible = [
            r for r in restaurants
            if r["Area"].casefold() == "west austin"
            and "fine dining" in r["Price Tier"].casefold()
        ]

    else:
        return False

    eligible_names = {
        r["Restaurant Name"].casefold()
        for r in eligible
    }

    return all(
        r["Restaurant Name"].casefold() in eligible_names
        for r in mentioned
    )


def retrieval_hit(expects: str, results) -> bool:
    if not expects:
        return False

    needle = expects.strip().lower()
    return any(
        needle in (r.text or "").lower()
        for r in results
    )
