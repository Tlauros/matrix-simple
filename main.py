a = int(input("Number first : ")) #enter default 1
b = int(input("Number Second : ")) #enter default 2
c = int(input("Number third : ")) #enter default 3
f = []
f.append(a)
f.append(b)
f.append(c)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            print(f[i] , f[j] , f[k])

