import re
import csv
import mysql.connector
class password:
    @staticmethod
    def changepassword():
        mydb= mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="Shiyam@17",
                                      auth_plugin="mysql_native_password",
                                      database="application")

        mycursor=mydb.cursor(buffered=True)
        print("-----------------------CHANGE PASSWORD-------------------------")
        newPasswd=input("Enter your current password=")
        mycursor.execute("SELECT Student_Password FROM students_details")
        record=mycursor.fetchone()
        fl=True
        for x in record:
            if x==newPasswd:
                while 1:
                    nxtpasswd=input("Enter new password :")
                    nxt_passwd=input("Renter Password   :")
                    pattern=r"^[A-Z]+[A-Za-z]{6,29}$"
                    if nxtpasswd==nxt_passwd and re.search(pattern,nxtpasswd):
                        one=(nxt_passwd,rollNo)
                        two=("UPDATE Students_details SET Student_Password=%s WHERE Student_RollNo=%s")
                        mycursor.execute(two,one)
                        mydb.commit()
                        mydb.close()
                        print("******************Password Changed Succesfully*******************")
                        fl=False
                        break
                    else:
                        print("---------------Password Doesnot Match/Incorret Form---------------------")
        if fl==True:
            print("-------------------------Incorrect Password----------------------")
    
    @staticmethod
    def viewdetails():
        print("---------------Personal Details-------------------")
        print("['StudentName','RegNo','Dept','Year','MailId','Dob','Batch','Password']")
        mydb= mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="Shiyam@17",
                                      auth_plugin="mysql_native_password",
                                      database="application")

        mycursor=mydb.cursor()
        mycursor.execute("SELECT * FROM Students_Details WHERE Student_RollNo=%s",rollNo1)
        view=mycursor.fetchall()
        for x in view:
            print(x)
class Students(password):

    #Student Login
    @staticmethod
    def studLogin():
        global rollNo1
        global rollNo
        flag=True
        print("///////////////// STUDENT MODULE ////////////////")
        rollNo=int(input("Enter Register No\t\t\t:"))
        confpaw=input("Enter Password\t\t\t:")
        rollNo1=(rollNo,)
        confpaw1=(confpaw,)
        mydb= mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="Shiyam@17",
                                      auth_plugin="mysql_native_password",
                                      database="application")

        mycursor=mydb.cursor()
        mycursor.execute("SELECT Student_RollNo FROM Students_details")
        stud_login=mycursor.fetchall()
        mycursor.execute("SELECT Student_Password FROM Students_details WHERE Student_RollNo=%s",rollNo1)
        stud_pass=mycursor.fetchone()
        for row in stud_login:
            if row==rollNo1:
                if stud_pass==confpaw1:
                    print("\n>>>>>>>>>>>>LOGIN DONE<<<<<<<<<<<<<<")
                    while 1:
                        print("/////////////////////// HOME MENU ////////////////////////")
                        value=input("\n1.Fee\n2.Account Details\n3.LogOut\nEnter Your Choice:")
                        if value=="1":
                            s.fee()
                        elif value=="2":
                            s.account()
                        elif value=="3":
                            print("\n>>>>>>>>>>>>>>>>>>>> BACK TO MAIN MENU <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            flag=False
                            break
                        else:
                            print("\n.................INVALID OPTION....................")
                if flag==True:
                    print("Invalid Password")
                    flag=False
        if flag==True:
            print("\n.............STUDENT NOT REGISTERED..............")  
       

    #personal details  
    @staticmethod
    def account():
        print("////////////// ACCOUNT DETAILS  ///////////////////")
        while 1:
            value=int(input("\n1.View Details\n2.Change password\nEnter Your Choice:"))
            if value==1:
                s.viewdetails()
                break
            elif value==2:
                s.changepassword()
                break
            else:
                print("----------Invalid option-----------------")

    #fees
    @staticmethod
    def fee():
        print("///////////  COLLEGE FEES //////////////")
        global fee_year
        mydb= mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="Shiyam@17",
                                      auth_plugin="mysql_native_password",
                                      database="application")

        mycursor=mydb.cursor()
        mycursor.execute("SELECT Student_year FROM Students_Details WHERE Student_RollNo=%s",rollNo1)
        yearfee=mycursor.fetchone()
        for x in yearfee:
            x=str(x)
            with open("Login123.csv","r") as f:
                fee=csv.reader(f)
                for row in fee:
                    if x==row[0]:
                        print(row)
s=Students()
