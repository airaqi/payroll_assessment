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
        pass

if __name__ == '__main__':
    app = App()
    app.run()
