# 单例模式

class SingletonPattern:

    __obj = None

    @classmethod
    def get_instance(cls):
        if cls.__obj is None:
            cls.__obj = SingletonPattern()
        return cls.__obj

if __name__ == '__main__':
    obj1 = SingletonPattern.get_instance()
    print(obj1)
    obj2 = SingletonPattern.get_instance()
    print(obj2)
    obj3 = SingletonPattern.get_instance()
    print(obj3)