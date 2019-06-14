
try:
    int("a")
except ValueError as e:
    print("value error", e)

print("this is error")