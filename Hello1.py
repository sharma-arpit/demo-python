import argparse


def argParse():

    parser = argparse.ArgumentParser()
    parser.add_argument("--employee_name", help="Name to greet", required=True)
    arguments = parser.parse_args()

    return arguments


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
    # name = input("Hello! Type your name:")

    args = argParse()
    employee_name = args.employee_name

    main(name=employee_name)
