from ranges import *
from collections import UserDict

class DictRange(UserDict):
    def __init__(self):
        super().__init__()
        # empty range
        self['x'] = RangeSet()
        self['m'] = RangeSet()
        self['a'] = RangeSet()
        self['s'] = RangeSet()

    def init_default(self):
        self['x'] = RangeSet(Range(1,4001)) # include end = false
        self['m'] = RangeSet(Range(1,4001)) # include end = false
        self['a'] = RangeSet(Range(1,4001)) # include end = false
        self['s'] = RangeSet(Range(1,4001)) # include end = false
    def difference(self, other):
        ret = self.copy()
        if isinstance(other, DictRange):
            for k in self.keys():
                ret[k] = ret[k].difference(other[k])
        else:
            for k in self.keys():
                ret[k] = ret[k].difference(other)
        return ret
    def union(self, other):
        ret = self.copy()
        if isinstance(other, DictRange):
            for k in self.keys():
                ret[k] = ret[k].union(other[k])
        else:
            for k in self.keys():
                ret[k] = ret[k].union(other)
        return ret

    def intersection(self, other):
        ret = self.copy()
        if isinstance(other, DictRange):
            for k in self.keys():
                ret[k] = ret[k].intersection(other[k])
        else:
            for k in self.keys():
                ret[k] = ret[k].intersection(other)
        return ret

    def copy(self):
        other = DictRange()
        for k in self.keys():
            other[k] = self[k].copy()
        return other
    def length(self):
        l = 1
        for k in self.keys():
            p = 0
            for i in range(1,4001):
                if i in self[k]:
                    p += 1
            l *= p
        return l

