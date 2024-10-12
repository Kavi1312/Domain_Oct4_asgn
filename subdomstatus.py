import requests
from tabulate import tabulate
import time
import os

# List of subdomains with corresponding ports
subdomains = [
    "sub1.localhost:8081",
    "sub2.localhost:8082",
    "sub3.localhost:8083"
]

# Function to check the status of a subdomain
def check_status(subdomain, protocol="http"):
    try:
        response = requests.get(f"{protocol}://{subdomain}", timeout=5)
        if response.status_code == 200:
            return "Up"
        else:
            return f"Down ({response.status_code})"
    except requests.ConnectionError:
        return "Down (Connection Error)"
    except requests.Timeout:
        return "Down (Timeout)"
    except requests.RequestException as e:
        return f"Down ({str(e)})"

# Function to display the results in a table
def display_table(subdomain_statuses):
    # Clear the screen for better display
    os.system('cls' if os.name == 'nt' else 'clear')  # Works for Windows (cls) and Linux/macOS (clear)
    
    table = []
    for subdomain, status in subdomain_statuses.items():
        table.append([subdomain, status])
    print(tabulate(table, headers=["Subdomain", "Status"], tablefmt="grid"))

# Function to check the status of all subdomains every minute
def check_subdomains(subdomains):
    try:
        while True:
            subdomain_statuses = {}
            for subdomain in subdomains:
                status = check_status(subdomain)
                subdomain_statuses[subdomain] = status

            # Display the statuses in a table
            display_table(subdomain_statuses)
            
            # Wait for 60 seconds before checking again
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nExiting the script...")
        exit(0)

# Start checking the subdomains
check_subdomains(subdomains)
        
        
