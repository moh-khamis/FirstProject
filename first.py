def cleanWord(word):
     if len(word) == 1:
          return word
     else:
          if word[0] == word[1]:
               return cleanWord(word[1:])   
          
          return word[0] + cleanWord(word[1:])

print(cleanWord('WWWWoooorrrllld'))







u_name     = input("Enter your name :")
u_email    = input("Enter your email :")
u_password = input("Enter your password :")
u_age      = input("Enter your age :")

p_up = 0
p_lw = 0

for c in u_password :
    if c.isupper():
        p_up = 1
    else:
        p_lw = 1    



if not u_age.isnumeric():
    print('*'*50)
    print("Enter age in number") 
    print('*'*50)
elif len(u_password) < 8:
        print('*'*50)
        print('password must be at least 8 letters')
        print('*'*50)
elif p_up == 0:
        print('*'*50)
        print('password must have one upper letter')    
        print('*'*50)
elif p_lw == 0:
        print('*'*50)
        print('password must have one lower letter')        
        print('*'*50)
else:
  print('*'*50)
  print(f"your name is {u_name} \nand your email is {u_email} \nand your password is {u_password} \nand your age is {u_age}")
  print('*'*50)