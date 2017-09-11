## Linked Lists

class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first
    1
    >>> s.rest
    Link(2, Link(3))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

## Trees

class Tree:
    def __init__(self, root, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.root = root
        self.branches = branches

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.root, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):
        return type(other) is type(self) and self.root == other.root \
               and self.branches == other.branches

# Binary trees

class BTree(Tree):
    """A tree with exactly two branches, which may be empty."""
    empty = Tree(None)

    def __init__(self, root, left=empty, right=empty):
        for b in (left, right):
            assert isinstance(b, BTree) or b is BTree.empty
        Tree.__init__(self, root, (left, right))

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return [self.left, self.right] == [BTree.empty] * 2

    def __repr__(self):
        if self.is_leaf():
            return 'BTree({0})'.format(self.root)
        elif self.right is BTree.empty:
            left = repr(self.left)
            return 'BTree({0}, {1})'.format(self.root, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BTree.empty'
            template = 'BTree({0}, {1}, {2})'
            return template.format(self.root, left, right)

# Binary search trees

def bst(values):
    """Create a balanced binary search tree from a sorted list.

    >>> bst([1, 3, 5, 7, 9, 11, 13])
    BTree(7, BTree(3, BTree(1), BTree(5)), BTree(11, BTree(9), BTree(13)))
    """
    if not values:
        return BTree.empty
    mid = len(values) // 2
    left, right = bst(values[:mid]), bst(values[mid+1:])
    return BTree(values[mid], left, right)

## Streams

class Stream:
    empty = 'empty'
    def __init__(self, first, compute_rest=lambda: Stream.empty):
        self.first = first
        self.cached_rest = None
        assert callable(compute_rest)
        self.compute_rest = compute_rest
    @property
    def rest(self):
        """Return the rest, computing it if necessary."""
        if self.compute_rest is not None:
            self.cached_rest = self.compute_rest()
            self.compute_rest = None
        return self.cached_rest
    def __repr__(self):
        rest = self.cached_rest if self.compute_rest is None else '<...>'
        return 'Stream({}, {})'.format(self.first, rest)

def constant_stream(x):
    """The infinite stream all of whose values are X."""
    result = Stream(x, lambda: result)
    return result

def make_integer_stream(first=1):
    def compute_rest():
        return make_integer_stream(first+1)
    return Stream(first, compute_rest)

def stream_to_list(s, n=10):
    """A list containing the elements of stream S,
    up to a maximum of N."""
    r = []
    while n > 0 and s is not Stream.empty:
        r.append(s.first)
        s = s.rest
        n -= 1
    return r

def combine_streams(fn, a, b):
    """The stream consisting of FN(a1, b1), FN(a2, b2), ..., where
    ai and bi are elements of streams A and B, respectively, and FN
    is a two-parameter function.  The stream terminates when either of
    A or B terminates."""
    if a is Stream.empty or b is Stream.empty:
        return Stream.empty
    else:
        return Stream(fn(a.first, b.first),
                      lambda: combine_streams(fn, a.rest, b.rest))

def map_stream(fn, s):
    if s is Stream.empty:
        return s
    return Stream(fn(s.first), lambda: map_stream(fn, s.rest))