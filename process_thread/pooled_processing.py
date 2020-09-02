from multiprocessing import Pool
import os, time, random

'''如果要启动大量的子进程，可以用进程池的方式批量创建子进程'''

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done.')

'''
task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行
由于pool的限制，最多同时执行4个tasks
'''
