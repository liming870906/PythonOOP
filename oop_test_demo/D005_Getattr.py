# 反射


class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        return "(%s - %d)" %(self.name, self.age)


obj = Foo('James',22)

# 通过反射获取名称及年龄(通过反射获取属性)
nick = getattr(obj,'name')
print(nick)
age = getattr(obj,'age')
print(age)
# 反射获取方法对象
func = getattr(obj,'show')
print(func())
# 判断是否有属性和方法
print(hasattr(obj,'show'))
# 设置属性
setattr(obj,'k1',33)
print(obj.k1)
# 删除delattr  删除属性或者方法