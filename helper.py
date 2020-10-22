
class Employee:

    def __init__(self, name, psid=None):
        self._name = name
        self._psid = psid
        self._dept = None

    def set_dept(self, dept):
        self._dept = dept

    def set_psid(self, psid):
        self._psid = psid

    def set_name(self, name):
        self._name = name

    def get_dept(self):
        return self._dept

    def get_psid(self):
        return self._psid

    def get_name(self):
        return self._name
        
    def __str__(self):
        return "Name: " + self.name + ", PSID: " + self.psid + ", DEPT: " + self.dept
