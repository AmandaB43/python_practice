def hello():
    print("Oh hello deary.")
def pack(a,b,c):
    return[a,b,c]
def eat_lunch(my_1st):
    if len(my_1st) == 0:
        print("I have no lunch!")
    else:
        for i in range(len(my_1st)):
            if i == 0:
                print(f"First I eat {my_1st[0]}")
            else:
                print(f'Next I eat {my_1st[i]}')
hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana", "sandwich", "cookie"])