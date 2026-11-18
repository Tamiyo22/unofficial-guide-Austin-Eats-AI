# Unofficial Guide: Austin Eats AI

Originally developed as a CodePath AI Engineering RAG project, Unofficial Guide has been extended with Austin Eats AI, a restaurant recommendation assistant that uses retrieval-augmented generation and Google Gemini.

Melissa Hargis - city_guides

---

# Unit 1

## What This Does

The Unofficial Guide is a retrieval-augmented question-answering system built from 14 fictional city and regional travel guides. It answers questions about transportation, accessibility, dining, accommodations, attractions, and the best times to visit. The system retrieves focused sections from the guides and generates brief answers that name their source documents. When the retrieved material is not relevant enough, the system refuses to answer rather than inventing information.

## Chunking Strategy

**Chunk size:**
**Overlap:**

At first, I wanted to preserve as much information as possible in each chunk, so I experimented with limits of 2,400, 2,800, and 3,000 characters. However, these limits were too large to separate the city guides into focused topics. I replaced the starter’s fixed 800 character windows with heading based chunking because the guides are organized into labeled sections. The starter produced 51 chunks, while my custom strategy produced 84 chunks averaging 362 characters. Each chunk retains its document title and section heading. No overlap is necessary because complete sections remain together and the document title provides context.

## Sample Chunks

**Chunk 1** — source: `— produced by:`

```
======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
======================================================================
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

## Straightforward



**Thornby Wells** is the easiest town in the region. It is flat, compact, and

everything is within three minutes of everything else. Parking is free for two

hours anywhere in town and the station is central. The pump room and gardens

are level throughout.



**Marchwood** has a modern tram network with level boarding on all four lines,

running every 8 minutes on weekdays. The city museum and covered market are both

step-free. The distances between districts are the main consideration.



**Brightwater** is level along the river and through the centre. The mill museum

is step-free. The station is a 15-minute walk from campus on flat ground, or the

shuttle meets the four busiest arrivals.

```

**Chunk 2** — source: `— produced by:`

```
======================================================================
Chunk 2  |  source: guide_corry_vale.md#5  |  produced by: chunker.py::split_documents
======================================================================
# Corry Vale

## When to go



May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.
```

**Chunk 3** — source: `— produced by:`

```
======================================================================
Chunk 3  |  source: guide_givens_mill.md#2  |  produced by: chunker.py::split_documents
======================================================================
# Givens Mill

## Eat and drink



A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.
```

**Chunk 4** — source: `— produced by:`

```
======================================================================
Chunk 4  |  source: guide_kestrelford.md#4  |  produced by: chunker.py::split_documents
======================================================================
# Kestrelford

## Where to stay



Two inns on the square and a handful of rooms above the pubs. Booking ahead matters between May and September and not at all otherwise. There is no accommodation of any kind within four miles of the town in either direction.

```

**Chunk 5** — source: `— produced by:`

```
======================================================================
Chunk 5  |  source: guide_pellew_sands.md#6  |  produced by: chunker.py::split_documents
======================================================================
# Pellew Sands

## Practical notes



Cash is still useful at the market and in smaller places, though cards are

accepted almost everywhere now. Mobile coverage is good in the centre and

patchy on the outskirts. The nearest full hospital is in Brightwater; there is

a minor injuries unit locally with limited hours.


```

## Sample Answer

**Question:** python app.py ask "How frequently do Marchwood's trams run on weekdays?" --show-prompt

# Answer using only the documents above, and name the file you used.

**Answer:** ======================================================================
System instruction sent with the prompt
======================================================================
You answer questions using only the documents provided to you.

Rules:

- Use only the information in the documents below. Do not use anything you know from elsewhere.
- If the documents don't cover the question, say you don't have enough information. Do not guess.
- Name the document your answer came from, using the filename given in each excerpt.
- Be brief. Two or three sentences is usually enough.

======================================================================
The assembled prompt, exactly as sent
======================================================================
Documents:

[from guide_marchwood.md]

# Marchwood

## Getting around

A tram network of four lines, running every 8 minutes on weekdays and every 15 at weekends, until midnight. A day ticket costs less than two single fares and nobody tells you this at the machine. The centre is walkable but the interesting districts are not adjacent to each other.

[from guide_eating.md]

# Eating across the region

## Markets

Kestrelford's Saturday market has run since the 1400s and is the region's best,

though much reduced from November to February. Brightwater's Tuesday market

sets up at 7am in the square and is finished by 1pm. Marchwood's covered market

has operated since 1863, runs six days a week, and is at its best on a weekday

morning.

[from guide_marchwood.md]

# Marchwood

## Eat and drink

The best eating is in the Northgate district, a 12-minute tram ride from the station, where about thirty restaurants sit within four streets. The area immediately around the station is uniformly poor and expensive. Marchwood keeps later hours than anywhere else in the region — kitchens serve until 10:30pm, and until midnight on Fridays and Saturdays.

[from guide_kestrelford.md]

# Kestrelford

## When to go

Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.

[from guide_marchwood.md]

# Marchwood

Marchwood is the regional hub — 180,000 people, the junction everyone changes trains at, and a city most visitors pass through rather than stop in. That is a mistake, though an understandable one, since almost nothing of interest is near the station.

## Getting there

Every railway line in the region meets here, which is the city's defining feature. Trains to Brightwater run every 40 minutes until 11pm. The airport is 20 minutes out by a dedicated bus that runs every 15 minutes and costs more than the equivalent taxi shared between three people.

---

Question: How frequently do Marchwood's trams run on weekdays?

