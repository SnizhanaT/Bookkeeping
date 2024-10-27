import csv
from faker import Faker
import random

# Initialize Faker
fake = Faker()


def random_hire_date():
    year = random.randint(2000, 2023)  # Random year between 2000 and 2023
    month = random.randint(1, 12)      # Random month
    day = random.randint(1, 28)         
    return f"{year}-{month:02d}-{day:02d}"


def random_birthday():
    year = random.randint(1960, 2005)  
    month = random.randint(1, 12)      # Random month
    day = random.randint(1, 28)         
    return f"{year}-{month:02d}-{day:02d}"


def generate_employee_data(num_employees):
    employees = []
    departments = ['Sales', 'Marketing', 'Engineering', 'HR', 'Finance']

    for _ in range(num_employees):
        employee = {
            'Name': fake.name(),
            'Hiring Date': random_hire_date(),
            'Department': random.choice(departments),
            'Birthday': random_birthday()
        }
        employees.append(employee)

    return employees


def write_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    num_employees = 20  # Specify the number of employees you want to generate
    employee_data = generate_employee_data(num_employees)
    write_to_csv('database.csv', employee_data)
    print(f"Generated {num_employees} employee records and saved to database.csv.")