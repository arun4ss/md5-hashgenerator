
import hashlib 

print("input string")
str = input()
print(str)


result = hashlib.md5(str.encode()) 
 
print("The hexadecimal equivalent of hash is : ", end ="") 
print(result.hexdigest()) 

