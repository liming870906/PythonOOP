"""
继承
"""


# # 基类（父类）
# class Father:
#
#     def f1(self):
#         print('F.f1')
#
#     def f2(self):
#         print('F.f2')
# # 派生类（子类）
# class Son(Father):
#
#     def s1(self):
#         print('S.s1')
#
#     def f1(self):
#         print('S.f1')
#         super(Son,self).f1()
#
#     def f2(self):
#         print('S.f2')
#         Father.f2(self)
#
#
# if __name__ == '__main__':
#     son = Son()
#     son.s1()
#     son.f1()
#     son.f2()
#     son.f2()
#     print('分隔符'.center(100,'-'))
#     father = Father()
#     father.f1()
#     father.f2()
#     # father.s1()



# class Base:
#     def a(self):
#         print("base.a")
#
# class GF(Base) :
#     def a1(self):
#         print('GF.a')
# class F1(GF) :
#     def a1(self):
#         print('f1.a')
#         super(F1,self).a()
# class F2(Base) :
#     def a(self):
#         print('f2.a')
#
# class S(F1, F2):
#     pass
#
# son = S()
# son.a()

# class BaseRequest:
#     def __init__(self):
#         print('BaseRequest-init')
# class RequestHandler:
#
#     def __init__(self):
#         print('RequestHandler-init')
#         BaseRequest.__init__(self)
#
#     def serve_forever(self):
#         print('RequestHandler-serve_forever')
#         self.process_request()
#
#     def process_request(self):
#         print('RequestHandler-process-request')
#
# class Minx:
#
#     def process_request(self):
#         print('Minx-process-request')
#
# class Son(Minx, RequestHandler):
#
#     @staticmethod
#     def abc():
#         print('static method')
#
#     @classmethod
#     def bcd(cls):
#         # cls 是类名
#         print('class method')
#
#
#     @staticmethod
#     def cde():
#         pass
#
# s = Son()
#
# s.serve_forever()
#
# Son.abc()
# Son.bcd()



# import socketserver
#
# obj = socketserver.ThreadingTCPServer(1,2)
# obj.serve_forever()

class PageObject:
    def __init__(self, p):
        try:
            self.page = int(p)
        except Exception as ex:
            self.page = 1
        self.number = 0
    @property
    def start(self):
        return (self.page - 1) * 10
    @property
    def end(self):
        return self.page * 10

    def getA(self):
        return self.number
    def setA(self,num):
        self.number = num
    def delA(self):
        self.number = 0

    pro = property(fget=getA,fset=setA,fdel=delA)

if __name__ == '__main__':
    li = []
    for i in range(200):
        li.append(i)

    while True:
        page = input('please print page number:')
        mPage = PageObject(page)
        print(li[mPage.start:mPage.end])
        if li:
            mPage.pro = li[int(mPage.start + (mPage.end - mPage.start)/2)]
            print(mPage.pro)
            del mPage.pro
            print(mPage.pro)




