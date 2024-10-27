import csv
import sys
from collections import defaultdict


def parse_arguments():
    if len(sys.argv) != 3:
        print("Usage: python3 report.py <database_file> <month>")
        sys.exit(1)
    database_file = sys.argv[1]
    month = sys.argv[2].lower()
    return database_file, month


def read_employee_data(filename):
    employees = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row)
    return employees


def generate_report(employees, month):
    birthdays = defaultdict(list)
    anniversaries = defaultdict(list)
    
    month_map = {
        'january': '01',
        'february': '02',
        'march': '03',
        'april': '04',
        'may': '05',
        'june': '06',
        'july': '07',
        'august': '08',
        'september': '09',
        'october': '10',
        'november': '11',
        'december': '12'
    }

    for employee in employees:
        
        birthday_month = employee['Birthday'].split('-')[1]
        if birthday_month == month_map.get(month):
            birthdays[employee['Department']].append(employee['Name'])

        
        hiring_month = employee['Hiring Date'].split('-')[1]
        if hiring_month == month_map.get(month):
            anniversaries[employee['Department']].append(employee['Name'])

    return birthdays, anniversaries


def print_report(birthdays, anniversaries):
    print(f"Report for {month.capitalize()} generated")
    
    print("--- Birthdays ---")
    total_birthdays = sum(len(names) for names in birthdays.values())
    print(f"Total: {total_birthdays}")
    print("By department:")
    for dept, names in birthdays.items():
        print(f"- {dept}: {len(names)}")

    print("--- Anniversaries ---")
    total_anniversaries = sum(len(names) for names in anniversaries.values())
    print(f"Total: {total_anniversaries}")
    print("By department:")
    for dept, names in anniversaries.items():
        print(f"- {dept}: {len(names)}")


if __name__ == "__main__":
    database_file, month = parse_arguments()
    employees = read_employee_data(database_file)
    birthdays, anniversaries = generate_report(employees, month)
    print_report(birthdays, anniversaries)
