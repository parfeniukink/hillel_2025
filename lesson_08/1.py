import asyncio


class AsyncFile:
    async def __aenter__(self):
        print("Opening file")
        await asyncio.sleep(1)
        print("File opened")
        return self

    async def __aexit__(self, *args, **kwargs):
        print("Closing file")
        await asyncio.sleep(1)
        print("File closed")


async def main():
    async with AsyncFile():
        print("Reading file ...")


asyncio.run(main())
