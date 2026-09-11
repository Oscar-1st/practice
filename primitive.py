print('====== number ======')
'''VARIABLE
JAVA/C:name of storage location;
PYTHON: variable is named reference! 
'''

count = 100
count_type = type(count)
print(f"he count: {count} and type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print('====== string ======')
# METHODS: upper() lower() title() find() replace()

course = "AI Python Fullstack"
result = type(course)
print(f"result (1): {course}")

result = course.title()  # makes capital every first letter of  word
print("result (2):", result)

result = course.upper()
print("result (3):", result)

result = course.replace("Fullstack", "MasterClass")
print("result (4):", result)

print('====== boolean ======')
# functions -> type() input() bool() int() str()
y = input("Give your value for y:")
print("y:", y)

result = y.isnumeric()
print(f"the numbers is numeric: {result}")

# TRUTHY vs FALSY value
# TRUTHY > True 100 -100 "MIT"
# FALSY > False 0 "" None

test_falsy = "" or False or None or 0
print("the FALSY:", bool(test_falsy))

test_truthy = "MIT"
print("the TRUTHY:", bool(test_truthy))
