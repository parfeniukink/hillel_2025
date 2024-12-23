import abc
from typing import Protocol


class PaymentProvider(Protocol):
    def checkout(self, username: str, amount: int): ...


# class PaymentProvider(abc.ABC):
#     @abc.abstractmethod
#     def checkout(self, username: str, amount: int):
#         """"""


class Stripe:
    def checkout(self, username: str, amount: int):
        print("...")


class PayPal:
    pass


def main(payment_provider: PaymentProvider):
    payment_provider.checkout()  # type: ignore


main(PayPal())
