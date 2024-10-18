from flask import Blueprint
from views.animal import get_all_animals, get_animal_by_id, add_animal, update_animal, delete_animal

bp_animal = Blueprint("bp_animal", __name__)

# Route to get all animals
@bp_animal.route("/animals", methods=["GET"])
def route_get_all_animals():
    return get_all_animals()

# Route to get animal by id
@bp_animal.route("/animals/<int:animal_id>", methods=["GET"])
def route_get_animal_by_id(animal_id):
    return get_animal_by_id(animal_id)

# Route to add new animal
@bp_animal.route("/animals", methods=["POST"])
def route_add_animal():
    return add_animal()

# Route to update animal
@bp_animal.route("/animals/<int:animal_id>", methods=["PUT"])
def route_update_animal(animal_id):
    return update_animal(animal_id)

# Route to delete animal
@bp_animal.route("/animals/<int:animal_id>", methods=["DELETE"])
def route_delete_animal(animal_id):
    return delete_animal(animal_id)

