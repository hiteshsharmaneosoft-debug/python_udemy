## Example3: Encode the message
# the message is the string of numbers, each letter of alphabet is represented by its position 
# for ex: (A=0,B=1,C=2....)
# And these numbers are concatended into one long string


encode_message = 123658263429824

last_digit = encode_message % 26
print("last digit of given string is:",last_digit)

# Convert that numeric value into a character 
chr(last_digit + 65)   # 65 is ASCII for 'A'
print("The alphabet value of given string is:",chr(last_digit + 65)) 
