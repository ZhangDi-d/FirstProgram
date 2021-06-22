# coding:utf-8

"""
进程池与进出锁
Pool

apply_async 异步加入进程池
close 关闭进程池
join 等待进程池任务结束
"""

import multiprocessing
import os
import time


def work(count, lock):
    lock.acquire()
    print(count, os.getpid())
    time.sleep(3)
    lock.release()
    return 'result is %s ，pid is %s ' % (count, os.getpid())


if __name__ == "__main__":
    pool = multiprocessing.Pool(4)
    manager = multiprocessing.Manager()
    lock = manager.Lock()

    results = []
    for i in range(20):
        result = pool.apply_async(func=work, args=(i, lock))
        results.append(result)

    for result in results:
        print(result.get())
        # time.sleep(10)  # 1.阻塞主进程，防止程序推出

    pool.close()
    pool.join()  # 2.进程池的任务全部完成，主进程才退出

"""
进程锁
manager = multiprocessing.Manager()
lock = manager.Lock()
lock.acquire()
lock.release()
"""

from multiprocessing import Manager
