
d8_0 = [0,1,2,3,4,5,6,7]
d8_1 = [1,2,3,0,5,6,7,4]
d8_2 = [2,3,0,1,6,7,4,5]
d8_3 = [3,0,1,2,7,4,5,6]
d8_4 = [4,7,6,5,0,3,2,1]
d8_5 = [5,4,7,6,1,0,3,2]
d8_6 = [6,5,4,7,2,1,0,3]
d8_7 = [7,6,5,4,3,2,1,0]
d8 = [d8_0, d8_1, d8_2, d8_3, d8_4, d8_5, d8_6, d8_7]

''' note that you only nneed to store half of the table because rows are 
reverse sequences of eachother'''

traslate = ['e','R','R^2', 'R^3', 'F', 'RF', 'R^2F', 'R^3F']

G = [0,1,2,3,4,5,6,7]
inverses = [0,3,2,1,4,5,6,7]

# let f be the congugate -> conjugacy group


stackSyb = []
stackNum = []
stackSybForBracket = []
stackNumForBracket = []

def mult():
	while len(stackSyb)>1:
		letterLeft = stackSyb.pop()
		letterRight = stackSyb.pop()

		numberLeft = stackNum.pop()
		numberRight = stackNum.pop()
		result = d8[numberLeft][numberRight]
		stackNum.append(result)
		stackSyb.append(traslate[result])

	print(stackSyb)
	print(stackNum)

def multInBracket():
	while len(stackSybForBracket)>1:
		letterLeft = stackSybForBracket.pop()
		letterRight = stackSybForBracket.pop()

		numberLeft = stackNumForBracket.pop()
		numberRight = stackNumForBracket.pop()
		result = d8[numberLeft][numberRight]
		stackNumForBracket.append(result)
		stackSybForBracket.append(traslate[result])


	print(stackSybForBracket)
	print(stackNumForBracket)

def parse(symString):
	print(symString)
	syms = list(symString)
	print(syms)
	while (len(syms)):
		# print("i: " + str(i))
		print(syms)
		sym = syms.pop()
		print(sym)
		if sym.isdigit():
			temp = sym
			print("temp: " + temp)
			if syms.pop() == '-':
				print("Neg")
				if syms.pop() == ')':
					while 1:
						symInBracket = syms.pop()
						if symInBracket == '(':
							break
						if symInBracket == 'F':
							stackNumForBracket.append(4)
							stackSybForBracket.append(sym)
						if symInBracket == 'R':
							stackNumForBracket.append(1)
							stackSybForBracket.append(sym)
					multInBracket()
					print(stackSybForBracket)
					print(stackNumForBracket)
					syms.append(stackSybForBracket)

				letter = syms.pop()
				print("Letter Neg: " + letter)
				if temp == '1':
					stackNum.append(3)
					stackSyb.append('R^3')
				if temp == '2':
					stackNum.append(2)
					stackSyb.append('R^2')
				if temp == '3':
					stackNum.append(1)
					stackSyb.append('R')


				# i += 3
			else:
				print("Not a neg")
				letter = syms.pop()
				if temp == '2':
					stackNum.append(2)
					stackSyb.append('R^2')
				if temp == '3':
					stackNum.append(3)
					stackSyb.append('R^3')
				

				# i += 2
		else:
			if sym == 'F':
				stackNum.append(4)
				stackSyb.append(sym)
			if sym == 'R':
				stackNum.append(1)
				stackSyb.append(sym)
	print(stackSyb)
	print(stackNum)


def orbit(x):
	orbit_list = []
	for i in range(0,8):
		#temp = d8[i][x]
		orbit_list += [d8[d8[i][x]][inverses[i]]]
		# for j in xrange(0,8):
		# 	string = translate[d8[i][j]]+translate[x]+translate[inverses[d8[i][j]]
		# 	parse(string)
	# print(orbit_list)
	# print(list(set(orbit_list)))

	return list(set(orbit_list))


def main(symString):
	orbits = []
	for i in range(0,8):
		orbits += [orbit(i)]

	print(orbits)
	# parse(symString)
	# mult()


main("R^2FR^3FFR^-2(RFRFR)^-1")
