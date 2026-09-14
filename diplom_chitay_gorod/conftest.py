# conftest.py
import pytest

# Константы для API тестов
BASE_URL = "https://web-gate.chitai-gorod.ru/api/v2/"
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcml..."
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36..."

HEADERS = {
    "User-Agent": USER_AGENT,
    "authorization": f"Bearer {TOKEN}"
}