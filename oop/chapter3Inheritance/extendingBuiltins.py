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
c1=  Contact('John','jona@gm.com')
c2 = Contact('John b','jonb@gmail.com')
c3 = Contact('Jenna b','jin@email.com')
ar = [c.name for c in Contact.all_contacts.search('John')]
print(ar)
print(Contact.all_contacts[1].name)