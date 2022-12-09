
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
    console.log("pociasg costam");
    Socket.send("Etrain");
}
function chooseTV() {
    console.log("telewizor efekt");
    Socket.send("Etv");
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
    // Socket.send("VCB" + document.getElementById("favcolor").value);
    console.log("VCB" + document.getElementById("favcolor").value)
}
function ChangeStaticColor() {
    Socket.send("VCS" + document.getElementById("favcolor").value);
}
function EnableTimer() {
    Socket.send("VTS" + document.getElementById("clocl").value);
}
function DisableTimer() {
    Socket.send("VTD");
}