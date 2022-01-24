#ifndef GRADIENTS_H
#define GRADIENTS_H

char webpage123[] = R"=====(
<html>
<head>
  <script>
    var Socket;
    function init() {
      Socket = new WebSocket('ws://' + window.location.hostname + ':81/');
      Socket.onmessage = function(event){
         console.log(event.data);
      }
    }

    function sendBrightness() {
      console.log("jasność costam");
      Socket.send("VB" + document.getElementById("brightness").value);
    }
    function chooseDisable() {
      Socket.send("Edisable");
    }
    function chooseTrain() {
      console.log("pociag costam");
      Socket.send("Etrain");
    }
    function chooseRainbow() {
      Socket.send("Erainbow");
    }
    function chooseRainbow2() {
      Socket.send("Erainbow2");
    }
    function chooseBounce() {
      Socket.send("Ebounce");
    }
    function chooseTrain2() {
      Socket.send("Etrain2");
    }
    function chooseStaticColor() {
      Socket.send("Estatic");
    }
    function chooseRain() {
      Socket.send("Erain");
    }
    function chooseFire() {
      Socket.send("Efire");
    }
    function chooseStroboscop() {
      Socket.send("Estroboscop");
    }
    function chooseGradientMoving() {
        var x = document.getElementById("gradientMovingChoose").value;
        Socket.send("Egradientmoving" + x);
    }
    function chooseGradientMusic() {
      Socket.send("Egradientmusic");
    }
    function chooseFullColor() {
      Socket.send("Efullcolor");
    }
    function chooseFullColor2() {
      Socket.send("Efullcolor2");
    }
    function sendSpeed() {
      Socket.send("VS" + document.getElementById("speed").value);
    }
    function ChangeBounceColor() {
      Socket.send("VCB" + document.getElementById("favcolor").value);
    }
    function ChangeStaticColor() {
      Socket.send("VCS" + document.getElementById("favcolor").value);
    }
  </script>
</head>
<body onload="javascript:init()">
  <div>
    <input type="button" value="Disable" id="disable" onclick="chooseDisable();" />
  </div>
  <hr/>
  <div>
    <input type="button" value="Train" id="rainbow" onclick="chooseTrain();" />
  </div>
  <hr/>
  <div>
    <input type="button" value="Rainbow" id="rainbow" onclick="chooseRainbow()" />
  </div>  
  <hr/>
  <div>
    <input type="button" value="Bounce" id="bounce" onclick="chooseBounce()" />
  </div>  
    <hr/>
  <div>
    <input type="button" value="Train 2" id="train2" onclick="chooseTrain2()" />
  </div>
  <hr/>
  <div>
    <input type="button" value="StaticColor" id="staticColor" onclick="chooseStaticColor()" />
  </div>
  <hr/>
  <div>
    <input type="button" value="Rainbow2" id="rainbow2" onclick="chooseRainbow2()" />
  </div>
  <hr/>
  <div>
    <input type="button" value="Rain" id="rain" onclick="chooseRain()" />
  </div>
  <hr/>
  <div>
    <input type="button" value="Fire" id="fire" onclick="chooseFire()" />
  </div>
  <hr/>
  <div>
    <input type="button" value="Stroboscop" id="stroboscop" onclick="chooseStroboscop()" />
  </div>
  <hr/>
  <div>
    <input type="button" value="GradientMoving" id="GradientMoving" onclick="chooseGradientMoving()" />
    <select id="gradientMovingChoose">
        <option value="sunset">Sunset</option>
        <option value="nether">Nether</option>
        <option value="rgb">RGB</option>
        <option value="redblue">Red Blue</option>
      </select>
  </div>
  <hr/>
  <div>
    <input type="button" value="GradientMusic" id="GradientMusic" onclick="chooseGradientMusic()" />
  </div>
  <hr/>
  <div>
    <input type="button" value="FullColor" id="fullColor" onclick="chooseFullColor()" />
  </div>
  <hr/>
  <div>
    <input type="button" value="FullColor2" id="fullColor2" onclick="chooseFullColor2()" />
  </div>    



  <hr/>
  <div>
    <input type="range" min="1" max="255" value="123" id="brightness" onchange="sendBrightness()" />
  </div>
  <hr/>
  <div>
    <input type="range" min="0" max="100" value="50" id="speed" onchange="sendSpeed()" />
  </div>
  <hr/>
  <div>
    <input type="color" id="favcolor" name="favcolor" value="#ff0000" />
  </div>
  <hr/>
  <div>
    <input type="button" value="Submit" id="sumbit" onclick="ChangeBounceColor()" />
  </div>
  <hr/>
  <div>
    <input type="button" value="Submit2" id="sumbit2" onclick="ChangeStaticColor()" />
  </div>
</body>
</html>
)=====";;

#endif