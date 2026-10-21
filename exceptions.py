try:
    a = 5/1
    b = a + '4'
except TypeError as e:
    print(e)

# or

try:
    c = 5/1
    d = c + '2'
except Exception as e:
    print(e) # type error
except ZeroDivisionError as e:
    print(e)
else:
    print("everything is fine")

finally:
    print("always runs ")




class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x>100:
        raise ValueTooHighError('Value is too high')
    if x<5:
        raise ValueTooSmallError('value is too small',x)

try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)

