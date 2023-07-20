import pandas as pd
import matplotlib.pyplot as pmt
import numpy as np
df=pd.DataFrame()
dt=pd.DataFrame()
ha=pd.DataFrame()
n=[]
a=[]
l=[]
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
y6=[]
y7=[]
name=[] 
age=[] 
add=[] 
are=[] 
pno=[] 
r=[] 
phone=[]  
area=[]  
adhar=[] 
credit=[]
p=1;
while(p==1):
    s1=0
    s2=0
    s3=0
    s4=0
    p=int(input("entet 1 to continue\t"))
    xt=int(input("1-sanitisation toilet scheme \n2- mensturation scheme \nenter choice\n"))
    if(xt==2):
        print("PM sanitary napkin scheme")
        ch=input("are you registered for the Mensturation hygiene\t")
        if(ch[0]=='n'):
            n.append(input("enter name ->\n"))
            a.append(int(input("enter age ->\n")))
            area.append(int(input("enter area code ->\n")))
            l.append((input("enter location ->\n")))
            phone.append((input("enter phone number ->\n")))
            adhar.append(input("enter adhar number ->\n"))
            print("yes(1) or no(0) section")
            y1.append(int(input("do you have access to menstural products within 10 kms of your location?\t")))
            y2.append(int(input("can you afford the products available?\t")))
            y3.append(int(input("are you socially encouraged to use period products?\t")))
            y4.append(int(input("have you been educated about such products?\t")))
            credit.append(50)
        elif(ch[0]=='y'):
            cho=int(input("1-add credit\n2-remove credit\nenter choice\t"))
            adh=input("enter adhar number ->")
            for i in range(0,len(adhar)):
                if(adhar[i]==adh):
                    if(cho==1):
                        ab=int(input("prize of product bought\t"))
                        abc=(10/100)*ab
                        credit[i]+=abc
                    elif cho==2:
                        ab=int(input("prize of product bought\t"))
                        abc=(10/100)*ab
                        credit[i]-=abc
                    print(n[i],"\n",adhar[i],"\n",credit[i])
            
        data={"Name":n,'Age':a,'Adhar':adhar,"Credit":credit}
        df=pd.DataFrame(data)
        print(df);
        dat={'Adhar':adhar,'Access':y1,'afford':y2,'encourage':y3,'educate':y4}
        dt=pd.DataFrame(dat)
        print(dt);
        x=np.arange(0,len(n),dtype="int")
        y=np.array(y1)
        pmt.plot(x,y,marker="*")
        pmt.title("graph for accessibility")
        pmt.xlabel("number of participants")
        pmt.ylabel("access")
        pmt.show()
        x=np.arange(0,len(n),dtype="int")
        y=np.array(y2)
        pmt.plot(x,y,marker="o",linestyle="dotted")
        pmt.title("graph for affordability")
        pmt.xlabel("number of participants")
        pmt.ylabel("affordability")
        pmt.show()
        x=np.arange(0,len(n),dtype="int")
        y=np.array(y3)
        pmt.plot(x,y,marker="*",linestyle="dotted")
        pmt.title("graph for ecouragement")
        pmt.xlabel("number of participants")
        pmt.ylabel("encoragement")
        pmt.show()
        x=np.arange(0,len(n),dtype="int")
        y=np.array(y4)
        pmt.plot(x,y,marker="o",linestyle="dotted")
        pmt.title("graph for education")
        pmt.xlabel("number of participants")
        pmt.ylabel("education")
        pmt.show()
        for i in range(len(n)):
            s1=s1+y1[i]
            s2+=y2[i]
            s3+=y3[i]
            s4+=y4[i]
        print(((s1/len(n))*100) ,"% of the recorded cases get access to period products within 10 kms of their house")
        print(((s2/len(n))*100) ,"% of the recorded cases can afford period products")
        print(((s3/len(n))*100) ,"% of the recorded cases are encouraged to use such products")
        print(((s4/len(n))*100) ,"% of the recorded cases are educated about such products")
    if (xt==1):
       print("The objectives of Swachh Bharat include eliminating open defecation through the construction of household-owned and community-owned toilets and establishing an accountable mechanism of monitoring toilet use.")
       print("********PM swasthy suraksha yojana**********")
       print("Do you have at least one Toilet at home?")
       ch=int(input("Enter number of toilets for yes and 0 for no or for addition of toilets:"))
       y6.append(int(input("enter number of year if youve has toilets for more than 10 years otherwise 0")))
       y7.append(int(input("enter number of members in the house")))
       if(ch>=1):
           y5.append(ch) 
           a=input("Do you have any issues with your Toilet? (yes/no)\n")
           if a=="yes":
               print("What are the issues which you are facing? \n 1.Plumbing Work \n 2.Maintanance \n 3.Require general sanitization?")
               toilet=int(input("Enter the value!:\t"))
               if toilet==1:
                   print("******Click on the website leading below for plumbing work******")
                   print("https://www.indianplumbing.org/")
               if toilet==2:
                   print("******Click on the below link for maintanance issues******")
                   print("https://www.moglix.com/plumbing/118000000")
               if toilet==3 :
                   print("******Click for home and toilet sanitation******")
                   print("https://www.cdc.gov/healthywater/global/sanitation/index.html")
               else:
                   print("*** Congratulations! Keep up with the hygeine! ***")
           else:
               print("Thanks for using our application!")
               break; 
       if(ch==0):
           aaaa=int(input("enter number of toilets"))
           y5.append(aaaa)
           xx=int(input("1-Get one by registering for the Pradhan Mantri Swasthya Suraksha Yojana!\n2-to get another"))
           if xx==1:
               name.append(input("Enter name:"))
               age.append(int(input("Enter age:")))
               add.append(input("Enter address:"))
               are.append(int(input("Enter area pincode:")))
               pno.append(int(input("Enter phone number:")))
               adhar.append(int(input("Enter adhaar card number:")))
               credit.append(50)
           if xx==2:
               opt=int(input("Enter choice:\n1-add credit\n2-remove credit\n"))
               for i in range(0,len(adhar)):
                   adh=input("Enter adhar")
                   if(adhar[i]==adh):
                       if(opt==1):
                           ab=int(input("Enter the cost of your product:\t"))
                           abc=(10/100)*ab
                           credit[i]+=abc
                       elif (opt==2):
                           ab=int(input("Enter the cost of your product:\t"))
                           abc=(10/100)*ab
                           credit[i]-=abc
                           print(name[i],"\n",adhar[i],"\n",credit[i])
       da={"Name":name,'Age':age,'Adhar':adhar,"Credit":credit}
       ha=pd.DataFrame(da)
       print(ha)
       x=np.arange(0,len(name),dtype="int")
       y=np.array(y5)
       pmt.plot(x,y,marker="o",linestyle="dotted")
       pmt.title("graph for number of restroom per house")
       pmt.xlabel("number of participants")
       pmt.ylabel("number of toilets")
       pmt.show()
       x=np.arange(0,len(name),dtype="int")
       y=np.array(y6)
       pmt.plot(x,y,marker="*",linestyle="dashed",color='r')
       pmt.title("graph for years for which participants have had toilets")
       pmt.xlabel("number of participants")
       pmt.ylabel("number of years")
       pmt.show()
       x=np.array(y5)
       y=np.array(y7)
       pmt.plot(x,y,marker="o",color='r')
       pmt.title("graph for no of toilets and participants")
       pmt.xlabel("number of toilets")
       pmt.ylabel("number of people in house")
       pmt.show()

        