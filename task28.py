N = int(input('qancha son kiritilsin:'))
katta = None
kichik = None
for i in range(N):
    son = int(input('ball:'))
    if katta is None or son > katta:
        katta = son
    if kichik is None or son < kichik:
        kichik = son
print('yuqori:',katta,'past:',kichik)