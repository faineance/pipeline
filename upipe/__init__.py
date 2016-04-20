class Pipe(object):
    def __init__(self, func):
        self.func = func


class Map(Pipe): __ror__ = lambda self, iterable: [(yield self.func(obj)) for
                                                   obj in iterable]


class Filter(Pipe): __ror__ = lambda self, iterable: [(yield obj) for
                                                      obj in iterable if
                                                      self.func(obj)]

#
# class Reduce(Pipe):
#     __ror__ = lambda self, iterable: [(yield )]


class Apply(Pipe): __ror__ = lambda self, iterable: self.func(iterable)


Reverse = Apply(reversed)

Sort = Apply(sorted)

List = Apply(list)

Set = Apply(set)

FrozenSet = Apply(frozenset)

Int = Apply(int)

Float = Apply(float)

Complex = Apply(complex)

Bool = Apply(bool)

Str = Apply(str)

Sum = Apply(sum)

Tuple = Apply(tuple)

Oct = Apply(oct)

Ord = Apply(ord)

Hex = Apply(hex)

Chr = Apply(chr)

Bin = Apply(bin)

Abs = Apply(abs)

Len = Apply(len)

Max = Apply(max)

Min = Apply(min)
