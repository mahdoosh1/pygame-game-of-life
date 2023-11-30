def extent2d(arr):
    y = len(arr)
    x = len(arr[0])
    new = [[False for _ in range(x+2)] for _ in range(y+2)]
    for j in range(y+2):
        for i in range(x+2):
            new[j][i] = arr[(j-1)%y][(i-1)%x]
    return new
def replace2(inp,arena,x,y,typ):
    replaced = []
    for i in inp:
        if type(i) is str:
            replaced.append(filter(i,arena,x,y,typ))
        elif type(i) is list:
            replaced = replaced + [search(i)]
    return idxs
def filter(inp,arena,x,y,typ):
    if ":" in inp: return isin(inp,arena,x,y,typ)
    else: return inp
def isin(st,arena,x,y,typ):
    n = neigh(arena,x,y,typ,extent=True,state=int(st.split(":")[0]))
    return bool(str(n)in(st.split(":")[1]))
def neigh(arr,idx,idy,typ=8,extent=False,state=1):
    y = len(arr)
    x = len(arr[0])
    f = int(extent)
    if typ >= 8 and (idx+2+f)%x > (idx-1+f)%x:
        t = arr[(idy-1+f)%y][(idx-1+f)%x:(idx+2+f)%x]
        m = [arr[idy+f][(idx-1+f)%x]]+[arr[idy+f][(idx+1+f)%x]]+([arr[idy+f][(idx+f)%x]] if typ == 9 else [])
        b = arr[(idy+1+f)%y][(idx-1+f)%x:(idx+2+f)%x]
        out = (t+m+b).count(state)
    else:
        if not extent:
            extent = []
            for i in extent2d(arr):
                extent.append(arrint(i))
        else:
            extent = arr
        ne = [extent[idy][idx] if (typ!=4) else 0]
        n = [extent[idy][idx+1]]
        nw = [extent[idy][idx+2] if (typ!=4) else 0]
        e = [extent[idy+1][idx]]
        m = [extent[idy+1][idx+1] if (type == 9) else 0]
        w = [extent[idy+1][idx+2]]
        se = [extent[idy+2][idx] if (typ!=4) else 0]
        s = [extent[idy+2][idx+1]]
        sw = [extent[idy+2][idx+2] if (typ!=4) else 0]
        out = (ne+n+nw+e+m+w+se+s+sw).count(state)
    return out
def arrint(arr,st=False):
    return set(map(int,set(arr))) if st else list(map(int,list(arr)))
def construct(y,x):
    return [[None for _ in range(x)] for _ in range(y)]
def simulate(arr,rule): return nextframe(arr,rule)rule if rule["mode"] else nextframe2(arr,rule)
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
def nextframe2(arr,rule):
    extent = []
    for i in extent2d(arr):
        extent.append(arrint(i))
    s = {}
    temp = []
    for key, val in rule.items():
        if not key in ["mode","type"]:   s[key] = val
        else:                            typ = val
    y = len(arr)
    x = len(arr[0])
    new = arr
    for j in range(y):
        for i in range(x):
            cell = arr[j][i]
            for key,val in s.items():
                frm,to = list(map(int,key.split(":")))
                if bool(eval(str(replace2(val,extent,i,j,typ))
                .replace("[","(").replace("]",")")
                .replace(",","").replace("'",""))) and (cell == frm):
                    new[j][i] = to
    return new
def revule(rule):
    if rule[mode] == 0:
        psb = list(range(8,-1,-1))
        inv = set(range(9))
        return {
        "type":rule["type"],
        "survive":''.join(list(map(str,[psb[i] for i in inv-arrint(rule["born"],True)]))),
        "born":''.join(list(map(str,[psb[i] for i in inv-arrint(rule["survive"],True)])))
        }
    else:
        new = rule
        for key,val in rule.items():
            if not key in ["mode","type"]:
                new[key] = ["not",val]
        return new
CONWAY = {
"mode": 0
"type":8,
"survive":"23",
"born":"3"
}
WIREWORLD = {
"mode": 1
"type":8,
"1:2":["2:12"],
"2:3":["True"],
"3:1":["True"]
}
DAYNIGHT = {
"type":8,
"survive":"34678",
"born":"3678"
}
if __name__ == '__main__':
    print("Sorry, this is a module. not an executable.")
    input("Press enter to exit...")