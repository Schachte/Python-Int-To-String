import sys

number = raw_input('Enter a number less than 10,000: ')

size = 0

for i in range(0,len(str(number))):
	size = size + 1

lower = {0: '',1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10:'ten', 11: 'eleven', 12: 'twelve'}
teens = {0: '', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
upper = {0: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8:'eighty', 9:'ninety', 100:'hundred'}
word_appendage = [' hundred ', ' thousand ']

x = 0
if (size == 1):
	print lower[int(number)]

elif (size == 2 and number[0] == '1'):
	if ('11' or '12' in (number)):
		print lower[int(number)]
	else:
		print teens[int(number)]

elif (size == 2):
	print upper[int(number[0])] + ' ' + lower[int(number[1])]

elif (size == 3):
	print lower[int(number[0])] + word_appendage[0] + upper[int(number[1])] + ' ' +lower[int(number[2])]

elif (size == 4 and '0' not in number[1]):
	print lower[int(number[0])] + word_appendage[1] + lower[int(number[1])] + word_appendage[0] + upper[int(number[2])] + ' ' +lower[int(number[3])]

elif (size == 4 and '0' in number[1]):
	print lower[int(number[0])] + word_appendage[1] + lower[int(number[1])]  + upper[int(number[2])] + ' ' +lower[int(number[3])]
