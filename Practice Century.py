year = 1905
century = 0
if year >100:
    century= (year/100)+1
else:
    century=1
century= int(century)
print("siglos: " +str(century))