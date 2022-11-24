file = open('countries.txt','r')
file_content = file.read()
print( file_content )
file.close()

#dla polskich znaków: encoding = "utf-8"