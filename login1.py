import time
from admin import Admin
from student import Students
print("-------------------WELCOME-----------------------------")
class Main:
    def main123(self):
        while 1:
            print("\n1.Admin\n2.Student\n3.Exit")
            val=input("Enter Your Choice:")
            l=Admin()
            s=Students()
            if val=="1":
                l.admin()
            elif val=="2":
                s.studLogin()
            elif val=="3":
                print("------------------------------LOGGING OUT-------------------------------------")
                time.sleep(2)
                print("---------------------------------LOGGED OUT-----------------------------------")
                break
            else:
                print("----------------------------------Enter proper Choice-------------------------------------")

