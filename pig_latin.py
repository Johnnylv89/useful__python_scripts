def pig_latin(word):
	first_letter = word[0]
	if first_letter in 'aeiou':
		pig_word = word + 'ay'
	else:
		pig_word = word[1:] + first_letter + 'ay'
	print(pig_word)

pig_latin('Eva')

def lesser_of_two_evens(n1,n2):
	if n1%2==0 and n2%2==0:
		return min(n1,n2)
	else:
		return max(n1,n2

def animal_crackers(text):
	words = text.split()
	first = words[0]
	second = words[1]
	return first[0] == second[0]

def animal_crackers(text):
	words = text.lower().split()
	return words[0][0] == words[1][0]

def makes_twenty(n1,n2):
	if n1+n2 == 20:
		return True
	elif n1 ==20:
		return True
	elif n2 == 20:
		return True
	else:
		return False

def makes_twenty(n1,n2):
	return (n1+n2)==20 or n1==20 or n2==20
#My test comment. Checking git mechanism
#second important comment
