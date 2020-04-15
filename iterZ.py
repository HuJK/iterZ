class iterZ:
    def __init__(self,self_obj):
        self.obj = self_obj
    def __iter__(self):
        return self
    def __next__(self):
        return next(self.obj)
    def __str__(self):
        return self.obj.__str__()
    def __repr__(self):
        return self.obj.__repr__()
    def __getitem__(self, x):
        return self.obj.__getitem__[x]
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
    def join(self,Jstr):
        return Jstr.join(self)
