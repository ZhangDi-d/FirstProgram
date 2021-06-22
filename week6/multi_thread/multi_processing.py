# coding:utf-8

"""
process 创建一个进程

start
join
kill
is_alive
"""
import time
import os
import multiprocessing


def work_a():
    for i in range(5):
        print(i, 'a', os.getpid())
        time.sleep(1)


def work_b():
    for i in range(5):
        print(i, 'b', os.getpid())
        time.sleep(1)


if __name__ == "__main__":
    start_time = time.time()
    a_p = multiprocessing.Process(target=work_a)
    # a_p.start()
    # a_p.join()
    b_p = multiprocessing.Process(target=work_b)
    # b_p.start()

    for p in (a_p, b_p):
        p.start()
    for p in (a_p, b_p):
        p.join()  # p 抢占时间片
    print(time.time() - start_time)
    print('parent pid is %s' % os.getpid())
    for p in (a_p, b_p):
        print(p.is_alive())
