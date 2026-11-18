# Run log — retrieval_test

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `austin_restaurants` (index variant `default`)
- top-k: 15 · relevance cutoff: 0.65
- Runs per question: 3, caching off
- When: 2026-11-17 19:13

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What restaurants are in South Congress? | pass | pass | pass |
| Recommend restaurants in North Austin. | pass | pass | pass |
| Which South Congress restaurants cost $20 or less per person? | pass | pass | pass |
| Recommend restaurants in Downtown Austin for under $30 per person. | pass | pass | pass |
| Recommend casual restaurants in East Austin. | pass | pass | pass |
| Find fine-dining restaurants in West Austin. | pass | pass | pass |
| Recommend a restaurant in Austin that serves food made from moon rocks. | pass | pass | pass |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.65. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.897 | refused |
| How do I change the oil in a diesel engine? | 0.898 | refused |
| Who won the 1994 World Cup? | 0.976 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.768 | refused |
| How do I write a for loop in Rust? | 0.826 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### What restaurants are in South Congress? — run 1

- Best distance: 0.3657 (passed the gate)
- Sources retrieved: east_austin.md, far_north_austin.md, north_austin.md, south_austin.md, south_congress.md, south_lamar.md, southeast_austin.md

```
Based on the provided documents (south_congress.md), the restaurants in South Congress are:

* Toasty Badger
* June's
* Home Slice Pizza
* Two Hands
* Aba Austin
```

### What restaurants are in South Congress? — run 2

- Best distance: 0.3657 (passed the gate)
- Sources retrieved: east_austin.md, far_north_austin.md, north_austin.md, south_austin.md, south_congress.md, south_lamar.md, southeast_austin.md

```
Based on south_congress.md, the restaurants located in South Congress are:

- Toasty Badger
- June's
- Home Slice Pizza
- Two Hands
- Aba Austin
```

### What restaurants are in South Congress? — run 3

- Best distance: 0.3657 (passed the gate)
- Sources retrieved: east_austin.md, far_north_austin.md, north_austin.md, south_austin.md, south_congress.md, south_lamar.md, southeast_austin.md

```
Based on the provided documents, the restaurants in South Congress are Toasty Badger, June's, Home Slice Pizza, Two Hands, and Aba Austin (from south_congress.md).
```

### Recommend restaurants in North Austin. — run 1

- Best distance: 0.2692 (passed the gate)
- Sources retrieved: central_austin.md, east_austin.md, far_north_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, south_austin.md, southeast_austin.md

```
Based on `north_austin.md`, here are the recommended restaurants in North Austin:

* **The Grill-eria**: A budget-friendly spot on West Parmer serving Rio Grande Valley-style breakfast tacos, carnitas gorditas, and chilaquiles.
* **Conans Pizza (North)**: A casual restaurant on West Anderson Lane serving thick whole-wheat pan pizzas, strombolis, and lunch slice specials.
* **Mom's Special Cooking**: Austin’s only Burmese restaurant, offering home-style Shan noodles and tea leaf salad with every menu item under $15.
* **Maudie's North Lamar**: A classic Tex-Mex institution serving enchiladas, chips and salsa, and margaritas in a lively dining room.
```

### Recommend restaurants in North Austin. — run 2

- Best distance: 0.2692 (passed the gate)
- Sources retrieved: central_austin.md, east_austin.md, far_north_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, south_austin.md, southeast_austin.md

```
Based on the provided documents, here are the restaurants in North Austin:

* **The Grill-eria**: A welcoming spot on West Parmer near Gracy Woods serving breakfast tacos, carnitas gorditas, and chilaquiles (from `north_austin.md`).
* **Conans Pizza (North)**: Located on West Anderson Lane, serving thick whole-wheat pan pizzas, strombolis, and lunch slice specials in a 1970s dining room (from `north_austin.md`).
* **Mom's Special Cooking**: Austin's only Burmese restaurant, offering home-style Shan noodles and tea leaf salad (from `north_austin.md`).
* **Maudie's North Lamar**: A classic Tex-Mex institution serving enchiladas, chips and salsa, and margaritas (from `north_austin.md`).
```

