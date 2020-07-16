import argparse


def argParse():

    parser = argparse.ArgumentParser()
    parser.add_argument("--employee_name", help="Name to greet", required=True)
    parser.add_argument("--psid", help="PeopleSoft ID", required=False, default=None)
    arguments = parser.parse_args()

    return arguments


def main(name, psid):
    
    print("Name:", name)
    print("PSID:", psid)


if __name__ == "__main__":

    args = argParse()

    employee_name = args.employee_name
    psid = args.psid

    main(name=employee_name, psid=psid)