# Answer using only the documents above, and name the file you used.

Marchwood's trams run every 8 minutes on weekdays (guide_marchwood.md).

Sources retrieved: guide_eating.md, guide_kestrelford.md, guide_marchwood.md

```

```

**My relevance cutoff: 0.65**

The five in corpus questions had best distances ranging from 0.238 to 0.513, while the five out of scope questions ranged from 0.835 to 0.997. This created a clear gap between 0.513 and 0.835. The midpoint of that gap is approximately 0.67, but I selected 0.65 to be slightly more conservative and favor refusing uncertain questions rather than producing unsupported answers. The cutoff still leaves enough room above the highest in-corpus distance to answer all five supported questions, while rejecting all five out of scope questions.

| Question                                                      | In corpus? | Best distance |
| ------------------------------------------------------------- | ---------- | ------------: |
| How frequently do Marchwood’s trams run on weekdays?          | Yes        |         0.238 |
| What is the easiest town for travelers with limited mobility? | Yes        |         0.513 |
| Where can visitors find less expensive food in Halden Bay?    | Yes        |         0.333 |
| What time does Kestrelford’s bakery usually sell out?         | Yes        |         0.335 |
| Does Brightwater’s local bus operate on Sundays?              | Yes        |         0.289 |
| What is the capital of Mongolia?                              | No         |         0.846 |
| How do I change the oil in a diesel engine?                   | No         |         0.880 |
| Who won the 1994 World Cup?                                   | No         |         0.997 |
| What is the recommended dosage of ibuprofen for a headache?   | No         |         0.835 |
| How do I write a for loop in Rust?                            | No         |         0.836 |

## How I Used AI

**1.**
I first wrote a chunk acceptance target of three successful chunks out of five and asked ChatGPT to pressure test whether it was specific and defensible. It pointed out that 60% was a fairly weak target for documents with clearly labeled sections, so I changed the target to four out of five.

**2.**
I also asked ChatGPT for help designing a chunking strategy for the structured city guides. It suggested splitting at Markdown section headings and retaining the document title in every chunk. My first implementation produced only four chunks because return chunks was inside the document loop, so I used the output and code inspection to locate the indentation problem. After correcting the implementation and testing it again, the chunker processed all 14 documents and produced 84 complete, heading-based chunks.

---

# Unit 2

## Run Log — Before

| Criterion                                  | Target | Run 1 | Run 2 | Run 3 | Verdict |
| ------------------------------------------ | ------ | ----- | ----- | ----- | ------- |
| 1. Retrieved chunk contains the answer     | 4 of 5 | 4/5   | 4/5   | 4/5   | MET     |
| 2. Every answer names a source             | 5 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 3. Gate stops out-of-corpus questions      | 5 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 4. Exclude text from an unrelated sections | 5 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 5. Agent doesn't crash                     | 5 of 5 | 5/5   | 5/5   | 5/5   | MET     |

How frequently do Marchwood’s trams run on weekdays?

QUESTION: How frequently do Marchwood’s trams run on weekdays?
EXPECTS: '8 minutes'
ANSWER : "Marchwood's trams run every 8 minutes on weekdays (guide_marchwood.md)."
run 1: pass (best distance 0.238)

QUESTION: How frequently do Marchwood’s trams run on weekdays?
EXPECTS: '8 minutes'
ANSWER : "Marchwood's trams run every 8 minutes on weekdays (from `guide_marchwood.md`)."
run 2: pass (best distance 0.238)

QUESTION: How frequently do Marchwood’s trams run on weekdays?
EXPECTS: '8 minutes'
ANSWER : "Marchwood's trams run every 8 minutes on weekdays (from guide_marchwood.md)."
run 3: pass (best distance 0.238)

What is the easiest town for travelers with limited mobility?

QUESTION: What is the easiest town for travelers with limited mobility?
EXPECTS: 'Thornby Wells'
ANSWER : 'Based on the provided documents, Thornby Wells is the easiest town in the region for travelers with limited mobility. \n\nSource: guide_accessibility.md'
run 1: pass (best distance 0.513)

QUESTION: What is the easiest town for travelers with limited mobility?
EXPECTS: 'Thornby Wells'
ANSWER : 'The easiest town for travelers with limited mobility is Thornby Wells, as it is flat, compact, and everything is within three minutes of everything else. \n\nSource: `guide_accessibility.md`'
run 2: pass (best distance 0.513)

QUESTION: What is the easiest town for travelers with limited mobility?
EXPECTS: 'Thornby Wells'
ANSWER : 'The easiest town for travelers with limited mobility is Thornby Wells (source: `guide_accessibility.md`).'
run 3: pass (best distance 0.513)

Where can visitors find less expensive food in Halden Bay?

QUESTION: Where can visitors find less expensive food in Halden Bay?
EXPECTS: 'Fell Street'
ANSWER : 'Visitors can find less expensive food on Fell Street, one level up from the harbour front. \n\nSources: \n- `guide_halden_bay.md`\n- `guide_eating.md`'
run 1: pass (best distance 0.333)

QUESTION: Where can visitors find less expensive food in Halden Bay?
EXPECTS: 'Fell Street'
ANSWER : 'Visitors can find less expensive food on Fell Street, which has comparable food for roughly half the price of the harbour front. \n\nSources: `guide_halden_bay.md` and `guide_eating.md`'
run 2: pass (best distance 0.333)

QUESTION: Where can visitors find less expensive food in Halden Bay?
EXPECTS: 'Fell Street'
ANSWER : 'Visitors can find less expensive food on Fell Street, which is located one level up from the harbour front. \n\nSources: `guide_halden_bay.md` and `guide_eating.md`'
run 3: pass (best distance 0.333)

