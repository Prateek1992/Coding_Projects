letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25::-1]
print(backwards[9:12:1]) #challenge1
print(backwards[21::1])  #challenge2
print(letters[25:17:-1]) #challenge3

# [::-1] is a python idiom for reversing a string
print(letters[-1:])
print(letters[:1])