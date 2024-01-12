class Category:
    def __init__(self, name, ledger = None):
        self.name = name
        self.ledger = ledger if ledger else []

    def format(self, amount, description):
        format_amount = "{:.2f}".format(amount)
        len_amount = len(format_amount)
        format_description = description[0 : (30 - len_amount - 1)]
        line = format_description + " " + format_amount.rjust(30- len(format_description)-1)
        return line
    
    def __str__(self):
        left_char = 30 - len(self.name)
        self.title = "*"*(left_char // 2) + self.name + "*"*(left_char - (left_char // 2))
        self.lines = ""
        for d in self.ledger:
            self.lines += self.format(d["amount"], d["description"]) + "\n"
        self.final_line = "Total:"+ " " + str(self.get_balance()) 
        return f"{self.title}\n{self.lines}{self.final_line}"
        
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for d in self.ledger:
            balance += d["amount"]
        return balance
    
    def transfer(self, amount, cat):
        description1 = "Transfer to " + cat.name
        if self.check_funds(amount):
            description2 = "Transfer from " + self.name
            cat.deposit(amount, description2)
            self.withdraw(amount, description1)
            return True
        else:
            return False
        
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    

def create_spend_chart(categories):
    names = []
    each_spent = []
    for i in range(len(categories)):
        names.append(categories[i].name)
        each_spent.append(0)
        for d in categories[i].ledger:
            if d["amount"] < 0:
                each_spent[i] -= d["amount"]
    total_spent = sum(each_spent)
    percentage = []
    for s in each_spent:
        percentage.append(round((s/total_spent*100)//10*10))

    title = "Percentage spent by category"
    bar_line = " "*4 + "-"*(1 + len(percentage)*3)

    percent_lines = [[]]*11
    for i in range(11):
        num = str((10 - i)*10)
        format_num = num.rjust(3)
        percent_lines[i] = [format_num + "| " , ["   "]*len(percentage)]
    for j in range(len(percentage)):
        for pl in percent_lines[(100 - percentage[j])//10:11]:
            pl[1][j] = "o  "
    for i in range(11):
        percent_lines[i][1] = "".join(percent_lines[i][1])
        percent_lines[i] = "".join(percent_lines[i])
        if i < 10:
            percent_lines[i] += "\n"
    percent_lines = "".join(percent_lines)
    

    max_len = max(len(name) for name in names)
    name_lines = [[" " * 5, [" " * 3] * len(names)] for _ in range(max_len)]
    for k in range(len(names)):
        for l in range(len(names[k])):
            name_lines[l][1][k] = names[k][l] + " "*2
    for j in range(len(name_lines)):
        name_lines[j][1] = "".join(name_lines[j][1])
        name_lines[j] = "".join(name_lines[j])
        name_lines[j] += "\n"
    name_lines = "".join(name_lines)
    
    return f"{title}\n{percent_lines}\n{bar_line}\n{name_lines}"


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)


    

    