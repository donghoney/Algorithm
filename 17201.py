n = int(input())
mg = input()
num = 0
	
if len(mg) != n*2:
	print("No")
else:
	pre = mg[0]
	for a in mg:
		if a == '1' and pre == '2':
			pre = a
			num+=1
		elif a == '2' and pre == '1':
			pre = a
			num+=1
	if num == (2*n-1):
		print("Yes")
	else:
		print("No")
