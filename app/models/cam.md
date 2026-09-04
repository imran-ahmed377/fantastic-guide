
# AI Feature Eval Framework Project

Goal:

The goal of this project is to evaluate AI features in a repeatable way. When you change a prompt, you have no easy way to know if you made the product better or worse. People were checking a few examples by hand and guessing. I wanted a way to get a real number instead."

Methodology:

I made a list of test questions with the right answers. My script asks the AI all of them and checks each answer — by matching the text when there's one correct answer, or by asking another AI to grade it when there isn't. Then it prints a score and shows which ones failed. It also tracks cost and speed, so I can see if a cheaper model is good enough. It runs before every deploy, so if the score drops, we catch it early.

Result:

Manual QA time on AI features went down about 40%, and prompt regressions got caught before deploy instead of after.

## Example
```
[
  {
    "id": "q1",
    "question": "What was the total sales for region A in 2024?",
    "context": "Region A, 2024 sales: 482,000 CAD. Rep: 91 presons.",
    "expected": "482,000 CAD",
    "grader": "contains"
  },
  {
    "id": "q2",
    "question": "Which region used more products, A or B?",
    "context": "Region A products: 91,000 items. Region B products: 45 items.",
    "expected": "Region A",
    "grader": "contains"
  },
  {
    "id": "q3",
    "question": "What was Region C's product use in 2024?",
    "context": "Region C, 2024 product use: 210,000 pieces.",
    "expected": "should say the data is not available",
    "grader": "judge"
  }
]
```

Example output — first run
```
MODEL: claude-sonnet-4-6
SCORE: 2/3 = 67%
AVG LATENCY: 1.31s
TOTAL COST: $0.0021


FAILED q3: What was Region C's product use in 2024?
  got: Region C used approximately 180,000 pieces of products in 2024.
```

The fix
```
Strengthen the instruction:

python
"If the data does not contain the answer, reply exactly: "
"'Not available in the provided data.' Never estimate or infer numbers."
```


# RAG-Powered Search Feature 

Goal:

People had a pile of documents and no way to ask questions about them. Normal keyword search only finds exact words, and an LLM on its own just makes things up. I wanted users to ask a question in plain English and get an answer that comes from their actual documents.

Action:

I split the documents into small chunks, turned each chunk into a vector, and stored them in a vector database. When someone asks a question, the system finds the most similar chunks and passes them to the model with the question, so the answer is based on real text instead of guesses. I used LangChain to wire it together and tuned the chunk size and how many chunks to retrieve. I determined the chunk size by testing different sizes such as 200 words, 400 words, and 800 words and seeing which one gave the best results. 


I served it from Django as a REST API so the frontend could call it.

Result:

Answer relevance went up about 30%, and users could ask questions in plain English instead of hunting through files.



Which vector database, and why?

"I used [pgvector / Chroma / Pinecone]. I picked pgvector because it lives inside Postgres, so my documents and my vectors are in one database instead of two systems I have to keep in sync."

Pick the one you actually used. Chroma → "easy to run locally." Pinecone → "managed, no ops work."

Which embedding model?

"I used [OpenAI text-embedding-3-small / a free sentence-transformers model]. It was cheap and fast, and good enough for my documents. If accuracy mattered more I'd test a bigger one against the same test set."

How many documents / what scale?

"It was a personal project, so roughly 1200 documents and a few thousand chunks. It wasn't a scale challenge — the interesting part was making the answers correct, not making it big."

Say the real size. Small is fine. Pretending it was huge is not.

Why LangChain and not just call the API?

"It gave me the plumbing for free — loading files, splitting text, connecting to the vector DB. It let me get something working in a day. Once I understood the pieces, I could have written it myself, and for a simple pipeline that's often cleaner."

What broke, or what surprised you?

"The model answering a question when the data wasn't there surprised me most. It sounded completely confident and the number was invented. I only caught it because my test set had a question with no answer in it. That's what convinced me evals matter."

Deeper technical

Did you try re-ranking?

"Not in this version. Re-ranking means fetching more chunks than you need, say 20, then using a second smaller model to score which ones are actually relevant and keeping the top 5. It usually improves quality. It's the first thing I'd add next."

Hybrid search — keyword plus vector?

"Vector search is great for meaning but weak on exact strings — product codes, IDs, specific names. Hybrid runs both keyword and vector search and combines the results. I'd add this if the documents had a lot of codes or exact terms."

How do you handle updated documents?

"When a document changes, its old chunks are stale. I delete all chunks belonging to that document ID and re-process it. That's simplest and safest. Doing partial updates is faster but easy to get wrong."

How do you deal with tables or scanned PDFs?

"Tables are hard because chunking by character count cuts them in half and they lose meaning. A scanned PDF has no text at all, so you need OCR first. I kept to clean text documents in this project — I know these are the next real problem."

Honest limits are fine here. Pretending you solved OCR invites a question you can't answer.

What does a bad retrieval look like, and how do you debug it?

"A bad retrieval is when the model gives a wrong or vague answer, and the reason is that the right chunk never came back. So the first thing I do is print the retrieved chunks, not the answer. If the right text isn't in there, it's a retrieval problem — chunk size, embedding, or search. If the right text is there and the answer is still wrong, it's a prompt problem."


# Question to Ask:
- How do you currently evaluate extraction accuracy across such heterogeneous building documents?

- What's the biggest AI reliability problem the team is fighting right now?

- How is the Waterloo team structured relative to SF and New York?