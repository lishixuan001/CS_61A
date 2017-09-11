def withdraw(balance):
	def get(amount):
		if amount > balance:
			return 'Insufficient Funds'
		balance = balance - amount
		return balance
	return get
