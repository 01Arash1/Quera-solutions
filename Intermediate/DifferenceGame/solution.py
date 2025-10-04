def game(number):
	tensDigit = number //10 
	onesDigit = number % 10
	if tensDigit >= onesDigit:
		return tensDigit - onesDigit
	else:
		return onesDigit - tensDigit