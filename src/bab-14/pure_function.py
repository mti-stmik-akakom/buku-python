# pure_function.py

a = 200

def no_change_state():

    # jangan mengakses variable dari luar scope def func ini
    # 

    return 10*10

print(no_change_state())
print(no_change_state())
print(no_change_state())
print(no_change_state())
print(no_change_state())
