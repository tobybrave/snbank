import random, time, os

def staff_sign_in():
	sign_in = True
			
	while sign_in:
		entered_staff_username = input("Enter Username: ").lower()
		entered_staff_password = input("Enter password: ")
		
		with open("staff.txt", "r") as staff_file:
			staffs = staff_file.readlines()
			staff_list = []
			for staff in staffs:
				staff_list.append(staff.split())
			
			staff_index = 0
			total_staff = len(staff_list)
			access_granted = True
			
			while staff_index < total_staff:
				staff_username = staff_list[staff_index][0]
				staff_password = staff_list[staff_index][1]
				if staff_username == entered_staff_username and staff_password == entered_staff_password:
					access_granted = False
				staff_index += 1
				
			if access_granted == False:
				sign_in = False
				
			else:
				print("Incorrect username or password!! Try again")
	return entered_staff_username


def new_account():
  account_name = input("\nAccount name: ")
  is_opening_balance_number = True
  
  while is_opening_balance_number:
    try:
      opening_balance = eval(input("Opening Balance (in Naira): "))
      is_opening_balance_number = False
    except:
      print(" Only digits can be inputted!!")
      
  account_type = input("Account type: ")
  account_number = "".join(str(random.randint(0,9)) for i in range(10))
  
  with open("customer.txt", "a") as customers:
  	customers.write(f'{account_number} Account_Name:"{account_name}" Opening_Balance:{opening_balance} Account_Type:{account_type}\n')
  	
  return (f"Account Number: {account_number}")


def check_account():
	with open("customer.txt", "r") as customers_file:
		customers = customers_file.readlines()
		customers_list = []
		for customer in customers:
			customers_list.append(customer.split())
			
		is_account_number_correct = True
		while is_account_number_correct:
			entered_account_number = input("\nAccount Number: ")
			customer_index = 0
			total_customers = len(customers_list)
			
			while customer_index < total_customers:
				account_number = customers_list[customer_index][0]
				if entered_account_number == account_number:
					customer_details = customers_list[customer_index]
					is_account_number_correct = False
				customer_index += 1	
				
	return customer_details
	

menu = True
print("*** SN Banking ***")
while menu:
	print("""\nStaff Login
Close App""")
	entry = input("Enter S to select Staff Log in and C to Close App: ").upper()
	
	if entry == "C":
		menu = False
		
	elif entry == "S":
		sign_in = staff_sign_in()
		print(f"\nWelcome {sign_in}")
		with open("session_file.txt", "w") as session:
			session_time = time.ctime()
			session.write(sign_in + " logged in " +session_time)
		sub_menu = True
		
		while sub_menu:
			is_selected_digit = True
			
			while is_selected_digit:
				print("""
1. Create New Account
2. Check Account Details
3. Logout""")
				try:
					selected = int(input("Enter the corresponding number to select: "))
					is_selected_digit = False
				except ValueError:
					print("\nOnly digits allowed!!")
					
			if selected == 1:
				print(new_account())
			elif selected == 2:
				print(check_account())
			elif selected == 3:
				os.remove("session_file.txt")
				sub_menu = False
				
			else:
				print("\nEnter the corresponding number!!!")
						
	else:
		print("\nInvalid entry!! Try again")