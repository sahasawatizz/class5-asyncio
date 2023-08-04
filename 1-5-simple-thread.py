import asyncio
import time
from concurrent.futures.thread import ThreadPoolExecutor #เตรียมสร้างเทรด
# Sleep function with out synchronous
def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)
# Sum the data with synchronous thread
async def sum(name, numbers):
    _executor = ThreadPoolExecutor(2) #สร้างเทรดขึ้นมา2ช่อง
    total = 0
    for number in numbers: #สั่งลูปค่าทั้งหมด
        print(f'Task {name}: Computing {total}+{number}')
        await loop.run_in_executor(_executor, sleep)
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
# Basic event to run all task
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')
