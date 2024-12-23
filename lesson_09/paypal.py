STORAGE = [
    {
        "username": "john",
        "secret": "john123",
        "authorized": False,
    },
]


def authorize(token: str) -> bool:
    for index, item in enumerate(STORAGE):
        if item["secret"] == token:
            STORAGE[index]["authorized"] = True
            return True

    return False


def checkout(username: str, product_name: str, amount: int):
    for item in STORAGE:
        if item["username"] == username:
            if item["authorized"] is True:
                print(f"Checkout: {username}, {product_name}, {amount}")
            else:
                print(f"{username} is not authorized")
