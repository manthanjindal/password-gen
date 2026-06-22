import random

alpha = "qwertyuiopasdfghjklzxcvbnm"
num = '1234567890'
spl_char = "!@#$%^&*()_+{|\][:;?><,}./~``]"

all_chars = [alpha, num, spl_char]

# def check_pass_critera(password):
#     confirmed_password = 'k'
    
#     alpha_count = 0
#     num_count = 0
#     spl_count = 0 
#     for i in password:
#         if i.isalpha():
#             alpha_count +=1
#         if i.isdigit():
#             num_count +=1 
#         if not i.isalnum():
#             spl_count += 1
    
#     if alpha_count > (len(password)/2):
#         #what to do
    

#     return confirmed_password



def generate_password(len_requirement):
    
    password = ''
    length = 0

    while length != len_requirement:
        password += random.choice(random.choice(all_chars))
        length += 1

    # final_password = check_pass_critera(password)
    return password
    

def main():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print("Generated Password:", password)

main()