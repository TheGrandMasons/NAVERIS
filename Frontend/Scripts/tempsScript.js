async function fetchTemperatureData(capitalCity) {
  const apiKey = 'ebc79dbb8dbbc5b4fc767069c24982e8';
  const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${capitalCity}&appid=${apiKey}&units=metric`;

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    return data.main.temp;
  } catch (error) {
    console.error('Failed to fetch temperature data:', error);
    return null;
  }
}

async function updateCountryColors() {
  try {
    const response = await fetch('Frontend/Scripts/countryData.json'); // Check the path to your JSON file
    if (!response.ok) {
      throw new Error('Failed to fetch country capitals data');
    }
    const countryData = await response.json();

    const temperaturePromises = Object.entries(countryData).map(async ([countryId, capitalCity]) => {
      const temperature = await fetchTemperatureData(capitalCity);
      return { countryId, temperature };
    });

    const temperatureResults = await Promise.all(temperaturePromises);

    temperatureResults.forEach(({ countryId, temperature }) => {
      if (temperature !== null) {
        let fillColor;

        if (temperature < 0) {
          fillColor = '#e9c4ff'; // Extreme cold
        } else if (temperature < 15 && temperature >= 0) {
          fillColor = '#5881db'; // Cold
        } else if (temperature >= 15 && temperature < 25) {
          fillColor = '#aaf26b'; // Normal
        } else if (temperature >= 25 && temperature < 35) {
          fillColor = '#eb9e60'; // Warm
        } else if (temperature >= 35) {
          fillColor = '#ed5d47'; // HOT
        }

        const country = document.getElementById(countryId);
        if (country) {
          country.style.fill = fillColor;
        }
      }
    });

    const countryPaths = document.querySelectorAll('.country');

    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    document.body.appendChild(tooltip);

    countryPaths.forEach((countryPath) => {
      let hoverTimeout;
    
      countryPath.addEventListener('mouseenter', async (e) => {
        const countryId = e.target.getAttribute('id');
        const capitalCity = countryData[countryId];
    
        if (capitalCity) {
          hoverTimeout = setTimeout(async () => {
            const temperature = await fetchTemperatureData(capitalCity);
            if (temperature !== null) {
              tooltip.textContent = `Temperature in ${capitalCity}: ${temperature}°C`;
              tooltip.style.left = `${e.pageX}px`;
              tooltip.style.top = `${e.pageY}px`;
              tooltip.style.display = 'block';
            }
          }, 300);
        }
      });
    
      countryPath.addEventListener('mouseleave', () => {
        clearTimeout(hoverTimeout);
    
        tooltip.style.display = 'none';
      });
    });
  } catch (error) {
    console.error('Error fetching country capitals data:', error);
  }
}

const capitalCity = 'YourCapitalCity'; 

window.onload = () => {
  updateCountryColors();
};