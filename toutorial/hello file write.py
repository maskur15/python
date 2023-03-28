#File write in python
try:
    myfile = open("D:\File/test.text", "w")
    amount = myfile.write("This is written by python file operation");
    print(amount)
finally:
    myfile.close()
# In the following procedure the file is automitacally close
with open("D:\File/test.text", "r") as f:
    print(f.read())

