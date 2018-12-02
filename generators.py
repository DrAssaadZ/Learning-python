def fun(fn):
    def hello():
        print("this is")
        fn()
        print("call me J")
    return hello


def fn():
    print("Jeff")


fun(fn())
