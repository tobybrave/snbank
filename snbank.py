import random

def new_account():
  details = {}
  acc_name = input("\nAccount name: ")
  bal = True
  while bal:
    try:
      opening_bal = eval(input("Opening Balance (in $): "))
      bal = False
    except:
      print(" Only digits can be inputted!!")
  acc_type = input("Account type: ")
  acc_number = int("".join(str(random.randint(0,9)) for i in range(10)))
  
  details["Account Name"] = acc_name
  details["Opening Balance"] = opening_bal
  details["Account Type"] = acc_type
  details["Account Number"] = acc_number
  print(details)
  return details

menu = True
print("*** SN Banking System***")
while menu:
  print("""\nStaff Login
Close App""")

  entry = input(" Enter S to select Staff Login and C to Close App: ").upper()

  if entry == "C":
    break
    
  login = True
  if entry == "S":
    while login:
      entered_username = input("Enter Username: ").lower()
      entered_password = input("Enter password: ")
      with open("staff.txt", "r") as staff:
      	registered_staff = eval(staff.read())
      staff1_username = registered_staff["staff1"]["username"] 
      staff1_password = registered_staff["staff1"]["password"]
      staff2_username = registered_staff["staff2"]["username"]
      staff2_password =  registered_staff["staff2"]["password"]
      if (entered_username == staff1_username and entered_password ==  staff1_password) or (entered_username == staff2_username and entered_password ==  staff2_password):
        #put a loop here
        sub_menu = True
        
        print(f"\nWelcome {entered_username}")
        while sub_menu:
          print("""
1. Create New Account
2. Check Account Details
3. Logout""")

          digit = True
          while digit:
          	try:
          		selected = int(input(" Enter the corresponding number to select: "))
          		digit = False
          	except ValueError:
          		print("Only digits allowed!!")
          		
          if selected == 1:
            userDetails = new_account()
            with open("customer.txt", "w") as customer_file:
            	customer_file.write(str(userDetails))
          
          elif selected == 2:
            print("\nAccount Details")
            with open("customer.txt", "r") as customer_file:
            	customer_details = customer_file.read()
            	print(customer_details)
          
          elif selected == 3:   
            sub_menu = False
            login = False
            
      else:
        print(" Wrong Username or password! Try again")
    
  else:
    print("\nInvalid entry!!")