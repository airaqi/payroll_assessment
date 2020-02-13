import sys

class App:
    """
    ***************************************
    DON'T CHANGE THIS FUNCTION 
    ***************************************
    Main application class
    """
    def run(self):
        """
        ***************************************
        DON'T CHANGE THIS FUNCTION 
        ***************************************
        Initial exeuction point
        """
        self.readinput()
        self.process()

    def readinput(self):
        """
        ***************************************
        DON'T CHANGE THIS FUNCTION 
        ***************************************
        Reads input from file
        """
        self.cashboxBal = int(input("Cashbox balance: "))
        self.empNo = int(input("Employees Number: "))
        self.emps = []

        for i in range(self.empNo):
            msg = "Employee's data (emp_no emp_type salary loan incentive): "
            if sys.version_info < (3, 0):
                emp = list(map(int, raw_input(msg).split()))
            else:
                emp = list(map(int, input(msg).split()))
            self.emps.append(emp)


        print('Cashbox Balance ', self.cashboxBal)
        print('Employees Number ', self.empNo)
        print('Employees', self.emps)

    def process(self):
        """
        *************************** WRITE YOUR CODE HERE **************************
        """
        typeRegular = 1
        typeParttimer = 2
        typeFreelancer = 3
        # employee_id employeeType salary loan incentive
        self.totalSalaries = 0.00
        self.totalTaxes = 0.00
        self.totalSs = 0.00
        self.cashbox = 0.00
        self.cashShort = 0.00

        for emp in self.emps:
            taxRate = 0.00
            tax = 0.00
            sse = 0.00
            ssc = 0.00
            ss = 0.00
            employeeId = emp[0]
            employeeType = emp[1]
            salary = emp[2]
            loan = emp[3]
            incentive = emp[4]
            if int(salary) > 0:
                if employeeType in [typeRegular, typeParttimer]:
                    # Salary (positive number / all)
                    # Tax (float percentage number / Regular and Part timer)
                    if salary <= 7000.00:
                        # 0% below $7000
                        taxRate = 0.00
                    elif salary > 7000.00 and salary <= 10000.00:
                        # 5% above $7000 till $10,000.00
                        taxRate = 0.05
                    elif salary > 10000.00 and salary <= 50000.00:
                        # 7.5% above $10,000.00 till $50,000.00
                        taxRate = 0.075
                    elif salary > 50000.00:
                        # 10% above $50,000.00
                        taxRate = 0.10
                    tax = salary * taxRate
                    # Total amount of taxes
                    self.totalTaxes = self.totalTaxes + tax

                if employeeType == typeRegular:
                    # Social Security (float percentage / Regular)
                    # Employee share is 14% of basic salary
                    sse = salary * 0.14
                    # Company share is 24% of basic salary
                    ssc = salary * 0.26
                    ss = sse + ssc
                    # Total amount of Social security
                    self.totalSs = self.totalSs + ss

                # Net Amount
                netAmount = salary + loan + incentive - tax - sse
                # print(net_amount)
                # Total amount of salaries
                self.totalSalaries = self.totalSalaries + netAmount

        # Cashbox amount after salaries
        remainingCash = self.cashboxBal - self.totalSalaries
        self.cashbox = 0 if remainingCash < 0 else remainingCash

        # Cashbox short amount if any
        self.cashShort = 0 if self.cashbox > 0 else remainingCash

        print("Salaries: {:.2f}".format(self.totalSalaries))
        print("Taxes: {:.2f}".format(self.totalTaxes))
        print("SS: {:.2f}".format(self.totalSs))
        print("Cashbox: {:.2f}".format(self.cashbox))
        print("Cash short: {:.2f}".format(self.cashShort))


if __name__ == '__main__':
    app = App()
    app.run()
