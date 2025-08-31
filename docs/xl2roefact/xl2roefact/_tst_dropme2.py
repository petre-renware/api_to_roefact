
def a(p = ...):
    if p is None:
        print(f"p sent as {p=}")
        return
    if p == ...:
        print("p not specified in call")
        return


print("call without p")
a()

print("call with p = None")
a(None)
a(p=None)


print("call with p = 444")
a(444)



print("test if elipsis (`...`) is diffrent of None")
b = ...
n = None
t1 = bool(b == n)
t2 = bool(b is n)
print(f"test equal: {t1}")
print(f"test equal identity: {t2}")





 




