
class Employee:

    def __init__(self, name, psid=None):
        self.name = name
        self.psid = psid
        self.dept = None

    def set_dept(self, dept):
        self.dept = dept

    def __str__(self):
        return "Name: " + self.name + ", PSID: " + self.psid + ", DEPT: " + self.dept