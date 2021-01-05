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