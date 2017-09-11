from lab04 import *

# Q7
def deep_len(lst):
    """Returns the deep length of the list.

    >>> deep_len([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # deep list
    >>> deep_len(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> deep_len(x)
    6
    >>> x = []
    >>> for i in range(100):
    ...     x = [x] + [i]       # very deep list
    ...
    >>> deep_len(x)
    100
    """
    if type(lst) == list:
        total = len(lst)
    else:
        return 1
    index = False
    for i in range(len(lst)):
        if type(lst[i]) == list:
            total = total + deep_len(lst[i]) - 1
            index = True
    return total
        


# Q8
def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    if len(deck) % 2 == 0:
        index = int(len(deck) / 2)
        first = deck[:index]
        second = deck[index:]
        last = []
    else:
        inded = int((len(deck) - 1) / 2)
        first = deck[:index]
        second = deck[index:]
        last = deck[-1]
        second.pop()
    new = []
    for i in range(len(first)):
        new.append(first[i])
        new.append(second[i])
    new += last

    return new

# Q9
def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    """
    return [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
