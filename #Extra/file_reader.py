filepath='D:\Programs\#Python\#Extra\pi_digits.txt'
with open(filepath) as file_objects:
    lines=file_objects.readlines()
    
pi_string=''
for line in lines:
    pi_string+=line.strip()
print(pi_string[:52]+"...")
print(len(pi_string))
birthday=input('Enter you birthday, in the form of mmddyy:')
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi.')
