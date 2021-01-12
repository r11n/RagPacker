from typing import Optional
class DictObj(dict):
    MARKER = object()
    
    def __init__(self, hash=None):
        if hash is None:
            pass
        elif isinstance(hash, dict):
            for key in hash:
                self.__setitem__(key, hash[key])
        else:
            raise TypeError('expected dict')
    
    def __setitem__(self, key, value):
        if isinstance(value, dict) and not isinstance(value, DictObj):
            value = DictObj(value)
        super(DictObj, self).__setitem__(key, value)
    
    def __getitem__(self, key):
        found = self.get(key, DictObj.MARKER)
        if found in DictObj.MARKER:
            found = DictObj()
            super(DictObj, self).__setitem__(key, found)
        return found
    __setattr__, __getattr__ = __setitem__, __getitem__

class Delegator:
    def delegate(self, method_names=['foo'], supplier=''):
        """Creates given methods in the current class
        
        Example
        ```python
        class A:
            def foo(self):
                print('foo')
            def bar(self):
                print('bar')
        a = A()
        class B(Delegator):
            def __init__(self, obj):
                self.delegate(['foo', 'bar'], obj)
        b = B(a)
        b.foo()
        # 'foo'
        b.bar()
        # 'bar'
        ```
        """
        for method in method_names:
            setattr(self.__class__, method, getattr(supplier, method, None))
    
    def dict_to_obj(self, hash={}):
        return DictObj(hash)
