import functools
type_temp = {}

def iterZ(self_obj):
    if type(self_obj) in type_temp:
        return type_temp[type(self_obj)](self_obj)
    class iterC:
        def __init__(self,self_obj):
            self.iterZ_original_obj = self_obj
        def map(self,func):
            return iterZ(map(func,self.iterZ_original_obj))
        def filter(self,func):
            return iterZ(filter(func,self.iterZ_original_obj))
        def reduce(self,func):
            iter_obj = iter(self.iterZ_original_obj)
            return functools.reduce(func,iter_obj, next(iter_obj))
        def list(self):
            return iterZ(list(self.iterZ_original_obj))
        def sorted(self, *args, **kwargs):
            return iterZ(sorted(self.iterZ_original_obj, *args, **kwargs))
        def join(self,Jstr):
            return Jstr.join(self)
    def decorator_iterZ(func):
        def _decorator_iterZ(*args, **kwargs):
            args = [a.iterZ_original_obj if hasattr(a,"iterZ_original_obj") else a for a in args]
            ret = func(*args, **kwargs)
            return iterC(ret) if type(ret) == type(args[0]) else ret
        return _decorator_iterZ
    for d in dir(type(self_obj)):
        if d not in ["__class__","__init__","__new__","__setattr__","__getattribute__"] :
            attrset = getattr(type(self_obj), d)
            if callable(attrset):
                setattr(iterC,d, decorator_iterZ(attrset))
            else:
                setattr(iterC,d, attrset)
    iterC.__name__ = "iterZ_" + type(self_obj).__name__
    type_temp[type(self_obj)] = iterC
    return iterC(self_obj)
