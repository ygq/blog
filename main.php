<?php
	$rec_file = 'data/db';
	if($_GET['type'] == 'read'){
		$file_pointer = fopen($rec_file,'r');
		$file_read = fread($file_pointer, filesize($rec_file));
		fclose($file_pointer); 
		echo $file_read;
	}
	if($_GET['type'] == 'write'){
	    $_GET['art_name'];
		$art_list = array("art_name" => $_GET['art_name'],"art_author" => $_GET['art_author'],"art_content" => $_GET['art_content'], "time"=>date('Y-m-d H:i:s',time()));
		if($_GET['art_name'] != null){
			$file_pointer = fopen($rec_file,'a');
			fwrite($file_pointer,json_encode($art_list).'__a__');
			fclose($file_pointer);
		}
	}
?>
