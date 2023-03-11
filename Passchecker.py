import string
import getpass

def check_password_strength():
    password = getpass.getpass('Enter the password:')
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0 
    
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1 
    if lower_count >= 1: 
        strength += 1
    if upper_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    
    if strength == 1:
        remarks = ('trash password')
    elif strength == 2:
        remarks = ('weak password')
    elif strength == 3:
        remarks = ('not great, not terrible password')
    elif strength >= 4:
        remarks = ('that is fine password')
        
    print('Your password has:-')
    print(f'{lower_count} lowercase letters')
    print(f'{upper_count} uppercase letters')
    print(f'{wspace_count} whitespaces')
    print(f'{num_count} digits')
    print(f'{special_count} special chars')
    print(f'Password Score:{strength / 5}')
    print(f'Remarks: {remarks}')
    

def check_pwd(another_pw=False):
    vaild = False
    if another_pw:
        choice = input (
            'Do You want to check another passwords strength (y/n):')
    else:
        choice = input(
            'Do you want to check Your passwords strength (y/n):')
    while not vaild:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            print('Exiting...')
            return False
        else:
            print('Invalid input \n')
        
if __name__ == '__main__':
    print('===Welcome ot passchecker===')
    check_pw = check_pwd()
    while check_pw:
        check_password_strength()
        check_pw = check_pwd(True)    
        
        
        