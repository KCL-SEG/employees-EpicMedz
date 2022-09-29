"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthlySalary=0, contractHoursWorked=0, contractRate=0, numberOfCommissionContracts=0, commission=0):
        self.name = name
        self.monthlySalary = monthlySalary
        self.contractHoursWorked = contractHoursWorked
        self.contractRate = contractRate
        self.numberOfCommissionContracts = numberOfCommissionContracts
        self.commission = commission
        self.finalPay = 0


    def get_pay(self):
        pay = 0
        if self.monthlySalary > 0:
            pay = pay + self.monthlySalary
        if (self.contractHoursWorked > 0) and (self.contractRate > 0):
            pay = pay + (self.contractHoursWorked * self.contractRate)
        if self.commission >= 0:
            if self.numberOfCommissionContracts > 1:
                pay = pay + (self.commission * self.numberOfCommissionContracts)
            else:
                pay = pay + self.commission
        
        self.finalPay = pay
        return pay

    def __str__(self):
        string = f"{self.name} works on a "
        if self.monthlySalary > 0:
            string = string + f"monthly salary of {self.monthlySalary}"
        if self.contractHoursWorked > 0:
            string = string + f"contract of {self.contractHoursWorked} hours at {self.contractRate}/hour"
        if self.numberOfCommissionContracts >= 1:
            string = string + f" and receives a commission for {self.numberOfCommissionContracts} contract(s) at {self.commission}/contract."
        if self.commission > 0 and self.numberOfCommissionContracts == 0:
            string = string + f" and receives a bonus commission of {self.commission}."
        if self.commission == 0 and self.numberOfCommissionContracts == 0:
            string = string + "."

        string = string + f"  Their total pay is {self.finalPay}."
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', monthlySalary=4000)
billie.get_pay()
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contractHoursWorked=100, contractRate=25)
charlie.get_pay()
print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', monthlySalary=3000, numberOfCommissionContracts=4, commission=200)
renee.get_pay()
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', contractHoursWorked=150, contractRate=25, commission=220, numberOfCommissionContracts=3)
jan.get_pay()
print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', monthlySalary=2000, commission=1500)
robbie.get_pay()
print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contractHoursWorked=120, contractRate=30, commission=600)
ariel.get_pay()
print(str(ariel))
