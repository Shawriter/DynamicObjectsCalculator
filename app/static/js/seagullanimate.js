
window.addEventListener('load',initialize,false);

var isMouseDown = false;

function initialize(){

  var screenWidth = document.documentElement.clientWidth;
  console.log(screenWidth);

  var addContentBody = document.getElementById("add_content_body");
  var seagull = document.getElementById("seagull");

  addContentBody.addEventListener('mouseover',function(e){ 
    
   
        var mouseX = e.clientX; 
        var mouseY = e.clientY
        //console.log("mouseX: " + mouseX);
        var coordinates1 = [mouseX, mouseY]; 
        moveSeagull(coordinates1, screenWidth);
        
},false);
addContentBody.addEventListener('mousedown',function(e){ 
    
    isMouseDown = true; 
    var loop = setInterval(function() {
      if (!isMouseDown) { 
        clearInterval(loop);
      } else {
        
        seagull.style.left = 10000 + "px";
        seagull.style.top = 10000 + "px";
      }
    }, 100);
    
},false);

addContentBody.addEventListener('mouseup',function(e){ 
    isMouseDown = false;
  },false);

function moveSeagull(coordinates1) { 

  
    var coordinates2 = [coordinates1[0], coordinates1[1]];
    console.log(coordinates1);
    console.log(coordinates2);
    var left2 = coordinates1[0];
    var top2 = coordinates1[1];
    seagull.style.left = left2 + "px";
    seagull.style.top = top2 + "px";

  }
  
  
  document.getElementById("seagull").style.transition = "all 3s";
}

