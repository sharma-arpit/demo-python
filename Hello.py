
def main(name):

    if name == "Arpit":
        print(f"1 Hello! {name}")
    elif name == "World":
        print(f"1 Hello! {name}")
    else:
        print("Hello")

    print("2 Hello!", name)
    print("3 Hello! {0}".format(name))
    print("4 Hello! %s"%(name))
    print("5 Hello! " + name)


if __name__ == "__main__":
    name = input("Hello! Type your name:")

    main(name=name)
