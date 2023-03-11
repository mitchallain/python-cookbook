"""
Demonstrate how to easily build dynamic instantiation from a class hierarchy
given the string subclass name, using the __init_subclass__ special method
in python >= 3.6.

https://stackoverflow.com/a/53101259
"""


class Base(object):
    # initialize plugins with this class
    PLUGINS = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.PLUGINS[cls.__name__] = cls

    def __init__(self, *args, **kwargs):
        print("Base.__init__")


class Sub1(Base):
    def __init__(self, *args, **kwargs):
        print("Sub1.__init__")
        super().__init__(*args, **kwargs)


class Sub2(Base):
    def __init__(self, *args, **kwargs):
        print("Sub2.__init__")
        super().__init__(*args, **kwargs)


def main():
    # Dynamically instantiate a class from a string subclass name
    # using the __init_subclass__ special method.
    print("Possible subclasses: {}".format(Base.PLUGINS.keys()))

    for cls_name in ["Sub1", "Sub2"]:
        cls = Base.PLUGINS[cls_name]
        cls()


if __name__ == "__main__":
    main()
