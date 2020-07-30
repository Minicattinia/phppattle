<?php

$url = "";
$data = "";
$mr = curl_init();
curl_setopt_array($mr, array(
	CURLOPT_PORT => 
	CURLOPT_URL =>
	CURLOPT_HTTPHEADER => 
	CURLOPT_RETURNTRANSFER =>
	CURLOPT_SSL_VERIFYPEER =>
	CURLOPT_TIMEOUT =>
	CURLOPT_CUSTOMREQUEST =>
	CURLOPT_POSTFIELDS =>
));

$neko = curl_exec($mr);
curl_close($mr)
$js = json_decode($neko,true);
echo ""
sleep(5);
