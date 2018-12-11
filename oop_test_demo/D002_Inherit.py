"""
继承
"""


# 基类（父类）
class Father:

    def f1(self):
        print('F.f1')

    def f2(self):
        print('F.f2')
# 派生类（子类）
class Son(Father):

    def s1(self):
        print('S.s1')


if __name__ == '__main__':
    son = Son()
    son.s1()
    son.f1()
    son.f2()
    print('分隔符'.center(100,'-'))
    father = Father()
    father.f1()
    father.f2()
    # father.s1()