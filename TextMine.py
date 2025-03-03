# Format: Pay/Pays <receiver> rupees <amount>

class User:
    def __init__(self, user, text):
        self.sender = user
        self.text = text
        self.receiver = None
        self.amt = None

    #FOL :Pay(self.user, self.receiver, amt)
    def MakePayment(self):
        lst = self.text.split()
        if 'pay' in lst:
            lst.remove('pay')
        elif 'pays' in lst:
            lst.remove('pays')

        for i in lst:
            if i.isnumeric():
                self.amt = int(i)
            elif i == 'rupees' or i == 'Rupees':
                continue
            else:
                self.receiver = i
        return (self.user, self.receiver, self.amt)
    
    def Pay(self):
        return None