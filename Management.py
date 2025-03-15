employees=[{"Name":"Sakthi","Age":19,"Type":"Employee","Role":"Data Scientist","Salary":87000,"No of leaves":0,"Alerts":[]},{"Name":"Jeevan","Age":19,"Type":"Employee","Role":"Tester","Salary":87000,"No of leaves":0,"Alerts":[]},{"Name":"Magesh","Age":20,"Type":"Employee","Role":"Developer","Salary":87000,"No of leaves":0,"Alerts":["You're fired."]},
           {"Name":"Ram","Age":24,"Type":"HR","Role":"Human Resource","Salary":96000,"No of leaves":0,"Alerts":[]},{"Name":"Raghu","Age":26,"Type":"HR","Role":"Human Resource","Salary":96500,"No of leaves":0,"Alerts":[]},{"Name":"Ravi","Age":24,"Type":"HR","Role":"Human Resource","Salary":94000,"No of leaves":0,"Alerts":[]},
           {"Name":"Hema","Age":28,"Type":"Manager","Role":"Product Manager","Salary":120000,"No of leaves":0,"Alerts":[]},{"Name":"Rohit","Age":26,"Type":"Manager","Role":"Manager","Salary":130000,"No of leaves":0,"Alerts":[]},{"Name":"Mano","Age":30,"Type":"Manager","Role":"Manager","Salary":150000,"No of leaves":0,"Alerts":[]},{"Name":"Shankar","Age":36,"Type":"Admin","Role":"Administrator","Salary":180000,"No of leaves":0,"Alerts":[]}]
credentials=[{"emp id":"sakthi@gmail.com","password":"12345678"},{"emp id":"Jeevan@gmail.com","password":"12345678"},{"emp id":"Magesh@gmail.com","password":"12345678"},
             {"emp id":"ram@gmail.com","password":"12345"},{"emp id":"raghu@gmail.com","password":"12346"},{"emp id":"ravi@gmail.com","password":"12347"},
             {"emp id":"hema@gmail.com","password":"12345"},{"emp id":"rohit@gmail.com","password":"12346"},{"emp id":"mano@gmail.com","password":"12347"}]


class Employee:

    
    def info(self):
        print("Name:",employees[self.ind]["Name"])
        print("Age:",employees[self.ind]["Age"])
        print("Role:",employees[self.ind]["Role"])
        print("Salary:",employees[self.ind]["Salary"])
        print("No of leaves:",employees[self.ind]["No of leaves"])

    def check_alerts(self):

        if employees[self.ind]["Alerts"]:
            print("Inbox:",employees[self.ind]["Alerts"])
            if any("fire" in alert.lower() for alert in employees[self.ind]["Alerts"]):
                        print("Here after you cannot login again ")
                        employees.pop(self.ind)
                        credentials.pop(self.ind)
                        self.ind=-1
        else:
            print("Inbox: No messages")
            
    def request_leave(self):
        self.reason=input("Enter your reason:")
        employees[self.ind]["No of leaves"]+=1
        if employees[self.ind]["No of leaves"] >4:
            print("Your request for the leave has been accepted👍")
            print("Alert:Your salary will be deducted by 1000")
            
        else:
            print("Your request for the leave has been accepted👍")
 

        

