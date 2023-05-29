class SecretString:
    '''A not at all security'''
    def __init__(self,plain_text,pass_phrase):
        self.__plain_text = plain_text
        self.__pass_phrase = pass_phrase
    def decrypt(self,pass_phrase):

        if pass_phrase==self.__pass_phrase:
            return self.__plain_text
        else:
            return ''
secret_string = SecretString('topp ssecret','anterwe')
print(secret_string.decrypt('anterwe'))
'''Name mangling _className<variableName> '''
print(secret_string._SecretString__plain_text)