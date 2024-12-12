def maksimal(a, b):
    max = a
    if b>max:
        max = b
    return max
def minimal(a, b):
    min = a
    if b<min:
        min = b
    return min
batas = 0
bilangan = int(input())
nilai = list(map(int,input().split()))
minim = 100000
maks = -100000
while batas < bilangan:
    nilai1=nilai[batas]
    maks = maksimal(maks, nilai1)
    minim = minimal(minim, nilai1)
    batas = batas + 1
print(maks, minim)

