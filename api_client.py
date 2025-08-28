from typing import List, Optional
import requests
from requests.exceptions import RequestException

USERS_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_and_display_users(num_users:int)
    Optional[list[dict]]
if not isinstance(num_users,int) or num_users <=0:
    print("fetch_and_display_users: num_users must be a positive integer.")
    return0
try:
    resp = requests.get(USERS_URL,timeout = 10)
except RequestException as e:
    print(f"Network error while fetching users: {e}")
    return0
if resp.status_code!= 200:
    print(f"Reuest failed: status code {resp.status_code} (expected 200).")
    return0
try:
    users = resp.json()
except ValueError as e:
    print(f"ERROR PARSING JSON response: {e}")
    return0
results = []
for i,user in enumerate(users[:num_users]):
    try:
        name = user["name"]
        email = user["email"]
        city = user["address"]["city"]
    except(KeyError,TypeError):
        print(f"Warning: user at index {i} missing expected fields: {user}")
        continue
    print(f":{i+1} {name} {email} {city}"):
    results.append(user)
    
            
if__name__ == "__main__":
print("---fetch 3 users ---")
fetch_and_display_users(3)

print("\n---fetch 15 users(will show up to available users) ---")
fetch_and_display_users(15)