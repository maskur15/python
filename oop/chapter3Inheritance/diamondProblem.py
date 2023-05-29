class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class ContactList(list):
    def search(self,name):
        '''Return all contacts that contain the search value
        in their name '''

        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)
    def showContact(self):
        for contatct in self.all_contacts:
            print(contatct)
class Friend(Contact,AddressHolder):
    def __init__(self, name, email, phone,street,city,state,code):
        Contact.__init__(self,name,email)
        AddressHolder.__init__(self,street,city,state,code)
        self.phone = phone
class MailSender:
    def send_mail(self,message):
        print('sending mail to '+self.email)
class EmailableContact(Contact,MailSender):
    pass


e = EmailableContact('maskur al','maskur@gmail.com')
e.send_mail('simple message')



c1=  Contact('John','jona@gm.com')
c2 = Contact('John b','jonb@gmail.com')
c3 = Contact('Jenna b','jin@email.com')
ar = [c.name for c in Contact.all_contacts.search('John')]
print(ar)
print(Contact.all_contacts[1].name)
