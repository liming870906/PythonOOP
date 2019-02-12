



def test_Exception():
    ret = 0
    try:
        li = [11,22,33]
        # li[999]
        # int('qws')
        raise IndexError('lalalal')
    except IndexError as e :
        print(str(e))
    except ValueError as e :
        print(e)
    except Exception as e :
        print(e)
    else:
        ret = 1
        print('else:%d'%ret)
    finally:
        print("exception is error")

# 自定义Exception
class MyException(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)



if __name__ == '__main__':
    test_Exception()

    try:
        # 断言
        assert 1 == 2
        # 自定义异常
        raise MyException("自定义Exception")
    except AssertionError as e :
        print("AssertionError: %s" %str(e))
    except MyException as e :
        print("自定义异常：%s" %str(e))

