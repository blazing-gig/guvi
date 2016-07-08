n = int(raw_input())
l = []

l = map(int, raw_input().split())

if len(l) > n:
	print 0
elif len(l) == 1:
	print 0
else:
	flag = 0
	d = dict.fromkeys(l,0)
	for key in l:
		d[key] = d[key] + 1
	for key in d.keys():
		if d[key] > 1:
			print key
			flag = 1
	if flag == 0:
		print 0
