from flask import Blueprint
from views.employee import get_all_employees, get_employee_by_id, add_employee, update_employee, delete_employee

bp_employee = Blueprint("bp_employee", __name__)

# Route to get all employees
@bp_employee.route("/employees", methods=["GET"])
def route_get_all_employees():
    return get_all_employees()


# Route to get employee by id
@bp_employee.route("/employees/<int:employee_id>", methods=["GET"])
def route_get_employee_by_id(employee_id):
    return get_employee_by_id(employee_id)


# Route to add new employee
@bp_employee.route("/employees", methods=["POST"])  
def route_add_employee():
    return add_employee()


# Route to update employee
@bp_employee.route("/employees/<int:employee_id>", methods=["PUT"])
def route_update_employee(employee_id):
    return update_employee(employee_id)


# Route to delete employee
@bp_employee.route("/employees/<int:employee_id>", methods=["DELETE"])
def route_delete_employee(employee_id):
    return delete_employee(employee_id)
