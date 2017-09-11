from objects import *

## Iterators

class LinkIterator:
    """
    >>> lnk = Link(1, Link(2, Link(3)))
    >>> lnk_iter = LinkIterator(lnk)
    >>> next(lnk_iter)
    1
    >>> next(lnk_iter)
    2
    """
    def __init__(self, link):
        self.link = link

    def __iter__(self):
        return self

    def __next__(self):
        if self.link is Link.empty:
            raise StopIteration
        result = self.link.first
        self.link = self.link.rest
        return result

## Generators

def in_order(t):
    """
    Yields the entries of a valid binary search tree in sorted order.

    >>> b = BTree(5, BTree(3, BTree(2), BTree(4)), BTree(6))
    >>> list(in_order(b))
    [2, 3, 4, 5, 6]
    >>> list(in_order(bst([1, 3, 5, 7, 9, 11, 13])))
    [1, 3, 5, 7, 9, 11, 13]
    >>> list(in_order(BTree(1)))
    [1]
    """
    if t.root is BTree.empty:
        return []
    if t.is_leaf():
        return [t.root]
    else:
        return in_order(t.left) + [t.root] + in_order(t.right)

def permutations(lst):
    """Generates all permutations of sequence LST. Each permutation is a
    list of the elements in LST in a different order.

    The order of the permutations does not matter.

    >>> sorted(permutations([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> type(permutations([1, 2, 3]))
    <class 'generator'>
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    if not lst:
        yield []
        return
    # for k in range(len(lst)):
    #     for i in range(len(lst)):
    #         result = lst
    #         result[k], result[i] = result[i], result[k]
    #         yield result
            # return
    def helper(x,l):
        return [ l[0:i] + [x] + l[i:]  for i in range(len(l)+1) ]

    for y in permutations(lst[1:]):
        for x in helper(lst[0], y):
            yield x
## Streams

def scale_stream(s, k):
    """Return a stream of the elements of S scaled by a number K.

    >>> ints = make_integer_stream(1)
    >>> s = scale_stream(ints, 5)
    >>> stream_to_list(s, 5)
    [5, 10, 15, 20, 25]
    >>> s = scale_stream(Stream("x", lambda: Stream("y")), 3)
    >>> stream_to_list(s)
    ['xxx', 'yyy']
    >>> stream_to_list(scale_stream(Stream.empty, 10))
    []
    """
    if s is Stream.empty:
        return s
    result = s.first * k
    return Stream(result, lambda: scale_stream(s.rest, k))

def merge(s0, s1):
    """Return a stream over the elements of strictly increasing s0 and s1,
    removing repeats. Assume that s0 and s1 have no repeats.

    >>> ints = make_integer_stream(1)
    >>> twos = scale_stream(ints, 2)
    >>> threes = scale_stream(ints, 3)
    >>> m = merge(twos, threes)
    >>> stream_to_list(m, 10)
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    if s0 is Stream.empty:
        return s1
    elif s1 is Stream.empty:
        return s0

    e0, e1 = s0.first, s1.first
    if e0 < e1:
        return Stream(e0, lambda:merge(s0.rest, s1))
    elif e1 < e0:
        return Stream(e1, lambda:merge(s0, s1.rest))
    else:
        return Stream(e0, lambda:merge(s0.rest, s1.rest))

def make_s():
    """Return a stream over all positive integers with only factors 2, 3, & 5.

    >>> s = make_s()
    >>> stream_to_list(s, 20)
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36]
    """
    # index = 2
    # def check(num):
    #     count = 0
    #     for i in range(2,num):
    #         if num / i == 0:
    #             count += 1
    #             if i not in [2, 3, 5]:
    #                 return False
    #     if count == 0:
    #         return False
    #     return True
    # #
    # # ints = make_integer_stream(2)
    # index = 1
    #
    # def findit(num):
    #     for _ in range(10000):
    #         num += 1
    #         if check(num):
    #             return num
    #     return 2
    #
    # # def helper(k):
    # #     def cals(k):
    # #         k = findit(k)
    # #         return helper(k)
    # #     return Stream(k, lambda:cals(k))
    # def helper(first=2):
    #     nonlocal index
    #     index += 1
    #     def compute_rest(num):
    #         return helper(findit(num))
    #     return Stream(first, lambda:compute_rest(first))


    def rest():
        # return helper()
        # nonlocal index
        # num = index
        # if num/2 == 0 or num/3 == 0 or num/5 == 0:
        #     index += 1
        #     return Stream(num, rest)
        # else:
        #     index += 1
        #     return rest()
        # ints = make_integer_stream(1)
        # twos = scale_stream(ints, 2)
        # threes = scale_stream(ints, 3)
        # fives = scale_stream(ints, 5)
        # result1 = merge(twos, threes)
        # result = merge(result1, fives)
        # return result
        # nonlocal index
        # number = index
        # index += 1
        # if check(number):
        #     return Stream(number, rest)
        # else:
        #     index += 1
        #     return rest()

        # result = ints.first
        # if check(result):
        #     ints = ints.rest
        # else:

        # nonlocal index
        # index += 1
        # if index > 10000:
        #     return Stream.empty

        twos = scale_stream(s, 2)
        threes = scale_stream(s, 3)
        fives = scale_stream(s, 5)
        result1 = merge(twos, threes)
        return merge(result1, fives)


    # return helper(1)
    s = Stream(1, rest)
    return s


from operator import add, mul, mod

def make_random_stream(seed, a, c, n):
    """The infinite stream of pseudo-random numbers generated by the
    recurrence r[0] = SEED, r[i+1] = (r[i] * A + C) % N.

    >>> s = make_random_stream(25, 29, 5, 32)
    >>> stream_to_list(s, 10)
    [25, 26, 23, 0, 5, 22, 3, 28, 17, 18]
    >>> s = make_random_stream(17, 299317, 13, 2**20)
    >>> stream_to_list(s, 10)
    [17, 894098, 115783, 383424, 775373, 994174, 941859, 558412, 238793, 718506]
    """
    def helper(num, a, c, n):
        return make_random_stream( ((num * a + c) % n), a, c, n)
    return Stream(seed, lambda:helper(seed, a, c, n))

def make_stream_of_streams():
    """
    >>> stream_of_streams = make_stream_of_streams()
    >>> stream_of_streams
    Stream(Stream(1, <...>), <...>)
    >>> stream_of_streams.rest
    Stream(Stream(2, <...>), <...>)
    >>> stream_of_streams.rest.rest
    Stream(Stream(3, <...>), <...>)
    >>> stream_of_streams
    Stream(Stream(1, Stream(2, Stream(3, <...>))), Stream(Stream(2, Stream(3, <...>)), Stream(Stream(3, <...>), <...>)))
    """
    def helper(num):
        return Stream(num, lambda:helper(num+1))
    # def second(lst):
    #     return Stream(helper(lst),lambda: second(lst + 1))
    def next_step(fn, strm):
        return Stream(fn(strm.first), lambda: next_step(fn, strm.rest))
    result = Stream(helper(1), lambda:next_step(lambda x: x.rest, result))
    # result = Stream(helper(1), lambda:second(2))
    return result


















'''END'''
