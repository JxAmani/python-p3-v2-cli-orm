from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()


# Department functions

def list_departments():
    """List all departments."""
    departments = Department.get_all()
    if not departments:
        print("No departments found.")
    for dept in departments:
        print(dept)


def find_department_by_name():
    """Find a department by name."""
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    if department:
        print(department)
    else:
        print(f"Department '{name}' not found.")


def find_department_by_id():
    """Find a department by ID."""
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        print(department)
    else:
        print(f"Department {id_} not found.")


def create_department():
    """Create a new department."""
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f"Success: {department}")
    except Exception as exc:
        print("Error creating department:", exc)


def update_department():
    """Update an existing department."""
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if not department:
        print(f"Department {id_} not found.")
        return

    try:
        name = input("Enter the department's new name: ")
        location = input("Enter the department's new location: ")
        department.name = name
        department.location = location
        department.update()
        print(f"Success: {department}")
    except Exception as exc:
        print("Error updating department:", exc)


def delete_department():
    """Delete a department by ID."""
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        department.delete()
        print(f"Department {id_} deleted.")
    else:
        print(f"Department {id_} not found.")


# Employee functions (placeholders for lab)

def list_employees():
    """List all employees."""
    employees = Employee.get_all()
    if not employees:
        print("No employees found.")
    for emp in employees:
        print(emp)


def find_employee_by_name():
    pass


def find_employee_by_id():
    pass


def create_employee():
    pass


def update_employee():
    pass


def delete_employee():
    pass


def list_department_employees():
    pass
