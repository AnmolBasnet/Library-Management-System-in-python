def request_book():
    success=True
    while success==True:
        try:
            import bookdetails# It imports bookdetails module
            bookdetails.bookdetail() # and it calls read_ function from above imported module
            print("press 1 Inorder to borrow the book.")
            print("Press 2 for returning the book.")
            print("Press 3 to exit.")
            an=int(input(""))
            if an==1:
                import read 
                read.borrow()
            elif an==2:
                import read 
                read.return_()
            elif an==3:            
                print("thank you")
                success=False
            else:   
                print("enter 1 2 3" )
        except:
            print("Please Enter a valid number eg:1,2,3")
request_book()             
            
                
            
 
