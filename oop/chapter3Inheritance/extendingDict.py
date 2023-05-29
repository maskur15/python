class ContactDict(dict):
    '''Extending the dictionary  class and add a method which will find the largest key '''
    def findLongestKey(self):
        key = None
        for k in self.keys():
            if key is None or len(k) > len(key):
                key= k
        return key
    def showDict(self):
        for key in self:
            print(key,self[key])
class Contact():
    contactDict = ContactDict()
    contactDict['maskur']=2
    contactDict['hasan']=1
    contactDict['maskur al shal sabil']=23
    print(contactDict.findLongestKey())

    contactDict.showDict()