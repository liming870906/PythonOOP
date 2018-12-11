"""
类型及相关内容
    注意： 函数中的self代表成名的对象实体。
"""

class Bar :

    def __init__(self):
        """
        构造方法
        """
        print(self)

    def __init__(self,name, age, gender):
        """
        带参数构造方法
        :param name:
        :param age:
        :param gender:
        """
        self.name = name
        self.age = age
        self.gender = gender

    def foo(self, content):
        """
        输出方法
        :param name:
        :param age:
        :param gender:
        :param content:
        :return:
        """
        print(self.name,self.age,self.gender,content)


# bar = Bar()
# bar.name = 'james'
# bar.foo('JamesLM',18,'man','hello world')

# bar2 = Bar()
# bar2.foo('JamesLM-11111',18,'man','hello world')

bar3 = Bar('LM',12,'nv')
bar3.foo('test')

# bar4 = Bar()
# bar4.foo('test')