What time does Kestrelford’s bakery usually sell out?

QUESTION: What time does Kestrelford’s bakery usually sell out?
EXPECTS: '11am'
ANSWER : "Kestrelford's bakery usually sells out by 11am. \n\nSources: `guide_kestrelford.md` and `guide_eating.md`"
run 1: pass (best distance 0.335)

QUESTION: What time does Kestrelford’s bakery usually sell out?
EXPECTS: '11am'
ANSWER : "Kestrelford's bakery usually sells out by 11am. \n\nSources: `guide_kestrelford.md` and `guide_eating.md`"
run 2: pass (best distance 0.335)

QUESTION: What time does Kestrelford’s bakery usually sell out?
EXPECTS: '11am'
ANSWER : "Kestrelford's bakery usually sells out by 11am. \n\nSources: `guide_kestrelford.md` and `guide_eating.md`"
run 3: pass (best distance 0.335)

Does Brightwater’s local bus operate on Sundays?

QUESTION: Does Brightwater’s local bus operate on Sundays?
EXPECTS: 'minimal to non-existent'
ANSWER : 'No, the local bus stops entirely on Sundays (guide_brightwater.md).'
run 1: fail (best distance 0.289)

QUESTION: Does Brightwater’s local bus operate on Sundays?
EXPECTS: 'minimal to non-existent'
ANSWER : 'No, the local bus stops entirely on Sundays. \n\nSource: guide_brightwater.md'
run 2: fail (best distance 0.289)

QUESTION: Does Brightwater’s local bus operate on Sundays?
EXPECTS: 'minimal to non-existent'
ANSWER : 'No, the local bus stops entirely on Sundays. \n\nSource: guide_brightwater.md'
run 3: fail (best distance 0.289)

Out-of-scope questions (the gate should refuse these):
refused (best distance 0.846) What is the capital of Mongolia?
refused (best distance 0.903) How do I change the oil in a diesel engine?
refused (best distance 0.997) Who won the 1994 World Cup?
refused (best distance 0.835) What is the recommended dosage of ibuprofen for a headache?
refused (best distance 0.836) How do I write a for loop in Rust?
-> gate refused 5 of 5

## Verdicts

| #   | Criterion                               | Verdict | How I decided                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --- | --------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.  | Retrieved chunk contains the answer     | MET     | Four out of five answers included the expected keywords. For the question "Does Brightwater’s local bus operate on Sundays?", the response was: "No, the local bus stops entirely on Sundays. Source: guide_brightwater.md". The initial evaluation expectation was that the response would include the words "minimal to non-existent". However, after reviewing the corpus, I realized my evaluation criterion itself was flawed, not the model's output. Therefore, I updated the final verdict to MET instead of MISSED. |
| 2.  | Every answer names a source             | MET     | All five answers include a source, even the question that did not entirely meet answer expectations included rescources to validate its response.                                                                                                                                                                                                                                                                                                                                                                            |
| 3.  | Gate stops out-of-corpus questions      | MET     | Five out of five out-of-corpus questions successfully triggered the expected refusal response. Additional exploratory testing yielded the same consistent results.                                                                                                                                                                                                                                                                                                                                                           |
| 4.  | Exclude text from an unrelated sections | MET     | All five responses remained strictly within the scope of the queried topic without pulling in irrelevant information.                                                                                                                                                                                                                                                                                                                                                                                                        |
| 5 . | Agent doesn't crash                     | MET     | The agent remained stable across multiple tests and query variations. Response times and performance were consistently stable.                                                                                                                                                                                                                                                                                                                                                                                               |

## Diagnoses

Every criterion was successfully met. Upon further reflection, I realized that I set my initial target metrics too low.
The only discrepancy encountered during testing involved the question, "Does Brightwater’s local bus operate on Sundays?" After reviewing the underlying corpus documents, I concluded that my predefined evaluation criterion was broken rather than the system failing.
To improve future validation passes, I will implement a more thorough testing strategy by increasing both the volume and complexity of the evaluation dataset. Specifically, I plan to introduce edge cases, such as intentional misspellings and special symbols, to better uncover potential vulnerabilities.

## The Improvement

**What I changed:**

     "question": "Does Brightwater’s local bus operate on Sundays?",
        "expects": "stops entirely on Sundays",

        Changed from minimal to non-existent to stops entirely on Sundays

**Why I picked it:**

During testing, a discrepancy was identified regarding the local transit verification dataset. For the test assertion checking if Brightwater's local bus operates on Sundays, the expected target string was updated from "minimal to non-existent" to "stops entirely on Sundays". This adjustment corrects a flawed test metric, ensuring the evaluation criteria accurately reflects the true facts stated within the guide_brightwater.md source document.

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

     How frequently do Marchwood’s trams run on weekdays?

QUESTION: How frequently do Marchwood’s trams run on weekdays?
EXPECTS: '8 minutes'
ANSWER : "Marchwood's trams run every 8 minutes on weekdays (from `guide_marchwood.md`)."
run 1: pass (best distance 0.238)

QUESTION: How frequently do Marchwood’s trams run on weekdays?
EXPECTS: '8 minutes'
ANSWER : "Marchwood's trams run every 8 minutes on weekdays (guide_marchwood.md)."
run 2: pass (best distance 0.238)

QUESTION: How frequently do Marchwood’s trams run on weekdays?
EXPECTS: '8 minutes'
ANSWER : "Marchwood's trams run every 8 minutes on weekdays (from `guide_marchwood.md`)."
run 3: pass (best distance 0.238)

