def count_change(amount):
	i = 0
	lst = []
	k = 0

	while k <= amount:
		k = 2 ** i
		lst = lst + [k]

    def count_partitions(n,m):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == len(lst):
            return 0
        else:
            return count_partitions(n-lst[m],m) + count_partitions(n,m+1)
    return count_partitions(amount, 0)
