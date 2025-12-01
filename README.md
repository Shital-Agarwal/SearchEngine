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


