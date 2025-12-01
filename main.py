from fastapi import FastAPI, Query
from typing import List
import httpx

app = FastAPI(title="Simple Search Engine")

EXTERNAL_API = "https://november7-730026606190.europe-west1.run.app/messages"
PAGE_SIZE = 10 

cache = {}

@app.get("/search")
async def search(query: str = Query(..., min_length=1), page: int = 1, page_size: int = PAGE_SIZE):
    cache_key = f"{query}-{page}-{page_size}"
    if cache_key in cache:
        return cache[cache_key]

    async with httpx.AsyncClient(timeout=0.05) as client:
        response = await client.get(EXTERNAL_API)
        response.raise_for_status()
        messages = response.json()

    filtered = [msg for msg in messages if query.lower() in msg.get("content", "").lower()]

    start = (page - 1) * page_size
    end = start + page_size
    paginated = filtered[start:end]

    result = {
        "query": query,
        "page": page,
        "page_size": page_size,
        "total_results": len(filtered),
        "results": paginated
    }

    cache[cache_key] = result

    return result
