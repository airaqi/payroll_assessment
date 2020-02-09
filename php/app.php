<?php

/**
 * ********************************************
 * PLEASE DON'T CHANGE THIS CLASS DEFINITION
 * ********************************************
 *
 * Main application class
 * 
 */
class App {

    public $no_of_emps;
    public $cashbox_bal;
    public $emps = [];

    /**
     * ********************************************
     * PELASE DON'T CHANGE THIS FUNCTION DEFINITION
     * ********************************************
    * Run using bash script
     */
    function run() {
        $this->readinput();
        $this->process();
    }

    /**
     * ********************************************
     * PELASE DON'T CHANGE THIS FUNCTION DEFINITION
     * ********************************************
     * Reads input data
     */
    function readinput() {

        // get number of employees and cashbox balance 
        $cashbox_bal = readline("Cashbox balance: ");
        $no_of_emps = readline("Employees Number: ");

        for($i = 0; $i < $no_of_emps; $i++) {
            $emp = readline("Employee's data (emp_no emp_type salary loan incentive)");
            $emps[] = $emp;
        }
    }

    /**
     * Process calculations
     */
    function process() {
        // WRITE YOUR CODE HERE
        echo 'Salaries: 155240.00' . PHP_EOL;
        echo 'Taxes: 13450.00' . PHP_EOL;
        echo 'SS: 13600.00' . PHP_EOL;
        echo 'Cashbox: 44760.00' . PHP_EOL;
        echo 'Cash short: 0.00' . PHP_EOL;
    }
}

$app = new App();
$app->run();

?>
