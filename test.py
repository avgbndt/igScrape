from sys import argv

print(argv)


class Test(object):
    def __init__(self, *args):
        self.arguments = [i for i in args]


myTest = Test(["xd", "xd"])

print(myTest.arguments)
