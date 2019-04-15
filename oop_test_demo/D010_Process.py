import time

from multiprocessing import Process


def f(name):
    time.sleep(1)
    print("Name：%s = Time:%s" %(name,time.time()))


if __name__ == '__main__':
    process_list=[]

    for i in range(10):
        process = Process(target = f,args=('James:number:%d'%i,))
        process_list.append(process)
        process.start()
    #
    # for p in process_list:
    #     p.join()

    print("end".center(50,'-'))