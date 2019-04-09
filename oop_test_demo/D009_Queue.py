
import queue
import threading
import time

exit_flag = False

class MyThread(threading.Thread):
    """
    创建自定义线程
    """
    def __init__(self,thread_id, name, queue):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.queue = queue

    def run(self):
        print("开始线程："+self.name)
        process_data(self.name,self.queue)
        print("结束线程："+self.name)

def process_data(thrad_name, queue):
    """
    处理数据方法
    :param thrad_name:
    :param queue:
    :return:
    """
    while not exit_flag:
        if not work_queue.empty():
            data = queue.get()
            print("%s processing %s" % (thrad_name, data))
        time.sleep(1)


if __name__ == '__main__':
    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    nameList = ["One", "Two", "Three", "Four", "Five","a","b","c","d","e","One", "Two", "Three", "Four", "Five","a","b","c","d","e"]
    work_queue = queue.Queue(10)
    threads = []
    threadID = 1
    # 创建新线程
    for tName in threadList:
        thread = MyThread(threadID, tName, work_queue)
        thread.start()
        threads.append(thread)
        threadID += 1
    # 填充数据
    for word in nameList:
        work_queue.put(word)
        print("添加数据：%s"%word)

    # 等待队列清空
    while not work_queue.empty():
        pass

    exit_flag = True

    # 等待所有线程完成
    for t in threads:
        t.join()
    print("退出主线程")