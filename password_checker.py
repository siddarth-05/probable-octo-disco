import re
import hashlib
import requests

def passwordchecker(txt):
    #Flags set to false
    specialcharcheck = False
    lengthcheck = False
    numcheck = False
    capscheck = False
    lowercasecheck = False
    #length checker, change how you want to
    if len(txt) >= 14:
        lengthcheck = True
    #special character check - change this if you want to check for more, but be careful with the regex. It breaks easy.
    if re.search(r"[~!@#$%^&*()_+=;:,.?]", txt):
        specialcharcheck = True
    #capital letters
    if re.search(r"[A-Z]", txt):
        capscheck = True
    if re.search(r"[a-z]", txt):
        lowercasecheck = True
    if re.search(r"[0-9]", txt):
        numcheck = True
    #just checking flags and telling you WHY your password is bad.
    if not lengthcheck:
        print("\nToo small. At least 14 characters.")
    if not numcheck:
        print("\nNo numbers. Add digits.")
    if not capscheck:
        print("\nNo capital letters.")
    if not specialcharcheck:
        print("\nNo special characters.")
    if not lowercasecheck:
        print("\nNo lowercase letters.")

    if numcheck and lengthcheck and capscheck and lowercasecheck and specialcharcheck:
        return txt + " is a good password"
    else:
        return txt + " is not a good password"

def checkagainstPWNdatabase(txt):
    #encode gives us binary, hexdigest gives us the hexadecimal notation, and upper makes it all caps.
    hashed = hashlib.sha1(txt.encode()).hexdigest().upper()
    prefix = hashed[:5]
    suffix = hashed[5:]
    #this is for the HIBP API, which takes the prefix as an argument for the range searching.
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    for line in response.text.splitlines():
        parts = line.split(':')
        if parts[0] == suffix:
            #returns a string, in the form of hexadecimal suffix: number of times it has been found.
            #we're using the split method to break it up into two parts
            return f"Password breached {parts[1]} times, consider refreshing if the number is greater than 20."
    return "Password not found in breaches"

# Input from the user
print("Your password here:")
txt = input()

# Run the password checker
result = passwordchecker(txt)
print(result)

# Check against PWN database
pwn_result = checkagainstPWNdatabase(txt)
print(pwn_result)