class HR(Employee):


    def HR_info(self):
        print("Name:",employees[self.ind]["Name"])
        print("Age:",employees[self.ind]["Age"])
        print("Role:",employees[self.ind]["Role"])
        print("Salary:",employees[self.ind]["Salary"])
        print("No of leaves:",employees[self.ind]["No of leaves"])

    def check_alerts_hr():
        if employees[self.ind]["Alerts"]:
            print("Inbox:",employees[self.ind]["Alerts"])
            if any("fire" in alert.lower() for alert in employees[self.ind]["Alerts"]):
                        print("Here after you cannot login again ")
                        employees.pop(self.ind)
                        credentials.pop(self.ind)
        else:
            print("Inbox: No messages")
            
        
            
    def emp_info(self):
        get=input("Enter the employee id:")
        index=-1
        for i in range(len(employees)):
            if check == credentials[i]["emp id"] and employees[i]["Type"]=="Employee":

                print("Name:",employees[self.ind]["Name"])
                print("Age:",employees[self.ind]["Age"])
                print("Role:",employees[self.ind]["Role"])
                print("Salary:",employees[self.ind]["Salary"])
                print("No of leaves:",employees[self.ind]["No of leaves"])
        
        if i<0:
            print("Employee not found🤷‍♂️.")
            print("Or double check your input.")


    def List_of_employees_hr_chk(self):
        for i in range(len(employees)):
            if employees[i]["Type"]=="Employee":
                print(employees[i])
    
    def Check_leave(self):
        get=input("Enter the employee id:")
        i=0
        for i in range(len(employees)):
            if get == credentials[i]["emp id"] and employees[i]["Type"]=="Employee":
            
                print("No of leaves:",employees[i]["No of leaves"])
                if employees[i]["No of leaves"] >4:
                    print('''Your salary is deducted by 1k.
                             Explain about your inconsistency in terms of attendance to the HR.''')

        if i<0:
            print("Employee not found🤷‍♂️.")
            print("Or double check your input.")

    
    def raise_alert_by_hr(self):
        get=input("Enter the employee id:")
        index=-1
        
        for i in range(len(employees)):
            if get == credentials[i]["emp id"] and employees[i]["Type"]=="Employee":
                index=i
                
                print('''Choose the type of alert
                        1.Notify them about something
                        2.Notify them about their dismissal''')
                type_of_alert=int(input("Enter option:"))

                if type_of_alert==1:
                    self.notification=input("Enter your message:")
                    employees[i]["Alerts"].append(self.notification)

            
                elif type_of_alert==2:
                    self.reason_fire=input("Enter the proper reason for firing this employee:")
                    employees[i]["Alerts"].append(self.reason_fire)
                    
        
        if i<0:
            print("Employee not found🤷‍♂️.")
            print("Or double check your input.")


class Manager(HR):

    def __init__(self,employees,credentials):
        self.employees=employees
        self.credentials=credentials
        # self.notifications=notifications
        # self.reason_fire=reason

    def manager_info(self):
        print("Name:",employees[self.ind]["Name"])
        print("Age:",employees[self.ind]["Age"])
        print("Role:",employees[self.ind]["Role"])
        print("Salary:",employees[self.ind]["Salary"])
        print("No of leaves:",employees[self.ind]["No of leaves"])
            
    def emp_info(self):
        get=input("Enter the employee id:")
        index=-1
        for i in range(len(employees)):
            if get == credentials[i]["emp id"] and employees[i]["Type"]=="Employee":
                print("Name:",employees[i]["Name"])
                print("Age:",employees[i]["Age"])
                print("Role:",employees[i]["Role"])
                print("Salary:",employees[i]["Salary"])
                print("No of leaves:",employees[i]["No of leaves"])
                index=i
        
        if index<0:
            print("Employee not found🤷‍♂️.")
            print("Or double check your input.")


    def List_of_employees_Mg_chk(self):
        for i in range(len(employees)):
            if employees[i]["Type"]=="Employee":
                print(employees[i])

    def HRs_info(self):
        get=input("Enter the HR id:")
        index=-1
        for i in range(len(employees)):
           if get == credentials[i]["emp id"] and employees[i]["Type"]=="Employee":
                print("Name:",employees[i]["Name"])
                print("Age:",employees[i]["Age"])
                print("Role:",employees[i]["Role"])
                print("Salary:",employees[i]["Salary"])
                print("No of leaves:",employees[i]["No of leaves"])
        
        if i<0:
            print("Employee not found🤷‍♂️.")
            print("Or double check your input.")

           
    
    def List_of_HRs(self):
        for i in range(len(employees)):
            if employees[i]["Type"]=="HR":
                print(employees[i])

    def raise_alert_by_mg(self):
        get=input("Enter the employee id:")
        index=-1
        for i in range(len(employees)):
            if get == credentials[i]["emp id"] and employees[i]["Type"]=="Employee":
                index=i
                print('''Choose the type of alert
                        1.Notify them about something
                        2.Notify them about their dismissal''')
                type_of_alert=int(input("Enter option:"))

                if type_of_alert==1:
                    self.notification=input("Enter your message:")
                    employees[i]["Alerts"].append(self.notification)

            
                elif type_of_alert==2:
                    self.reason_fire=input("Enter the proper reason for firing this employee:")
                    employees[i]["Alerts"].append(self.reason_fire)
                    
            
        if i<0:
            print("Employee not found🤷‍♂️.")
            print("Or double check your input.")

            
                
    def add(self):
        print("Fill the below details to add an employee")
        name=input("Enter the name of the employee:")
        age=int(input("Enter their age:"))
        type_emp=input("Enter the type of the employee:")
        role=input("Enter their role:")
        salary=int(input("Enter their salary:"))

        print("Create their employee id and password")
        emp_id=input("create their id:")
        password=input("create a password:")
        Confirm_password=input("Confirm password:")

        if password == Confirm_password:
            new_employee={"Name":name,"Age":age,"Type":type_emp,"Role":role,"Salary":salary,"No of leaves":0,"Alerts":[]}
            employees.append(new_employee)
            new_credential={"emp id":emp_id,"password":password}
            credentials.append(new_credential)

    def login(self):
        
        check=input("Enter your emp id:")
        check2=input("Enter password:")

        for i in range(len(employees)):
            if check ==credentials[i]["emp id"] and check2 ==credentials[i]["password"]:
                print("You're logged in")
                self.ind=i
             
                return True
        return False

        
