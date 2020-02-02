handle = open('mail.txt')
counts=dict()
for line in handle:
	if not line.startswith('From'): continue
	l=line.split()
	if len(l)<3:continue
	t=l[len(l)-2][0:2]
	counts[t]=counts.get(t,0)+1
lst=sorted(counts.items())
for v,k in lst[:]:
	print(v,k)
print('change #1')