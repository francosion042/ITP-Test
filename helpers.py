# -*- coding: utf-8 -*-

import re 
   
# for validating an Email 

      
 
def validate_email(email):  
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    
    if(re.search(regex,email)):  
        print("Valid Email")
        return True
          
    else:  
        print("Invalid Email")
        return False
        
        
        
def validate_phone(phone):
    regex = "^(\d{10})$"
  

    if(re.search(regex,phone)):  
        print("Valid Phone")
        return True
          
    else:  
        print("Invalid Phone")  
        return False
      
  
validate_phone('1234567890')