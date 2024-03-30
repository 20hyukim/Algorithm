dicta = {}

for i in range(10):
    a = int(input())
    dicta[a%42] = 1
    
print(len(dicta))