What is the easiest town for travelers with limited mobility?

QUESTION: What is the easiest town for travelers with limited mobility?
EXPECTS: 'Thornby Wells'
ANSWER : 'Based on `guide_accessibility.md`, the easiest town in the region for travelers with limited mobility is Thornby Wells.'
run 1: pass (best distance 0.513)

QUESTION: What is the easiest town for travelers with limited mobility?
EXPECTS: 'Thornby Wells'
ANSWER : 'The easiest town for travelers with limited mobility is Thornby Wells (source: `guide_accessibility.md`).'
run 2: pass (best distance 0.513)

QUESTION: What is the easiest town for travelers with limited mobility?
EXPECTS: 'Thornby Wells'
ANSWER : 'The easiest town for travelers with limited mobility is Thornby Wells (source: `guide_accessibility.md`).'
run 3: pass (best distance 0.513)

Where can visitors find less expensive food in Halden Bay?

QUESTION: Where can visitors find less expensive food in Halden Bay?
EXPECTS: 'Fell Street'
ANSWER : 'Visitors can find less expensive food on Fell Street, which is one level up from the harbour front (guide_halden_bay.md and guide_eating.md).'
run 1: pass (best distance 0.333)

QUESTION: Where can visitors find less expensive food in Halden Bay?
EXPECTS: 'Fell Street'
ANSWER : 'Visitors can find less expensive food on Fell Street, one level up from the harbour front (_guide_halden_bay.md_ and _guide_eating.md_).'
run 2: pass (best distance 0.333)

QUESTION: Where can visitors find less expensive food in Halden Bay?
EXPECTS: 'Fell Street'
ANSWER : 'Visitors can find less expensive food on Fell Street, one level up from the harbour front (_guide_halden_bay.md_ and _guide_eating.md_).'
run 3: pass (best distance 0.333)

What time does Kestrelford’s bakery usually sell out?

QUESTION: What time does Kestrelford’s bakery usually sell out?
EXPECTS: '11am'
ANSWER : "Kestrelford's bakery usually sells out by 11am. \n\nSources: `guide_kestrelford.md` and `guide_eating.md`."
run 1: pass (best distance 0.335)

QUESTION: What time does Kestrelford’s bakery usually sell out?
EXPECTS: '11am'
ANSWER : "Kestrelford's bakery usually sells out by 11am. \n\nSources: `guide_kestrelford.md` and `guide_eating.md`."
run 2: pass (best distance 0.335)

QUESTION: What time does Kestrelford’s bakery usually sell out?
EXPECTS: '11am'
ANSWER : "Kestrelford's bakery usually sells out by 11am. \n\nSources: `guide_kestrelford.md` and `guide_eating.md`"
run 3: pass (best distance 0.335)

Does Brightwater’s local bus operate on Sundays?

QUESTION: Does Brightwater’s local bus operate on Sundays?
EXPECTS: 'stops entirely on Sundays'
ANSWER : 'No, the local bus stops entirely on Sundays. \n\nSource: guide_brightwater.md'
run 1: pass (best distance 0.289)

QUESTION: Does Brightwater’s local bus operate on Sundays?
EXPECTS: 'stops entirely on Sundays'
ANSWER : "No, Brightwater's local bus stops entirely on Sundays. \n\nSource: `guide_brightwater.md`"
run 2: pass (best distance 0.289)

QUESTION: Does Brightwater’s local bus operate on Sundays?
EXPECTS: 'stops entirely on Sundays'
ANSWER : 'No, the local bus stops entirely on Sundays. \n\nSource: guide_brightwater.md'
run 3: pass (best distance 0.289)

Out-of-scope questions (the gate should refuse these):
refused (best distance 0.846) What is the capital of Mongolia?
refused (best distance 0.903) How do I change the oil in a diesel engine?
refused (best distance 0.997) Who won the 1994 World Cup?
refused (best distance 0.835) What is the recommended dosage of ibuprofen for a headache?
refused (best distance 0.836) How do I write a for loop in Rust?
-> gate refused 5 of 5

| Criterion                                  | Target | Run 1 | Run 2 | Run 3 | Verdict |
| ------------------------------------------ | ------ | ----- | ----- | ----- | ------- |
| 1. Retrieved chunk contains the answer     | 5 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 2. Every answer names a source             | 5 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 3. Gate stops out-of-corpus questions      | 5 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 4. Exclude text from an unrelated sections | 5 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 5. Agent doesn't crash                     | 5 of 5 | 5/5   | 5/5   | 5/5   | MET     |

**Did it help?**

Yes. The change helped because it fixed the only criterion that was failing during evaluation. Before the change, the question "Does Brightwater's local bus operate on Sundays?" was consistently marked as a fail even though the correct information was being retrieved. After debugging and correcting the evaluation issue, all five test questions passed across the evaluation runs. I know the change helped because the before and after evaluation results showed the failing criterion moving from a fail to a pass while the other successful tests continued to pass.

## What's Still Broken

None of the original evaluation criteria are currently failing. However, the evaluation still relies on exact string matching in some places, which could make it sensitive to wording differences even when an answer is factually correct. If I continued improving the project, I would make the evaluation more robust by checking for semantic correctness rather than exact phrases. I stopped here because the project now meets the required criteria and the remaining improvements are enhancements rather than fixes for failing tests.

## What I'd Do Differently

