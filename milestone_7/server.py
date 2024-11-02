from flask import Flask, request, jsonify

app = Flask(__name__)


employees = [
    {"id": 1, "name": "John Doe", "birthday": "Apr 18", "anniversary": "Apr 25", "department": "HR"},
    {"id": 2, "name": "Jane Smith", "birthday": "May 12", "anniversary": "Apr 30", "department": "HR"},
    {"id": 3, "name": "Bob Johnson", "birthday": "Apr 22", "anniversary": "Jun 1", "department": "Engineering"},
]


def filter_employees(month, department, key):
    filtered_employees = []
    for emp in employees:
        if emp[key].startswith(month[:3]) and emp["department"] == department:
            filtered_employees.append({"id": emp["id"], "name": emp["name"], key: emp[key]})
    return filtered_employees


@app.route('/birthdays', methods=['GET'])
def get_birthdays():
    month = request.args.get('month')
    department = request.args.get('department')
    birthday_employees = filter_employees(month, department, "birthday")

    response = {
        "total": len(birthday_employees),
        "employees": birthday_employees
    }
    return jsonify(response)


@app.route('/anniversaries', methods=['GET'])
def get_anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')
    anniversary_employees = filter_employees(month, department, "anniversary")

    response = {
        "total": len(anniversary_employees),
        "employees": anniversary_employees
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
