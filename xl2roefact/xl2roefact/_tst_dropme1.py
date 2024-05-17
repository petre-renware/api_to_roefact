

class C1:
    a: str

    def __init__(self, p):
        self.a = "a as instance var"
        a = "a as class var"
        self.b = a
        print(f"{self.a=}")
        print(f"{a=}")
        print(f"b instance var as copy of class a is: {self.b=}")



if __name__ == "__main__":
    x = C1(1)