### Recommend restaurants in North Austin. — run 3

- Best distance: 0.2692 (passed the gate)
- Sources retrieved: central_austin.md, east_austin.md, far_north_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, south_austin.md, southeast_austin.md

```
Based on the documents provided, here are the restaurants recommended in North Austin:

* **The Grill-eria**: A welcoming spot on West Parmer serving Rio Grande Valley-style breakfast tacos, carnitas gorditas, and chilaquiles (from `north_austin.md`).
* **Conans Pizza (North)**: Located on West Anderson Lane, serving thick whole-wheat pan pizzas, strombolis, and lunch slice specials in a 1970s dining room (from `north_austin.md`).
* **Mom's Special Cooking**: Austin's only Burmese restaurant, offering portions of home-style Shan noodles and tea leaf salad (from `north_austin.md`).
* **Maudie's North Lamar**: A classic Austin Tex-Mex institution serving enchiladas, chips and salsa, and margaritas (from `north_austin.md`).
```

### Which South Congress restaurants cost $20 or less per person? — run 1

- Best distance: 0.2846 (passed the gate)
- Sources retrieved: downtown.md, north_austin.md, northwest_austin.md, south_austin.md, south_congress.md, south_lamar.md, southeast_austin.md

```
Based on the provided documents, the South Congress restaurants that fall into the $20 or less price tier are:

* **Toasty Badger** (Budget: $10-$20)
* **Home Slice Pizza** (Casual: $10-$20)

*(Source: south_congress.md)*
```

### Which South Congress restaurants cost $20 or less per person? — run 2

- Best distance: 0.2846 (passed the gate)
- Sources retrieved: downtown.md, north_austin.md, northwest_austin.md, south_austin.md, south_congress.md, south_lamar.md, southeast_austin.md

```
Based on the provided document, the South Congress restaurants that cost $20 or less per person are:
- **Toasty Badger** (Budget, $10-$20)
- **Home Slice Pizza** (Casual, $10-$20)

*(Source: south_congress.md)*
```

### Which South Congress restaurants cost $20 or less per person? — run 3

- Best distance: 0.2846 (passed the gate)
- Sources retrieved: downtown.md, north_austin.md, northwest_austin.md, south_austin.md, south_congress.md, south_lamar.md, southeast_austin.md

```
Based on the documents, the South Congress restaurants that cost $20 or less per person are:

* **Toasty Badger** ($10-$20 budget price tier)
* **Home Slice Pizza** ($10-$20 casual price tier)

This information comes from `south_congress.md`.
```

### Recommend restaurants in Downtown Austin for under $30 per person. — run 1

- Best distance: 0.2416 (passed the gate)
- Sources retrieved: central_austin.md, downtown.md, east_austin.md, far_north_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, south_austin.md, southeast_austin.md, west_austin.md

```
Based on the provided documents, here are restaurant recommendations in Downtown Austin for under $30 per person:

* **Taqueria De Diez (D/10)**: A budget-friendly spot ($10-$20 price tier) hidden down an alley serving mesquite-grilled carne asada and al pastor tacos (*downtown.md*).
* **Anthem**: A mid-range Tex-Asian pub ($20-$30 price tier) on Rainey Street known for brisket rangoons and tiki drinks (*downtown.md*).
```

### Recommend restaurants in Downtown Austin for under $30 per person. — run 2

- Best distance: 0.2416 (passed the gate)
- Sources retrieved: central_austin.md, downtown.md, east_austin.md, far_north_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, south_austin.md, southeast_austin.md, west_austin.md

```
Based on the provided documents, here are restaurant recommendations in Downtown Austin for under $30 per person:

* **Taqueria De Diez (D/10)**, located in the Waller Creek District, offers a budget-friendly price tier ($10–$20) with mesquite-grilled carne asada and al pastor tacos (Source: `downtown.md`).
* **Anthem**, located in the Rainey Street Historic District, is in the Mid-Range price tier ($20–$30) and serves Tex-Asian fare like brisket rangoons and tiki drinks (Source: `downtown.md`).
```

