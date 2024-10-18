from flask import jsonify, request


employees = [
    {"id": 1, "name": "John", "email": "john@gmail.com", "phone": "761-167", "role": "manager"},
    {"id": 2, "name": "Jane", "email": "jane@gmail.com", "phone": "716-617", "role": "secretary"},
    {"id": 3, "name": "Jim", "email": "jim@gmail.com", "phone": "167-761", "role": "supervisor"},
    {"id": 4, "name": "Jill", "email": "jill@gmail.com", "phone": "617-716", "role": "staff"},
    {"id": 5, "name": "Jack", "email": "jack@gmail.com", "phone": "617-716", "role": "admin"},
]

# Get all employees data
def get_all_employees():
    return jsonify({"employees": employees})

# Get employee by id
def get_employee_by_id(employee_id):
    employee = next((employee for employee in employees if employee["id"] == employee_id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"Error": "Employee not found"}), 404
    
# Add new employee
def add_employee():
    employee_data = request.get_json()
    employee_id = len(employees) + 1
    employee_data["id"] = employee_id
    employees.append(employee_data)
    return jsonify({"id": id, "employee": employee_data}), 201

# Update employee
def update_employee(employee_id):
    employee = next((employee for employee in employees if employee["id"] == employee_id), None)
    if employee:
        employee_update_data = request.get_json()
        employee.update(employee_update_data)
        return jsonify(employee)
    else:
        return jsonify({"Error": "Employee not found"}), 404
    
# Delete employee
def delete_employee(employee_id):
    global employees
    employee = next((employee for employee in employees if employee["id"] == employee_id), None)
    if employee:
        employees = [employee for employee in employees if employee["id"] != employee_id]
        return jsonify({"message": "Employee deleted successfully"})
    else:
        return jsonify({"Error": "Employee not found"})