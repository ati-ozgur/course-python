def classtree(cls, indent=0):
    print ('\t' * indent + cls.__name__)
    for subcls in cls.__subclasses__():
        classtree(subcls, indent+1)

classtree(BaseException)