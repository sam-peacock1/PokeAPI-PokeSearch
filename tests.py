import pytest
from poke_api import *
import requests

### Unit Tests
# Verify the pokeAPI is working
def test_get_pokemon():
    pokemon = get_pokemon_info("Pikachu")
    assert(pokemon["name"] == 'pikachu')
    assert(pokemon["types"] == ['electric'])
    assert(pokemon["height"] == 4)
    assert(pokemon["weight"] == 60)
    assert(pokemon["abilities"] == ['static', 'lightning-rod'])

### Integration Tests
# Connection self-test, verify we can get to the search page, and search a pokemon
# Must be run with server running
#def test_search():
#    headers = {'Accept-Encoding': 'identity'}
#    r = requests.get(f"http://{host}:{port}/", headers=headers)
#    assert(r.status_code == 200)
#    r = requests.get(f"http://{host}:{port}/pokemon?pokemon=pikachu", headers=headers)
#    assert(r.status_code == 200)
#
#def test_not_found():
#    headers = {'Accept-Encoding': 'identity'}
#    r = requests.get(f"http://{host}:{port}/pokemon?pokemon=none", headers=headers)
#    assert(r.status_code == 200)