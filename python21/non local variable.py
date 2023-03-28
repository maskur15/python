#Non local variable page 137
#python undergraduate course
def outer ():
    title = "original title"
    def inner():
        nonlocal title
        title+=" maskur"
        print(title)
    print(title)
    inner()
outer()
