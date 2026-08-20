#task 1
vegetables =["onion","tomato","carrot","potato","spinach"]

for vegetable in vegetables:
    print (vegetable)


#task 2
prices = [45,120,89,200,55,150,30,180]
count=0
for i in prices:
    if i>100:
        count=count+1
print(count)

#task 3
for i in range(2,21,2):
    print(i)

#task 4
for i in range (5,0,-1):
    print(i)
print("done")

#task 5
items = [120,80,200,150,60,90,110]
total=0
for i in items:
    total=total+i

    if total>=500:
        break
print(total)

