#CODE FOR CUSTOMER PROGRAM

import mysql.connector

print("\n""**********************************************************************")
print("*                             SA RESORTS                             *")
print("*                                                                    *")
print("*                            ⓦⓔⓛⓒⓞⓜⓔ                           *")
print("*                                                                    *")
print("*                     FEEL HOME WITH SA RESORTS                      *")
print("**********************************************************************""\n")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="sardb",
    buffered=True)

mycursor=mydb.cursor()

#CREATE TABLES
mycursor.execute("create table if not exists ncustomer( name varchar(20), emailid varchar(40), contact_number varchar(10), password varchar(20))")
mycursor.execute("create table if not exists ecustomer(emailid varchar(40), check_in_date datetime, check_out_date datetime, persons int, rooms int, room_size varchar(20), booking_amnt decimal(10,0))")
mycursor.execute("create table if not exists bill(emailid varchar(40), contact_number varchar(10), services varchar(12), booking_amnt decimal(10,0), total_bill decimal(10,0))")

def space(V):
    global sp
    sp=""
    l=15-len(str(V))
    for i in range(l):
        sp=sp+" "
    return sp

def spaces(V):
    global sp
    sp=""
    l=20-len(str(V))
    for i in range(l):
        sp=sp+" "
    return sp


#NEW CUSTOMER SIGNUP

def signup():
    
    n=input("Enter name:   ")
    e=input("Enter email id:   ")
    m=input("Enter mobile number:   ")
    while len(m)!=10:
        print("Enter 10 digit mobile number")
        m=input("Enter mobile number:   ")
    return n,e,m


#EXISTING CUSTOMER BOOKING DETAILS

def details():
    
    print("*NOTE*""\n""You are humbly requested to enter your details carefully and correctly as you won't be able to make changes later. Thank you""\n")
    di=input("Check in date (yyyy/mm/dd):   ")
    do=input("Check out date (yyyy/mm/dd):   ")
    np=int(input("Number of people:   "))
    nr=int(input("Number of rooms required:   "))
    price=0
    wb=''

    print("\n""*****************************************************************************")
    print("*     ROOM PRICES                                                           *""\n"
          "*     (per night stay)(inclusive of maintenance charges)                    *""\n"
          "*        Regular(2 persons): Rs 1,800/-                                     *""\n"
          "*        Delux(4 persons)  : Rs 2,500/-                                     *""\n"
          "*        Supreme(6 persons): Rs 3,000/-                                     *")
    print("*****************************************************************************""\n")
            
    for i in range(0,nr):
        rs=input("Select room size (r/d/s):   ").lower()
        wb=wb+' '+rs
        if rs=='r':
            price=price+1800
        if rs=='d':
            price=price+2500
        if rs=='s':
            price=price+3000
                
    bp=price+price*0.1
    print("Booking Price (inclusive of all taxes):   ",bp,"INR")

    return ee,di,do,np,nr,wb,bp


def avail():

    print("\n""*****************************************************************************")
    print("*     SERVICES TO AVAIL                                                     *")
    print("*       1> Laundry (Rs 5/- per garment)                                     *")
    print("*       2> Breakfast (Complementary)                                        *")
    print("*       3> Transport (Select from sight seeing packages)                    *")
    print("*       4> Gym and spa (Rs 100/- per hour)                                  *")
    print("*       5> Lounge (Rs 200/- per hour)(Complemetary snacks and Beverages)    *")
    print("*****************************************************************************""\n")
    
    ser=input("Enter service codes (1,2,3,4,5):   ")
    print("Respective charges for additional services will be applied later")

    return ee, ser

                
def bill_amnt():

    ee=input("Enter email id:   ")
    kth=(ee,)
    mycursor.execute("select emailid from ecustomer")
    vante=mycursor.fetchall()

    if kth in vante:

        mycursor.execute("SELECT * FROM bill WHERE emailid=%s",(ee,))
        myresult=mycursor.fetchall()
           
        print("----------------------------------------------------------------------------------------------")
        print("EMAIL ID", spaces("EMAIL ID"),"CONTACT NUMBER",space("CONTACT NUMBER"),"SERVICES",space("SERVICES"),"BOOKING AMOUNT",space("BOOKING AMOUNT"),"TOTAL BILL AMOUNT")
        print("----------------------------------------------------------------------------------------------")

        for x in myresult:
            print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4])
        print("----------------------------------------------------------------------------------------------")

    else:
        print("No records found. Try contacting the Reception.")


