from flask import Flask, jsonify, request
from datastructures import FamilyStructure
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Inicialización de la instancia de la familia Jackson
jackson_family = FamilyStructure('Jackson')

# Agregamos algunos miembros iniciales a la familia
jackson_family.add_member({
    "first_name": "John",
    "age": 33,
    "lucky_numbers": [7, 13, 22]
})
jackson_family.add_member({
    "first_name": "Jane",
    "age": 35,
    "lucky_numbers": [10, 14, 3]
})
jackson_family.add_member({
    "first_name": "Jimmy",
    "age": 5,
    "lucky_numbers": [1]
})

# Endpoint para obtener todos los miembros de la familia
@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Endpoint para obtener un miembro específico por ID
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"message": "Member not found"}), 404

# Endpoint para añadir un nuevo miembro a la familia
@app.route('/member', methods=['POST'])
def add_member():
    member_data = request.get_json()
    jackson_family.add_member(member_data)
    return jsonify({"message": "Member added successfully"}), 200

# Endpoint para eliminar un miembro de la familia por ID
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        jackson_family.delete_member(member_id)
        return jsonify({"done": True}), 200
    else:
        return jsonify({"message": "Member not found"}), 404

# Punto de entrada principal para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)

