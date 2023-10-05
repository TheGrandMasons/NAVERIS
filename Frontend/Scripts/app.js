var mainsection = document.getElementById("main")
var mapbtn = document.getElementById("mapBtn")
var mapsection = document.getElementById("mapSection")


mapbtn.addEventListener('click', function() {
  console.log("confirmito2");
  mapsection.style.display = 'flex';
  mapsection.scrollIntoView({ behavior: 'smooth' }); 
  
});
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);
      
      if (targetElement) {
          window.scrollTo({
              top: targetElement.offsetTop,
              behavior: 'smooth'
          });
      }
  });
});

