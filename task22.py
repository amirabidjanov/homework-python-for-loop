N = 5
katta = None
kichik = None
for i in range(N):
    narx = int(input('narxni kiriting:'))
    if katta is None or narx > katta:
        katta = narx
    if kichik is None or narx < kichik :
        kichik = narx
ortacha = (katta + kichik) / 2 
print('O\'rtacha', ortacha)