def binary_search(data, followers):
    if len(data) == 1 and data[0]["followers"] == followers:
        return data[0]["name"]
    elif len(data) == 1 and data[0]["followers"] != followers:
        return None

    if data[len(data)//2]["followers"] < followers:
        return binary_search(data[len(data)//2:], followers)
    elif data[len(data)//2]["followers"] > followers:
        return binary_search(data[:len(data)//2], followers)
    else:
        return data[len(data)//2]["name"]
            


# don't touch below this line


def test(data, followers):
    name = binary_search(data, followers)
    print(f"Searching for: {followers}")
    print(f"Found: {name}")
    print("====================================")


def main():
    test_data = [
        {"name": "John", "followers": 5},
        {"name": "Jane", "followers": 10},
        {"name": "James", "followers": 15},
        {"name": "Judy", "followers": 20},
        {"name": "Jenny", "followers": 25},
        {"name": "Jasper", "followers": 30},
        {"name": "Jack", "followers": 35},
        {"name": "Jill", "followers": 40},
        {"name": "Bob", "followers": 45},
        {"name": "Borice", "followers": 50},
        {"name": "Boris", "followers": 55},
        {"name": "Donald", "followers": 60},
        {"name": "Doris", "followers": 65},
        {"name": "Derek", "followers": 70},
        {"name": "Diana", "followers": 75},
        {"name": "Dennis", "followers": 80},
        {"name": "Daisy", "followers": 85},
        {"name": "Duke", "followers": 90},
        {"name": "Duke", "followers": 95},
        {"name": "Duke", "followers": 100},
    ]
    to_search = [50, 40, 30, 20, 5000]
    for v in to_search:
        test(test_data, v)


main()
