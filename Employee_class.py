class Employee:
    def __init__(self, i_num, fname, lname, work_experience, education_level, salary, age):
        self.i_num = i_num
        self.fname = fname
        self.lname = lname
        self.work_experience = work_experience
        self.education_level = education_level
        self.salary = salary
        self.age = age
    def display_info(self):
        return f"{self.i_num} {self.fname} {self.lname} {self.work_experience} {self.education_level} {self.salary} {self.age}"
    
    def __repr__(self):
        return f"{self.i_num} {self.fname} {self.lname} {self.work_experience} {self.education_level} {self.salary} {self.age}"
    
    def bonus(self):
        if self.education_level == "Висше образование" and self.work_experience >= 0:
            self.salary += self.salary * (5/100) + ((self.salary * (1.2/100)) * self.work_experience)
            print(self.salary)
        elif self.education_level == "Средно образование" and self.work_experience >= 0:
            self.salary += self.salary * (2/100) + ((self.salary * (1.2/100)) * self.work_experience)
            print(self.salary)
        elif self.education_level == "Основно образование" and self.work_experience >= 0:
            self.salary = self.salary + ((self.salary * (1.2/100)) * self.work_experience)
            print(self.salary)

employee_list = []

while True:
    i_num = int(input("Enter i_num: "))
    if i_num == 0:
        break
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ") 
    work_ex = int(input("Enter Work expirience: "))
    education_level = input("Enter education level: ")
    salary = int(input("Enter salary: "))
    age = int(input("Enter age: "))
    employee_list.append(Employee(i_num, fname, lname, work_ex, education_level, salary, age))

def sort_employee(employee_list):
    print(sorted(employee_list, key = lambda x:x.age, reverse = False))
      

def search_by_name(employee_list,fname,lname):
    for x in employee_list:
        if fname == x.fname and lname == x.lname:
            print(x)
            return
    else:
        print("Not found")


def print_by_education_experience(employee_list, education, experience):
    for x in employee_list:
        if education == x.education_level and experience == x.work_experience:
            print(x)

def remove_employee(employee_list, i_num):
    for x in employee_list:
        if i_num == x.i_num:
            employee_list.remove(x)
            print("Information deleted")
            return
    else:
        print("Wrong i_num")  

#display information for all employees
#for emp in employee_list:
    #print(emp.display_info())

# call the bonus method for each employee
for x in employee_list:
    print(x.bonus())

Employee.bonus(education_level)

#display information for all employees after bonus
#for emp in employee_list:
    #print(emp.display_info())

sort_employee(employee_list)
search_by_name(employee_list, "Martin", "Petkov")
print_by_education_experience(employee_list, "Висше образование", 5)
remove_employee(employee_list, 3)
