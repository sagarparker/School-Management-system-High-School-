print("\t\t\tWelcome to School Management System.(INS High School)")

while True:
    inp=(input("\nEnter the password:-\n*********************\n"))
    if inp!="admin":
        print("\n**The password is incorrect.**")
        
    if inp=="admin":
        print("\nThe password is correct.")
        break


while True:
    no=(input("\nEnter your ID no:-\n*******************\n"))
    
    if no.isnumeric() and (int(no)>0) and (int(no)<21):
        print("\nID no = ",no)
        break
    
    else:
        print("\n**Enter a valid ID no**")

        

listt=['','Mr.Sagar P.','Mr.Karan P.','Mr.Ajay P.','Mr.Smeet N.',
       'Ms.Aarti P.','Mr.Satish D.','Ms.Mamta H.','Mr.Dhruv G.',
       'Mr.Lalit M.','Mr.Akash S.','Mr.Varun D.','Mr.Sandeep N.',
       'Mr.Sahil S.','Mr.Vinay W.','Ms.Amruta P.','Ms.Sonika W.',
       'Mr.Saish P.','Mr.Omkar M.','Ms.Sanika K.','Ms.Shreya G.'];

print("\n\t\t\tWelcome",listt[int(no)])

print("\nSelect an option:-\n******************")
print("\n1. Enter 1 to see which classes you are teaching this week.")
print("\n2. Enter 2 to see Students information.")
print("\n3. Enter 3 to see your salary information.")
print("\n4. Enter 4 to add students or staff.")
print("\n5. Enter 5 to remove staff member.")
print("\n6. Enter 6 to remove students.")
print("\n7. Enter 7 to exit. ")


