ortacha = 0 
katta = None
kichik = None
for i in range(5):
    yosh = int(input('yosh kiriting:'))
    if katta is None or yosh > katta:
        katta = yosh
    if kichik is None or yosh < kichik:
        kichik = yosh
ortacha = (katta + kichik) / 2
print('O\'rtacha:', ortacha)