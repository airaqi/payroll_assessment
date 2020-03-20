# Monthly Payroll Assessment

Company employees can be categorized into three categories with their relative ID's as follows:

1. Regular
2. Part timer
3. Freelancer

Payroll calculations are composed of the following categories -  category (data type / employee type applied for):

* Salary (positive number / all)
* Tax (float percentage number / Regular and Part timer)
    * 0% below $7000
    * 5% above $7000 till $10,000.00
    * 7.5% above $10,000.00 till $50,000.00
    * 10% above $50,000.00 
* Social Security (float percentage / Regular)
    * Employee share is 14% for basic salary.
    * Company share is 26% of basic salary.
* Loans (Positive number for request, negative for setlement / Regular)
* Insentives (Positive number / Regular, Part-timer)

## Equations
1. Taxes = (salary - Social Security, Employee share + Incentives) * Tax Rate
2. Social Security
    1. Employee Contribution = Basic salary * 14%
    2. Company Contribution = Basic * 26%
3. Net Amount = salary + loan + incentive - tax - Social Security (Employee Cont.)
4. Cashbox = Cash box - Salaries
5. Cash short = Salaries - Cash box

> Use __sample_data.xlsx__ for full calculation details.

You need to create an application that applys above rules, and print out the following amounts:
* Total amount of salaries
* Total amount of taxes
* Total amount of Social security.
* cashbox amount after salaries
* cashbox short amount if any.

## Inputs
First line you will get N number of employees in first line, and cash box amount available on hand in the second line, then employees data each in separate line which is composed of the following:

```
number_of_employees 
cashbox_amount
employee_id employee_type salary loan incentive
```

## Sample

Below is a sample input:

```
200000
5
1 1 5000 5000 300
2 1 9000 0 1000
3 1 20000 -400 0
4 2 10000 0 100
5 3 110000 0 0
```

Sample output should be:

```
Salaries: 141790.00
Taxes: 13450.00
SS: 13600.00
Cashbox: 58210.00
Cash short: 0.00
```

## Explanation:

Employee 1:
```
Social Security Employee Contribution (sse) = salary * 0.14 
                                            = 5000.00 * 0.14 = 700.00

Social Security Company Contribution (ssc)  = salary * 0.26 
                                            = 5000.00 * 0.14 = 1300.00

Social Security Tatal Amount (ss)           = sse + ssc 
                                            = 700.00 + 1300.00 = 2000.00

Tax                                         = salary * 0 
                                            = 5000.00 * 0 = 0

Net Amount                                  = salary + loan + incentive - tax - sse 
                                            = 5000.00 + 5000.00 + 300.00 - 0.00 - 700.00 = 9600.00
```

Employee 2:
```
Social Security Employee Contribution (sse) = salary * 0.14 
                                            = 9000.00 * 0.14 = 1260.00

Social Security Company Contribution (ssc)  = salary * 0.26 
                                            = 9000.00 * 0.26 = 2340.00

Social Security Tatal Amount (ss)           = sse + ssc 
                                            = 1260.00 + 2340.00 = 3600.00

Tax                                         = salary * 0 
                                            = 9000.00 * 0.05 = 450.00

Net Amount                                  = salary + loan + incentive - tax - sse 
                                            = 9000.00 + 0.00 + 1000.00 - 0.00 - 700.00 = 8290.00
```

## Notes
```
* Select the language that you want to use either php or python
* Don't update any function difinitions in App class
* Run application using provided run.sh script 
* Provide data file to the run.sh script or use default sample.txt
* "run.sh" script attempts to find the sample data file in local directory first, then in data directory.
* Develop unit tests to test your implementation.
* Fork the repository and add a pull request to submit the assignment.
* Use spreadsheets in data directory as a sample data and calculations
```
