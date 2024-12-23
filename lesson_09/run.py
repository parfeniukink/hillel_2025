"""
Abstractions...
Template
SOLID...
"""

from abc import ABC, abstractmethod
from typing import Type

from dataclasses import dataclass


STRIPE_ACCESS_TOKEN = "3f91b4bc-2713-418f-bbc9-d3f93f67b1db"
PAYPAL_CREDENTIALS = {
    "username": "hillel",
    "password": "hillel123",
}


@dataclass
class Card:
    number: int
    expire_date: str
    cvv: int


@dataclass
class Product:
    name: str
    price: int


@dataclass
class User:
    id: int
    email: str
    age: int
    card: Card


class PaymentProvider(ABC):
    def __init__(self, user: User):
        self.user: User = user

    @abstractmethod
    def healthcheck(self):
        """..."""

    @abstractmethod
    def authorize(self, **kwargs):
        """..."""

    @abstractmethod
    def checkout(self, product: Product, **kwargs):
        """..."""


class Stripe(PaymentProvider):
    def authorize(self, **kwargs):
        token = kwargs.get("token", "")
        # StripeAPI.authorize(
        #         token=token,
        #         user_email=self.user.email
        #         card_number=self.user.card.number
        #         expire_date=self.user.card.exire_date
        #         cvv=self.user.card.cvv
        # )
        print("Authorized with Stripe")

    def _check_card(self):
        if "444" in str(self.user.card.number):
            raise ValueError("card invalid")

    def checkout(self, product: Product, **kwargs):
        self._check_card()
        # StripeAPI.checkout(user_email=self.user.email, price=product.price)
        print(f"Checkout with {self.__class__.__name__}. {product}")

    def healthcheck(self):
        # if StripeAPI.healthcheck() is False:
        #     raise Exception("Stripe is not available")
        return True


class PayPal(PaymentProvider):
    def authorize(self, **kwargs):
        username = kwargs.get("username", "")
        password = kwargs.get("password", "")

        # PayPal.authorize(
        #         username=username,
        #         password=password,
        #         user_email=self.user.email
        #         card=self.user.card.as_dict()
        # )
        print("Authorized with PayPal")

    def checkout(self, product: Product, **kwargs):
        # PayPal.checkout(user_email=self.user.email, price=product.price)
        print(f"Checkout with {self.__class__.__name__}. {product}")

    def healthcheck(self):
        # if PayPalAPI.healthcheck() is False:
        #     raise Exception("Stripe is not available")
        return True


def provider_dispatcher(name: str, user: User) -> PaymentProvider:
    if name == "stripe":
        return Stripe(user=user)
    elif name == "paypal":
        return PayPal(user=user)
    else:
        raise Exception(f"Provider {name} is not supported")


def main():
    john = User(
        id=1,
        email="john@emai.com",
        age=30,
        card=Card(
            number=4545000011112222,
            expire_date="12/25",
            cvv=300,
        ),
    )
    marry = User(
        id=2,
        email="marry@emai.com",
        age=20,
        card=Card(
            number=4545333311112222,
            expire_date="12/25",
            cvv=324,
        ),
    )

    samsung = Product(name="Samsung", price=30_000)
    iphone = Product(name="iPhone", price=32_000)

    # stripe_credentials = {"token": "........"}
    paypal_credentials = PAYPAL_CREDENTIALS

    payment_provider: PaymentProvider = provider_dispatcher("paypal", marry)
    payment_provider.healthcheck()
    payment_provider.authorize(**paypal_credentials)
    payment_provider.checkout(product=iphone)


main()
