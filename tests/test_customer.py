from client import client


def test_customer():
    """
    test customer crud methods
    """

    # create customer
    response = client.post(
        "/customer",
        json={
            "data": {
                "username": "tcustomer",
                "password": "testpassword",
                "email": "tcustomer@gmail.com",
            }
        },
    )

    assert response.status_code == 201
    assert response.json()["data"]["username"] == "tcustomer"
    assert response.json()["data"]["email"] == "tcustomer@gmail.com"

    print("Customer created successfully!")

    # get customer
    response = client.get("/customer")
    first = response.json()["data"][0]

    assert response.status_code == 200

    print("Customer retrieved successfully!")

    # delete customer
    response = client.delete(f"/customer/{first['id']}")
    assert response.status_code == 200

    print("Customer deleted successfully!")


if __name__ == "__main__":
    test_customer()
