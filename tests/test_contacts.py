def test_home(client):

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "Contacts API is running"


def test_create_contact(client):

    response = client.post(
        "/api/contacts",
        json={
            "name": "Aadarsh",
            "phone": "9876543210",
            "email": "aadarsh@example.com"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["name"] == "Aadarsh"
    assert data["phone"] == "9876543210"
    assert data["email"] == "aadarsh@example.com"


def test_get_contacts(client):

    client.post(
        "/api/contacts",
        json={
            "name": "Aadarsh",
            "phone": "9876543210",
            "email": "aadarsh@example.com"
        }
    )

    response = client.get(
        "/api/contacts"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) == 1
    assert data[0]["name"] == "Aadarsh"


def test_get_single_contact(client):

    create_response = client.post(
        "/api/contacts",
        json={
            "name": "Rahul",
            "phone": "8888888888",
            "email": "rahul@example.com"
        }
    )

    contact_id = create_response.get_json()["id"]

    response = client.get(
        f"/api/contacts/{contact_id}"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["name"] == "Rahul"


def test_update_contact(client):

    create_response = client.post(
        "/api/contacts",
        json={
            "name": "Rahul",
            "phone": "8888888888",
            "email": "rahul@example.com"
        }
    )

    contact_id = create_response.get_json()["id"]

    response = client.put(
        f"/api/contacts/{contact_id}",
        json={
            "phone": "7777777777"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["phone"] == "7777777777"


def test_delete_contact(client):

    create_response = client.post(
        "/api/contacts",
        json={
            "name": "Rahul",
            "phone": "8888888888",
            "email": "rahul@example.com"
        }
    )

    contact_id = create_response.get_json()["id"]

    response = client.delete(
        f"/api/contacts/{contact_id}"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == \
        "Contact deleted successfully"


def test_missing_field(client):

    response = client.post(
        "/api/contacts",
        json={
            "name": "Aadarsh"
        }
    )

    assert response.status_code == 400