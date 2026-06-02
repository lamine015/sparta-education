from pymongo import MongoClient
import requests

client = MongoClient()

db = client["starwars"]

characters = db["characters"]
starships = db["starships"]

response = requests.get("https://swapi.info/api/starships")

ships = response.json()

for ship in ships:
    pilot_ids = []
    for pilot_url in ship.get("pilots", []):
        character = characters.find_one({"url": pilot_url})
        if character:
            pilot_ids.append({character["id"]})

    ship["pilots"] = pilot_ids

starships.insert_many(ships)

print(f"Succesfully inserted {len(ships)} starships")
