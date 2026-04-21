

# password = input("Введите пароль: ")

def is_strong_password(password):

    has_lower = False
    has_upper = False
    has_digit = False
    spec_count = 0
    
    specials = "!@#$%^&*()-_+=;:,./?|"

    for c in password:
        if c.islower():
            has_lower = True
        elif c.isupper():
            has_upper = True
        elif c.isdigit():
            has_digit = True
        
        if c in specials:
            spec_count += 1

    res_len = len(password) >= 6
    res_str = has_lower and has_upper and has_digit
    res_spec = spec_count >= 2

    if res_len and res_str and res_spec:
        return True
    else:
        return False
    


    

print(is_strong_password('$PassW/12'))
print(is_strong_password('3gT*5?O'))
print(is_strong_password('k2-iR!49;'))



print(is_strong_password('12345'))
print(is_strong_password('password'))
print(is_strong_password('???!!!'))

