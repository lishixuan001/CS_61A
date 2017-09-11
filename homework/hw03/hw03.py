HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """

    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """


    if n <= 3:
        return n
    a = 3
    b = 2
    c = 1
    i = 1
    total = 0
    for i in range(n - 3):
        total = a + 2 * b +  3 * c
        a, b, c = total, a, b
    return total


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    while k // 10 > 0:
        if k % 10 == 7:
            return True
        else:
            k = k // 10
    if k == 7:
        return True
    else:
        return False

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    # index = list(range(1,n+1))
    # num = 1
    # i = 2
    # indicate = True
    # while i <= n:
    #     if (i - 1) % 7 == 0 or has_seven(i - 1):
    #         indicate = not indicate
    #     if indicate:
    #         num = num + 1
    #     else:
    #         num = num - 1
    #     i = i + 1
    # return num
    def helper(i, num, index):
        if i == n:
            return num
        if index:
            if (i+1) % 7 == 0 or has_seven(i+1):
                return helper(i + 1, num + 1, not index)
            else:
                return helper(i + 1, num + 1, index)
        else:
            if (i+1) % 7 == 0 or has_seven(i+1):
                return helper(i + 1, num - 1, not index)
            else:
                return helper(i + 1, num - 1, index)
    return helper(1, 1, True)




def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """

    i = 0
    lst = []
    k = 0
    while k <= amount:
        k = 2 ** i
        lst = lst + [k]
        i = i + 1
    lg = len(lst) - 1


    def count_partitions(n,m):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 1
        else:
            return count_partitions(n-lst[m],m) + count_partitions(n,m-1)
    return count_partitions(amount, lg)
# def the_lst(i, k, n, lst):
#     if k > n:
#         lst.pop[0]
#         return lst
#     else:
#         lst = lst + [k]
#         return the_lst(i + 1, (i + 1)**2, n, lst)
# print(the_lst(0,1,amount,[]))

# def count_partitions(n, m, lst):
#     if n == 0:
#         return 1
#     elif n < 0:
#         return 0
#     elif m == len(lst):
#         return 0
#     else:
#         return count_partitions(n - lst[m], m, lst) + count_partitions(n, m + 1, lst)
# return count_partitions(amount, 0, the_lst(0, 1, amount, []))

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if n == 1:
        print ('Move the top disk from rod %d to rod %d' %(start,end))
    else:
        if start == 1:
            if end == 2:
                other = 3
            else:
                other = 2
        elif start == 2:
            if end == 1:
                other = 3
            else:
                other = 1
        else:
            if start == 1:
                other = 2
            else:
                other = 1
        move_stack(n-1,start, other)
        print('Move the top disk from rod %d to rod %d' %(start,end))
        move_stack(n-1, other, end)

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    def function(lst, new):
        for i in range(len(lst)):
            if type(lst[i]) == list:
                new = function(lst[i], new)
            else:
                new = new + [lst[i]]
        return new

    return function(lst, [])


def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    if type(lst1) == list and type(lst2) == list:
        new = lst1 + lst2
    elif type(lst1) == list and type(lst2) == int:
        new = lst1 + [lst2]
    elif type(lst2) == list and type(lst1) == int:
        new = lst2 + [lst1]
    else:
        new = [lst1, lst2]

    if type(new) == list:
        new = sorted(new)
    else:
        new = sorted([new])
    return new

def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    # new = merge(seq, [])
    if seq == []:
        return []
    elif len(seq) == 1:
        return seq
    else:
        first = seq[:len(seq)//2]
        last = seq[len(seq)//2:]
        return merge(mergesort(first), mergesort(last))
