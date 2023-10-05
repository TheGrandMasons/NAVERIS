document.addEventListener('DOMContentLoaded', function () {
  const alertBtn = document.getElementById('alertbtn');
  const alertBox = document.getElementById('alertBox');

  async function addWarnings() {
    try {
      const response = await fetch('/databaseModel.json');
      if (!response.ok) {
        throw new Error('Failed to fetch warning data');
      }
      const warningData = await response.json();
  
      console.log(warningData);
  
      warningData.forEach((item) => {
        const { cc, probability } = item;
  
        const probabilityNumber = probability;
        if (probabilityNumber > 70) {
          const warningElement = document.createElement('p');
          warningElement.classList.add('warning');
          warningElement.innerHTML = `Warning for ${cc}: Probability is ${probability}%`;
  
          contentElement.appendChild(warningElement);
        }
      });
    } catch (error) {
      console.error('Error fetching warnings', error);
    }
  }

  alertBtn.addEventListener('click', function () {
    if (alertBox.style.display === 'none' || alertBox.style.display === '') {
      alertBox.style.display = 'flex';
      alertBox.style.background = 'rgba(206, 213, 194, 0.2)';
      alertBox.style.backdropFilter = 'blur(6.9px)';
      alertBox.style.borderRadius = '10px';
      alertBox.style.width = '300px';
      alertBox.style.padding = '20px';
      alertBox.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
      addWarnings();
    } else {
      alertBox.style.display = 'none';
    }
  });
});