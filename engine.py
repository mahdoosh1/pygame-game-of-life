def extent2d(arr):
	y = len(arr)
	x = len(arr[0])
	new = [[False for _ in range(x+2)] for _ in range(y+2)]
	for j in range(y+2):
		for i in range(x+2):
			new[j][i] = arr[(j-1)%y][(i-1)%x]
	return new
def neigh(arr,idx,idy,typ=8,extent=False):
	y = len(arr)
	x = len(arr[0])
	f = int(extent)
	if typ == 8 and (idx+2+f)%x > (idx-1+f)%x:
		t = arr[(idy-1+f)%y][(idx-1+f)%x:(idx+2+f)%x]
		m = arr[idy+f][(idx-1+f)%x:(idx+2+f)%x]
		b = arr[(idy+1+f)%y][(idx-1+f)%x:(idx+2+f)%x]
		out = sum(t+m+b)-arr[idy+f][idx+f]
	else:
		if not extent:
			extent = []
			for i in extent2d(arr):
				extent.append(arrint(i))
		else:
			extent = arr
		ne = extent[idy][idx] if (typ!=4) else 0
		n = extent[idy][idx+1]
		nw = extent[idy][idx+2] if (typ!=4) else 0
		e = extent[idy+1][idx]
		w = extent[idy+1][idx+2]
		se = extent[idy+2][idx] if (typ!=4) else 0
		s = extent[idy+2][idx+1]
		sw = extent[idy+2][idx+2] if (typ!=4) else 0
		out = (ne+n+nw+e+w+se+s+sw)
	return out
def arrint(arr):
	return [int(i) for i in list(arr)]
def construct(y,x):
	return [[None for _ in range(x)] for _ in range(y)]
def nextframe(arr,rule):
	extent = []
	for i in extent2d(arr):
		extent.append(arrint(i))
	typ = rule["type"]
	born = arrint(rule["born"])
	surv = arrint(rule["survive"])
	y = len(arr)
	x = len(arr[0])
	new = construct(y,x)
	for j in range(y):
		for i in range(x):
			cell = arr[j][i]
			n = neigh(extent,i,j,typ,extent=True)
			cell = int(n in surv) if cell else int(n in born)
			new[j][i] = cell
	return new
CONWAY = {
"type":8,
"survive":"23",
"born":"3"
}
DAYNIGHT = {
"type":8,
"survive":"34678",
"born":"3678"
}
if __name__ == '__main__':
	print("Sorry, this is a module. not an executable.")
	input("Press enter to exit...")