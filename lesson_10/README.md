# Basic threading example

```python
import time
from threading import Thread


def task(n: int = 2):
    print("Task started")
    time.sleep(n)
    print("Task completed")


def main():
    thread = Thread(target=task, args=(4,))
    thread.start()


main()
```

# Threads / Processes

```python
from collections.abc import Generator
import uuid
import time
import random
from threading import Thread
from multiprocessing import Process


def random_name() -> str:
    return f"{str(uuid.uuid4())[:4]}"


def random_delay():
    return random.random() * 5


def random_countdown():
    return random.randrange(5)


def launch_rocket(name: str, delay: float, countdown: int):
    time.sleep(delay)

    for i in reversed(range(countdown)):
        print(f"{i}...")
        time.sleep(1)

    print(f"Rocket launched: {name}")


def main():
    n = 10_000  # user input

    # sequential approach
    # for _ in range(n):
    #     launch_rocket(random_name(), random_delay(), random_countdown())

    # multithreading
    threads: Generator[Thread, None, None] = (
        Thread(
            target=launch_rocket,
            args=(
                random_name(),
                random_delay(),
                random_countdown(),
            ),
        )
        for _ in range(n)
    )

    # for thread in threads:
    #     thread.start()

    # for thread in threads:
    #     thread.join()

    # multiprocessing
    processes: Generator[Process, None, None] = (
        Process(
            target=launch_rocket,
            args=(
                random_name(),
                random_delay(),
                random_countdown(),
            ),
        )
        for _ in range(n)
    )

    for process in processes:
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    main()
```

# Processes for financial facility

```python
from functools import partial
from multiprocessing import Process, Queue
import time
import random


def evaluate_rule(rule_id: int, transaction: dict, results_queue: Queue):
    try:
        print(f"Checking with rule {rule_id}")
        time.sleep(random.randint(1, 3))

        if transaction["id"] % 5 == 0 and rule_id == 2:
            while True:
                pass
        is_valid: bool = transaction["amount"] > 10_000 and random.choice([True, False])

        results_queue.put((rule_id, transaction["id"], is_valid))

    except Exception as error:
        print(f"Error: {error}")
        results_queue.put((rule_id, transaction["id"], f"Error {error}"))


def process_transaction(transaction: dict, rules: list[int]):
    processes = []
    queue = Queue()

    for rule_id in rules:
        p = Process(
            target=evaluate_rule,
            kwargs={
                "rule_id": rule_id,
                "transaction": transaction,
                "results_queue": queue,
            },
        )
        p.start()
        processes.append(p)

    for index, p in enumerate(processes):
        p.join(timeout=3)
        if p.is_alive():
            print(f"Completing with rule {rules[index]}")
            p.terminate()
            p.join()

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
```
