#1
numbers = (1,2,3,4,5,6,7,8,9,10)
print(numbers[2:7])

#2
tuple = (1, 5, 2, 5, 3, 5, 4, 5, 6, 5)
print(tuple.count(5))

#3
num1 = (10,20,30,40,50)
print(100 in num1)

#4
num2 = {1,2,3,4,5}
num2.add(6)
print(num2)

#5
num2.remove(3)
print(num2)

#6
num3 = {1,2,3,4,5,5,5}
print(len(num3))

#7
student = {
    "name" : "Thabu",
    "age" : 20,
    "city": "London"
}
print(student["name"])

#8
print(student.keys())

#9
mark =  {'roll': 101, 'name': 'Rahul', 'marks': 85, 'grade': 'A'}
print(mark['marks'])

#10
mark.update({"grade": "A+"})
print(mark)