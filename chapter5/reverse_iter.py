class reverse_iter:
    def __init__(self,l):
        self.n=len(l)
        self.l=l

    def __iter__(self):
        return self

    def next(self):
          if self.n > 0:
            self.n -= 1
            return self.l[self.n]
          else:
            raise StopIteration()

a=reverse_iter([1,9,3])
print a.next()
print a.next()
print a.next()


