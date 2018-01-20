R=178
G=141
B=112

max=max(R,G,B)
min=min(R,G,B)
V=max
S=(max-min)/max
if R == max:
    H =(G-B)/(max-min)* 60
if G == max:
    H = 120+(B-R)/(max-min)* 60
if B == max:
    H = 240 +(R-G)/(max-min)* 60
if H < 0:
    H = H+ 360

print (R,G,B)