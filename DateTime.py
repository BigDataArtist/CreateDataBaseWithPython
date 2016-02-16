import datetime

start = datetime.datetime.now()

i = 0

while i < 10000000:
	i=i+1
	print(i)


end = datetime.datetime.now()	

print(end-start)
