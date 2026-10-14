ch = '1'
print(ch.isdigit())  # True
ch = 'a'
print(ch.isdigit())  # False
print(ch.isalpha())  # True

str = '12345'
print(str.isdigit())  # True
str = '123a5'
print(str.isdigit())  # False
print(str.isalnum())  # True