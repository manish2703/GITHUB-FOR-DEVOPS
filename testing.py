"""
Basic Python demo module.
Shows variables, conditions, functions, and loops.
"""

# print output
print("Hello, World!")

# constants
USER_NAME = "Manish"
AGE = 31

# condition
if AGE >= 18:
    print("Adult")
else:
    print("Minor")


def greet(user_name):
    """Return a greeting message for the given user."""
    return f"Hello, {user_name}"


print(greet(USER_NAME))

# loop
for i in range(3):
    print(i)

