import sys
from importlib import import_module
print("In fillerup script")


class GetTheBag(dict):

    def __init__(self, lib_dict):
        self.lib_dict = lib_dict

    def go_get_it(self):
        if self.lib_dict['shorthand']:
            print("loading shorthand modules")
            for (name, short) in self.lib_dict['shorthand']:
                try:
                    print("Loading" + str(name))
                    lib = import_module(package=name)
                except ImportError as e:
                    print("Error")
                else:
                    globals()[short] = lib

        print("passed shorthand import")

        if self.lib_dict['pure']:
            print("loading pure modules")
            for libname in self.lib_dict['pure']:
                try:
                    print("Loading " + str(libname))
                    lib = import_module(libname)
                except ImportError as e:
                    print("Error")
                else:
                    globals()[libname] = lib

        print("passed longhand import")
        return True
