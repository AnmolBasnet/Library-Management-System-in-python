def bill_(SN,name2,author,amount,price):
    from datetime import datetime
    from datetime import timedelta
    expiry_date=(datetime.now()+timedelta(days=10)).strftime('%Y-%m-%d')
    import datetime #Imports datetime for today date
    Date_=datetime.date.today()   
    now=datetime.datetime.now()
    name=input("Full name: ")
    bill=open("bill.txt","w")
    bill.write("S.N: "+str(SN)+"\n")
    bill.write("Full Name: "+name+"\n")#wites the inserted name of the user
    bill.write("Name of the Book required: "+name2+"\n")
    bill.write("Author of the book: "+author+"\n")
    bill.write("quant borrowed: "+str(amount)+"\n")
    bill.write("Price: "+price+" per unit"+"\n")
    bill.write("Total Price: $"+str(amount*float(price.replace("$","")))+"\n")
    bill.write("Date: "+str(Date_)+"\n") 
    bill.write("Time: "+str(now.strftime("%H:%M:%S"))+"\n")
def return_(SN,name2,author,amount):
    import datetime
    Date_=datetime.date.today()
    now=datetime.datetime.now()
    Name__=input("Full name:")#Asks the respective user name while returnong the issued book
    success=False
    while success==False:
        try:
            days=int(input("Days borrowed: ")#Asks the user to enter the number of days of book issued
            success=True
        except:
            print("Invalid")#If the book is not avilable at the stock it prints invalid
    regularbill=open("returned book.txt","a")#opens book.txt file for bill generation
    regularbill.write("S.N: "+str(SN)+"\n")
    regularbill.write("Full Name: "+Name__+"\n")
    regularbill.write("Name of the Book required: "+name2+"\n")
    regularbill.write("Author of the book: "+author+"\n")
    regularbill.write("quant Returned: "+str(amount)+"\n")
    regularbill.write("Date: "+str(Date_)+"\n") 
    regularbill.write("Time: "+str(now.strftime("%H:%M:%S"))+"\n") 
    if days>10:
        Due=days-10# If the book is issued above the expiry date it aaks the user to pa fine $1.5 per day
        regularbill.write("Fine: $1 per day"+"n")
        regularbill.write("Due days:" +str(Due)+"\n")
        regularbill.write("Total:"+"$"+str(Due*1)+"\n")
    regularbill.write("")#Generates bill with all the required ionformation in it