#user choice

user=input("Enter a: Admin/ c: Customer:   ")

if user=="c" or user=="C":
    print("\n""*NOTE*""\n""You are humbly requested to enter your inputs carefully. Thank you""\n")
    cont='y' and 'Y'

    #display choices
   
    while cont=='y' or cont=='Y':

        print("**********************************************************************")
        print("*       ENTER                                                        *")
        print("*       1> ABOUT US                                                  *")
        print("*       2> SALIENT FEATURES                                          *")
        print("*       3> CONTACT US                                                *")
        print("*       4> BOOK A ROOM                                               *")
        print("*       5> LOG IN / SIGN UP                                          *")
        print("*       6> CANCEL BOOKING                                            *")
        print("**********************************************************************""\n")

        print("**********************************************************************")
        print("*  > ENTER 'S' TO AVAIL FOR ADDITIONAL SERVICES.                     *")
        print("*  > ENTER 'B' TO VIEW TOTAL BILL AMOUNT .                           *")
        print("*  > ENTER 'R' TO WRITE A REVIEW.                                    *")
        print("**********************************************************************""\n")

        e=input("Enter your choice:   ")
        
        if e=='1':
            print("\n""********************************************************************** ")
            print("*   Soffrito Ala-Carte or SA Resorts are a collection of hotels      * ")
            print("*   that combine the social culture of a hotel with innovative       * ")
            print("*   design, award-winning dishes and beverages, and a                * ")
            print("*   community-driven atmosphere.                                     * ")
            print("*                                                                    * ")
            print("*   SA Resorts take their cues from the surrounding neighbourhood,   * ")
            print("*   developing an ambience that is a microcosm of the best each      * ")
            print("*   city has to offer.                                               * ")
            print("********************************************************************** ""\n")
            cont=input("Wish to continue? (y/n):   ").lower()
            
        elif e=='2':
            print("\n""**********************************************************************")
            print("*    SALIENT FEATURES                                                *")
            print("*       > Aesthetic interiors                                        *")
            print("*       > Great food                                                 *")
            print("*       > Indoor swimming pool                                       *")
            print("*       > Free Wifi                                                  *")
            print("*       > Social lounge                                              *")
            print("**********************************************************************""\n")
            cont=input("Wish to continue? (y/n):   ")

        elif e=='3': 
            print("\n""**********************************************************************")
            print("*       Mobile Number: 1> 9753186421                                 *")
            print("*                      2> 9753186420                                 *")
            print("*                                                                    *")
            print("*       Email ID: sa@gmail.com                                       *")
            print("**********************************************************************""\n")
            cont=input("Wish to continue? (y/n):   ")

        elif e=='4':
            ee=input("Enter email id:   ")
            kth=(ee,)
            mycursor.execute("select emailid from ncustomer")
            vante=mycursor.fetchall()

            if kth in vante:
                z=details()

                #sql code existing customer
        
                entriesb="insert into ecustomer(emailid, check_in_date, check_out_date, persons, rooms, room_size, booking_amnt) values ('{}','{}','{}','{}','{}','{}','{}')".format(z[0],z[1],z[2],z[3],z[4],z[5],z[6])
                mycursor.execute(entriesb)
                mydb.commit()

                N=20
                rrr= mycursor.execute("select rooms from ecustomer group by rooms")
                avr= mycursor.fetchall()
                ccc= mycursor.execute("select count(rooms) from ecustomer group by rooms")
                avr2= mycursor.fetchall()

                countr=0
                v1=0

                for ii in avr:
                    nofr=avr2[v1][0]*ii[0]
                    v1=v1+1
                    countr= countr+nofr

                N=N-countr
                if (N>=0):
                    print("\n""Checking for rooms...")
                    print("Rooms are available")
    
                    p=input("Enter password to confirm booking:   ")
                    mycursor.execute("select password from ncustomer where emailid=%s",(z[0],))
                    pcheck=mycursor.fetchall()

                    for v in pcheck:
                        if (v[0]==p):
                            print("Booking confirmed. Thanks for choosing SA Resorts.")
                            lor=[]
                            for i in range(countr-z[4]+1,countr+1):
                                lor.append(i)
                                
                            if len(lor)==1:
                                print("Your room number is:",lor)
                            else:
                                print("Your room numbers are:",lor)
                        else:
                            print("Password is incorrect. Enter details again to book.")
                            deleter="delete from ecustomer where emailid=%s"
                            mycursor.execute(deleter,(z[0],))
                            mydb.commit()
                            
                else:
                    print("\n""Checking for rooms...")
                    print("Sorry required number of rooms is not available.")
                    deleter="delete from ecustomer where emailid=%s"
                    mycursor.execute(deleter,(z[0],))
                    mydb.commit()
                
            else:
                print("\n""Login first to book a room")
                t=signup()
                
                #sql code new customer
                
                def sqlncust():
                    entries="insert into ncustomer(name, emailid, contact_number, password) values ('{}','{}','{}','{}')".format(t[0],t[1],t[2],pswd)
                    mycursor.execute(entries)
                    mydb.commit()
                    mycursor.execute("select * from ncustomer")
                
                a=input("Enter ok to continue/ In case if there's an error, press anything to go back:   ").lower()
                if a=='ok':
                    pswd=input("Set a password:   ")
                    aa=input("Enter submit to register/ To re-enter password, press anything:   ").lower()
                
                    if aa=='submit':
                        print("You have been successfully registered")
                        sqlncust()
                        
                    else:
                        zz=input("Do you want to exit? (y/n):   ")
                        while zz=='n' or zz=='N':
                            pswd=input("Set a password:   ")
                            aa=input("Enter submit to register/ To re-enter password, press anything:   ").lower()
                            if aa=='submit':
                                print("You have been successfully registered")
                                sqlncust()
                                break
                            else:
                                zz=input("Do you want to exit? (y/n):   ")
                                
                        if zz=='y' or zz=='Y':
                            print("Login cancelled")
                            
                else:
                    yz=input("Do you want to exit? (y/n):   ")
                    if yz=='y' or yz=='Y':
                        print("Login cancelled")
                    
                    while yz=='n' or yz=='N':
                        t=signup()
                        a=input("Enter ok to continue/ In case if there's an error, press anything to go back:   ").lower()
                        if a=='ok':
                            pswd=input("Set a password:   ")
                            aa=input("Enter submit to register/ To re-enter password, press anything:   ").lower()
                        
                            if aa=='submit':
                                print("You have been successfully registered")
                                sqlncust()
                                break
                            else:
                                zz=input("Do you want to exit? (y/n):   ")
                                while zz=='n' or zz=='N':
                                    pswd=input("Set a password:   ")
                                    aa=input("Enter submit to register/ To re-enter password, press anything:   ").lower()
                                    if aa=='submit':
                                        print("You have been successfully registered")
                                        sqlncust()
                                        break
                                    else:
                                        zz=input("Do you want to exit? (y/n):   ")
                                break
                                if zz=='y' or zz=='Y':
                                    print("Login cancelled")
                        else:
                            yz=input("Do you want to exit? (y/n):   ")

            cont=input("\n""Wish to continue? (y/n):   ")

        elif e=='5':
            t=signup()

            #sql code new customer
                
            def sqlncust():
                entries="insert into ncustomer(name, emailid, contact_number, password) values ('{}','{}','{}','{}')".format(t[0],t[1],t[2],pswd)
                mycursor.execute(entries)
                mydb.commit()
                mycursor.execute("select * from ncustomer") 
            
            a=input("Enter ok to continue/ In case if there's an error, press anything to go back:   ").lower()
            if a=='ok':
                pswd=input("Set a password ")
                aa=input("Enter submit to register/ To re-enter password, press anything:   ").lower()
                
                if aa=='submit':
                    print("You have been successfully registered")
                    sqlncust()
                    
                else:
                    zz=input("Do you want to exit? (y/n):   ")
                    while zz=='n' or zz=='N':
                        pswd=input("Set a password:   ")
                        aa=input("Enter submit to register/ To re-enter password, press anything:   ").lower()
                        if aa=='submit':
                            print("You have been successfully registered")
                            sqlncust()
                            break
                        else:
                            zz=input("Do you want to exit? (y/n):   ")
                    if zz=='y' or zz=='Y':
                        print("Login cancelled")
                              
            else:
                yz=input("Do you want to exit? (y/n):   ")
                if yz=='y' or yz=='Y':
                    print("Login cancelled")
                    
                while yz=='n' or yz=='N':
                    t=signup()
                    a=input("Enter ok to continue/ In case if there's an error, press anything to go back:   ").lower()
                    if a=='ok':
                        pswd=input("Set a password:   ")
                        aa=input("Enter submit to register/ To re-enter password, press anything:   ").lower()
                        
                        if aa=='submit':
                            print("You have been successfully registered")
                            sqlncust()
                            break
                        else:
                            zz=input("Do you want to exit? (y/n):   ")
                            while zz=='n' or zz=='N':
                                pswd=input("Set a password:   ")
                                aa=input("Enter submit to register/ To re-enter password, press anything:   ").lower()
                                if aa=='submit':
                                    print("You have been successfully registered")
                                    sqlncust()
                                    break
                                else:
                                    zz=input("Do you want to exit? (y/n):   ")
                            break
                            if zz=='y' or zz=='Y':
                                print("Login cancelled")
                    else:
                        yz=input("Do you want to exit? (y/n):   ")

            cont=input("\n""Wish to continue? (y/n):   ")

        elif e=='6':
            emc=input("Enter email id:   ")
            print("\n""*NOTE*""\n""Only 80% of the total deposited amount will be refunded.")
            confc=input("Do you want to confirm cancellation of your booking (y/n):   ")
            
            if confc=='y':
                mycursor.execute("select booking_amnt from ecustomer where emailid=%s",(emc,))
                canc=mycursor.fetchall()
                for a in canc:
                    refamnt=a[0]*80/100
                delcan="delete from ecustomer where emailid=%s"
                mycursor.execute(delcan,(emc,))
                mydb.commit()
                print("Booking cancelled. Rs ",refamnt," refunded")
                
            else:
                print("Cancellation withdrawn. No changes made to the booking.")
            cont=input("\n""Wish to continue? (y/n):   ")

        elif e=='S' or e=='s':

            ee=input("Enter email id:   ")
            kth=(ee,)
            mycursor.execute("SELECT emailid FROM ecustomer")
            vante=mycursor.fetchall()

            if kth in vante:
                z=avail()

                mycursor.execute("SELECT contact_number FROM ncustomer WHERE emailid=%s",(ee,))
                cn=mycursor.fetchall()
                
                mycursor.execute("SELECT booking_amnt FROM ecustomer WHERE emailid=%s",(ee,))
                ba=mycursor.fetchall()

                entriesc="insert into bill(emailid, contact_number, services, booking_amnt, total_bill) values ('{}','{}','{}','{}','{}')".format(z[0],cn[0][0],z[1],ba[0][0],ba[0][0])
                mycursor.execute(entriesc)
                mydb.commit()

            else:
                print("No records found. Try contacting the Reception.")
            cont=input("\n""Wish to continue? (y/n):   ")

        elif e=='b' or e=='B':

            bill_amnt()
            cont=input("\n""Wish to continue? (y/n):   ")

        elif e=='r' or e=='R':

            n=input("Enter name:   ")
            r=input("Drop your views (in 200 characters):   ")

            mycursor.execute("create table if not exists review(cname varchar(20), rev varchar(200))")
            mycursor.execute("insert into review(cname, rev) values ('{}','{}')".format(n,r))
            cont=input("\n""Wish to continue? (y/n):   ")
            

    print("Thanks for visiting. Have a nice day :)")
    