m=Manager(employees,credentials)
while True:
    p=int(input("Press 1 for Login :"))
    if p==1:
        
        t=m.login()
        while t==True:
            if m.ind <0:
                break
            if employees[m.ind]["Type"]=="Employee":

                if  employees[m.ind]["Alerts"]:
                    print("You have some alerts in your inbox. Please do check it")
                   

                print('''
                        1.Info
                        2.Request Leave
                        3.Alerts
                        4.End session.
                    ''')
                opt=int(input("Enter the option:"))
            
                if opt==1:
                    m.info()
                elif opt==2:
                    m.request_leave()
                elif opt==3:
                    m.check_alerts()
                    if any("fire" in alert.lower() for alert in employees[m.ind]["Alerts"]):
                        break
                elif opt==4:
                    break

            elif employees[m.ind]["Type"]=="HR":

                if  employees[m.ind]["Alerts"]:
                    print("You have some alerts in your inbox. Please do check it")
                 

                print('''
                        1.Info
                        2.List of employees
                        3.Info of an employee
                        4.Check leaves of an employee
                        5.Raise an alert to an employee
                        6.Check alerts
                        7.End session.
                    ''')
                opt=int(input("Enter the option:"))

                if opt==1:
                    m.HR_info()
                elif opt==2:
                    m.List_of_employees_hr_chk()
                elif opt==3:
                    m.emp_info()
                elif opt==4:
                    m.Check_leave()
                elif opt==5:
                    m.raise_alert_by_hr()
                elif opt==6:
                    m.check_alerts_hr()
                    if any("fire" in alert.lower() for alert in employees[m.ind]["Alerts"]):
                        break
                else:
                    break

            elif employees[m.ind]["Type"]=="Manager":

                print('''
                        1.Info
                        2.List of employees
                        3.List of HRs
                        4.Info of an employee
                        5.Info of a HR
                        6.Raise an alert to an employee
                        7.Appoint an employee
                        8.End session.
                    ''')
                opt=int(input("Enter the option:"))

                if opt==1:
                    m.manager_info()
                elif opt==2:
                    m.List_of_employees_Mg_chk()
                elif opt==3:
                    m.List_of_HRs()
                elif opt==4:
                    m.emp_info()
                elif opt==5:
                    m.HRs_info()
                elif opt==6:
                    m.raise_alert_by_mg()
                elif opt==7:
                    m.add()
                else:
                    break























       

      
