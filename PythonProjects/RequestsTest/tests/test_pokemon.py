import requests
import pytest

def test_cheack_status_code():
    response = requests.get('https://pokemonbattle.me:9104/trainers')
    assert response.status_code == 200

def test_part_of_response():
        response = requests.get('https://pokemonbattle.me:9104/trainers', 
                                params = {'trainer_id' : 1875})
        assert response.json()['trainer_name'] == 'Elena'