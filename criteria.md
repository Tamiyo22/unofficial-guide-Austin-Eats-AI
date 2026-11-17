# Acceptance criteria — The Unofficial Guide

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
I chose 4 out of 5 because information in the city_guides corpus appears in both individual town guides and regional guides, sometimes with different surrounding context. This makes one retrieval miss possible, while requiring four successful questions still demonstrates that the system finds the relevant section, does not hallucinate and is grounded.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
I chose every answer because every retrieved chunk should be well grounded, and have a low distance from the source document, therefore the system should be able to cite a source for every answer. If an answer cannot name a source, that might hint at poor distance and retrieval.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" or "I do not have enough information in the provided documents to answer" every time.

**Why this target:**
The agent should be grounded and pull only from the documents provided to it, not from what it already knows.

---

## 4. Exclude text from an unrelated sections

Chunks will contain one complete topic or headed section without including text from an unrelated section. There should be little overlap and all sentences should be complete.

**Why this target:**

The retrieval should have a low distance that is able to return a complete and accurate sentence that the user can easily understand.

---

## 5. Agent doesn't crash

When the search tool returns nothing, the agent says so and moves on instead of crashing, in all 60 of my triggered failures.

**Why this target:**
The agent needs to be able to handle a high volume of failures and still work with multiple clients.

---

# Capstone

# Acceptance Criteria — Unofficial Guide: Austin Eats AI

---

## 1. Restaurant recommendations match the requested Austin area

**When** a user asks for dining options in a specific Austin area, such as South Congress or East Austin.

**Then** the system recommends only restaurants listed in that area in the Austin Eats AI dataset.

**Target:** 100% of recommended restaurants must match the requested area across three test trials.

**Why this target:**
Location is one of the main reasons someone would use Austin Eats AI. I want users to receive recommendations in the area they requested rather than having to search through restaurants across the city. Since the dataset already identifies each restaurant's area, I expect the system to respect that information.

---

## 2. Restaurant recommendations respect the user's maximum budget

**When** a user specifies a maximum price, such as "under $20" or "no more than $30 per person."

**Then** the system recommends only restaurants whose estimated price ranges fit within the user's stated budget.

**Target:** 100% of recommended restaurants must have an estimated upper price limit at or below the user's maximum budget across three test trials. If no restaurant qualifies, the system must say so.

**Why this target:**
Affordability is important when choosing where to eat. I want the chatbot to respect the user's budget rather than recommend restaurants that may cost more than they are comfortable spending. Since the dataset contains estimated price ranges, the system should be able to use them when filtering recommendations.

---

## 3. The system does not invent restaurants or unsupported information

**When** the system searches the Austin Eats AI dataset and cannot find matching restaurants or supporting information.

**Then** the system explicitly states that it does not have enough information to answer the question instead of inventing a restaurant, menu item, price, or other detail.

**Target:** The system must acknowledge insufficient information and avoid unsupported claims in all three test trials.

**Why this target:**
Austin Eats AI uses retrieval-augmented generation, so its answers should be grounded in the restaurant documents rather than relying on Gemini's general knowledge. I want users to be able to trust that the recommendations come from the dataset.

---

## 4. The original Unofficial Guide functionality continues to work

**When** a user asks one of the original city_guides questions about landmarks, transportation, or other information covered by the existing documents.

**Then** the system retrieves the appropriate city guide information and returns an accurate answer without crashing or mixing in Austin restaurant data.

**Target:** Three previously successful city_guides questions must continue to produce accurate, grounded answers without errors.

**Why this target:**
This capstone extends an existing application rather than replacing it. I want to demonstrate that adding the Austin Eats AI restaurant corpus does not break the original RAG functionality. Maintaining backward compatibility is important when extending software.

---

## 5. Restaurant recommendations match the selected dining price category

**When** a user requests a dining category such as Budget, Casual, Mid-range, Upscale, or Fine Dining.

**Then** the system recommends restaurants assigned to that category in the Austin Eats AI dataset.

**Target:** 100% of recommended restaurants must match the requested category across three test trials. If the category is unavailable in the requested area, the system must explain that no matching restaurants were found.

**Why this target:**
Not everyone wants to enter a specific dollar amount when searching for restaurants. Some users prefer choosing a general dining category based on the experience they want. I want Austin Eats AI to support these simpler choices while keeping its recommendations consistent with the dataset.

---
