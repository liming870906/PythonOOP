# 私有修饰符："__"
# 子类不可以访问父类的自由字段
"""

class BaseFoo :
    def __init__(self):
        self.__gene = 987

class Foo(BaseFoo):
    __v = "123"
    def __init__(self,name, age):
        self.name = name
        # 私有属性
        self.__age = age
        super(Foo,self).__init__()

    def showAge(self):
        print(self.__age)

    @staticmethod
    def showV():
        return Foo.__v

    def __getMe(self):
        return '456'
    def getM(self):
        return self.__getMe()

    def showPrint(self):
        print(self.name)
        print(self.__age)
        # print(self.__gene)

foo = Foo("benben",20)
print(foo.name)
foo.showAge()
print(Foo.showV())
print(foo.getM())
foo.showPrint()

"""

# 特殊成员
"""
__doc__ 查看尖的描述信息
__module__表示当前操作的对象所在的模块
__class__表示当前操作的对象所属的类
__init__构造方法 通过类创建对象自动执行
__del__析构方法,当前对象在内存中被释放自动斩妖执行
__call__对象后面加括号触发执行
__dict__查看类或对象中的成员
__str__如果一个类中定义了此方法,那么打印此类对象时,输出此方法的返回值 
__getitem__当类中定义了一个字典的属性成员,可以获取
__setitem__设置修改类中字典的数据
__delitem__删除 类中字典的数据
__metalass__其用来表示该类由 谁 来实例化创建
__new__触发 __init__创建实例
__int__将对象强制转换为整数是调用该方法
__add__两个对象相加的时候会执行—__add__函数，并把第二个对象当成参数传入到__add__函数中
"""
class Foo:
    def __init__(self):
        print('hello')
    def __call__(self, *args, **kwargs):
        print('call')
    def __int__(self):
        return 2222
    def __str__(self):
        return "str__mmmm"
    def __add__(self, other):
        return 888
    def __getitem__(self, item):
        """
        后去索引，并返回索引加10
        :param item:
        :return:
        """
        if type(item) == slice:
            print(item.start)
            print(item.stop)
            print(item.step)
        else:
            return item + 10


foo = Foo()
foo()

print(int(foo))
print(foo)
str(1)

f1 = Foo()
f2 = Foo()
r = f1 + f2
print(r, type(r))
d = f1.__dict__
print(d)
print(f1[9])
# 切片方式
print(f1[1:5:2])


class Entity:

    def __init__(self):
        pass

    def __iter__(self):
        return iter([11,22,33,44,55])


# 声明Entity对象
entity = Entity()
# 如果类中有__iter__方法被称为可迭代对象。返回值是一个迭代器
# for循环遇到迭代器直接执行next方法，如果获取的是可迭代对象需要手动执行next方法
# 1.执行Entity对象的类Entity中的__iter__方法，并获取返回值
# 2.循环可迭代对象
for i in entity:
    print(i)
