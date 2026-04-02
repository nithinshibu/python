user = {
    "id": 1,
    "name": "Nithin",
    "is_active": True
}

# Access Patterns 

user["name"]        # ❌ crashes if key missing
user.get("name")    # ✅ safe

name = user.get("name","Unknown")
# Always use .get() in APIs unless you're 100% sure

# Iterating dictionaries 

# Keys
for key in user:
    print(key)

#Values
for value in user.values():
    print(value)

# for Key + Value (Important)

for key, value in user.items():
    print(key,value)

# Nested dictionaries 

response = {
    "user": {
        "id": 1,
        "name": "Nithin"
    },
    "orders": [
        {"id": 101, "price": 100},
        {"id": 102, "price": 200}
    ]
}

# Access Nested data

user = response.get("user",{})
name = user.get("name")

#Prevents crashes in production


""" 
TRANSFORMING DATA (VERY IMPORTANT)

"""

# Extract the order prices 

orders = response["orders"]

prices = [order["price"] for order in orders]

# Filter the expensive orders 

expensive = [o for o in orders if o["price"] > 150]


# API response mapping 

users = [
    {"id": 1, "name": "A"},
    {"id": 2, "name": "B"}
]

result = [{"user_id":u["id"],"username":u["name"]} for u in users]

# Dictionary Comprehension 

nums = [1,2,3]

square_map = {x: x*x for x in nums}

users = [
    {"id": 1, "name": "A"},
    {"id": 2, "name": "B"}
]

user_map = {u["id"]: u for u in users}

""" 
Output:
{
    1: {"id": 1, "name": "A"},
    2: {"id": 2, "name": "B"}
}

"""

# Merging dictionaries 

a = {"x":1}
b = {"y":2}

merged = {**a,**b}

base = {"status": "success"}
data = {"user": user}

response = {**base, **data}