I would write the criterion about answer correctness differently. Initially, I treated a question as correct only if the expected phrase appeared in the generated answer. During testing, I found that a correct answer could still be marked as incorrect because of wording differences rather than an actual retrieval or reasoning problem. If I rewrote the criterion, I would focus on whether the answer communicates the correct information and cites the appropriate source rather than requiring a specific phrase. This would better measure the quality of the RAG system and reduce false failures caused by evaluation wording.

## Capstone

### What This Extends

This capstone extends my existing Unofficial Guide RAG application with restaurant recommendations for Austin, Texas. The new capability allows users to ask questions about restaurants based on location, cuisine, and budget, using retrieved restaurant information to ground Gemini's responses.

### The Shape

I selected Shape C: Extend One Capability. I added an Austin restaurant recommendation corpus while preserving the existing RAG pipeline.

Out of scope for this submission are live restaurant APIs, real-time prices, reservations, maps, and recommendations outside Austin.

### Running It

This project uses Shape C: Extend One Capability and runs locally through the existing Python command-line application. Setup instructions and prerequisites are documented in [RUNNING.md](RUNNING.md).

From the project directory, activate the virtual environment, configure the Gemini API key as described in `RUNNING.md`, and index the `austin_restaurants` corpus if it has not already been indexed.

Then ask a question with:

```cmd
python app.py --corpus austin_restaurants ask "What restaurants are in South Congress?"
```

The application retrieves relevant restaurant information, checks the relevance threshold, generates a grounded answer, adds website links when available, and writes a request record to `results/request_log.jsonl`.

The original `city_guides` corpus remains available through the same pipeline.

### Instrumentation

Austin Eats AI records each request in `results/request_log.jsonl` using structured JSON Lines logging. The logger captures successful restaurant recommendations, relevance-gate refusals, and application errors.

Each record contains:

- `timestamp`: UTC timestamp of the completed request.
- `question`: Original user question.
- `answer`: Generated response, refusal message, or `null` if processing fails.
- `sources`: Retrieved document filenames associated with the response.
- `refused`: Whether the relevance gate rejected the question.
- `best_distance`: Closest semantic retrieval distance; lower values indicate greater similarity.
- `duration_seconds`: Total request execution time, measured with `time.perf_counter()`.
- `error`: Exception message when a request fails; otherwise `null`.

#### Instrumentation Results

Ten distinct questions were submitted to the instrumented application.

| Test category                      | Requests | Result                    |
| ---------------------------------- | -------: | ------------------------- |
| Neighborhood recommendations       |        3 | Successful                |
| Budget-conscious recommendations   |        2 | Successful                |
| Upscale restaurant recommendations |        1 | Successful                |
| Pizza recommendations              |        1 | Successful                |
| Out-of-scope questions             |        3 | Correctly refused         |
| **Total**                          |   **10** | **No application errors** |

All seven restaurant responses included website links retrieved from the restaurant documents. All three unrelated questions were rejected by the relevance gate rather than answered using unsupported information.

The successful restaurant requests took between **0.666 and 4.068 seconds**. The three refused requests took between **0.654 and 0.785 seconds**.

These results demonstrate that the application can answer several types of restaurant questions, reject unrelated requests, and record its behavior for debugging.

#### Ten Actual Log Entries

The following ten records are preserved in `results/request_log.jsonl` and reproduced below as text.

