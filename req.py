import requests
import json

#получение списка питомцев
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

#создание питомца
info_pet = {
  "id": 1,
  "category": {
    "id": 2,
    "name": "Cat"
  },
  "name": "Koshka",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(info_pet, ensure_ascii=False))

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

#изменения данных питомца
new_info_pet = {
  "id": 1,
  "category": {
    "id": 2,
    "name": "Koshka"
  },
  "name": "Viva",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}


res = requests.put(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(new_info_pet, ensure_ascii=False))

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

#удаление питомца
res = requests.delete(f"https://petstore.swagger.io/v2/pet/1", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(new_info_pet, ensure_ascii=False))

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))