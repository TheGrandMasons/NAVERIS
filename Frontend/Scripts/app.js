var infobtn = document.getElementById("infoBtn")
var infosection = document.getElementById("infoSection")
var mapbtn = document.getElementById("mapBtn")
var mapsection = document.getElementById("mapSection")


infobtn.addEventListener('click', function() {
  console.log("confirmito")
  infosection.style.display = 'flex';
  infosection.scrollIntoView({ behavior: 'smooth' }); 
  
});
mapbtn.addEventListener('click', function() {
  console.log("confirmito2")
  mapsection.style.display = 'flex';
  mapsection.scrollIntoView({ behavior: 'smooth' }); 
  
});