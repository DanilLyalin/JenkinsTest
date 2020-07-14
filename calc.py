import sys

args = sys.argv
if len(args) != 4:
	print("Неверный параметр!")
else:
	op,x,y = args[1],float(args[2]),float(args[3])
	if op in ('+', '-', '*', '/'):
		if op == '+':
			print("%.10f" % (x+y))
		elif op == '-':
			print("%.10f" % (x-y))
		elif op == '*':
			print("%.10f" % (x*y))
		elif op == '/':
			if y == 0:
				print("Деление на ноль!")
				exit()
			print("%.10f" % (x/y))
	else:
		print("Неверный параметр!")