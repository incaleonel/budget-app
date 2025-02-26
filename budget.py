class Category:
    
    def __init__(self, category):
        self.ledger = []
        self.category = category
        
    def __repr__(self):
        
        text_print = self.category.center(30,'*') + '\n'
        for item in self.ledger:
            amount_format = '{:.2f}'.format(item.get('amount'))
            text_print += item.get('description')[:23].ljust(30 - len(amount_format))
            text_print += amount_format + '\n'
        text_print += 'Total: ' + '{:.2f}'.format(self.get_balance())
        return text_print    
#'deposit that accepts an amount and description. If no description is given, it should default to an empty string.
#The method should append an object to the ledger list in the form of {"amount": amount, "description": description}   
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': float(amount), 'description': description})
        
#'withdraw' method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number.
#If there are not enough funds, nothing should be added to the ledger. 
#This method should return True if the withdrawal took place, and False otherwise.
    def withdraw(self, amount, description=''):
        if self.get_balance() - amount >= 0: 
            self.ledger.append({'amount': -1*amount, 'description':description})
            return True
        return False
#'get_balance' method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    def get_balance(self):
        total = 0
        for amount in self.ledger:
            total += amount.get('amount')
        return total
    
#A transfer method that accepts an amount and another budget category as arguments.
#The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". 
#The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
#If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
    def transfer(self, amount, budget):
        if self.withdraw(amount, 'Transfer to '+ budget.category):
            budget.deposit(amount, 'Transfer from '+ self.category)
            return True
        return False
#A check_funds method that accepts an amount as an argument. 
#It returns False if the amount is greater than the balance of the budget category and returns True otherwise. 
#This method should be used by both the withdraw method and transfer method.    
    def check_funds(self, amount):
        return False if amount > self.get_balance() else True
        
def create_spend_chart(categories):
    
    title = 'Percentage spent by category\n'
    withdrawals_total = 0
    spend_category = []
    max_length = 0
    for category in categories:
        spend = 0
        max_length = len(category.category) if max_length < len(category.category) else max_length
        for item in category.ledger:
            if item.get('amount') < 0:
                spend += item.get('amount')
        spend_category.append(spend)
        withdrawals_total += spend
    
    chart1 = ''
    line = '-'
    for i in reversed(range(0,101,10)):
        
        chart1 += '' if i else ' '
        chart1 += str(i) + '| ' if i==100 else ' ' + str(i) + '| '
        
        for percent in spend_category:
            percent = int(percent*100/withdrawals_total)
            if percent >= i:
                chart1 += 'o  '
            else:
                chart1 += '   '
            if i==100:
                line +='---'
        chart1 +='\n'       
    line = line.rjust(len(line)+4)
    chart2 = ''
    for i in range(max_length):
        chart2 += '     '
        for category in categories:
            chart2 += category.category[i] + '  ' if len(category.category) > i else '   '
        chart2 +='\n' if i != max_length-1 else ''
    return title + chart1 + line + '\n' + chart2 