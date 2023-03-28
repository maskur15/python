#Data hiding in python
class Spam:
    _egg1=5 #single underscore use as weakly private
    __egg=3 #strongly private
    def show(self):
        print(self.__egg)
p=Spam()
p.show()
print(p._egg1)
#accessing the strong private attribute
print(p._Spam__egg)

