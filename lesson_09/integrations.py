class Stripe:
    STORAGE = [
        {
            "username": "john",
            "password": "john123",
            "authorized": False,
        },
    ]

    @classmethod
    def authorize(cls, username: str, password: str) -> bool:
        for index, item in enumerate(cls.STORAGE):
            if item["username"] == username and item["password"] == password:
                cls.STORAGE[index]["authorized"] = True
                return True

        return False

    @classmethod
    def checkout(cls, username: str, product_name: str, amount: int):
        for item in cls.STORAGE:
            if item["username"] == username:
                if item["authorized"] is True:
                    print(f"Checkout: {username}, {product_name}, {amount}")
                else:
                    print(f"{username} is not authorized")


class PayPal:
    STORAGE = [
        {
            "username": "john",
            "secret": "john123",
            "authorized": False,
        },
    ]

    @classmethod
    def authorize(cls, token: str) -> bool:
        for index, item in enumerate(cls.STORAGE):
            if item["secret"] == token:
                cls.STORAGE[index]["authorized"] = True
                return True

        return False

    @classmethod
    def checkout(cls, username: str, product_name: str, amount: int):
        for item in cls.STORAGE:
            if item["username"] == username:
                if item["authorized"] is True:
                    print(f"Checkout: {username}, {product_name}, {amount}")
                else:
                    print(f"{username} is not authorized")
