import argparse
import helper


def argParse():

    parser = argparse.ArgumentParser()
    parser.add_argument("--employee_name", help="Name to greet", required=True)
    parser.add_argument("--psid", help="PeopleSoft ID", required=False, default=None)
    arguments = parser.parse_args()

    return arguments


def main(name_list, psid_list):

    emp = []

    for i in range(0, len(name_list)):
        emp_object = helper.Employee(name=name_list[i], psid=psid_list[i])

        if psid_list[i] == "007":
            emp_object.set_dept(dept="BOND")
        else:
            emp_object.set_dept(dept="OTHER")

        emp.append(emp_object)

    for e in emp:
        print("Name:", e.name)
        print("PSID:", e.psid)
        print(e)
        print("-------------------")


if __name__ == "__main__":

    args = argParse()

    employee_name = args.employee_name.split(',')
    psid = args.psid.split(',')

    main(name_list=employee_name, psid_list=psid)
