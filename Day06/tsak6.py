#Tuple
nums = (80,90,75,95,88)
print(max(nums))
print(min(nums))
print(sum(nums)/len(nums))
print(nums[4])

#list
citys = ["chennai","madurai","salem"]
citys[1]="coimbatore"
print(citys)

tuple = (10,20,30,20,40)
print(tuple.count(20))
print(tuple.index(30))

student = {
"id": 101,
"name": "thabu",
"salary": 35000
}
print(student.keys())
print(student.values())
student.pop("salary")
student.update({"id": 105})
print(student)