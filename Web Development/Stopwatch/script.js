const start=document.getElementById("start");
const stop=document.getElementById("stop");
const reset=document.getElementById("reset");
const time=document.getElementById("time");
var hr=00;
var min=00;
var sec=00;
var ms=00;
reset.onclick=function(){
    time.textContent="00:00:00:00";
    hr=00;
    min=00;
    sec=00;
    ms=00;
    isrun=false;
    start.textContent="Start";
    start.style.display="inline-block";
    stop.style.display="none";
}
var isrun=false;
stop.onclick=function(){
    isrun=false;
    start.textContent="Resume";
    start.style.display="inline-block";
    stop.style.display="none";
}

function count(){
    if(isrun==true){
        ms=ms+1
        if (ms>99){
            ms=00;
            sec=sec+1;
        }
        if (sec>59){
            sec=00;
            min=min+1;
        }
        if (min>59){
            min=00;
            hr=hr+1;
        }
        ms=String(ms).padStart(2,"0");
        sec=String(sec).padStart(2,"0");
        min=String(min).padStart(2,"0");
        hr=String(hr).padStart(2,"0");
        time.textContent=`${hr}:${min}:${sec}:${ms}`;
        ms=Number(ms),sec=Number(sec),min=Number(min),hr=Number(hr);
    }
}
start.onclick=function(){
    isrun=true;
    setInterval(count,10);
    stop.style.display="inline-block";
    start.style.display="none";
}
