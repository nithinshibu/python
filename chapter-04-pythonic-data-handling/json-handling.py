import json

user = {
    "id": 1,
    "name": "Nithin",
    "is_active": True
}

# Dict --> JSON
json_string = json.dumps(user)

# JSON --> Dict 
data = json.loads(json_string)

payload = '{"name": "Nithin"}'

data = json.loads(payload)

name = data.get("name")

# Common Backend Mistakes 

# 1. Assuming keys always exist

user["email"]  # crash --> use .get()

# 2. Deep nesting without checks
response = {}

response["user"]["profile"]["name"]  # risky

name = response.get("user", {}).get("profile", {}).get("name", "Unknown")

# 3. Modifying dict while iterating

for k in user:
    del user[k]  # ❌ runtime error

# 4. Confusing JSON vs dict

# JSON = string
# dict = Python object

response = '{"user": {"name": "Nithin"}}'  # JSON from API

data = json.loads(response)  # convert to dict

print(data["user"]["name"])  # safe to use now

response = '{"user": {"name": "Nithin"}}'

print(response["user"])  # ❌ ERROR, because response is a string, not a dict

request = {
    "users": [
        {"name": "A", "age": 25},
        {"name": "B", "age": 17}
    ]
}

# return only Adults 

users = request.get("users",[])

adults = [user for user in users if user.get("age") >=18]


response = {"count":len(adults),"data":adults}

