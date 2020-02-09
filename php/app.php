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

    public  $no_of_emps;
    public  $cashbox_bal;
    public $emps = [];
    public  $data;
	
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
		
		
		 $this->data['cashbox_bal'] = $cashbox_bal;
		 $this->data['no_of_emps'] = $no_of_emps;
		 $this->data['emps'] = $emps;
			
		
    }

    /**
     * Process calculations
     */
    function process() {
		 
		  $salaries=0.0;
		  $tax_rate;$total_social_security=0.0;
		  $total_taxes=0;$incentives=0;$cashbox;
		   // get number of employees and cashbox balanc and all employess' data
		  $no_of_emps=  $this->data['no_of_emps'];
		  $cashbox_bal= $this->data['cashbox_bal'];
		  $emps_object= $this->data['emps']; //employee_id employee_type salary loan incentive
		
	
	foreach($emps_object as $single_employee):
	$employe_input_array = explode(" ", $single_employee); // convert employee data into array for further manipulations
	$emp_id=$employe_input_array[0]; // employee id
	$job_type=$employe_input_array[1]; // employee type
	$emp_salary=$employe_input_array[2]; // emplyee salary
	
	if( $job_type == 1 || $job_type == 2)://apply Incentive for regular and partime 
	$incentives = (isset($employe_input_array[4]) ? $employe_input_array[4] : 0.0); // employee Incentive
	endif;
	
	//social security calculations
    $social_security=$this->getEmpSS($job_type,$emp_salary);
	if($social_security)	:
	$total_social_security += $social_security;
	endif;
	
	
	//Tax Rate
	$tax_rate=$this->getTaxRate ($job_type,$emp_salary);
	
	
	//Taxes = (salary - Social Security, Employee share + Incentives) * Tax Rate		  
	$tax=($emp_salary-$social_security+$incentives)*$tax_rate;
	$total_taxes+=$tax;
	
	$salaries+=$emp_salary; //accumulate all the salaries
	$cash_short = ($cashbox_bal > $salaries) ? 0.0 : abs($salaries-$cashbox_bal); // Cash Short
	endforeach;
    $cashbox= $cashbox_bal - $salaries;
	$this->getResult($cashbox,$salaries,$total_taxes,$total_social_security,$cash_short);

	
}


function getEmpSS($job_type,$emp_salary){
	$social_security=0;
	if($job_type == 1):
	$social_security_employe= floatval((14 / 100) * $emp_salary);
	$social_security_company=floatval((26 / 100) * $emp_salary);
	$social_security = floatval($social_security_company + $social_security_employe); 
	endif;
	return $social_security;
}


function getTaxRate ($job_type,$emp_salary){
	switch( $job_type == 1 ||$job_type == 2 ){
	case($emp_salary <= 7000 ):
	$tax_rate=0;
	break;
	
	case ( 7000 < $emp_salary  && $emp_salary <= 10000 ):
	$tax_rate=0.05;
	break;
	
	case (10000 < $emp_salary  && $emp_salary <= 50000 ):
	$tax_rate=0.075;
	break;
	
	case ($emp_salary > 50000 ):
	$tax_rate=0.1;
	break;
	
	default:
	$tax_rate=0;
	break;
	}
	return $tax_rate;
	
}


function getResult($cashbox,$salaries,$total_taxes,$total_social_security,$cash_short){
	
	echo"\n\n";
	echo "***********************";
	echo "\n\n";
	echo "Salaries : ". $salaries ."\n";
	echo "Taxes : ". $total_taxes ."\n";
	echo "SS : ". $total_social_security ."\n";
	echo "Cashbox : ". $cashbox ."\n";   
	echo "Cash short : ". $cash_short ."\n";   
}
}

$app = new App();
$app->run();

?>
