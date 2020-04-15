def decorator_iterZ(func):
    def _decorator_iterZ(self,*args, **kwargs):
        ret = func(self.obj,*args, **kwargs)
        return iterZ(ret) if hasattr(ret,"__iter__") else ret
    return _decorator_iterZ

class iterZ:
    def __init__(self,self_obj):
        self.obj = self_obj
        for d in dir(self_obj):
            if d not in ["__class__"]:
                attrset = getattr(self_obj, d)
                if callable(attrset):
                    decorator_iterZ(setattr(self,d, attrset))
                else:
                    setattr(self,d, attrset)
    def __iter__(self):
        return self.obj.__iter__()
    def __next__(self):
        return self.obj.__next__()
    def __str__(self):
        return self.obj.__str__()
    def __repr__(self):
        return self.obj.__repr__()
    def __len__(self):
        return self.obj.__len__()
    def __getitem__(self, x):
        return self.obj.__getitem__(x)
    def __eq__(self,a):
        return iterZ(self.obj.__eq__(a.obj if type(a) == iterZ else a))
    def __ge__(self,a):
        return iterZ(self.obj.__ge__(a.obj if type(a) == iterZ else a))
    def __gt__(self,a):
        return iterZ(self.obj.__gt__(a.obj if type(a) == iterZ else a))
    def __le__(self,a):
        return iterZ(self.obj.__le__(a.obj if type(a) == iterZ else a))
    def __lt__(self,a):
        return iterZ(self.obj.__lt__(a.obj if type(a) == iterZ else a))
    def __add__(self,a):
        return iterZ(self.obj.__add__(a.obj if type(a) == iterZ else a))
    def map(self,func):
        return iterZ(map(func,self.obj))
    def filter(self,func):
        return iterZ(filter(func,self.obj))
    def reduce(self,func):
        import functools
        iter_obj = iter(self.obj)
        return functools.reduce(func,iter_obj, next(iter_obj))
    def list(self):
        return iterZ(list(self.obj))
    def sorted(self, *args, **kwargs):
        return iterZ(sorted(self.obj, *args, **kwargs))
    def join(self,Jstr):
        return Jstr.join(self)
