import pyodbc
from datetime import date

DRIVER_NAME = "ODBC Driver 17 for SQL Server"
SERVER_NAME = "DESKTOP-JE09TUR\\SQLEXPRESS"
DATABASE_NAME = "Banking Database"

def get_connection():
    return pyodbc.connect(
        f"DRIVER={{{DRIVER_NAME}}};"
        f"SERVER={SERVER_NAME};"
        f"DATABASE={DATABASE_NAME};"
        "Trusted_Connection=yes;"
    )


# ------------------- UTILITY FUNCTIONS -------------------
def clear():
    for _ in range(65):
        print()

def account_status(acno):
    conn = get_connection()
    cursor = conn.cursor()
    sql = f"SELECT status, balance FROM customer WHERE acno = '{acno}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    conn.close()
    return result

# ------------------- DEPOSIT -------------------
def deposit_amount():
    conn = get_connection()
    cursor = conn.cursor()
    clear()
    acno = input("Enter account No : ")
    amount = input("Enter amount : ")
    today = date.today()
    result = account_status(acno)
    if result and result[0] == 'active':
        sql1 = f"UPDATE customer SET balance = balance + {amount} WHERE acno = '{acno}' AND status='active'"
        sql2 = f"INSERT INTO [transaction](amount, type, acno, dot) VALUES ({amount}, 'deposit', '{acno}', '{today}')"
        cursor.execute(sql2)
        cursor.execute(sql1)
        conn.commit()
        print("\nAmount deposited")
    else:
        print("\nClosed or Suspended Account....")
    input("\n\n\n Press any key to continue....")
    conn.close()

# ------------------- WITHDRAW -------------------
def withdraw_amount():
    conn = get_connection()
    cursor = conn.cursor()
    clear()
    acno = input("Enter account No : ")
    amount = input("Enter amount : ")
    today = date.today()
    result = account_status(acno)
    if result and result[0] == 'active' and int(result[1]) >= int(amount):
        sql1 = f"UPDATE customer SET balance = balance - {amount} WHERE acno = '{acno}' AND status='active'"
        sql2 = f"INSERT INTO [transaction](amount, type, acno, dot) VALUES ({amount}, 'withdraw', '{acno}', '{today}')"
        cursor.execute(sql2)
        cursor.execute(sql1)
        conn.commit()
        print("\nAmount withdrawn")
    else:
        print("\nClosed or Suspended Account Or Insufficient amount")
    input("\n\n\n Press any key to continue....")
    conn.close()

# ------------------- TRANSACTION MENU -------------------
def transaction_menu():
    while True:
        clear()
        print("Transaction Menu")
        print("\n1. Deposit Amount")
        print("\n2. Withdraw Amount")
        print("\n3. Back to Main Menu")
        print("\n\n")
        choice = int(input("Enter your choice ...: "))
        if choice == 1:
            deposit_amount()
        elif choice == 2:
            withdraw_amount()
        elif choice == 3:
            break

# ------------------- SEARCH MENU -------------------
def search_menu():
    conn = get_connection()
    cursor = conn.cursor()
    while True:
        clear()
        print("Search Menu")
        print("\n1. Account No")
        print("\n2. Aadhar Card")
        print("\n3. Phone No")
        print("\n4. Email")
        print("\n5. Names")
        print("\n6. Back to Main Menu")
        print("\n\n")
        choice = int(input("Enter your choice ...: "))
        field_name = ''
        if choice == 1:
            field_name = 'acno'
        elif choice == 2:
            field_name = 'aadhar_no'
        elif choice == 3:
            field_name = 'phone'
        elif choice == 4:
            field_name = 'email'
        elif choice == 5:
            field_name = 'name'
        elif choice == 6:
            break
        msg = f"Enter {field_name} : "
        value = input(msg)
        if field_name == 'acno':
            sql = f"SELECT * FROM customer WHERE {field_name} = '{value}'"
        else:
            sql = f"SELECT * FROM customer WHERE {field_name} LIKE '%{value}%'"
        #print(sql)
        cursor.execute(sql)
        records = cursor.fetchall()
        n = len(records)
        clear()
        print("Search Result for ", field_name, ":", value)
        print("-"*80)
        for record in records:
            print(record[0], record[1], record[2], record[3],
                  record[4], record[5], record[6], record[7], record[8])
        if n <= 0:
            print(field_name, ",", value, " does not exist")
        wait=input("\n\n\n Press any key to continue....")
    conn.close()
    wait = input("\n\n Press any key to continue....")

