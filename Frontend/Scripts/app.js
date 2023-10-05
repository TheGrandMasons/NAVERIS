var mainsection = document.getElementById("main")
var mapbtn = document.getElementById("mapBtn")
var mapsection = document.getElementById("mapSection")

  
mapbtn.addEventListener('click', function() {
  console.log("confirmito2");
  mapsection.style.display = 'flex';
  mapsection.scrollIntoView({ behavior: 'smooth' }); 
  
});

