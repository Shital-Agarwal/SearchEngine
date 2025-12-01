# Simple Search Engine

## Overview
This project is a small API service that provides a search endpoint `/search`. It queries the external `/messages` API and returns filtered, paginated results.

## Requirements
- Python 3.12+
- FastAPI
- httpx
- uvicorn

## How to Run Locally
1. Install dependencies:
pip install -r requirements.txt

## Run the server:
2. uvicorn main:app --host 0.0.0.0 --port 8000 --reload

## Test endpoint:
3. GET http://127.0.0.1:8000/search?query=hello&page=1&page_size=5

## Bonus 1: Design Notes
1. Several alternative approaches were considered for building the search engine:

● Server-side filtering (current approach)
● Fetch all messages from the external API on each request.
● Filter messages containing the query.
● Pros: Simple, minimal setup.
● Cons: Can be slow if the dataset grows.

2. Pre-indexing messages

● Periodically fetch messages and store in memory (Redis, SQLite).
● Use in-memory filtering or simple full-text search.
● Pros: Faster responses for repeated queries.
● Cons: Requires periodic updates.

3. Full-text search engine (Elasticsearch / Meilisearch)

● Index messages in a dedicated search engine.
● Supports relevance scoring, fuzzy search, and extremely fast queries.
● Pros: Very fast, scalable, feature-rich.
● Cons: More setup and infrastructure needed.

## Bonus 2: Data Insights (Reducing Latency)
To reduce latency to ~30ms, we can:

1. Use in-memory caching
● Cache results for frequent queries using Redis or Python cachetools.

2. Pre-fetch and index messages
● Avoid fetching all messages on every request by maintaining a local copy.

3. Use a dedicated search engine
● Elasticsearch or Meilisearch can return results almost instantly.

4. Optimize network requests
● Keep-alive connections, HTTP/2, and async requests reduce overhead.

5. Efficient pagination
● Only process and return the requested page, instead of filtering the entire dataset every time.


