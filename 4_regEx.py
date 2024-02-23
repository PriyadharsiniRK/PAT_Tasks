import re



def emailAdd_check(emailAddr): 
    ## Regular expression pattern for email address validation
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # Check if the email address matches the pattern
    if re.match(email_pattern, emailAddr):
        return True
       
    else:
        return False

emailAddr='test@gmail.com'
print(f"{emailAddr} is valid: {emailAdd_check(emailAddr)}")

def phNumber_check(phNumber):
    # Regular expression pattern for phone number validation
    ph_pattern=r"^\+(?:[0-9] ?){6,14}[0-9]$"

    # Check if the phone number matches the pattern
    if re.match(ph_pattern, phNumber):
        return True

    else:
        return False
       
phNumber= '+880 01054 694200'
print(f"{phNumber} is valid: {phNumber_check(phNumber)}")

def telephNumber_check(telephNumber):
    ## Regular expression pattern for telephone number validation
    teleph_pattern=r"^\(\d{3}\) \d{3}-\d{4}$"
    
    # Check if the telephone number matches the pattern
    if re.match(teleph_pattern, telephNumber):
        return True
        
    else:
        return False
       
telephNumber='(555) 555-1234'
print(f"{telephNumber} is valid: {telephNumber_check(telephNumber)}")

def password_check(password):
    # Regular expression pattern for password validation
    password_pattern = r"^[A-Za-z0-9!@#$%^&*()_+]{16}$"
    
    # Check if the password matches the pattern
    if re.match(password_pattern, password):
        return True
    else:
        return False
pwd = "Abcdef123!@#$%^&"
print(f"{pwd} is valid: {password_check(pwd)}")
