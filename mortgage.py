import pandas as pd
from sympy.solvers import solve
from sympy import Symbol
class Mortgage:
    def __init__(self,
             principal=250000,
             rate=0.045,
             period=12,
             years=30):
        self.principal=principal
        self.r=rate/period
        self.period=period
        self.years=years
        self.n=self.years*self.period
        
    def payments(self, principal=None):
        if principal == None:
            principal=self.principal
        return principal*(self.r+self.r/((1+self.r)**(self.n)-1))

    def schedule(self):
        schedule=[]
        balance=self.principal
        payments=self.payments()
        for i in range(self.n):
            interest_paid = balance*self.r
            principal_paid = payments-interest_paid
            balance=balance-principal_paid
            schedule.append(dict(
                            month=i+1,
                            interest=round(interest_paid,2),
                            principal=round(principal_paid,2),
                            balance=round(balance,2)            
                            ))
        return pd.DataFrame(schedule)
    def total_interest(self):
        return x.schedule()['interest'].sum()

    def get_max_principal(self, max_pay=5000):
        p = Symbol('p')
        return solve(self.payments(p)-max_pay, p)[0]
