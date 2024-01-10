<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
  <title>Hardware dolgozat</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 20px;
    }

    h1 {
      text-align: center;
      color: #333;
    }

    form {
      max-width: 500px;
      margin: 0 auto;
      background-color: #fff;
      padding: 20px;
      border-radius: 5px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    p {
      margin-top: 0;
    }

    input[type="text"],
    textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
      resize: vertical;
    }

    input[type="submit"] {
      background-color: #4CAF50;
      color: #fff;
      padding: 10px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }

    input[type="submit"]:hover {
      background-color: #45a049;
    }

    img {
      width:50%;
      height:auto;
      margin:auto;
    }
  </style>
</head>
<body>
  <h1>Hardware alapismeretek dolgozat</h1>
  <form action="submit.php" method="POST">
    <p>Vezetéknév</p>
    <input type="text" name="vnev" required><br>
    <p>Keresztnév</p>
    <input type="text" name="knev" required><br>
    
    <label for="osztaly">Osztály:</label>
      <input list="osztalyok" id="osztaly" name="osztaly" required>
      <datalist id="osztalyok">
          <option value="9akny">
          <option value="9bkny">
      </datalist>

    <br>
    <br>
    <br>

    <hr>

    <p>1. Adj meg 3 példát a hardware-re. /3</p>
    <input type="text" name="1kerdes01"><br>
    <input type="text" name="1kerdes02"><br>
    <input type="text" name="1kerdes03"><br>

    <hr>

    <p>2. Mi az a periféria? (1-2 mondatban add meg saját szavaiddal) /2</p>
    <textarea name="2kerdes" rows="2" cols="30" ></textarea><br>

    <hr>

    <p>3. Mit rövidít a RAM? /1</p>
    <input type="text" name="3kerdes" ><br>

    <hr>

    <p>4. Mi a különbség a software és a hardware között? /2</p>
    <textarea name="4kerdes" rows="3" cols="30" ></textarea><br>

    <hr>

    <p>5. Mit látsz a képen? /3</p>
    <p>a. <img src="res/01.jpg"></p>
    <input type="text" name="5kerdes01" ><br>
    <p>b. <img src="res/02.jpg"></p>
    <input type="text" name="5kerdes02" ><br>
    <p>c. <img src="res/03.jpg"></p>
    <input type="text" name="5kerdes03" ><br>

    <hr>

    <p>6. Mi a különbség az SSD és a HDD között? /3</p>
    <textarea name="6kerdes" rows="2" cols="30" ></textarea><br>

    <hr>

    <p>7. A PSU minek a rövidítése? /1</p>
    <input type="text" name="7kerdes" ><br>

    <hr>

    <p>8. Miért hívjuk felejtő memóriának is a RAM-ot? /2</p>
    <textarea name="8kerdes" rows="3" cols="30" ></textarea><br>

    <hr>

    <p>9. Add meg, hogy a képen látható periféria kimeneti, bemeneti vagy mindkettő. (Ha nem vagy biztos benne akkor írj egy rövid magyarázatot szerinted miért az.) /4</p>
    <p>a. <img src="res/eger.jpg"></p>
    <input type="text" name="9kerdes01" ><br>
    <p>b. <img src="res/nyomtato.jpg"></p>
    <input type="text" name="9kerdes02" ><br>
    <p>c. <img src="res/tablet.jpg"></p>
    <input type="text" name="9kerdes03" ><br>
    <p>d. <img src="res/kontroller.jpg"></p>
    <input type="text" name="9kerdes04" ><br>

    <hr>

    <p>10. Sorolj fel 3 fajta ROM-ot (adattároló eszközök). /3</p>
    <input type="text" name="10kerdes01" ><br>
    <input type="text" name="10kerdes02" ><br>
    <input type="text" name="10kerdes03" ><br>

    <hr>

    <p>11. Mit hívunk a számítógép agyának? /1</p>
    <input type="text" name="11kerdes" ><br>

    <hr>

    <p>12. Most szeretnénk egy új számítógépet venni és nagyon fontos, hogy gyors legyen. Milyen adattárolót javasolsz? (1-2 mondatban magyarázd meg, miért pont azt) /2</p>
    <textarea name="12kerdes" rows="3" cols="30" ></textarea><br>

    <hr>

    <p>13. Számítógép fejlesztés előtt állunk, mert a jelenlegi gép már nem tudja futtatni a mostani játékokat, de még a videó lejátszásnál is gyengén teljesít. Mit javasolsz, mit fejlesszünk a gépben? (1-2 mondatban magyarázd meg, miért pont azt) /2</p>
    <textarea name="13kerdes" rows="3" cols="30" ></textarea><br>

    <hr>

    <p>+1. Teljesen nulláról szeretnénk egy számítógépet építeni. Add meg milyen eszközökre lesz szükségünk, hogy müködő gépet tudjunk összerakni. (Minden eszköz mellé másolj be egy linket, hogy honnan érdemes megvenni az adott komponenst.) /5</p>
    <textarea name="14kerdes" rows="3" cols="30" ></textarea><br>

    <hr>

    <br>
    <p>Összesen elérhető pontszám: 34</p>
    <p>Csak akkor pipáld be, ha végeztél minden feladattal. <input type="checkbox" required></p>
    
    <br>
    <input type="submit" value="Dolgozat leadása">
    </form>
</body>
</html>
