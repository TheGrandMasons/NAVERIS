document.addEventListener('DOMContentLoaded', function () {
  const alertBtn = document.getElementById('alertbtn');
  const alertBox = document.getElementById('alertBox');
  
  async function fetchAlerts() {
    try {
      const response = await fetch('Frontend/Scripts/databaseModel.json');
      if (!response.ok) {
        throw new Error('Failed to fetch warning data');
      }
      const warningData = await response.json();

      const alertList = document.querySelector('.alertList');
      alertList.innerHTML = '';

      warningData.forEach((item) => {
        const { cc, probability, warning } = item;

        let warningType;
        if (warning === "H"){
          warningType = 'Hurricane'
        }else if(warning ==="T"){
          warningType = 'Tornado'
        }

        if (probability >= 70 ) {
          const warningElement = document.createElement('p');
          warningElement.classList.add('warning');
          warningElement.textContent = `Warning for ${cc}: ${warningType} with ${probability}% Probability`;
          alertList.appendChild(warningElement);

          let fillColor = '#f11111';
          const country = document.getElementById(cc);
          if (country) {
            country.style.animation= 'blink 0.4s infinite';
          }
        }
      });
    } catch (error) {
      console.error('Error fetching warnings', error);
    }
  }

  alertBtn.addEventListener('click', fetchAlerts);


  alertBtn.addEventListener('click', function () {
    if (alertBox.style.display === 'none' || alertBox.style.display === '') {
      alertBox.style.display = 'block';
      alertBox.style.background = 'rgba(206, 213, 194, 0.2)';
      alertBox.style.backdropFilter = 'blur(6.9px)';
      alertBox.style.borderRadius = '10px';
      alertBox.style.width = '300px';
      alertBox.style.padding = '20px';
      alertBox.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
    
    } else {
      alertBox.style.display = 'none';
    } 

  });
});