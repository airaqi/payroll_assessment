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

        """for i in range(self.empNo):
            msg = "Employee's data (emp_no emp_type salary loan incentive): "
            if sys.version_info < (3, 0):
                emp = list(map(int, raw_input(msg).split()))
            else:
                emp = list(map(int, input(msg).split()))
            self.emps.append(emp)"""

        self.emps=[[1, 1, 5000, 5000, 300], [2, 1, 9000, 0, 1000], [3, 1, 20000, -400, 0], [4, 2, 10000, 0, 100], [5, 3, 110000, 0, 0]]
        print('Cashbox Balance ', self.cashboxBal)
        print('Employees Number ', self.empNo)
        print('Employees', self.emps)

    def process(self):
        salary,sum_salary,loan,sse,ssc,tax,ss,net,incentive=0,0,0,0,0,0,0,0,0
        tax_1,tax_2,tax_3,tax_4=0,5,7.5,10
        Regular=1
        Part_timer=2
        Freelancer=3
        for emp in self.emps:
           salary=abs(emp[2])
           sum_salary+=salary
           
           
           if emp[1]==Regular:
             sse+=salary*.14
             ssc+=salary*.26
             loan +=emp[3]
           if emp[1]==Regular or emp[1]==Part_timer:
               incentive+=abs(emp[4])
           if salary<=7000:
                   tax+=salary*(tax_1/100)
           elif 7000<salary<=10000:
                   tax+=salary*(tax_2/100)
           elif 10000<salary<=50000:
                   tax+=salary*(tax_3/100)
           elif 50000<salary:
                   tax+=salary*(tax_4/100)
               
               
        ss=sse+ssc
        net=sum_salary+loan+incentive+ssc-ss-tax   
        print("Salaries   :  "+str(net))
        
        print("Taxes   :   "+str(tax))
        print("SS   :   "+str(ss))
        print("Cashbox :   "+str(self.cashboxBal-net))
        print("cash  short "+str(net-self.cashboxBal) if net>self.cashboxBal else 'cash  short :0' )
         
         

if __name__ == '__main__':
    app = App()
    app.run()
    
     
    
