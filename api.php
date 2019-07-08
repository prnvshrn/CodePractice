<?php
   $service_url = 'https://cat-fact.herokuapp.com/facts';
   $curl = curl_init($service_url);
   curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
   //curl_setopt($curl, CURLOPT_POST, false);
   curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
   $curl_response = curl_exec($curl);
   curl_close($curl);
   $json_objekat=json_decode($curl_response);
   //echo $json_objekat->all[0]->text;
   foreach($json_objekat->all as $item) { //foreach element in $arr
    //$uses = $item['text']; //etc
    print $item->text;
}
?>