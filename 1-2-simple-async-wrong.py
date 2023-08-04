import asyncio
import time
# Delay for 1 second
async def sleep(): #หน่วงเวลา
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

async def sum(name, numbers): #ฟังก์ชันบวกและเก็บค่าผลของtask
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time() #เวลาเริ่มต้น
# Make asynchronous loop from task A then B
loop = asyncio.get_event_loop() #เรียกไลบรารี่ฟังก์ชันอะซิงโครนัส
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks)) #ดำเนินการไล่บวกค่า
loop.close()

end = time.time() #ระยะเวลาสิ้นสุด
print(f'Time: {end-start:.2f} sec') #แสดงเวลา