# ------------------- ACCOUNT DETAILS -------------------
def account_details():
    clear()
    acno = input("Enter account no : ")
    conn = get_connection()
    cursor = conn.cursor()
    sql = f"SELECT * FROM customer WHERE acno='{acno}'"
    sql1 = f"SELECT tid, dot, amount, type FROM transaction t WHERE t.acno='{acno}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    clear()
    print("Account Details")
    print("-"*120)
    print("Account No :", result[0])
    print("Customer Name :", result[1])
    print("Address :", result[2])
    print("Phone No :", result[3])
    print("Email ID :", result[4])
    print("Aadhar No :", result[5])
    print("Account Type :", result[6])
    print("Account Status :", result[7])
    print("Current Balance :", result[8])
    print("-"*120)
    cursor.execute(sql1)
    results = cursor.fetchall()
    for result in results:
        print(result[0], result[1], result[2], result[3])
    conn.close()
    input("\n\n\nPress any key to continue....")

# ------------------- ADD ACCOUNT -------------------
def add_account():
    conn = get_connection()
    cursor = conn.cursor()

    clear()
    name = input("Enter Name : ")
    addr = input("Enter address : ")
    phone = input("Enter phone no : ")
    email = input("Enter Email : ")
    aadhar = input("Enter Aadhar no : ")
    actype = input("Account Type (saving/current) : ")
    balance = input("Enter opening balance : ")
    sql = f"INSERT INTO customer(name, address, phone, email, aadhar_no, acc_type, balance, status) VALUES ('{name}', '{addr}', '{phone}', '{email}', '{aadhar}', '{actype}', {balance}, 'active')"
    #print(sql)
    cursor.execute(sql)
    conn.commit()
    print("\n\n New customer added successfully")
    wait = input("\n\n\n Press any key to continue....")
    conn.close()

# ---------------- MODIFY ACCOUNT -----------------
def modify_account():
    conn = get_connection()
    cursor = conn.cursor()

    clear()
    acno = input('Enter customer Account No : ')
    print('Modify screen')
    print('\n1. Customer Name')
    print('\n2. Customer Address')
    print('\n3. Customer Phone No')
    print('\n4. Customer Email ID')

    choice = int(input('What do you want to change ? '))
    new_data = input('Enter New value : ')

    field_name = ''
    if choice == 1:
        field_name = 'name'
    elif choice == 2:
        field_name = 'address'
    elif choice == 3:
        field_name = 'phone'
    elif choice == 4:
        field_name = 'email'

    sql = f"UPDATE customer SET {field_name} = ? WHERE acno = ?"
    cursor.execute(sql, (new_data, acno))
    conn.commit()

    print('\nCustomer Information modified..')
    input('\n\n\n Press any key to continue....')

# ---------------- CLOSE ACCOUNT -----------------
def close_account():
    conn = get_connection()
    cursor = conn.cursor()

    clear()
    acno = input('Enter customer Account No : ')
    sql = "UPDATE customer SET status = ? WHERE acno = ?"
    cursor.execute(sql, ("closed", acno))  # status = 'closed'
    conn.commit()

    print('\n\n Account closed')
    input('\n\n\n Press any key to continue....')

# ---------------- ACTIVATE ACCOUNT -----------------
def activate_account():
    conn = get_connection()
    cursor = conn.cursor()

    clear()
    acno = input('Enter customer Account No : ')
    sql = "UPDATE customer SET status = ? WHERE acno = ?"
    cursor.execute(sql, ("active", acno))
    conn.commit()

    print('\n\n Account Activated')
    input('\n\n\n Press any key to continue....')

# ---------------- MAIN MENU -----------------
def main_menu():
    while True:
        clear()
        print(' Main Menu ')
        print('\n1. Add Account')
        print('\n2. Modify Account')
        print('\n3. Close Account')
        print('\n4. Activate Account')
        print('\n5. Transaction Menu')
        print('\n6. Search Menu')
        print('\n7. Activate Account')
        print('\n')

        choice = int(input('Enter your choice : '))

        if choice == 1:
            add_account()
        elif choice == 2:
            modify_account()
        elif choice == 3:
            close_account()
        elif choice == 4:
            activate_account()
        elif choice == 5:
            transaction_menu()
        elif choice == 6:
            search_menu()
        elif choice == 7:
            activate_account()
        elif choice == 8:
            break

# ---------------- RUN PROGRAM -----------------
if __name__ == "__main__":
    main_menu()