```json
{"timestamp": "2026-11-18T02:07:33.881964+00:00", "question": "What restaurants are in South Congress?", "answer": "According to my sources, the restaurants in South Congress are:\n- Toasty Badger\n- June's\n- Home Slice Pizza\n- Two Hands\n- Aba Austin\n\nThis information came from the file **south_congress.md**.\n\nRestaurant websites:\n- [Toasty Badger](https://www.loboshospitality.com/Toasty-Badger.asp)\n- [Home Slice Pizza](https://homeslicepizza.com/location/south-congress/)\n- [Two Hands](https://www.twohandshospitality.com/location/austin/)\n- [June's](http://junesallday.com/)\n- [Aba Austin](https://www.abarestaurants.com/austin/)", "sources": ["east_austin.md", "far_north_austin.md", "north_austin.md", "south_austin.md", "south_congress.md", "south_lamar.md", "southeast_austin.md"], "refused": false, "best_distance": 0.3657461329474946, "duration_seconds": 0.666, "error": null}
{"timestamp": "2026-11-18T02:07:57.512562+00:00", "question": "Where can I eat in Downtown Austin for under $30?", "answer": "You can eat at the following locations in Downtown Austin for under $30:\n\n* **Anthem**, a lively Tex-Asian pub on Rainey Street with a mid-range price tier of $20ΓÇô$30 (from `downtown.md`).\n* **Taqueria De Diez (D/10)**, located in the Waller Creek District with a budget price tier of $10ΓÇô$20 (from `downtown.md`).\n\nRestaurant websites:\n- [Taqueria De Diez (D/10)](https://taqueriadediez.com/)\n- [Anthem](http://eatdrinkanthem.com/)", "sources": ["central_austin.md", "downtown.md", "east_austin.md", "north_austin.md", "northeast_austin.md", "northwest_austin.md", "south_austin.md"], "refused": false, "best_distance": 0.27567877364744586, "duration_seconds": 4.049, "error": null}
{"timestamp": "2026-11-18T02:08:10.146972+00:00", "question": "What restaurants are available in East Austin?", "answer": "According to my sources (`east_austin.md`), the restaurants available in East Austin are:\n\n* **Cenote**\n* **Juniper**\n* **Las Trancas Taco Stand**\n\nRestaurant websites:\n- [Las Trancas Taco Stand](https://www.lastrancastacostand.com/menu)\n- [Cenote](https://cenoteaustin.com/)\n- [Juniper](https://www.juniperaustin.com/)", "sources": ["central_austin.md", "east_austin.md", "north_austin.md", "northeast_austin.md", "northwest_austin.md", "south_austin.md", "southeast_austin.md", "west_austin.md"], "refused": false, "best_distance": 0.3029575800399602, "duration_seconds": 3.897, "error": null}
{"timestamp": "2026-11-18T02:08:19.302061+00:00", "question": "Where can I find affordable food in South Lamar?", "answer": "According to my sources, you can find affordable food in South Lamar at **Thunder Chief**, which is in the budget price tier ($10-$20) and known for crispy wings, birria tacos, and $5 Monday smash burgers (source: `south_lamar.md`).\n\nRestaurant websites:\n- [Thunder Chief](http://thunderchiefatx.com/)", "sources": ["north_austin.md", "south_austin.md", "south_congress.md", "south_lamar.md", "west_austin.md"], "refused": false, "best_distance": 0.3234097600163707, "duration_seconds": 3.446, "error": null}
{"timestamp": "2026-11-18T02:08:28.875067+00:00", "question": "What restaurants are in North Austin?", "answer": "According to my sources, the restaurants located in North Austin are:\n* The Grill-eria (`north_austin.md`)\n* Conans Pizza (North) (`north_austin.md`)\n* Maudie's North Lamar (`north_austin.md`)\n* Santorini Cafe (`north_austin.md`)\n\nRestaurant websites:\n- [The Grill-eria](https://grill-eria.com/)\n- [Conans Pizza (North)](https://conanspizza.com/)\n- [Santorini Cafe](http://www.santorinicafe-atx.com/)\n- [Maudie's North Lamar](http://maudies.com/)", "sources": ["central_austin.md", "east_austin.md", "far_north_austin.md", "north_austin.md", "northeast_austin.md", "south_austin.md"], "refused": false, "best_distance": 0.2955946919951413, "duration_seconds": 4.068, "error": null}
{"timestamp": "2026-11-18T02:08:39.216251+00:00", "question": "What upscale restaurants are in Austin?", "answer": "According to my sources, the upscale restaurants in Austin are:\n\n* **District Kitchen + Cocktails** in South Austin (from `south_austin.md`)\n* **Mexican Sugar** in Far North Austin (from `far_north_austin.md`)\n* **Emmer & Rye** Downtown (from `downtown.md`)\n\nRestaurant websites:\n- [Emmer & Rye](http://www.emmerandrye.com/)\n- [Mexican Sugar](https://www.mexicansugarcocina.com/)\n- [District Kitchen + Cocktails](http://districtaustin.com/)", "sources": ["central_austin.md", "downtown.md", "east_austin.md", "far_north_austin.md", "north_austin.md", "northeast_austin.md", "south_austin.md", "southeast_austin.md", "west_austin.md"], "refused": false, "best_distance": 0.31576952219786714, "duration_seconds": 3.49, "error": null}
{"timestamp": "2026-11-18T02:08:50.640283+00:00", "question": "Where can I get pizza in Austin?", "answer": "You can get pizza at the following locations mentioned in the documents:\n\n* **Conans Pizza (South)** in South Austin (*south_austin.md*)\n* **Little Deli & Pizzeria (Windsor Park)** in Northeast Austin (*northeast_austin.md*)\n* **Conans Pizza (North)** in North Austin (*north_austin.md*)\n* **Little Deli & Pizzeria (Crestview)** in Central Austin (*central_austin.md*)\n* **Home Slice Pizza** in South Congress (*south_congress.md*)\n* **Pour House** in Northwest Austin (*northwest_austin.md*)\n\nRestaurant websites:\n- [Little Deli & Pizzeria (Crestview)](https://www.littledeliandpizza.com/)\n- [Conans Pizza (North)](https://conanspizza.com/)\n- [Little Deli & Pizzeria (Windsor Park)](https://www.littledeliandpizza.com/)\n- [Pour House](http://www.pourhousepintsandpies.com/)\n- [Conans Pizza (South)](https://conanspizza.com/)\n- [Home Slice Pizza](https://homeslicepizza.com/location/south-congress/)", "sources": ["central_austin.md", "east_austin.md", "far_north_austin.md", "north_austin.md", "northeast_austin.md", "northwest_austin.md", "south_austin.md", "south_congress.md"], "refused": false, "best_distance": 0.28067617019919633, "duration_seconds": 3.213, "error": null}
{"timestamp": "2026-11-18T02:09:05.536066+00:00", "question": "What is the capital of Mongolia?", "answer": "I don't have enough information about that.", "sources": [], "refused": true, "best_distance": 0.8968664962191669, "duration_seconds": 0.654, "error": null}
{"timestamp": "2026-11-18T02:09:16.079689+00:00", "question": "How do I change the oil in a diesel engine?", "answer": "I don't have enough information about that.", "sources": [], "refused": true, "best_distance": 0.8983973642605366, "duration_seconds": 0.785, "error": null}
{"timestamp": "2026-11-18T02:09:25.398209+00:00", "question": "How do I write a for loop in Rust?", "answer": "I don't have enough information about that.", "sources": [], "refused": true, "best_distance": 0.8264846775468542, "duration_seconds": 0.679, "error": null}
```

#### Limitations

The instrumentation records retrieved document filenames but not the exact passages supporting each recommendation. Future improvements could capture passage-level evidence, cache status, and token usage per request to make debugging and cost monitoring more precise.

