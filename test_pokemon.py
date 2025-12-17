import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "YOUR_TOKEN_HERE"
HEADER = {"Content-Type": "application/json"}

def test_status_code():
    response = requests.get(url = f"{URL}/trainers?trainer_id=_", headers = HEADER)
    assert response.status_code == 200

def test_status_code():
    response = requests.get(url = f"{URL}/trainers", headers = HEADER)
    assert response.status_code == 200