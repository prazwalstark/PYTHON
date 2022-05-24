filename='D:\Programs\#Python\#Extra\guest_book.txt'
with open(filename,'w') as file_object:
    print('Enter Your Name')
    name=input()
    file_object.write(name)
with open(filename,'r') as file_object:
    print("Hello " +file_object.read().strip()+' !Thank You For Signing Up!')

