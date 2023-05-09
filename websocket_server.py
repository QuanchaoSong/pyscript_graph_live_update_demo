import asyncio
import random
import websockets
import time


async def handler(websocket):
    while True:
        num = random.randrange(200, 1000)
        await websocket.send(str(num))
        time.sleep(1)
        # try:
        #     message = await websocket.recv()
        #     print(message)
        #     num = random.randrange(200, 1000)
        #     await websocket.send(str(num))
        #     time.sleep(3)
        # except websockets.ConnectionClosedOK:
        #     break        

async def main():
    async with websockets.serve(handler, "localhost", 8001):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
