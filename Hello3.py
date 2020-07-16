import argparse


def argParse():

    parser = argparse.ArgumentParser()
    parser.add_argument("--employee_name", help="Name to greet", required=True)
    parser.add_argument("--psid", help="PeopleSoft ID", required=False, default=None)
    arguments = parser.parse_args()

    return arguments


def main(name_list, psid_list):

    Employee = {}

    for i in range(0, len(name_list)):
        Employee[name_list[i]] = psid_list[i]

    for name in Employee:
        print("Name:", name)
        print("PSID:", Employee[name])


if __name__ == "__main__":

    args = argParse()

    employee_name = args.employee_name.split(',')
    psid = args.psid.split(',')

    main(name_list=employee_name, psid_list=psid)
