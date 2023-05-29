class Contact:
    all_contacts = [] #class variable
    def __init__(self,name,email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
class Supplier(Contact):
    def order(self,order):
        print('If this were a real we would send'"'{}' order to '{}'".format(order,self.name) )
c = Contact('maskur','sabil22@gmai.com')

s = Supplier('shahn','shah22@gmailc.om')
print(c.name,c.email,s.name,s.email)
print(c.all_contacts)
c1 = Contact('sabil','sk22@gmai.com')
s1 = Supplier('shamim','shamim22@gmai.com')
s1.order('a ssd333')