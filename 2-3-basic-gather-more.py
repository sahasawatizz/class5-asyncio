import asyncio
import time
#alert noti
async def hello(i):
    print(f"{time.ctime()}hello{i}started")
    await asyncio.sleep(4)
    print(f"{time.ctime()}hello{i}done")
#create 10 sequence
async def main():
    coros = [hello(i) for i in range(10)]
    await asyncio.gather(*coros)

#run function
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time:{end-start:.2f}sec')
