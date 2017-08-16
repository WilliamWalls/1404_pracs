user_name = input("Please Enter Your Name ")
out_file = open("name_file", "w")
print(user_name, file= out_file)
out_file.close()

in_file = open("name_file", "r")
name = in_file.read()
print("Your Name is ", name)
in_file.close()

in_file = open("numbers.txt", "r")
print (in_file)