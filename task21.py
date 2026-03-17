N = int(input('son kiriting:'))
juft = 0
toq = 0
for i in range(1, N+1):
    if i % 2 == 0:
        juft += i 
    else:
        toq += i
print('juft:', juft)
print('toq:', toq)