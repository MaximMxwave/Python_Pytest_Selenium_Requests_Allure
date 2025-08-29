import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ТОКЕН_ТРЕНЕРА'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '12291'

def test_status_code():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.status_code == 200

def test_response_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Максибон'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Максибон'), ('id', '12291')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID,})
    assert response_parametrize.json()["data"][0][key] == value