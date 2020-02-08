<?php
declare(strict_types=1);

use PHPUnit\Framework\TestCase;
require_once 'app.php';

class ProcessTest extends TestCase
{ 
private $app;
 
   public function setUp() :void 
    {
        $this->app = new App();
    }
  
   public function testEmpSS()
    {
        $result = $this->app->getEmpSS(1, 9000);
        $this->assertEquals(3600, $result);
    }

	public function testTaxRate()
    {
        $result = $this->app->getTaxRate(1, 9000);
        $this->assertEquals(0.05, $result);
    }
	
   
   
}