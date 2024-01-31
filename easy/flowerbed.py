flowerbed = [1,0,0,0,0,1]
n = 1
x=0
i=0

if flowerbed == [0]:
    x=1
else: 
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        x += 1
        i = 2

    while i < len(flowerbed) - 2:
        if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            x += 1
            i += 2
        else:
            i += 1
    if len(flowerbed) > 2:
        if flowerbed[len(flowerbed) -2] == 0 and flowerbed[len(flowerbed) -1] == 0:
            x += 1
print(x >= n)