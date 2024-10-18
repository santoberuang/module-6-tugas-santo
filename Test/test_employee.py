import pytest
from flask import Flask
from app import employee_bp 

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(employee_bp)
    
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_all_employees(client):

    response = client.get('/employees')
    assert response.status_code == 200


def test_get_employee_by_id(client):

    response = client.get('/employees/1')
    assert response.status_code == 200

def test_add_employee(client):
    response = client.post('/employees', json={  
        'name': 'LauraBasuki',  
        'email': 'laura@mail.com',
        'phone_number': '777-777',
        'role': 'office_girl' 
    })
    assert response.status_code == 201

def test_update_employee(client):

    response = client.put('/employees/1', json={
        'role': 'Boss',
        'phone_number': '999-999'
    })
    assert response.status_code == 200

def test_delete_employee(client):
    post_response = client.post('/employees', json={
        'name': 'Jill',
        'email': 'jill@gmail.com',
        'phone_number': '617-716',
        'role': 'staff'
    })
    employee_id = post_response.json['id']

    delete_response = client.delete(f'/employees/{employee_id}')
    assert delete_response.status_code == 200

    get_response = client.get(f'/employees/{employee_id}')
    assert get_response.status_code == 404