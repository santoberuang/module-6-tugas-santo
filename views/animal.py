from flask import jsonify, request


animals = [
    {"id": 1, "species": "dog", "age": 5, "gender": "male"},
    {"id": 2, "species": "cat", "age": 3, "gender": "female"},
    {"id": 3, "species": "fish", "age": 1, "gender": "male"},
    {"id": 4, "species": "snake", "age": 7, "gender": "female"},
    {"id": 5, "species": "bird", "age": 2, "gender": "male"},
]

# Get all animals data
def get_all_animals():
    return jsonify({"animals": animals})

# Get animal by id

def get_animal_by_id(animal_id):
    animal = next((animal for animal in animals if animal["id"] == animal_id), None)
    if animal:
         return jsonify(animal)
    else:
        return jsonify({"Error": "Animal not found"}), 404
    

# Add new animal
def add_animal():
    animal_data = request.get_json()
    animal_id = len(animals) + 1
    animal_data["id"] = animal_id
    animals.append(animal_data)
    return jsonify({"id": id, "animal": animal_data}), 201

# Update animal
def update_animal(animal_id):
    animal = next((animal for animal in animals if animal["id"] == animal_id), None)
    if animal:
        animal_update_data = request.get_json()
        animal.update(animal_update_data)
        return jsonify(animal)
    else:
        return jsonify({"Error": "Animal not found"}), 404
    
# Delete animal
def delete_animal(animal_id):
    global animals
    animal = next((animal for animal in animals if animal["id"] == animal_id), None)
    if animal:
        animals.remove(animal)
        return jsonify({"message": "Animal deleted successfully"})
    else:
        return jsonify({"Error": "Animal not found"}), 404