### What It Costs

I measured token usage using the output from `run_eval.py`, which reports the number of Gemini API calls and total input and output tokens consumed during each evaluation session.

My improved configuration (`top_k=15`) made 21 model calls and consumed 34,605 input tokens and 1,532 output tokens, for a total of 36,137 tokens.

Using an estimated Gemini 3.5 Flash-Lite standard API price of $0.30 per million input tokens and $2.50 per million output tokens:

**Measured evaluation cost estimate:**

- Input: 34,605 × ($0.30 / 1,000,000) = $0.01038
- Output: 1,532 × ($2.50 / 1,000,000) = $0.00383
- Total: approximately $0.01421 for 21 requests
- Average: $0.01421 ÷ 21 = **$0.000677 per request**

**Projected cost for 100 users per day:**

Assuming each user makes one request with similar token usage:

100 × $0.000677 = **$0.0677 per day**, or approximately **$2.03 over 30 days**.

The original `top_k=5` configuration consumed 14,162 tokens across 21 requests. Increasing retrieval depth to 15 improved recommendation coverage but raised token consumption by approximately 155%.

These estimates cover Gemini inference only, not infrastructure, hosting, or other operational expenses. Actual costs would vary with query complexity, response length, caching, and API pricing. The evaluation was run with caching disabled.

### Run Log and Verdicts

I evaluated Austin Eats AI using seven restaurant questions, each repeated three times, for 21 trials per configuration.

The original evaluation used `top_k=5`. The improvement increased retrieval depth to `top_k=15`, while keeping the relevance cutoff at `0.65`.

| Evaluation question                                     | Before (3 trials) | After (3 trials) |
| ------------------------------------------------------- | ----------------- | ---------------- |
| List all five South Congress restaurants                | 0/3               | 3/3              |
| Recommend North Austin restaurants                      | 3/3               | 3/3              |
| Find South Congress restaurants costing $20 or less     | 3/3               | 3/3              |
| Recommend Downtown restaurants under $30                | 0/3               | 3/3              |
| Recommend casual East Austin restaurants                | 3/3               | 3/3              |
| Find fine-dining West Austin restaurants                | 3/3               | 3/3              |
| Refuse unsupported moon-rock restaurant recommendations | 3/3               | 3/3              |
| **Total**                                               | **15/21 (71.4%)** | **21/21 (100%)** |

**Scoring note:** The original baseline report recorded all 21 trials as failures because the initial scorer required exact expectation phrases to appear in the answers. I subsequently corrected the scoring logic. The before results above are a manual reassessment of the saved responses; the after results were generated with the corrected scorer. The original baseline report remains unchanged.

**Out-of-scope safety:** All five unrelated questions were refused by the relevance gate in both configurations.

**Evidence files:**

- `results/run_2026-11-17_1856_before.md`
- `results/run_2026-11-17_1913_retrieval_test.md`

**Example improvement:** Before the change, the system listed four South Congress restaurants, omitting Aba Austin. After increasing retrieval depth, all five restaurants appeared in all three trials. The Downtown question also improved from an unsupported refusal to recommendations for Taqueria De Diez (D/10) and Anthem.

**Cost trade-off:** The baseline used 14,162 tokens across 21 calls, compared with 36,137 tokens after expanding retrieval. This is approximately a 155% increase in token usage in exchange for improved coverage.

### Acceptance Criteria — Before and After

The following results use the five acceptance criteria defined in `criteria.md` before testing began.

**Before improvement — top-k = 5**

| Criterion                                          | Target                        | Run 1      | Run 2      | Run 3      | Verdict      |
| -------------------------------------------------- | ----------------------------- | ---------- | ---------- | ---------- | ------------ |
| 1. Recommendations match the requested Austin area | 100% location accuracy        | 3/3        | 3/3        | 3/3        | MET\*        |
| 2. Recommendations respect maximum budget          | 100% budget compliance        | 1/2        | 1/2        | 1/2        | NOT MET      |
| 3. No invented or unsupported information          | 100% grounded refusals        | Pass       | Pass       | Pass       | MET          |
| 4. Original city_guides functionality works        | 3 accurate original questions | Not tested | Not tested | Not tested | NOT VERIFIED |
| 5. Recommendations match dining price category     | 100% category accuracy        | 2/2        | 2/2        | 2/2        | MET          |

_The original South Congress answer omitted one restaurant but did not recommend restaurants outside the requested area. The Downtown query returned no recommendations, so it did not demonstrate successful retrieval despite avoiding incorrect locations._

**After improvement — top-k = 15**

| Criterion                                          | Target                        | Run 1 | Run 2 | Run 3 | Verdict |
| -------------------------------------------------- | ----------------------------- | ----- | ----- | ----- | ------- |
| 1. Recommendations match the requested Austin area | 100% location accuracy        | 3/3   | 3/3   | 3/3   | MET     |
| 2. Recommendations respect maximum budget          | 100% budget compliance        | 2/2   | 2/2   | 2/2   | MET     |
| 3. No invented or unsupported information          | 100% grounded refusals        | Pass  | Pass  | Pass  | MET     |
| 4. Original city_guides functionality works        | 3 accurate original questions | 3/3   | 3/3   | 3/3   | MET\*\* |
| 5. Recommendations match dining price category     | 100% category accuracy        | 2/2   | 2/2   | 2/2   | MET     |

**Compatibility note:** The original city guide compatibility test produced 15 correct, source-grounded answers across five questions and three trials. The automated scorer initially marked them as failures because it only recognized Austin restaurant questions. Manual inspection verified the correct answers, and the scorer was subsequently updated to recognize the original city guide expectations.

