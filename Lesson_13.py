# Example: The CreditCard Class
class CreditCard:
    """A consumer credit card."""
    def __init__ (self, customer, bank, acnt, limit):
        """ Create a new credit card instance.
        
        The initial balance is zero

        customer the name of the customer
        bank     the name of the bank
        acnt     the acount identifier
        limit    credit limit
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    
    def get_customer(self): # Lấy ra
        """ Return name of the customer."""
        return self._customer
    
    def get_bank(self): # Lấy ra
        """ Return the bank's name."""
        return self._bank
    
    def get_account(self): # Lấy ra
        """ Return the card identifying number (typically stored as a string)."""
        return self._account
    
    def get_limit(self): # Lấy ra
        """ Return current credit limit."""
        return self._limit
    
    def get_balance(self): # Lấy ra
        """ Return current balance."""
        return self._balance
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit
        Return True if charge was processed; False if charge was denied
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""
    def __init__ (self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit) # call super constructor
        self._apr = apr
    def get_customer(self):
        return super().get_customer()

    def charge(self, price):
        """Charge given price to the card, assuming sufficent credit limit.
        Return True if charge was processed
        Return False and assess $5 fee if charge is denied
        """
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success
    
    def process_month(self):
        if self._balance > 0:
            """if positive balance , convert APR to monthly miltiplicatice factor"""
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor


