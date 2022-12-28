
de classtree(cls, indent=):
    print ('\t' * indent + cls.__name__)
    for subcls in cls.__subclasses__()
    classtree(subcls, indent-1)

classtree(BaseException,)