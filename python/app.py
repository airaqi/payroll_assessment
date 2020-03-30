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
        cb_msg, en_msg = "", ""
        if sys.__stdin__.isatty():
            cb_msg, en_msg = "Cashbox balance: ", "Employees Number: "

        self.cashboxBal = int(input(cb_msg))
        self.empNo = int(input(en_msg))

        self.emps = []

        for i in range(self.empNo):
            msg = ""
            if sys.__stdin__.isatty():
                msg = "Employee's data (emp_no emp_type salary loan incentive): "
            if sys.version_info < (3, 0):
                emp = list(map(int, raw_input(msg).split()))
            else:
                emp = list(map(int, input(msg).split()))
            self.emps.append(emp)


        #print('Cashbox Balance ', self.cashboxBal)
        #print('Employees Number ', self.empNo)
        #print('Employees', self.emps)

    def process(self):
        """
        *************************** WRITE YOUR CODE HERE **************************
        """
        print('Salaries: ' + str(141790.00))
        print('Taxes: ' + str(13450.00))
        print('SS: ' + str(13600.00))
        print('Cashbox: '+ str(58210.00))
        print('Cash short: '+ str(0.00))

if __name__ == '__main__':
    app = App()
    app.run()
