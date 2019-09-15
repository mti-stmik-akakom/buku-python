# non_pure_function.py

a = 200

def change_state():

    global a

    a += 100

    return a

print(change_state())
print(change_state())
print(change_state())
print(change_state())
print(change_state())

