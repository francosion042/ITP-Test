# -*- coding: utf-8 -*-

import json
from operator import itemgetter
from helpers import validate_email, validate_phone

contacts = []
leads = []

class ContactsList:
    def __init__(self, name, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone
        
    def __repr__(self):
        return "<__main__.ContactsList: name = " + str(self.name) + "; email = " + str(self.email) + "; phone = " + str(self.phone) + ">"
        
        
        
class LeadsList:
    def __init__(self, name=None, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone
        
    def __repr__(self):
        return "<__main__.LeadsList: name = " + str(self.name) + "; email = " + str(self.email) + "; phone = " + str(self.phone) + ">"



        
# The Function to accept the registration form's json data.       
def webinar(registrant):
    data = json.loads(registrant)
    
    name, email, phone = itemgetter('name', 'email', 'phone')(data['registrant'])
    
    #loop through the contacts to match email and phone
    for contact in contacts:
        
        if email != 'None' and email == contact.email:
            
            if contact.phone ==  'None' and phone != 'None': contact.phone = phone
            return
        
        elif phone != 'None' and phone == contact.phone:
            
            if contact.email == 'None' and email != 'None': contact.email = email
            return
        
    #loop through the leads to match email and phone    
    for lead in leads:
        
        if email != 'None' and email == lead.email:
            
            
            contacts.append(ContactsList(name, email, phone))
            leads.remove(lead)
            return
        
        elif phone != 'None' and phone == lead.phone:
            
            contacts.append(ContactsList(name, email, phone))
            leads.remove(lead)
            return
        
        
    if email != 'None' and not validate_email(email):
        return    
    elif phone != 'None' and not validate_phone(phone):
        return
    else:
        contacts.append(ContactsList(name, email, phone))
            
    
    


contacts.append(ContactsList('Alice Brown', 'None', '1231112223'))
contacts.append(ContactsList('Bob Crown', 'bob@crowns.com ', 'None'))
contacts.append(ContactsList('Carlos Drew', 'carl@drewess.com','3453334445'))
contacts.append(ContactsList('Doug Emerty', 'None','4564445556'))
contacts.append(ContactsList('Egan Fair', ' eg@fairness.com', '5675556667'))


leads.append(LeadsList('None','kevin@keith.com', 'None'))
leads.append(LeadsList('Lucy', 'lucy@liu.com', '3210001112'))
leads.append(LeadsList('Mary Middle ', 'mary@middle.com', '3331112223'))
leads.append(LeadsList('None', 'None', '4442223334'))
leads.append(LeadsList('None', 'ole@olson.com', 'None'))

    

    
registrant1 = { 
    "registrant": { 
        "name": "Lucy Liu", 
        "email": "lucy@liu.com",
        "phone": "None", },
    }    

registrant2 = { 
    "registrant": { 
        "name": "Doug", 
        "email": "doug@emmy.com",
        "phone": "4564445556", },
    }

registrant3 = { 
    "registrant": { 
        "name": "Uma Thurman", 
        "email": "uma@thurs.com",
        "phone": "None", },
    }

#Register Someone
webinar(json.dumps(registrant2))


for contact in contacts:
    print('CONTACTS: ', contact.name, contact.email, contact.phone)
    
for lead in leads:
    print('LEADS: ',lead.name)


        
