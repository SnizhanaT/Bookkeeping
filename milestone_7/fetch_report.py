import sys
import requests

def fetch_report(month, department):
    base_url = "http://127.0.0.1:5000"

    
    birthday_response = requests.get(f"{base_url}/birthdays", params={"month": month, "department": department})
    if birthday_response.status_code != 200:
        print("Failed to fetch birthdays.")
        return

   
    anniversary_response = requests.get(f"{base_url}/anniversaries", params={"month": month, "department": department})
    if anniversary_response.status_code != 200:
        print("Failed to fetch anniversaries.")
        return

    
    birthdays = birthday_response.json()
    anniversaries = anniversary_response.json()

    
    print(f"Report for {department} department for {month.capitalize()} fetched.")
    
    print(f"\nTotal Birthdays: {birthdays['total']}")
    print("Birthdays:")
    for employee in birthdays["employees"]:
        print(f"- {employee['birthday']}, {employee['name']}")
    
    print(f"\nTotal Anniversaries: {anniversaries['total']}")
    print("Anniversaries:")
    for employee in anniversaries["employees"]:
        print(f"- {employee['anniversary']}, {employee['name']}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 fetch_report.py <month> <department>")
        sys.exit(1)

    month = sys.argv[1]
    department = sys.argv[2]
    fetch_report(month, department)