**Evaluation limitations:** The original restaurant baseline was manually reassessed after identifying an overly strict scorer. The budget criterion treats an unanswered query as a failure because the system did not provide a useful qualifying recommendation. The automated restaurant scorer checks known restaurant names and dataset categories but is not a comprehensive hallucination detector.

**Supporting reports:**

- `results/run_2026-11-17_1856_before.md`
- `results/run_2026-11-17_1913_retrieval_test.md`
- `results/run_2026-11-17_1923_compatibility_after.md`

### The Improvement

#### What Changed and Why

The initial evaluation revealed that the RAG system sometimes failed to retrieve enough relevant restaurant information. With `TOP_K = 5`, the system omitted Aba Austin from its South Congress recommendations and could not provide an adequate answer to the Downtown Austin under-$30 question.

To address this, I increased `TOP_K` from **5 to 15** in `config.py`. This allowed Chroma to retrieve more potentially relevant document chunks before passing them to Gemini.

I chose this change because the missing information already existed in the restaurant corpus. The problem was primarily retrieval coverage rather than missing data.

#### Second Evaluation

I ran the same seven Austin restaurant questions across three trials after increasing `TOP_K`.

| Measurement                            | Before (`top_k=5`) | After (`top_k=15`)                          |
| -------------------------------------- | ------------------ | ------------------------------------------- |
| Restaurant evaluation trials           | 21                 | 21                                          |
| Manually reviewed successful trials    | 15/21              | 21/21                                       |
| Correct South Congress recommendations | Incomplete         | All five restaurants included               |
| Downtown under-$30 recommendations     | Missing            | Anthem and Taqueria De Diez (D/10) returned |
| Out-of-scope refusal checks            | 5/5                | 5/5                                         |
| Total measured tokens                  | 14,162             | 36,137                                      |

The improvement increased manually reviewed success from approximately **71% to 100%** on this evaluation set.

The trade-off was higher token usage: approximately **2.55 times** the original total. This is acceptable for the small prototype but would require optimization at larger scale.

**Evaluation evidence:**

- Before: `results/run_2026-11-17_1856_before.md`
- After: `results/run_2026-11-17_1913_retrieval_test.md`

The original evaluation scorer also had an overly strict exact-string comparison that incorrectly marked otherwise correct answers as failures. I investigated those results manually and improved the scorer rather than treating its initial failure counts as evidence that every answer was incorrect.

#### Additional Usability Improvement: Restaurant Website Links

After improving retrieval, I added restaurant website links to the generated recommendations.

The new `restaurant_links.py` helper reads website URLs from the existing restaurant Markdown documents and matches them to restaurant names mentioned in the generated answer.

This approach avoids asking Gemini to invent URLs and does not require an additional model call.

I also changed the response wording from "Based on the provided documents" to "According to my sources" to make the assistant sound more natural.

A separate ten-request instrumentation run tested seven distinct restaurant questions and three unrelated questions. All seven restaurant responses included website links, all three unrelated questions were refused, and no application errors were recorded.

#### Remaining Trade-Off

Increasing retrieval depth improved coverage but also increased the amount of context sent to Gemini. The next improvement would be neighborhood-aware retrieval filtering, allowing the system to retrieve fewer, more targeted chunks while preserving recommendation accuracy.

### What's Still Broken

Although Austin Eats AI passed all 21 trials in the final restaurant evaluation, the system still has limitations.

The most significant limitation is retrieval efficiency. Increasing `top_k` from 5 to 15 improved recommendation coverage, but it also increased token consumption by approximately 155%. The system retrieves semantically similar chunks without explicitly filtering by neighborhood, meaning it may include unrelated restaurant information in the context sent to Gemini.

The evaluation system also has room for improvement. While the updated scorer validates restaurant names against the dataset and checks location, budget, and dining categories, it does not detect every possible unsupported claim. Additionally, the current evaluation uses a relatively small set of seven restaurant questions.

If I revised my acceptance criteria, I would strengthen Criterion 3 by requiring every factual claim in a recommendation—not just restaurant names—to be supported by the retrieved documents. I would also expand testing to include misspelled neighborhood names, conflicting constraints, and requests for unavailable dining categories.

I stopped further development because the project met its current evaluation targets, and implementing more sophisticated retrieval and claim validation would require additional development and testing.

### What I'd Do Next

If I had another unit to continue developing Austin Eats AI, I would prioritize neighborhood-aware retrieval that filters restaurant documents by the user's requested location before sending them to Gemini. This could maintain the recommendation accuracy achieved with `top_k=15` while reducing irrelevant context, token consumption, and operating costs.

### How I Used AI

# One

One of the most valuable uses of AI was troubleshooting the evaluation pipeline. When my initial tests reported that every restaurant recommendation had failed, I worked with ChatGPT to investigate the discrepancy between the automated verdicts and the actual generated answers. We identified that the original scorer relied on overly restrictive string matching rather than validating restaurant recommendations against the dataset. I used AI assistance to develop a more appropriate scoring approach, tested the revised functions, and verified the results against saved evaluation logs.

# Two

I also used ChatGPT to investigate retrieval quality. By comparing the original evaluation results with the restaurant dataset, I identified incomplete South Congress recommendations and missing Downtown results. I tested an increase in retrieval depth from five to fifteen chunks and observed an improvement from 15 of 21 manually verified successful trials to 21 of 21 automated passes. I also examined the associated increase in token usage to understand the trade-off between retrieval coverage and operating cost.
