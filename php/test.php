<?php
declare(strict_types=1);

use PHPUnit\Framework\TestCase;

class AppTest extends TestCase 
{

    public function data()
    {
        return [
            "data1" => [ 'datain01.txt', 'dataout01.txt' ],
            "data2" => [ 'datain02.txt', 'dataout02.txt']
        ];
    }

    /**
     * @test
     * @dataProvider data
     */

    public function input($datain, $dataout) 
    {
        $current_path = getcwd();
        $data_path = "${current_path}/../data";

        $out = shell_exec("./run.sh ${datain}");
        $read = file_get_contents("${data_path}/${dataout}");
        $this->assertSame($out, $read);
    }
}

?>
