def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

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

    def __len__(self):
        """ Return the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        """
        return 1 + len(self.rest)

    def __getitem__(self, i):
        """Returning the element found at index i.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        """
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __setitem__(self, index, element):
        """Sets the value at the given index to the element

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1] = 5
        >>> s
        Link(1, Link(5, Link(3)))
        >>> s[4] = 5
        Traceback (most recent call last):
        ...
        IndexError
        """
        if index == 0:
            self.first = element
        elif self.rest is Link.empty:
            raise IndexError
        else:
            self.rest[index - 1] = element

    def __contains__(self, e):
        return self.first == e or e in self.rest

    def map(self, f):
        self.first = f(self.first)
        if self.rest is not Link.empty:
            self.rest.map(f)