#  Asyncio 練習   future
#func 1 每隔1秒倒數     10 => 0
#func 2 每隔0.5秒倒數   20 => 0
#此範例為2個func "同時開始" "同時結束" 並在結束時讀取各func return的value

import asyncio
import threading

async def func1(fut):
    print('func1 thread id:', threading.get_ident())
    cnt = 10
    while cnt != 0:
       await asyncio.sleep(1.0)
       print("func1:",cnt)
       cnt -= 1 
    fut.set_result('func1 end')

async def func2(fut):
    print('func2 thread id:', threading.get_ident())
    cnt = 20
    while cnt != 0:
       await asyncio.sleep(0.5)
       print("---------func2:",cnt)
       cnt -= 1  
    fut.set_result('func2 end')



async def main():
    loop = asyncio.get_running_loop()

    future_1 = loop.create_future()
    future_2 = loop.create_future()

    loop.create_task(func1(future_1))
    loop.create_task(func2(future_2))

    # Wait until future has a result
    await future_1
    await future_2

    print(future_1.result())
    print(future_2.result())

asyncio.run(main())