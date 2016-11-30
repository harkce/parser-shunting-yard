# referensi: https://en.wikipedia.org/wiki/Shunting-yard_algorithm

def isOp(x):
	return (x != 1)

# numbers = map(int, raw_input().split())
numbers = [1]

stackop = list()
stackrs = list()

valid = True
conditional = False

for x in numbers:
	if isOp(x):											# cek apakah x operator atau proposisi
		if not stackop:									# cek apakah list stackop kosong
			stackop.append(x)							# tambahkan element ke stackop
		else:											# kalo stackop nya engga empty
			if x == 10:									# cek apakah x itu )
				while stackop[-1] != 9:					# lakukan terus sampai ketemu (
					stackrs.append(stackop.pop())		# pop stackop, push ke stackrs
				stackop.pop()							# pop stackop, ngepop si (
			else:										# kalo x bukan ), berarti operator yg lain
				if (x > stackop[-1]) and (x != 9):		# kalo x lebih rendah prioritasnya dan bukan (
					stackrs.append(stackop.pop())		# pop stackop, masukin ke stackrs
				stackop.append(x)						# masukin x ke stackop
	else:												# kalo bukan operator (proposisi)
		stackrs.append(x)								# tinggal push ke stackrs
		# if len(stackrs) > 1:
		# 	if (stackrs[-1] == 1) and (stackrs[-2] == 1):
		# 		valid = False

while stackop:											# kalo stackop masih berisi
	stackrs.append(stackop.pop())						# push sisanya ke stackrs

while (valid) and (len(stackrs) > 1):
	if conditional:
		i += 1
	else:
		i = 0
	while (stackrs[i] == 1) and (valid):		# cari sampai ketemu operator
		i += 1
	if stackrs[i] == 2:			# kalo ketemu NOT
		if stackrs[i - 1] == 1:
			stackrs.pop(i)
		else:
			valid = False
	elif (stackrs[i] == 3) or (stackrs[i] == 4) or (stackrs[i] == 5) or (stackrs[i] == 8):	# kalo ketemu AND, OR, XOR, IFF
		if (stackrs[i - 1] == 1) and (stackrs[i - 2] == 1):									# cek 2 token sebelumnya, harus proposisi
			stackrs.pop(i)
			stackrs.pop(i - 1)
		else:
			valid = False
	elif stackrs[i] == 6:
		conditional = True
	elif stackrs[i] == 7:																# kalo ketemu THEN
		conditional = False
		if (stackrs[i - 1] == 1) and (stackrs[i - 2] == 6) and (stackrs[i - 3] == 1):	# cek apakah ada IF atau engga
			stackrs.pop(i)
			stackrs.pop(i - 1)
			stackrs.pop(i - 2)
		else:
			valid = False

print numbers
if valid and (stackrs[0] == 1):
	print "VALID"
else:
	print "TIDAK VALID"