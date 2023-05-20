import json

d = {
    20: [
        {
            "name": "RUB",
            "cost": 0.01354,
            "amount": 1000
        },
                {
            "name": "BTC",
            "cost": 36000,
            "amount": 0.03,
        }
    ],
    21: [
        {
            "name": "RUB",
            "cost": 0.01354,
            "amount": 2000,
        },
                {
            "name": "BTC",
            "cost": 72000,
            "amount": 0.03
        }
    ]    
}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

def load_data():
    with open("data.json") as f:
        data = json.load(f)
    return data

save_data(d)