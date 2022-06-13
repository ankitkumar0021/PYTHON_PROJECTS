email = input("Enter a Email :")                   
k,j,d = 0,0,0
if len(email)>=6:                                    #length of email
  if email[0].isalpha():                             #first letter should be a-z
    if ("@" in email) and (email.count("@")==1):     #'@' should be only one
      if (email[-4]==".") ^ (email[-3]== "."):       #these index can be '.'
        for i in email:           
          if i==i.isspace():                         #no space     
            k=1               
          elif i.isalpha():                          #a-z
            if i==i.upper():                         # no uppercase
             j=1 
          elif i.isdigit():                          # can be digit
              continue
          elif i=="_" or i=="." or i=="@":           #  it will check '_' , '.' , '@'
              continue
          else:                                      # it will check any special character
            d=1
        if k==1 or j==1 or d==1:
          print("wrong email 5")
        else:
          print('this Email is Right')
        
      else:
        print("wrong email 4")
    else:
      print("wrong email 3")
  else:
    print("wrong email 2")  
else:
  print("wrong email 1")