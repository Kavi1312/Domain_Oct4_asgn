import requests
from tabulate import tabulate
import time

# List of subdomains to check
subdomains = [
    "sub1.example.com",
    "sub2.example.com",
    "sub3.example.com"
]

# Function to check the status of a subdomain
def check_status(subdomain):
    try:
        response = requests.get(f"http://{subdomain}", timeout=5)
        if response.status_code == 200:
            return "Up"
        else:
            return f"Down ({response.status_code})"
    except requests.RequestException:
        return "Down"

# Function to display the results in a table
def display_table(subdomain_statuses):
    table = []
    for subdomain, status in subdomain_statuses.items():
        table.append([subdomain, status])
    print(tabulate(table, headers=["Subdomain", "Status"], tablefmt="grid"))

# Function to check the status of all subdomains every minute
def check_subdomains(subdomains):
    while True:
        subdomain_statuses = {}
        for subdomain in subdomains:
            status = check_status(subdomain)
            subdomain_statuses[subdomain] = status

        # Display the statuses in a table
        display_table(subdomain_statuses)
        
        # Wait for 60 seconds before checking again
        time.sleep(60)

# Start checking the subdomains
check_subdomains(subdomains)
