function getRandomInt() {
    min = Math.ceil(10);
    max = Math.floor(1000);
    var rand = Math.floor(Math.random() * (max - min + 1)) + min;
    return rand;
  }
window.addEventListener('load',initialize,false); 
function initialize(){
  
  document.getElementById("square").addEventListener('mouseover',function(e){ 
    
    var left = window.getComputedStyle(e.target).getPropertyValue("left"); 
    var right = window.getComputedStyle(e.target).getPropertyValue("right"); 
    var top = window.getComputedStyle(e.target).getPropertyValue("top");
    var bottom = window.getComputedStyle(e.target).getPropertyValue("bottom");
    
    var coordinates1 = [left, right, top, bottom]; 
    left = parseInt(left, 10); 
    right = parseInt(right, 10);
    top = parseInt(top, 10);
    bottom = parseInt(bottom, 10);
    
    moveSquare(left, right
      , top, bottom, 10, coordinates1) 
  }, false); 
} 

function moveSquare(left2, right2
      , top2, bottom2,numMoves, coordinates1) { 

  
  var left2 = getRandomInt();
  var right2 = getRandomInt();
  var top2 = getRandomInt();
  var bottom2 = getRandomInt();

  var coordinates2 = [left2, right2, top2, bottom2];
  console.log(coordinates1);
  console.log(coordinates2);
  
  document.getElementById("square").style.left = left2 + "px";
  
  document.getElementById("square").style.right = right2 + "px";
  
  document.getElementById("square").style.top = top2 + "px";
  
  document.getElementById("square").style.bottom = bottom2 + "px";

  function trig(){

      

  }
  document.getElementById("square").style.transform = "rotate" + "(30deg)";
  document.getElementById("square").style.transition = "all 2s";
  
  if (numMoves > 0) { 
    numMoves--;

    left2++;
    right2++;
    top2++;
    bottom2++; 

    //setTimeout(moveSquare,1000,left,right,top,bottom,numMoves); 

  } else { 
    return; 
  } 
} 