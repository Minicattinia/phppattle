<?php

$url = "https://dogecoins.club/doge/claim.php";
$headers = " [
	authority: dogecoins.club
	:method: POST
	:path: /doge/claim.php
	:scheme: https
	accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
	accept-encoding: gzip, deflate, br
	accept-language: en-US,en;q=0.9
	cache-control: max-age=0
	content-length: 77
	content-type: application/x-www-form-urlencoded" ];
$data = "cookie: __cfduid=ddee25f484ddee1847b5cf90a107b8b131595997450; _ga=GA1.2.1420432736.1595997451; PHPSESSID=8onfeun1eelgvug88fi95seqj7; _gid=GA1.2.1643832765.1596092160; DOGEToken=79QepLLw4XIaW3BBuoierFFg1ncP2uLT; DOGEtokensecur=VTJGc2RHVmtYMThUTkNET3pTbmoyYlhnV3pHUGdEOUpHWGF6azR2b3M4UT0=";
$mr = curl_init();
curl_setopt_array($mr, array(
	CURLOPT_PORT => "443",
	CURLOPT_URL => "$url",
	CURLOPT_HTTPHEADER => "$header",
	CURLOPT_RETURNTRANSFER => true,
	CURLOPT_SSL_VERIFYPEER => false,
	CURLOPT_TIMEOUT => 15,
	CURLOPT_CUSTOMREQUEST => "POST",
	CURLOPT_POSTFIELDS => $data,
));

$neko = curl_exec($mr);
curl_close($mr)
$js = json_decode($neko,true);
echo ""
sleep(60);
