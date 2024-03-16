import requests
import pytest

Host = "https://api.pokemonbattle.me/v2"
Trainer_ID = "220"
Trainer_token = "890b930ee2d8311051d0a20a47216f15"
HEADERS = {"Content-Type" :"application/json",
           "trainer_token" :Trainer_token  }

def test_status_code ():
    response = requests.get(url= f'{Host}/trainers', params = {"trainer_id" : 220 })  
    assert response.status_code == 200 


def test_part_of_response():
    response = requests.get(url= f'{Host}/trainers', params = {"trainer_id" : 220 }) 
    assert response.json()["data"][0]["id"] == "220"

 
def test_trainer_name():
    response = requests.get(url= f'{Host}/trainers', params = {"trainer_id" : 220 }) 
    assert response.json()["data"][0]["trainer_name"] == "Олег"

  