#END OF CUSTOMER PROGRAMME

#CODE FOR ADMIN PROGRAM


elif user=="a" or user=="A":
    info = ['admin@sa','sa0000']
   
    req = [input('Username: '),input('Password: ')]
    if req == info:
        mydb=None
        mycursor=None
        flag=0
        sp=""

        def check_connection():
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234")
            if mydb.is_connected():
                print("Successfully connected to MySQL Database")
                flag=1
            return flag


        def create_database():
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234")

            mycursor=mydb.cursor()

            mycursor.execute("CREATE DATABASE IF NOT EXISTS sardb")
           
            print("Database created or used")

        def create_table():
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")
           
            mycursor=mydb.cursor()

            mycursor.execute("CREATE TABLE IF NOT EXISTS employee(Empno int(5),Name varchar(20),Salary int(7),Address varchar(20),Joining date,Work varchar(20))")
            mycursor.execute("CREATE TABLE IF NOT EXISTS food(Name varchar(20),Qty int(7),Rate int(20),Amount int(20))")
            mycursor.execute("CREATE TABLE IF NOT EXISTS furniture(Name varchar(20),Qty int(7),Rate int(20),Amount int(20))")
           
            print("Tables under sardb: ")

            mycursor.execute("SHOW TABLES")

            for x in mycursor:
              print(x)

        def space(V):
            global sp
            sp=""
            l=15-len(str(V))
            for i in range(l):
                sp=sp+" "
            return sp

        def space2(V):
            global sp
            sp=""
            l=25-len(str(V))
            for i in range(l):
                sp=sp+" "
            return sp
        
        def space3(V):
            global sp
            sp=""
            l=20-len(str(V))
            for i in range(l):
                sp=sp+" "
            return sp

        #EMPLOYEE
            
        def emp_add_new_record():
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")

            mycursor=mydb.cursor()
            Empno=int(input("Enter Employee's Number ID:   "))        
            Name=input("Enter Employee's Name:   ")
            Salary=int(input("Enter Employee's Salary:   "))
            Address=input("Enter Employee's Address:   ")
            Joining=input("Enter Employee's Joining date (yyyy/mm/dd):   ")
            Work=input("Enter Employee's work:   ")

            sql="INSERT INTO employee(Empno,Name,Salary,Address,Joining,Work) VALUES({},'{}','{}','{}','{}','{}')".format(Empno,Name,Salary,Address,Joining,Work)           
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")

        def emp_display_all_record():
               
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")

            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM employee")

            myresult=mycursor.fetchall()
            print("----------------------------------------------------------------------------------------------------------------")
            print("Emp ID",space("Emp ID"),"EMPLOYEE NAME", space("EMPLOYEE NAME"),"SALARY",space("SALARY"),"ADDRESS",space("ADDRESS"),"JOINING DATE",space("JOINING DATE"),"WORK")
            print("----------------------------------------------------------------------------------------------------------------")

            for x in myresult:
                print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(x[4]),x[5])
            print("----------------------------------------------------------------------------------------------------------------\n")
               
        def emp_search_record():
               
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")

            mycursor=mydb.cursor()
            NAME=input("Enter name to search:   ")

            sql_select_query="select * from employee where Name=%s"

            mycursor.execute(sql_select_query, (NAME, ))
            myresult=mycursor.fetchall()

            if (mycursor.rowcount>0):
                   
                print("------------------------------------------------------------------------------------------------------------")
                print("Emp ID",space("Emp ID"),"EMPLOYEE NAME", space("EMPLOYEE NAME"),"SALARY",space("SALARY"),"ADDRESS",space("ADDRESS"),"JOINING DATE",space("JOINING DATE"),"WORK")
                print("------------------------------------------------------------------------------------------------------------")

                for x in myresult:
                    print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(x[4]),x[5])
                print("------------------------------------------------------------------------------------------------------------\n")

            else:
                print("No data to display")
               
        def emp_delete_record():

            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")

            mycursor=mydb.cursor()       
            NAME=input("Enter name to delete")
            sql_select_query="DELETE FROM employee WHERE name=%s"
            mycursor.execute(sql_select_query, (NAME, ))
            mydb.commit()

            print(mycursor.rowcount, "record(s) deleted")
            mycursor.execute("SELECT * FROM employee")
            myresult=mycursor.fetchall()
               
            print("----------------------------------------------------------------------------------------------------------------")
            print("Emp ID",space("Emp ID"),"EMPLOYEE NAME", space2("EMPLOYEE NAME"),"SALARY",space("SALARY"),"ADDRESS",space("ADDRESS"),"JOINING DATE",space("JOINING DATE"),"WORK")
            print("----------------------------------------------------------------------------------------------------------------")

            for x in myresult:
                print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(x[4]),x[5])
            print("----------------------------------------------------------------------------------------------------------------\n")

        def emp_update_record():
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")

            mycursor=mydb.cursor()

            print("\n**********************************************************************")
            print("*\t\tEMPLOYEE UPDATION                                    *")
            print("*\t\t1>  NAME                                             *")
            print("*\t\t2>  SALARY                                           *")
            print("*\t\t3>  ADDRESS                                          *")
            print("*\t\t4>  WORK                                             *")
            print("*\t\t5>  Return                                           *")
            print("**********************************************************************\n")
                 
            ch=int(input("Enter your choice:   "))

            if ch==1:
                NAME=input("Enter name to update:   ")
                NewName=input("Enter new Name of employee:   ")

                sql_select_query="UPDATE employee set name =%s WHERE name=%s"
                input1=(NewName,NAME)
                mycursor.execute(sql_select_query,input1)

                mydb.commit()

            elif ch==2:
                NAME=input("Enter name to update:   ")
                x=int(input("Enter by how many % you want to increase salary:   "))
                mycursor.execute("select Salary from employee where name=%s",(NAME, ))
                y=mycursor.fetchall()
                z=y[0][0]
                print(z)
                   
                sql_select_query="UPDATE employee set Salary=%s WHERE name=%s"
                input1=((z+(z*x)/100),NAME)
                mycursor.execute(sql_select_query,input1)

                mydb.commit()
                   
            elif ch==3:
                NAME=input("Enter name to update:   ")
                NewAddress=input("Enter new Address of employee:   ")
               
                sql_select_query="UPDATE employee set Address =%s WHERE name=%s"
                input1=(NewAddress,NAME)
                mycursor.execute(sql_select_query,input1)

                mydb.commit()

            elif ch==4:
                NAME=input("Enter name to update:   ")
                NewWork=input("Enter new place of Work of employee:   ")
                   
                sql_select_query="UPDATE employee set Work =%s WHERE name=%s"
                input1=(NewWork,NAME)
                mycursor.execute(sql_select_query,input1)

                mydb.commit()

            else:
                print("Wrong Choice, Please enter values between 1-4")
                   
            print(mycursor.rowcount, "record(s) updated")

            mycursor.execute("SELECT * FROM employee")
            myresult=mycursor.fetchall()                    
               
            print("-----------------------------------------------------------------------------------------------------------------")
            print("Emp ID",space("Emp ID"),"EMPLOYEE NAME", space2("EMPLOYEE NAME"),"SALARY",space("SALARY"),"ADDRESS",space("ADDRESS"),"JOINING DATE",space("JOINING DATE"),"WORK")
            print("-----------------------------------------------------------------------------------------------------------------")

            for x in myresult:
                print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(x[4]),x[5])
            print("-----------------------------------------------------------------------------------------------------------------\n")

            
        #FOOD
            
        def food_add_new_record():
            
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")
            mycursor=mydb.cursor()

            Name=input("Enter Name:   ")
            Qty=int(input("Enter qty:   "))
            Rate=int(input("Enter Rate:   "))
            Amount=Qty*Rate
                         
            sql="INSERT INTO food(Name,Qty,Rate,Amount) VALUES('{}',{},{},{})".format(Name,Qty,Rate,Amount)
           
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
           
        def food_display_all_record():
           
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")

            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM food")

            myresult=mycursor.fetchall()
            print("-----------------------------------------------------------------------")
            print("FOOD NAME", space("FOOD NAME"),"QUANTITY",space("QUANTITY"),"RATE",space("RATE"),"AMOUNT")
            print("-----------------------------------------------------------------------")

            for x in myresult:
                print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3])
            print("-----------------------------------------------------------------------\n")
           
        def food_search_record():
           
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")

            mycursor=mydb.cursor()
            NAME=input("Enter name to search:   ")
            sql_select_query="select * from food where Name=%s"
            mycursor.execute(sql_select_query, (NAME, ))
            myresult=mycursor.fetchall()

            if (mycursor.rowcount>0):
                print("-----------------------------------------------------------------------")
                print("FOOD NAME", space("FOOD NAME"),"QUANTITY",space("QUANTITY"),"RATE",space("RATE"),"AMOUNT")
                print("-----------------------------------------------------------------------")

                for x in myresult:
                    print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3])
                print("-----------------------------------------------------------------------\n")
           
            else:
                print("No data to display")
           
        def food_delete_record():

            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")

            mycursor=mydb.cursor()
            NAME=input("Enter name to delete:   ")
            sql_select_query="DELETE FROM food WHERE NAME=%s"
            mycursor.execute(sql_select_query, (NAME, ))
            mydb.commit()

            print(mycursor.rowcount, "record(s) deleted")
            mycursor.execute("SELECT * FROM food")
            myresult=mycursor.fetchall()
           
            print("-----------------------------------------------------------------------")
            print("FOOD NAME", space("FOOD NAME"),"QUANTITY",space("QUANTITY"),"RATE",space("RATE"),"AMOUNT")
            print("-----------------------------------------------------------------------")

            for x in myresult:
                print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3])
            print("-----------------------------------------------------------------------\n")


        #FURNITURE
            
        def furniture_add_new_record():
            
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")
            
            mycursor=mydb.cursor()

            Name=input("Enter Name:   ")
            Qty=int(input("Enter qty:   "))
            Rate=int(input("Enter Rate:   "))
            Amount=Qty*Rate

            sql="INSERT INTO furniture(Name,Qty,Rate,Amount) VALUES('{}',{},{},{})".format(Name,Qty,Rate,Amount)
           
            mycursor.execute(sql)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
           
        def furniture_display_all_record():
           
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")

            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM furniture")
            myresult=mycursor.fetchall()
            print("----------------------------------------------------------------------------")
            print("FURNITURE NAME", space("FURNITURE NAME"),"QUANTITY",space("QUANTITY"),"RATE",space("RATE"),"AMOUNT")
            print("----------------------------------------------------------------------------")

            for x in myresult:
                print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3])
            print("----------------------------------------------------------------------------\n")
           
        def furniture_search_record():
           
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")

            mycursor=mydb.cursor()
            NAME=input("Enter name to search:   ")
            sql_select_query="select * from furniture where Name=%s"
            mycursor.execute(sql_select_query, (NAME, ))
            myresult=mycursor.fetchall()

            if (mycursor.rowcount>0):
                print("----------------------------------------------------------------------------")
                print("FURNITURE NAME", space("FURNITURE NAME"),"QUANTITY",space("QUANTITY"),"RATE",space("RATE"),"AMOUNT")
                print("----------------------------------------------------------------------------")

                for x in myresult:
                    print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3])
                print("----------------------------------------------------------------------------\n")

            else:
                print("No data to display")
           
        def furniture_delete_record():

            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="hotel_admin")

            mycursor=mydb.cursor()
            NAME=input("Enter name to delete:   ")
            sql_select_query="DELETE FROM furniture WHERE Name=%s"
            mycursor.execute(sql_select_query, (NAME, ))
            mydb.commit()

            print(mycursor.rowcount, "record(s) deleted")
            mycursor.execute("SELECT * FROM furniture")
            myresult=mycursor.fetchall()
           
            print("----------------------------------------------------------------------------")
            print("FURNITURE NAME", space("FURNITURE NAME"),"QUANTITY",space("QUANTITY"),"RATE",space("RATE"),"AMOUNT")
            print("----------------------------------------------------------------------------")

            for x in myresult:
              print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3])
            print("----------------------------------------------------------------------------\n")


        #CUSTOMER DETAILS
            
        def customer_display_ecustomer():
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="sardb")

            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM ecustomer")
            myresult=mycursor.fetchall()
            print("--------------------------------------------------------------------------------------------------------------------------------")
            print("EMAIL ID", space3("EMAIL ID"),"CHECK IN DATE",space3("CHECK IN DATE"),"CHECK OUT DATE",space3("CHECK OUT DATE"),"PEOPLE",space("PEOPLE"),"ROOMS",space("ROOMS"),"ROOM SIZES",space("ROOM SIZES"),"BOOKING PRICE")
            print("--------------------------------------------------------------------------------------------------------------------------------")

            for x in myresult:
                print(x[0],space3(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),x[6])
            print("--------------------------------------------------------------------------------------------------------------------------------\n")

        def customer_display_ncustomer():
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="sardb")

            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM ncustomer")
            myresult=mycursor.fetchall()
            print("------------------------------------------------------------------------------------------------")
            print("CUSTOMER NAME", space2("CUSTOMER NAME"),"EMAIL ID",space2("EMAIL ID"),"CONTACT NUMBER",space2("CONTACT NUMBER"),"PASSWORD")
            print("------------------------------------------------------------------------------------------------")

            for x in myresult:
              print(x[0],space2(str(x[0])),x[1],space2(str(x[1])),x[2],space2(x[2]),x[3])
            print("------------------------------------------------------------------------------------------------\n")

        def customer_display_review():
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="1234",
                database="sardb")

            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM review")
            myresult=mycursor.fetchall()
            print("--------------------------------------------------------------------------------------------------")
            print("CUSTOMER NAME", space2("CUSTOMER NAME"),"REVIEW")
            print("--------------------------------------------------------------------------------------------------")

            for x in myresult:
              print(x[0],space2(str(x[0])),x[1])
            print("--------------------------------------------------------------------------------------------------\n")



        #MAIN
                 
        x=check_connection()
        if x==1:
            create_database()
            create_table()
        else:
            print("Kindly check connection")

        ans='y'
        while ans=='y' or ans=='Y':
            print("\n**********************************************************************")
            print("*\t\tADMIN CHOICES                                        *")
            print("*\t\t1>  EMPLOYEE MANAGEMENT                              *")
            print("*\t\t2>  SERVICES                                         *")
            print("*\t\t3>  CUSTOMER DETAILS                                 *")
            print("*\t\t4>  RETURN                                           *")
            print("**********************************************************************\n")
            choice=int(input("Enter your choice:   "))
            if choice==1:
                ans='y'
                while ans=='y' or ans=='Y':
                    print("\n**********************************************************************")
                    print("*\t\tEMPLOYEE MANAGEMENT                                  *")
                    print("*\t\t1>  Add                                              *")
                    print("*\t\t2>  Display                                          *")
                    print("*\t\t3>  Search                                           *")
                    print("*\t\t4>  Delete                                           *")
                    print("*\t\t5>  Update                                           *")
                    print("*\t\t6>  Return                                           *")
                    print("**********************************************************************\n")
                     
                    ch=int(input("Enter your choice:   "))

                    if ch==1:
                        emp_add_new_record()      
                    elif ch==2:
                        emp_display_all_record()
                    elif ch==3:
                        emp_search_record()
                    elif ch==4:
                        emp_delete_record()
                    elif ch==5:
                        emp_update_record()
                    else:
                        print("Please enter values between 1-5")

                    ans=input("Wish to continue in Employee? (y/n):   ")
                           
            elif choice==2:
                ans='y'
                while ans=='y' or ans=='Y':
                   
                    print("\n**********************************************************************")
                    print("*\t\tSERVICES                                             *")
                    print("*\t\t1>  FOOD                                             *")
                    print("*\t\t2>  FURNITURE                                        *")
                    print("*\t\t3>  Return                                           *")
                    print("**********************************************************************\n")
                     
                    ch=int(input("Enter your choice:   "))

                    if ch==1:
                        ans='y'
                        while ans=='y' or ans=='Y':
                           
                            print("\n**********************************************************************")
                            print("*\t\tFOOD                                                 *")
                            print("*\t\t1>  Add                                              *")
                            print("*\t\t2>  Display                                          *")
                            print("*\t\t3>  Search                                           *")
                            print("*\t\t4>  Delete                                           *")
                            print("*\t\t5>  Return                                           *")
                            print("**********************************************************************\n")
                             
                            ch=int(input("Enter your choice:   "))

                            if ch==1:
                                food_add_new_record()      
                            elif ch==2:
                                food_display_all_record()
                            elif ch==3:
                                food_search_record()
                            elif ch==4:
                                food_delete_record()
                           
                            else:
                                print("Please enter values between 1-4")

                            ans=input("Wish to continue in Food? (y/n):   ")

                    elif ch==2:
                        ans='y'
                        while ans=='y' or ans=='Y':
                            print("\n**********************************************************************")
                            print("*\t\tFURNITURE                                            *")
                            print("*\t\t1>  Add                                              *")
                            print("*\t\t2>  Display                                          *")
                            print("*\t\t3>  Search                                           *")
                            print("*\t\t4>  Delete                                           *")
                            print("*\t\t5>  Return                                           *")
                            print("**********************************************************************\n")
                             
                            ch=int(input("Enter your choice:   "))

                            if ch==1:
                                furniture_add_new_record()      
                            elif ch==2:
                                furniture_display_all_record()
                            elif ch==3:
                                furniture_search_record()
                            elif ch==4:
                                furniture_delete_record()
                           
                            else:
                                print("Please enter values between 1-4")

                            ans=input("Wish to continue in Furniture? (y/n):   ")
                           
                    else:
                        print("Please enter values between 1-2")
                            
                    ans=input("Wish to continue in Services? (y/n):   ")

            
            elif choice==3:
                ans='y'
                while ans=='y' or ans=='Y':
                   
                    print("\n**********************************************************************")
                    print("*\t\tCUSTOMER DETAILS                                     *")
                    print("*\t\t1>  Display Customer Details                         *")
                    print("*\t\t2>  Display Customer Booking Details                 *")
                    print("*\t\t3>  Display Customer Reviews                         *")
                    print("*\t\t4>  Return                                           *")
                    print("**********************************************************************\n")
                     
                    ch=int(input("Enter your choice:   "))
                    if ch==1:
                        customer_display_ncustomer()
                    elif ch==2:
                        customer_display_ecustomer()
                    elif ch==3:
                        customer_display_review()
                    else:
                        print("Please enter values between 1-3")
                           
                    ans=input("Wish to continue in customer details? (y/n):   ")

            else:
                 print("Please enter values between 1-3")
                   
            ans=input("Wish to go to main menu? (y/n):   ")


#END OF ADMIN PROGRAMME
