def bookdetail():
    #Displays the number of books present in the library
    print("Library Management System")
    print("------------------------------------------------------------------------------------")
    print("S/N"+"\t"+"Name of the book"+"\t"+"Author's Name"+"\t"+"Quantity available"+"\t"+"Price")
    print("------------------------------------------------------------------------------------")
    a=1
    file=open("library.txt", "r") #Helps you read the text file.
    for tab in file:
        x=tab.replace(",","\t\t") #Replaces "," to "tab"
        print(a,"\t",x)
        a=a+1
    print("------------------------------------------------------------------------------------")

