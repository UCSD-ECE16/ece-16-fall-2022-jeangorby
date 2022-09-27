## 0.3 Exercises

# 1
list_1 = [1,2,3,4,5,6,7,8,9,10]
# print(list_1)

# 2
list_2 = [11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0]
# print(list_2)

# 3
list_1[0] = 'one'
list_1[1] = 'two'
list_1[2] = 'three'
# print(list_1)

# 4
tup = ('eleven', 'twelve', 'thirteen')
list_2[0] = tup[0]
list_2[1] = tup[1]
list_2[2] = tup[2]
# print(list_2)

# 5
joint_1 = list_1[:]
joint_1.extend(list_2)
# print(joint_1)

joint_2 = list_1 + list_2
# print(joint_2)

# 6
def list_shift(base_list, new_data):
    base_list.extend(new_data)
    del base_list[:len(new_data)]
    return base_list

fixed_length_list = [1,2,3,4]
new_data = [5,6,7]
list_shift(fixed_length_list, new_data)
print(fixed_length_list)

# 7 bonus

## 1.4 Exercises

# 1
commands = ["STATUS", "ADD", "COMMIT", "PUSH", "PULL", "CLONE", "CLEAR"]

# 2
for x in commands:
    print(x)

# 3
i = 0
while i < len(commands):
    # print(commands[i])
    i += 1

# 4
new_list = ["PUSH FAILED", "BANANAS", "PUSH SUCCESS", "APPLES"]

# 5
text = "SUCCESS"

# 6
# print("SUCCESS" in "SUCCESS")
# print("SUCCESS" in "ijoisafjoijiojSUCCESS")
# print("SUCCESS" == "ijoisafjoijiojSUCCESS")
# print("SUCCESS" == text)
# print("finish" in "ijoisafjoijioj\finish")

# 7
for x in new_list:
    if(text in x):
        print("This worked!")
        break
    else:
        print(x)

## 2.2 Exercises

# 1
name = "JeanGorby"

# 2 
byte_name = name.encode('utf-8')

# 3
byte_name_bad = byte_name + b'\xef'

# 4
# byte_name_bad.decode('utf-8')
# This throws a UnicodeDecodeError

# 5 and 6
try:
    byte_name = byte_name.decode('utf-8')
except UnicodeDecodeError:
    byte_name = ""

print(byte_name)

try:
    byte_name_bad.decode('utf-8')
except UnicodeDecodeError:
    byte_name_bad = ""

print(byte_name_bad) 
