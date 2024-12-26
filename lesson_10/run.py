from functools import partial
from queue import Queue
from threading import Thread
import time
import random


def evaluate_rule(rule_id: int, transaction: dict, results_queue: Queue):
    try:
        print(f"Checking with rule {rule_id}")
        time.sleep(random.randint(1, 3))

        while True:
            pass

        if transaction["id"] % 5 == 0 and rule_id == 2:
            while True:
                pass
        is_valid: bool = transaction["amount"] > 10_000 and random.choice([True, False])

        results_queue.put((rule_id, transaction["id"], is_valid))

    except Exception as error:
        print(f"Error: {error}")
        results_queue.put((rule_id, transaction["id"], f"Error {error}"))


def process_transaction(transaction: dict, rules: list[int]):
    threads = []
    queue = Queue()

    for rule_id in rules:
        t = Thread(
            target=evaluate_rule,
            kwargs={
                "rule_id": rule_id,
                "transaction": transaction,
                "results_queue": queue,
            },
        )
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    results = []
    while not queue.empty():
        results.append(queue.get())

    return results


def main():
    transactions: list[dict] = [
        {"id": i, "amount": random.randint(1, 20_000)} for i in range(1, 10)
    ]

    rules = [1, 2, 3]

    for transaction in transactions:
        print(f"Start processing transaction {transaction['id']}")
        results = process_transaction(transaction, rules)

        for rule_id, transaction_id, result in results:
            print(f"[{rule_id}][{transaction_id}]: {str(result)[:10]}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
