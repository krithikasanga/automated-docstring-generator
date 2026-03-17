def calculate_area(radius):
    """
    Calculates the area of a circle given its radius.
    
    Parameters:
        radius: The radius of the circle.
    
    Returns:
        The calculated area of the circle (float)
    """
    return 3.14159 * radius * radius


def format_email(username, domain="gmail.com"):
    """
    Formats a username and domain into a valid email address.
    
    Parameters:
        username: The username to be formatted.
        domain: The domain to be used (default: 'gmail.com')
    
    Returns:
        The formatted email address (str)
    """
    return f"{username}@{domain}"


def is_even(number):
    """
    Checks if a given number is even.
    
    Parameters:
        number: The number to be checked.
    
    Returns:
        True if the number is even, False otherwise (bool)
    """
    if number % 2 == 0:
        return True
    return False


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the bank account.
        
        Parameters:
            amount: The amount to be deposited.
        
        Returns:
            The updated balance of the bank account (int)
        """
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the bank account.
        
        Parameters:
            amount: The amount to be withdrawn.
        
        Returns:
            The updated balance of the bank account (int) or 'Insufficient funds' if the withdrawal fails (str)
        """
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance