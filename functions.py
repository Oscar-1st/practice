'''FUNCTIONS
(1) DEFINE & CALL
(2) Parametr & Atguments
(3) Keyword & default arguments
(4) Scope
'''
print("=== DEFINE vs CALL =====")
# build in function > print () type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - parametr
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - argument
result1 = greet('Oscar')
print(" resultl:", result1)

result2 = greeting("Justin")
print("result:", result2)


print("==== Keyword & default arguments =====")


# DEFINE
def give_greet(name, age=20):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
result3 = give_greet(name="Oscar", age=22)
print("result3:", result3)

result4 = give_greet("Wwx")
print("result4:", result4)
