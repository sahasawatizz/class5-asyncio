import asyncio
import time
# Make function that calculate factorial and replacement by order
async def factorial(n):
    f = 1
    for i in range(2, n + 1):
        print(f"Computing factorial({n}), currently i={i}...")
        await asyncio.sleep(1) #make synchronous delay for 1 second
        f *= i #ending count
    return f
# Define factorial order
async def main():
    L = await asyncio.gather(factorial(2), factorial(3), factorial(4))
    print(L) # [2, 6, 24]
# Running the step the ending time at last
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')
