import time

# --- Database (Simulated using a Dictionary) ---
# Format: { account_number: { "pin": str, "balance": float, "name": str } }
accounts = {
    "123456": {"pin": "1122", "balance": 1500.00, "name": "Alex Mercer"},
    "789012": {"pin": "4455", "balance": 500.50, "name": "Sarah Connor"}
}

# --- Functions ---

def authenticate_user():
    """Handles user login with account number and PIN."""
    print("\n=== Welcome to the Citizen Bank ATM ===")
    attempts = 3
    
    while attempts > 0:
        account_num = input("Enter your 6-digit Account Number: ").strip()
        pin = input("Enter your 4-digit PIN: ").strip()
        
        # Check if account exists and PIN matches
        if account_num in accounts and accounts[account_num]["pin"] == pin:
            print(f"\n[SUCCESS] Login successful! Welcome back, {accounts[account_num]['name']}.")
            return account_num
        else:
            attempts -= 1
            print(f"\n[ERROR] Invalid Account Number or PIN. Attempts remaining: {attempts}")
            print("-" * 40)
            
    print("\n[BLOCKED] Too many incorrect attempts. Card retained. Please contact support.")
    return None


def check_balance(account_num):
    """Displays the current balance."""
    balance = accounts[account_num]["balance"]
    print("\n" + "="*30)
    print(f"Account Holder: {accounts[account_num]['name']}")
    print(f"Current Balance: ${balance:,.2f}")
    print("="*30)


def deposit_money(account_num):
    """Handles depositing money into the account."""
    try:
        amount = float(input("\nEnter amount to deposit: $"))
        if amount > 0:
            # Update balance
            accounts[account_num]["balance"] += amount
            print(f"\n[SUCCESS] ${amount:,.2f} deposited successfully.")
            print(f"New Balance: ${accounts[account_num]['balance']:,.2f}")
        else:
            print("\n[ERROR] Deposit amount must be greater than zero.")
    except ValueError:
        print("\n[ERROR] Invalid input. Please enter a valid numerical amount.")


def withdraw_money(account_num):
    """Handles withdrawing money from the account."""
    try:
        amount = float(input("\nEnter amount to withdraw: $"))
        current_balance = accounts[account_num]["balance"]
        
        if amount <= 0:
            print("\n[ERROR] Withdrawal amount must be greater than zero.")
        elif amount > current_balance:
            print(f"\n[DENIED] Insufficient funds. Your current balance is ${current_balance:,.2f}")
        else:
            # Update balance
            accounts[account_num]["balance"] -= amount
            print("\nProcessing transaction...")
            time.sleep(1) # Simulates ATM processing time
            print(f"[SUCCESS] Please collect your cash: ${amount:,.2f}")
            print(f"Remaining Balance: ${accounts[account_num]['balance']:,.2f}")
    except ValueError:
        print("\n[ERROR] Invalid input. Please enter a valid numerical amount.")


# --- Main Program Loop ---
def main():
    # 1. Authentication
    active_account = authenticate_user()
    
    if active_account is None:
        return # Exit program if authentication fails
        
    # 2. ATM Menu Loop
    while True:
        print("\n--- ATM MAIN MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit / Logout")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == "1":
            check_balance(active_account)
        elif choice == "2":
            deposit_money(active_account)
        elif choice == "3":
            withdraw_money(active_account)
        elif choice == "4":
            print(f"\nThank you for using Citizen Bank, {accounts[active_account]['name']}. Goodbye!")
            break
        else:
            print("\n[INVALID CHOICE] Please select a valid option from 1 to 4.")
            
        print("\n" + "-"*40)
        time.sleep(1)

# Run the program
if __name__ == "__main__":
    main()