<?php
    // Retrieve form data
    $vnev = $_POST['vnev'];
    $knev = $_POST['knev'];
    $osztaly = $_POST['osztaly'];

    $egykerdes01 = $_POST['1kerdes01'];
    $egykerdes02 = $_POST['1kerdes02'];
    $egykerdes03 = $_POST['1kerdes03'];

    $kettokerdes = $_POST['2kerdes'];
    $haromkerdes = $_POST['3kerdes'];
    $negykerdes = $_POST['4kerdes'];

    $otkerdes01 = $_POST['5kerdes01'];
    $otkerdes02 = $_POST['5kerdes02'];
    $otkerdes03 = $_POST['5kerdes03'];

    $hatkerdes = $_POST['6kerdes'];
    $hetkerdes = $_POST['7kerdes'];
    $nyolckerdes = $_POST['8kerdes'];

    $kilenc01 = $_POST['9kerdes01'];
    $kilenc02 = $_POST['9kerdes02'];
    $kilenc03 = $_POST['9kerdes03'];
    $kilenc04 = $_POST['9kerdes04'];

    $tiz01 = $_POST['10kerdes01'];
    $tiz02 = $_POST['10kerdes02'];
    $tiz03 = $_POST['10kerdes03'];

    $tizenegy = $_POST['11kerdes'];
    $tizenketto = $_POST['12kerdes'];
    $tizenharom = $_POST['13kerdes'];
    $tizennegy = $_POST['14kerdes'];

    // Create the text content
    $content = "Vezetéknév: $vnev\nKeresztnév: $knev\nOsztály: $osztaly\n
    1.kérdés a): $egykerdes01\n1.kérdés b): $egykerdes02\n1.kérdés c): $egykerdes03\n
    2.kérdés: $kettokerdes\n3.kérdés: $haromkerdes\n4.kérdés: $negykerdes\n
    5.kérdés a): $otkerdes01\n5.kérdés b): $otkerdes02\n5.kérdés c): $otkerdes03\n
    6.kérdés: $hatkerdes\n7.kérdés: $hetkerdes\n8.kérdés: $nyolckerdes\n
    9.kérdés a): $kilenc01\n9.kérdés b): $kilenc02\n9.kérdés c): $kilenc03\n9.kérdés d): $kilenc04\n
    10.kérdés a): $tiz01\n10.kérdés b): $tiz02\n10.kérdés c): $tiz03\n
    11.kérdés: $tizenegy\n12.kérdés: $tizenketto\n13.kérdés: $tizenharom\n14.kérdés: $tizennegy";

    // Define the file path and name
    $file_path = '/var/www/html/dolgozat/' . $osztaly . '/';
    $file_name = $vnev . ' ' . $knev . '.txt';
    $file = $file_path . $file_name;

    // Save data to the text file
    if (!file_exists($file_path)) {
        mkdir($file_path, 0777, true); // Create the uploads directory if it doesn't exist
    }

    if (file_put_contents($file, $content) !== false) {
        //echo "Data saved successfully to $file<br>";

        // Upload the text file to the server
        $target_dir = '/var/www/html/dolgozat/' . $osztaly . '/'; // Replace with the actual destination directory
        $target_file = $target_dir . $file_name;

        if (move_uploaded_file($file, $target_file)) {
            echo "<!DOCTYPE html>
            <html>
            <head>
              <title>Feedback Page</title>
              <style>
                body {
                  background-color: #f4f4f4;
                  font-family: Arial, sans-serif;
                  margin: 0;
                  padding: 0;
                }
                
                .container {
                  max-width: 600px;
                  margin: 50px auto;
                  background-color: #fff;
                  border-radius: 5px;
                  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                  padding: 20px;
                }
                
                h1 {
                  color: #333;
                  text-align: center;
                }
                
                p {
                  color: #666;
                  line-height: 1.5;
                }
                
                .feedback {
                  border: 1px solid #ccc;
                  background-color: #f9f9f9;
                  padding: 10px;
                  margin-top: 20px;
                  border-radius: 5px;
                  font-size: 18px;
                  color: #333;
                }
              </style>
            </head>
            <body>
              <div class='container'>
                <h1>Hardware alapismeretek dolgozat</h1>
                
                <div class='feedback'>
                  <p>Sikeres dolgozat leadás.</p>
                </div>
              </div>
            </body>
            </html>";
        } else {
            echo "<!DOCTYPE html>
            <html>
            <head>
              <title>Feedback Page</title>
              <style>
                body {
                  background-color: #f4f4f4;
                  font-family: Arial, sans-serif;
                  margin: 0;
                  padding: 0;
                }
                
                .container {
                  max-width: 600px;
                  margin: 50px auto;
                  background-color: #fff;
                  border-radius: 5px;
                  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                  padding: 20px;
                }
                
                h1 {
                  color: #333;
                  text-align: center;
                }
                
                p {
                  color: #666;
                  line-height: 1.5;
                }
                
                .feedback {
                  border: 1px solid #ccc;
                  background-color: #f9f9f9;
                  padding: 10px;
                  margin-top: 20px;
                  border-radius: 5px;
                  font-size: 18px;
                  color: #333;
                }
              </style>
            </head>
            <body>
              <div class='container'>
                <h1>Hardware alapismeretek dolgozat</h1>
                
                <div class='feedback'>
                  <p>Sikeres dolgozat leadás.</p>
                </div>
              </div>
            </body>
            </html>";
        }
    } else {
        echo "Error saving data to $file";
    }
   
?>