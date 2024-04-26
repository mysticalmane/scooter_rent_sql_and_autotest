# headers for HTTP request that points, that body request will be in a JSON format
headers = {
    "Content-Type": "application/json",
}

# Data for creating a new order
order_body = {
    "firstName": "Alex",
    "lastName": "Kostin",
    "address": "Testirovochnaia, 142 apt.",
    "metroStation": 6,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-04-30",
    "comment": "Hello world!",
    "color": [
        "BLACK"
    ]
}
