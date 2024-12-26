from collections.abc import Coroutine, Generator
import uuid
import time
import random
import asyncio


def random_name() -> str:
    return f"{str(uuid.uuid4())[:4]}"


def random_delay():
    return random.random() * 5


def random_countdown():
    return random.randrange(5)


async def launch_rocket(name: str, delay: float, countdown: int):
    await asyncio.sleep(delay)

    for i in reversed(range(countdown)):
        print(f"{i}...")
        await asyncio.sleep(1)

    print(f"Rocket launched: {name}")


async def main():
    n = 10_000  # user input
    tasks: Generator[Coroutine, None, None] = (
        launch_rocket(
            name=random_name(), delay=random_delay(), countdown=random_countdown()
        )
        for _ in range(n)
    )

    await asyncio.gather(*tasks)


asyncio.run(main())
