def read_():# This defines function to insert the book details in a dict
    counter=1
    display_book={}
    file=open("library.txt", "r")
     #fIt helps in reading the respective file
    for every_line in file:
        display_book[counter]=every_line.replace("\n", "").split(",")
        counter=counter+1
    print(display_book)
    return display_book
#It helps in borrowing the books.
def borrow():
    bookcode=read_()
    success=False
    while success==False:
        try:
            SN=int(input("Enter the Symbol number of the book that you wish to borrow."))#Asks the user to enter the symnol number of the required book
            if SN>0 and SN<=len(bookcode)+1:
                print(bookcode[SN])
                print("Book Information:")#Prints out the askedd book details
                print("Name of the book:", bookcode[SN][0],"\nAuthor's Name:", bookcode[SN][1], "\namountity available:", bookcode[SN][2], "\nPrice:", bookcode[SN][3])
                print("End")
                successa=False
                while successa==False:#It helps the program to continue the loop untill the user inserts valid information
                    request=input("Is this a book you wish to borrow(y/n)?")
                    request.lower()
                    if request=="n":
                        database=False
                        while database==False:
                            request2=input("Are you willing to exit(y/n)?")#aks the user if he/she wants to exit the transaction or not
                            if request2=="n":
                                successa=True
                                database=True
                            elif request2=="y":
                                successa=True
                                success=True
                                database=True  
                            else:
                                print("Enter(y/n)")
                    elif request=="y":
                        if int(bookcode[SN][2])==0:
                                    print(bookcode[SN][0],"It is not available at the moment.")#It prints the book is not available at the moment if it is out of stock
                                    successa=True
                                    success=True
                        else:
                            successb=True
                            while successb==True:
                                try:
                                    amount=int(input("How many books do you wish to borrow?"))#It asks the user the quantity of book he/she wants to borrow
                                    if amount>0 and amount<=int(bookcode[SN][2]):
                                        bookcode[SN][2]=str(int(bookcode[SN][2])-amount)
                                        print(bookcode[SN])
                                        name=str(bookcode[SN][0])
                                        author=str(bookcode[SN][1])
                                        price=str(bookcode[SN][3])
                                        import bill#It impoorts bill module for generating bill.
                                        bill.bill_(SN,name,author,amount,price)         
                                        successb=False
                                        successa=True
                                        success=True
                                        print("Thank You")
                                        file1=open("library.txt","w")#Re-wirtes text file for generating new updated text file
                                        for i in range(1,len(bookcode)+1,1):
                                            for j in range(0,len(bookcode[i])):
                                                print(bookcode[i][j]) 
                                                file1=open("library.txt","a")
                                                file1.write(bookcode[i][j])
                                                file1.write(",")
                                            file1.write("\n")         
                                   
                                    elif amount<0 or amount>int(bookcode[SN][2]):
                                        print("Invalid")
                                     
                                       
                                except:
                                    print("Out of context", "\nInvalid")
                    else:
                        print("Enter (y/n)")
            else:
                print("Invalid Context")
        except:
            print("Invalid Context")
    print("Thank you, Your book has been issued ")
#for returning the books
def return_():
    bookcode=read_()
    success=False
    while success==False:
        try:
            SN=int(input("Enter the Symobol number  of the book you want to return: "))# It asks the user to enter the symbol number of the respective book
            if SN>0 and SN<=len(bookcode):
                print("Book Details")#prints out book details with all the information in it
                print("Book Name:", bookcode[SN][0],"\nAuthor's Name:", bookcode[SN][1], "\namountity Available:", bookcode[SN][2], "\nPrice:", bookcode[SN][3])
                print("End")
                successa=False
                while successa==False:
                    request=input("Is this your book(y/n)?")#asks the user if this is the book he/she is willing to return
                    request=request.lower()
                    if request=="n":
                        database=False
                        while database==False:
                            ask2=input("Do you want to exit(y/n)?")#asks the user if the user is wiling to exit the program or not
                            if ask2=="n":
                                successa=True
                                database=True
                            elif ask2=="y":
                               successa=True
                               success=True
                               database=True  
                            else:
                                print("Enter(y/n)")
                    elif request=="y":
                        successb=False
                        while successb==False:
                            try:
                                amount=int(input("How many books do you want to return: "))#asks the user how many boks does the user wants to return
                                if amount<=0:
                                    print("Invalid context")
                                else:
                                    successb=True
                                    successa=True
                                    success=True
                                    name=str(bookcode[SN][0])
                                    author=str(bookcode[SN][1])
                                    import bill
                                    bill.return_(SN,name,author,amount)
                                    print("#Thank You")
                                    file1=open("library.txt","w")
                                    for i in range(1,len(bookcode)+1,1):
                                        for j in range(0,len(bookcode[i])):
                                            print(bookcode[i][j])                                     
                                            file1=open("library.txt","a")
                                            file1.write(bookcode[i][j])
                                            if j==3:
                                                break
                                            file1.write(",")
                                        file1.write("\n")
                            except:
                                print("Invalid Context, ")
                    else:
                        print("Enter(y/n):")                                
            else:
                print("Invalid context")
        except:
            print("Invalid context")

    print("Thank for returning the book. Have a nice day")