### Recommend restaurants in Downtown Austin for under $30 per person. — run 3

- Best distance: 0.2416 (passed the gate)
- Sources retrieved: central_austin.md, downtown.md, east_austin.md, far_north_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, south_austin.md, southeast_austin.md, west_austin.md

```
Based on the provided documents, here are restaurant recommendations in Downtown Austin for under $30 per person:

* **Taqueria De Diez (D/10)**, located in the Waller Creek District, offers mesquite-grilled carne asada and al pastor tacos for $5.50 (Price tier: Budget, $10-$20). Source: `downtown.md`
* **Anthem**, located in the Rainey Street Historic District, is a lively Tex-Asian pub known for brisket rangoons and tiki drinks (Price tier: Mid-Range, $20-$30). Source: `downtown.md`
```

### Recommend casual restaurants in East Austin. — run 1

- Best distance: 0.3077 (passed the gate)
- Sources retrieved: central_austin.md, east_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, south_austin.md, southeast_austin.md, west_austin.md

```
Based on the provided documents, a casual restaurant in East Austin is **Cenote**, a laid-back all-day cafe on East 7th. 

Source: `east_austin.md`
```

### Recommend casual restaurants in East Austin. — run 2

- Best distance: 0.3077 (passed the gate)
- Sources retrieved: central_austin.md, east_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, south_austin.md, southeast_austin.md, west_austin.md

```
Based on the provided documents, a casual restaurant in East Austin is **Cenote**, which is a laid-back all-day cafe offering French-pressed coffee and fresh breakfast tacos or sandwiches. 

Source: `east_austin.md`
```

### Recommend casual restaurants in East Austin. — run 3

- Best distance: 0.3077 (passed the gate)
- Sources retrieved: central_austin.md, east_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, south_austin.md, southeast_austin.md, west_austin.md

```
Based on the provided documents, a casual restaurant in East Austin is **Cenote**, a laid-back all-day cafe on East 7th. 

*(Source: east_austin.md)*
```

### Find fine-dining restaurants in West Austin. — run 1

- Best distance: 0.3212 (passed the gate)
- Sources retrieved: central_austin.md, east_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, south_austin.md, southeast_austin.md, west_austin.md

```
Based on the provided documents, Jeffrey's is a fine-dining restaurant located in West Austin (from west_austin.md).
```

### Find fine-dining restaurants in West Austin. — run 2

- Best distance: 0.3212 (passed the gate)
- Sources retrieved: central_austin.md, east_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, south_austin.md, southeast_austin.md, west_austin.md

```
According to west_austin.md, Jeffrey's is a fine-dining restaurant in West Austin.
```

### Find fine-dining restaurants in West Austin. — run 3

- Best distance: 0.3212 (passed the gate)
- Sources retrieved: central_austin.md, east_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, south_austin.md, southeast_austin.md, west_austin.md

```
Based on the provided documents, Jeffrey's is a fine-dining restaurant in West Austin. 

Source: `west_austin.md`
```

### Recommend a restaurant in Austin that serves food made from moon rocks. — run 1

- Best distance: 0.3929 (passed the gate)
- Sources retrieved: central_austin.md, far_north_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, west_austin.md

```
I do not have enough information to answer your question, as the documents do not mention any restaurants that serve food made from moon rocks.
```

### Recommend a restaurant in Austin that serves food made from moon rocks. — run 2

- Best distance: 0.3929 (passed the gate)
- Sources retrieved: central_austin.md, far_north_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, west_austin.md

```
I don't have enough information to recommend a restaurant that serves food made from moon rocks.
```

### Recommend a restaurant in Austin that serves food made from moon rocks. — run 3

- Best distance: 0.3929 (passed the gate)
- Sources retrieved: central_austin.md, far_north_austin.md, north_austin.md, northeast_austin.md, northwest_austin.md, west_austin.md

```
I do not have enough information to answer your question, as the documents do not mention any restaurants that serve food made from moon rocks.
```
