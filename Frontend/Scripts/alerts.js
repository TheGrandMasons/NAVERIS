document.addEventListener('DOMContentLoaded', function() {
  const alertBtn = document.getElementById('alerts');
  const alertBox = document.getElementById('alertBox');
  
  alertBtn.addEventListener('click', function() {
    if (alertBox.style.display === 'none' || alertBox.style.display === '') {
      alertBox.style.display = 'flex';
      alertBox.style.background= 'rgba(206, 213, 194, 0.2)';
      alertBox.style.backdropFilter='blur(6.9px)';
      alertBox.style.borderRadius='10px';
      alertBox.style.width='300px';
      alertBox.style.padding='20px';
      alertBox.style.boxShadow='0 4px 6px rgba(0, 0, 0, 0.1)'

    } else {
      alertBox.style.display = 'none'; 
    }
  });
});