class A:
    def say(self):
        print("a")


class B:
    def say(self):
        print("b")


class C(A, B):  # Method Resolution Order
    def say(self):
        super().say()
        # B.say(self)
        super(A, self).say()


C().say()
print(C.__mro__)
