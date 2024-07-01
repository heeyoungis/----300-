#021
letters = 'python'
print(letters[0], letters[2])

#022
license_plate = "24가 2210"
print(license_plate[4:])

#023
string = "홀짝홀짝홀짝"
print(string[::2])

#024
string = "PYTHON"
print(string[::-1])

#025
phone_number = "010-1111-2222"
new = phone_number.replace("-"," ")
print(new)

#026
phone_number = "010-1111-2222"
new = phone_number.replace("-","")
print(new)

#027
url = "http://sharebook.kr"
domain = url.split('.')
print(domain[1])

#028
# lang = 'python'
# lang[0] = 'P'
# print(lang)

#029
string = 'abcdfe2a354a32a'
new = string.replace("a","A")
print(new)

#030
string = 'abcd'
string.replace('b', 'B')
print(string)
