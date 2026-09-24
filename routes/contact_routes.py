from flask import Blueprint, request, jsonify

from extensions import db
from models.contact import Contact


contact_bp = Blueprint(
    "contacts",
    __name__,
    url_prefix="/api/contacts"
)


@contact_bp.route("", methods=["GET"])
def get_contacts():

    contacts = Contact.query.all()

    return jsonify([
        contact.to_dict()
        for contact in contacts
    ])


@contact_bp.route("", methods=["POST"])
def create_contact():

    data = request.get_json(silent=True) or {}

    required_fields = [
        "name",
        "phone",
        "email"
    ]

    for field in required_fields:

        if field not in data:
            return jsonify({
                "error": f"{field} is required"
            }), 400

    contact = Contact(
        name=data["name"],
        phone=data["phone"],
        email=data["email"]
    )

    db.session.add(contact)
    db.session.commit()

    return jsonify(contact.to_dict()), 201


@contact_bp.route("/<int:contact_id>", methods=["GET"])
def get_contact(contact_id):

    contact = db.session.get(
        Contact,
        contact_id
    )

    if contact is None:

        return jsonify({
            "error": "Contact not found"
        }), 404

    return jsonify(contact.to_dict())


@contact_bp.route("/<int:contact_id>", methods=["PUT"])
def update_contact(contact_id):

    contact = db.session.get(
        Contact,
        contact_id
    )

    if contact is None:

        return jsonify({
            "error": "Contact not found"
        }), 404

    data = request.get_json(silent=True) or {}

    if "name" in data:
        contact.name = data["name"]

    if "phone" in data:
        contact.phone = data["phone"]

    if "email" in data:
        contact.email = data["email"]

    db.session.commit()

    return jsonify(contact.to_dict())


@contact_bp.route("/<int:contact_id>", methods=["DELETE"])
def delete_contact(contact_id):

    contact = db.session.get(
        Contact,
        contact_id
    )

    if contact is None:

        return jsonify({
            "error": "Contact not found"
        }), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({
        "message": "Contact deleted successfully"
    })