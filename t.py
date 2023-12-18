k=1000
m=1000000
b=1000000
f="238B Followers".lower()
g=int("".join([i for i in f if i.isdigit()]))
if "k"  in f:
    g=g*k
elif "m" in f:
    g=g*m
elif "b" in f:
    g=g*b
else:
    g=g*1
print(g)