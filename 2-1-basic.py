import asyncio
import time
#alert noti
async def hello(i):
    print(f"{time.ctime()}hello{i}started")
    await asyncio.sleep(4)
    print(f"{time.ctime()}hello{i}done")
#create task
async def main():
    task1 = asyncio.create_task(hello(1))
    task2 = asyncio.create_task(hello(2))
    await task1 #wait task1
    await task2 #wait task2


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time:{end-start:.2f}sec')
