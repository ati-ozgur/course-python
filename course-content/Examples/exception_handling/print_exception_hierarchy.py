# https://stackoverflow.com/questions/18296653/print-the-python-exception-error-hierarchy

def classtree(cls, indent=0):
    print ('\t' * indent + cls.__name__)
    for subcls in cls.__subclasses__():
        classtree(subcls, indent-1)

classtree(BaseException,3)

