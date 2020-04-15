# iterZ
JavaScript flavor iterable

```python
a = iterZ([1,3,5,7,9,100])
a.map(lambda x:x+65).filter(lambda x:x<=90).map(lambda x:chr(x)).reduce(lambda a,b:str(a) + str(b))
# 'BDFHJ'