while True:
    A=['','\nRN-1,Aarav P-Fees paid.','\nRN-2,Vivan K-Fees not paid.','\nRN-3,Aditya S-Fees not paid.','\nRN-4,Amruta P-Fees paid.',
       '\nRN-5.Rahul N-Fees paid.','\nRN-6,Nikita P-Fees paid.','\nRN-7,Shaurya A-Fees not paid.','\nRN-8,Krish S-Fees paid.',
       '\nRN-9,Anik H-Fees not paid.','\nRN-10,Ajay P-Fees paid.','\nRN-11,Komal L-Fees Paid.','\nRN-12,Somya P-Fees paid.',
       '\nRN-13,Rohan P-Fees not paid.','\nRN-14,Sanjana I-Fees paid.','\nRN-15,Saloni N-Fees not paid.'];

    B=['','\nRN-1,Ananya K-Fees paid.','\nRN-2,Sagar P-Fees not paid.','\nRN-3,Kedar P-Fees paid.','\nRN-4,Swanand T-Fees not paid.',
       '\nRN-5,Aarti P-Fees paid.','\nRN-6,Diya K-Fees not paid.','\nRN-7,Riya K-Fees not paid.','\nRN-8,Karan P-Fees paid.','\nRN-9,Sarvesh B-Fees paid.',
       '\nRN-10,Shreya G-Fees paid.','\nRN-11,Gayatri S-Fees paid.','\nRN-12,Swaransh D-Fees not paid.','\nRN-13,Ketan D-Fees paid.',
       '\nRN-14,Sanal N-Fees paid.','\nRN-15,Saish M-Fees paid.','\nRN-16,Ayush p-Fees paid.'];

    C=['','\nRN-1,Krishna B-Fees paid.','\nRN-2,Shashank P-Fees not paid.','\nRN-3,Kaushik M-Fees paid.','\nRN-4,Trisha K-Fees paid.',
       '\nRN-5,Tanvi P-Fees not paid.','\nRN-6,Ishita K-Fees paid.','\nRN-7,Zoya F-Fees not paid.','\nRN-8,Vaishnavi R-Fees paid.',
       '\nRN-9,Reyansh P-Fees paid.','\nRN-10,Ishaan P-Fees paid.','\nRN-11,Rudra D-Fees paid.','\nRN-12,Chetan K-Fees paid.',
       '\nRN-13,Manish D-Fees not paid.','\nRN-14,Krutika P-Fees paid.','\nRN-15,Rohit K-Fees Paid.'];

    
    
    print("***************************************************************")

    nu=(input("\nOption:-"))

    if nu.isnumeric() and (int(nu)==1):

        we=(input("\nEnter the week no:-"))
        su=(input("\nEnter the subject you teach(Sci,Maths,Eng,Hin,His,Geo):-"))

    
        if su=="Sci" or "Maths" or "Eng" or "Hin" or "His" or "Geo":

            if we=="1":
                print("\nTime Table:-\n***********\nMonday    - Class 8\nTuesday   - Class 10\nWednesday - Class 9\nThursday  - Class 10\nFriday    - Class 8")
            
            if we=="2":
                print("\nTime Table:-\n***********\nMonday    - Class 9\nTuesday   - Class 8\nWednesday - Class 10\nThursday  - Class 9\nFriday    - Class 8")

            if we=="3":
                print("\nTime Table:-\n***********\nMonday    - Class 10\nTuesday   - Class 9\nWednesday - Class 8\nThursday  - Class 8\nFriday    - Class 10")

            if we=="4":
                print("\nTime Table:-\n***********\nMonday    - Class 10\nTuesday   - Class 9\nWednesday - Class 10\nThursday  - Class 8\nFriday    - Class 9")

            if we>("4") or we<("1"):
                print("\nEnter a valid option!!")

        
            

    if nu.isnumeric() and (int(nu)==2):

        std=(input("\nEnter the Class:-"))
        print("STD:-",std)
        rn=(input("\nEnter the roll no:-"))

        if std.isnumeric() and (int(std)==8) :
            if rn<("16") and rn>("1"):
                print(A[int(rn)])
            else:
                print("\nEnter a valid information!!!")
            
            
        if std.isnumeric() and (int(std)==9) :
            if rn<("17") and rn>("1"):
                print(B[int(rn)])
            else:
                print("\nEnter a valid information!!!")
            
        if std.isnumeric() and (int(std)==10):
            if rn<("16") and rn>("1"):
                print(C[int(rn)])
            else:
                print("\nEnter a valid information!!!")
            
        if int(std)<8 or int(std)>10:
            print("\nEnter a valid class")

    if nu.isnumeric()and (int(nu)==3):
        

        mon=(input("\nEnter the month:-"))
        yr=(input("\nEnter the year:-"))

        if mon.isnumeric() and yr.isnumeric() :
            if int(mon)==1:
                print("\nSalary will be issued on 31 /1/",yr)
                print("\nSalary last issued on 31/12/",yr)
            elif int(mon)>1 and int(mon)<13:
                print("\nSalary will be issued on 31 /",mon,"/",yr)
                print("\nSalary last issued on 31/",int(mon)-1,"/",yr)
            else:
                print("\nEnter a valid option!!!")
        

    if nu.isnumeric() and (int(nu)==4):

        y=(input("\nTo add students to class press S or press T to add Staff member:-"))
        if y=="T":
            le=(input("\nEnter the name of the Staff member:-"))
            listt.append(le);
            print("\n\nNew staff list:-")
            for sk in listt:
                print("\n",sk)
            
        if y=="S":
            s=(input("\nSelect the class:-"))
            na=(input("\nEnter the Roll no,name and fee status of the student:-"))
            if s=="8":
                A.append(na);
                for dk in A:
                    print('\n\n',dk)
                    
                
                
            if s=="9":
                B.append(na);
                for sk in B:
                    print('\n\n',sk)
                    
                
                
            if s=="10":
                C.append(na);
                for gk in C:
                    print('\n\n',gk)
        else:
            print("\nEnter a valid option.")

    if nu.isnumeric() and (int(nu)==5):
        nf=(input("\nEnter the Staff ID.no you want to remove:-"))
        if int(nf)>20 or int(nf)<1:
            print("\nEnter a valid ID no.")

        else:
            print("\nStaff removed:-",listt[int(nf)])
            print("\n\nNew Staff list:-\n")
            del listt[int(nf)];
            for gk in listt:
                print(gk)

    if nu.isnumeric() and (int(nu)==6):
        fg=(input("\nEnter A to remove all the student or R to remove one student:-"))
        if fg=='A' :
            hg=(input("\nEnter the class no to remove all students for new academic year:-"))
            if hg=="8":
                del A[:];
                print("\nAll the students from class 8 are removed.")
            
                    
            if hg=="9":
                del B[:];
                print("\nAll the students from class 9 are removed.")
                    
                
            if hg=="10":
                del C[:];
                print("\nAll the students from class 10 are removed.")

            elif int(hg)<8 or int(hg)>10:
                print("\nEnter a vaid option.")

        if fg=='R' :
            io=(input("\nSelect the class:-"))
            g=(input("\nEnter the Roll no:-"))
            if io=="8":
                print("\n\nNew students list:-")
                del A[int(g)];
                for dk in A:
                    print('\n',dk)
                    
                
                
            if io=="9":
                print("\n\nNew students list:-")
                del B[int(g)];
                for sk in B:
                    print('\n',sk)
                    
                
                
            if io=="10":
                print("\n\nNew students list:-")
                del C[int(g)];
                for gk in C:
                    print('\n',gk)

            if int(io)<8 or int(io)>10:
                print("\nEnter a vaid option.")

            
            
            

        
                    
    if nu.isnumeric() and (int(nu)==7):
        print("\nThank you!!!")
        break


    if nu.isnumeric() and (int(nu)>7):
        print("\n**Select a valid option!**")
        
