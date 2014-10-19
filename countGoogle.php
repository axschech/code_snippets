<?php

$str = file_get_contents('http://google.com');

$pattern = '/Google|google/';

preg_match_all($pattern, $str, $matches);

$ret = "Google appears ".count($matches[0])." many times in the source of http://google.com\n";

print_r($ret);

?>