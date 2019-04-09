import threading
import time

# 线程

exitFlag = 0


class MyThread(threading.Thread):
    """
    自定义线程类
    """

    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        """
        初始化方法
        """
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        """
        咸亨执行方法
        :return:
        """
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def print_time(thread_name, delay, counter):
    """
    输出方法
    :param thread_name:
    :param delay:
    :param counter:
    :return:
    """
    while counter:
        if exitFlag:
            thread_name.exit()
        time.sleep(delay)
        print("%s:%s" %(thread_name,time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)
thread3 = threading.Thread(target=print_time,args=('thread-3',3,2,))
t = [thread1,thread2,thread3]
if __name__ == '__main__':

    for i in t :
        # 守护线程。主线程执行结束的时候子线程也结束
        i.setDaemon(True)
        i.start()


    print ("退出主线程")

# # 开启新线程
# thread1.start()
# thread2.start()
# thread3.start()
# # thread1.join()
# # thread2.join()
# # thread3.join()
# print ("退出主线程")