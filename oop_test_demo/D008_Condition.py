import threading
import random
import time




class Producer(threading.Thread):
    """
    生产者线程
    """
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        """
        生产者制作方法
        :return:
        """
        # 全局列表放入产品
        global L
        # 循环生产产品
        while True:
            # 生成随机数
            val = random.randint(0,100)
            print("生产者",self.name,":Append"+str(val),L)
            if lock_condition.acquire():
                L.append(val)
                lock_condition.notifyAll()
                lock_condition.release()
            time.sleep(3)

class Consumer(threading.Thread):
    """
    消费者线程
    """
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        global L
        while True:
            lock_condition.acquire()
            if len(L) == 0:
                lock_condition.wait()
            print("消费者",self.name,":Delete"+str(L[0]),L)
            del L[0]
            lock_condition.release()
            time.sleep(1)






if __name__ == '__main__':
    # 生成数据列表
    L = []
    # 创建Condition锁
    lock_condition = threading.Condition()
    # 线程列表
    threads = []
    # 循环床架生产线程
    for i in range(5):
        # 创建生产者添加线程列表中->创建5个生产者
        threads.append(Producer())
    # 创建一个消费者放入线程队列中
    threads.append(Consumer())
    threads.append(Consumer())
    # 循环开启线程
    for t in threads:
        t.start()
    # 阻塞每个线程
    for t in threads:
        t.join()
