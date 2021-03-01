class Category:
    def __init__(self, category):
        self.category=category
        self.balance=0
        self.ledger=[]
        self.amount = 0
        n=30-len(self.category)
        st = "*"*(n//2)
        self.intro=st+self.category+st+"\n"

    def deposit(self, amount, description=""):
        self.amount=amount
        self.description=description
        self.balance=self.balance + self.amount
        self.ledger.append({"amount": self.amount, "description": self.description})
        self.intro += self.description[:23] + " "*(30-len(self.description[:23])-len(str(float(self.amount)))) + str(float(self.amount))+"\n"
    def withdraw(self, amount, description=""):
        self.amount=amount
        self.description=description
        newamount = 0
        if amount<=self.balance:
            newamount= 0-self.amount
            if not self.description.startswith("Transfer"):
                self.intro += self.description[:23] + " "*(29-len(self.description[:23])-len(str(float(self.amount)))) + str(float(newamount)) + "\n"
            self.balance=self.balance - self.amount
            self.ledger.append({"amount": newamount, "description": self.description})
            return True
        else:
            return False
    def get_balance(self):
        return self.balance
    def transfer(self, amount, receiver):
        self.receiver=receiver
        self.amount= amount
        if amount<= self.balance:
            self.intro += "Transfer to " + self.receiver.category + " "*(30-len("Transfer to " + self.receiver.category)-len(str(float(-self.amount)))) + str(float(0 - self.amount)) + "\n"
            self.withdraw(self.amount, "Transfer to [" + self.receiver.category + "]")
            self.receiver.deposit(self.amount, "Transfer from [" + self.receiver.category + "]")
            return  True
        else:
            return False
    def check_funds(self, amount):
        self.amount= amount
        if self.amount< self.balance:
            return False
        else:
            return True

def create_spend_chart(lst):
    L=[]
    M=[]
    R=[]
    for it in lst:
        R.append(len(str(it.category)))
    per=0
    for obj in lst:
        L.append(obj.balance)
    s=sum(L)
    for obj in lst:
        per=(obj.balance/s)*100
        M.append(per)
    print("100|", end=" ")
    n=len(M)
    for p in M:
        if p==100:
            print("o")
        if M.index(p)==n-1:
            print("")
        else:
            print("  ", end="")
    print(" 90|", end="  ")
    for p in M:
        if p>=90:
            print("o", end="  ")
        if M.index(p)==n-1:
            print("")
        else:
            print("  ", end="")
    print(" 80|",end="  ")
    for p in M:
        if p>=80:
            print("o", end="  ")
        if M.index(p)==n-1:
            print("  ")
        else:
            print("  ", end="")
    print(" 70|",end="  ")
    for p in M:
        if p>=70:
            print("o", end="  ")
        if M.index(p)==n-1:
            print("")
        else:
            print("  ", end="")
    print(" 60|",end="  ")
    for p in M:
        if p>=60:
            print("o", end="  ")
        if M.index(p)==n-1:
            print("")
        else:
            print("  ", end="")
    print(" 50|",end="  ")
    for p in M:
        if p>=50:
            print("o", end="  ")
        if M.index(p)==n-1:
            print("")
        else:
            print("  ", end="")
    print(" 40|",end="  ")
    for p in M:
        if p>=40:
            print("o", end="   ")
        if M.index(p)==n-1:
            print("")
        else:
            print("  ", end="")
    print(" 30|",end="  ")
    for p in M:
        if p>=30:
            print("o", end="   ")
        if M.index(p)==n-1:
            print("")
        else:
            print("  ", end="")
    print(" 20|",end="  ")
    for p in M:
        if p>=20:
            print("o", end="   ")
        if M.index(p)==n-1:
            print("")
        else:
            print("  ", end="")
    print(" 10|",end="  ")
    for p in M:
        if p>=10:
            print("o", end="   ")
        if M.index(p)==n-1:
            print("")
        else:
            print("  ", end="")
    print("  0|",end="  ")
    for p in M:
        if p>=0:
            print("o", end=" ")
        if M.index(p)==n-1:
            print("")
        else:
            print("  ", end="")
    t=max(R)
    for i in range(t):
        print("      ", end="")
        for elt in lst:
            try:
                print(str(elt.category)[i], end="   ")
            except:
                print("    ",end="")
        print("")