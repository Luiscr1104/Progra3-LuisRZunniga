a=[12, 46, 79, 45, 12, 14, 46]
r = []
u = []

for x in a:

    if x not in u:

        u.append(x)

    else:

        if x not in r:
            r.append(x)
if r == []:
    print(-2)
else:
    print("Los números repetidos en la lista son "+str(r))