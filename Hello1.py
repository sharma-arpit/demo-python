import argparse


def argParse():

    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="Name to greet", required=True)
    arguments = parser.parse_args()

    return arguments


def main(name):

    if name:
        print(f"1 Hello! {name}")
    else:
        print("Hello")
       

if __name__ == "__main__":

    args = argParse()
    name = args.name

    main(name=name)
