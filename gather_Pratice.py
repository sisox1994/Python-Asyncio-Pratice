#  Asyncio 練習   gather
#func 1 每隔1秒倒數     10 => 0
#func 2 每隔0.5秒倒數   20 => 0
#此範例為2個func "同時開始" "同時結束" 並在結束時讀取各func return的value

import asyncio
import threading

async def func1():
    print('func1 thread id:', threading.get_ident())
    cnt = 10
    while cnt != 0:
       await asyncio.sleep(1.0)
       print("func1:",cnt)
       cnt -= 1 
    return 'func1_end'

async def func2():
    print('func2 thread id:', threading.get_ident())
    cnt = 20
    while cnt != 0:
       await asyncio.sleep(0.5)
       print("---------func2:",cnt)
       cnt -= 1  
    return 'func2_end'


async def main():
    job1 = func1()
    job2 = func2()
    retValues = await asyncio.gather(job1,job2 )
    for ret in retValues:
        print("result=",ret)


asyncio.run(main())
