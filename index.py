# -*- coding: utf-8 -*-

import json
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


contacts.append(ContactsList('Alice Brown', 'None', '1231112223'))
contacts.append(ContactsList('Bob Crown', 'bob@crowns.com ', 'None'))
contacts.append(ContactsList('Carlos Drew', 'carl@drewess.com','3453334445'))
contacts.append(ContactsList('Doug Emerty', 'None','4564445556'))
contacts.append(ContactsList('Egan Fair', ' eg@fairness.com', '5675556667'))

leads.append(LeadsList('None',' kevin@keith.com', 'None'))
leads.append(LeadsList('Lucy', ' lucy@liu.com', '3210001112'))
leads.append(LeadsList('Mary Middle ', 'mary@middle.com', '3331112223'))
leads.append(LeadsList('None', 'None', '4442223334'))
leads.append(LeadsList('None', 'ole@olson.com', 'None'))




# print('Contacts', contacts[0].name)
# print('Leads', leads[0].name)



        
        
def webinar(registrant):
    data = json.loads(registrant)
    
    for contact in contacts:
        if data['email'] != contact.email:
            pass
            
        print(contact.name)
    
    print(data['registrant'])
    
    
    
registrant1 = { 
    "registrant": { 
        "name": "Lucy Liu", 
        "email": "lucy@liu.com ",
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


webinar(json.dumps(registrant1))


        
