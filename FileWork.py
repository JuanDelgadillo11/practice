# Reading data from a file
# obj = open("D:\WindRiver\Python\Automation2\data.txt",'r')

# Read all data from a file
# print(obj.read())

# Read 1 line from the file STP-JD-SP19-00-clean8
# print(obj.readline())

# Read characters from file STP-J
# print(obj.read(5))

# Read all characters from file and display 1 by 1 in different lines
# for i in obj.read():
#     print(i)

# Write data into a new file
# obj = open("D:\WindRiver\Python\Automation2\data1.txt",'w')
# obj.write("Hello this is new data")
# obj.close()

# File Handling
obj = open("D:\WindRiver\Python\Automation2\data.txt",'r')
obj.readline()
print(obj.seek(5))
print(obj.tell())
print(obj.read())