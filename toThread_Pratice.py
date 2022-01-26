#  Asyncio 練習   to_thread
#各自在新的thread執行
#func 1 每隔1秒倒數     10 => 0
#func 2 每隔0.5秒倒數   20 => 0
#此範例為2個func "同時開始" "同時結束" 並在結束時讀取各func return的value

import asyncio
import threading
import time

def func1():
    print('func1 thread id:', threading.get_ident())
    cnt = 10
    while cnt != 0:
       time.sleep(1.0)
       print("func1:",cnt)
       cnt -= 1 
    return 'func1_end'

def func2():
    print('func2 thread id:', threading.get_ident())
    cnt = 20
    while cnt != 0:
       time.sleep(0.5)
       print("---------func2:",cnt)
       cnt -= 1  
    return 'func2_end'


async def do_async_job(func):
    ret = await asyncio.to_thread(func)
    #await asyncio.sleep(1)
    print('job done!')
    return ret

async def main():
    task1 = asyncio.create_task(do_async_job(func1))
    task2 = asyncio.create_task(do_async_job(func2))  

    retValues = await asyncio.gather(task1, task2)
    for ret in retValues:
        print("result=",ret)

asyncio.run(main())