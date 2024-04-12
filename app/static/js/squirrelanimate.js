function getRandomInt() {
    min = Math.ceil(10);
    max = Math.floor(2000);
    var rand = Math.floor(Math.random() * (max - min + 1)) + min;
    return rand;
  }
window.addEventListener('load',initialize,false); 
function initialize(){
  
  document.getElementById("squirrel").addEventListener('mouseover',function(e){ 
    
    var left = window.getComputedStyle(e.target).getPropertyValue("left"); 
    var right = window.getComputedStyle(e.target).getPropertyValue("right"); 
    var top = window.getComputedStyle(e.target).getPropertyValue("top");
    var bottom = window.getComputedStyle(e.target).getPropertyValue("bottom");
    
    
    left = parseInt(left, 10); 
    right = parseInt(right, 10);
    top = parseInt(top, 10);
    bottom = parseInt(bottom, 10);

    var coordinates1 = [left, right, top, bottom]; 

    moveSquirrel(left, right
      , top, bottom, 10, coordinates1) 
  }, false); 
} 

function moveSquirrel(left2, right2
      , top2, bottom2,numMoves, coordinates1) { 

  
  var left2 = getRandomInt();
  var right2 = getRandomInt();
  var top2 = getRandomInt();
  var bottom2 = getRandomInt();

  var coordinates2 = [left2, right2, top2, bottom2];

  console.log(coordinates1);
  console.log(coordinates2);
  
  document.getElementById("squirrel").style.left = left2 + "px";
  document.getElementById("squirrel").style.right = right2 + "px";
  document.getElementById("squirrel").style.top = top2 + "px";
  document.getElementById("squirrel").style.bottom = bottom2 + "px";

  var direction = trig(coordinates1, coordinates2);

  function trig(coordinates1, coordinates2){

    var dis_vec =  Math.pow(coordinates2[0] - coordinates1[0], 2)+ Math.pow(coordinates2[1] - coordinates1[1], 2) + Math.pow(coordinates2[2] - coordinates1[2], 2) + Math.pow(coordinates2[3] - coordinates1[3], 2);
    var arc_tan = Math.atan((coordinates2[1] - coordinates1[1])/(coordinates2[0] - coordinates1[0]));
    var unit_vec = dis_vec / Math.sqrt(dis_vec);

    console.log(arc_tan, unit_vec);
    return arc_tan;

      

  }
  
  console.log(Math.round(direction))

  document.getElementById("squirrel").style.transform = "rotate" + "("+ Math.round(direction) +"deg)";
  document.getElementById("squirrel").style.transition = "all 2s";
  
  if (numMoves > 0) { 
    numMoves--;

    left2++;
    right2++;
    top2++;
    bottom2++; 

  } else { 
    return; 
  } 
} 