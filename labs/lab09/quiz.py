empty = 'X'

def link(first, rest=empty):
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(lnk):
    assert is_link(lnk), 'first only applies to linked lists.'
    assert lnk != empty, 'empty linked list has no first element.'
    return lnk[0]

def rest(lnk):
    assert is_link(lnk), 'rest only applies to linked lists.'
    assert lnk != empty, 'empty linked list has no rest.'
    return lnk[1]

def is_link(lnk):
    return lnk == empty or \
        type(lnk) == list and len(lnk) == 2 and is_link(lnk[1])

# Useful print_link function, used for testing.

def print_link(lnk):
    """Prints out a non-deep linked list."""
    line = ''
    while lnk != empty:
        if line:
            line += ' '
        line += str(first(lnk))
        lnk = rest(lnk)
    print('<{}>'.format(line))

def unreplicate_link(s):
    def unreplicate(the_link, iters):
        if the_link == empty:
            return empty
        elif iters == 0:
            return unreplicate_link(the_link)
        return unreplicate(rest(the_link), iters - 1)
    return link(first(s), unreplicate(rest(s), first(s) - 1))
