#Arithmetic
#1
a = 25
b = 4

print("Addition:", a + b)        
print("Subtraction:", a - b)     
print("Multiplication:", a * b)  
print("Division:", a / b)        
print("Floor Division:", a // b) 
print("Modulus:", a % b)         
print("Exponent:", a ** b)   

#2
marks = 87
total = 100

marks_left = total - marks
remainder = marks % total

print("Marks left to reach total:", marks_left)  
print("Remainder:", remainder)    

#3
a = 100
b = 3

times_fit = a // b   
leftover = a % b     

print("b fits into a:", times_fit, "times")  
print("Left over:", leftover)     

#4
a = 3
b = 4

result = a ** b
print("3 to the power of 4:", result)  

#5
a = 20
b = 5

sum_result = a + b
product_result = a * b

print("Sum:", sum_result)        
print("Product:", product_result) 

#Comparision
#1
price = 100
budget = 80

print("Within budget:", price <= budget)  
print("Over budget:", price > budget) 

#2
a = 7
b = 7

print(a == b)   
print(a != b)   
print(a >= b)   
print(a <= b)  

#3
score = 40
passing = 40

has_passed = score >= passing
print("Student has passed:", has_passed)

#4
x = 15
y = 20

print(x == y)  
print(x != y)  
print(x > y)   
print(x < y)   
print(x >= y)  
print(x <= y) 

#5
x = 8
y = 3

print("x > y:", x > y)      
print("x != y:", x != y)

#Logical
#1
age = 25
has_id = True

print(age >= 18 and has_id)  
print(age >= 18 or has_id)  
print(not has_id) 

#2
logged_in = True

is_logged_out = not logged_in
print("User is logged out:", is_logged_out)

#3
is_member = False
has_coupon = False

gets_discount = is_member or has_coupon
print("Gets discount:", gets_discount)

#4
has_ticket = True
has_id = True

can_enter = has_ticket and has_id
print("Can enter event:", can_enter) 

#5
is_student = True
is_senior = False

gets_discount = is_student or is_senior
print("Gets discount:", gets_discount)