import requests
import pytest


base_url = "https://petstore.swagger.io/v2"



def create_pet(name, status):
    url = f"{base_url}/pet"
    headers = {"Content-Type": "application/json"}
    payload = {
        "name": name,
        "status": status
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()



def get_pet_by_id(pet_id):
    url = f"{base_url}/pet/{pet_id}"
    response = requests.get(url)
    return response.json()


def update_pet_status(pet_id, status, name):
    url = f"{base_url}/pet"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    payload = {
        "id": pet_id,
        "name": name,
        "status": status
    }
    response = requests.put(url, headers=headers, json=payload)
    return response.json()



def delete_pet(pet_id):
    url = f"{base_url}/pet/{pet_id}"
    response = requests.delete(url)
    return response.json()



def test_create_pet():
    name = "Güneş"
    status = "available"
    response = create_pet(name, status)
    assert response["name"] == name
    assert response["status"] == status



def test_get_pet_by_id():
    name = "Hera"
    status = "available"
    pet_id = create_pet(name, status)["id"]
    response = get_pet_by_id(pet_id)
    assert response["name"] == name
    assert response["status"] == status



def test_update_pet_status():
    name = "Bomba"
    status = "available"
    pet_id = create_pet(name, status)["id"]
    new_status = "tampa"
    response = update_pet_status(pet_id, new_status, name)
    assert response["name"] == name
    assert response["status"] == new_status



def test_delete_pet():
    name = "Ela"
    status = "available"
    pet_id = create_pet(name, status)["id"]
    response = delete_pet(pet_id)
    assert response["code"] == 200
    assert response["type"] == "unknown"
    assert response["message"] == str(pet_id)



def test_delete_nonexistent_pet():
    response = delete_pet('abc')
    assert response["code"] == 404
    assert response["type"] == "unknown"



def test_get_nonexistent_pet():
    pet_id = 9999998
    response = get_pet_by_id(pet_id)
    assert response["code"] == 1
    assert response["type"] == "error"
    assert response["message"] == "Pet not found"



def test_update_nonexistent_pet_status():
    pet_id = "abc"
    name = "Baboli"
    new_status = "sold"
    response = update_pet_status(pet_id, new_status, name)
    assert response["code"] == 500
    assert response["type"] == "unknown"
    assert response["message"] == "something bad happened"



if __name__ == "__main__":
    pytest.main()
