async function fetchData(capitalCity) {
  const apiKey = 'ebc79dbb8dbbc5b4fc767069c24982e8';
  ';
  const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${capitalCity}&appid=${apiKey}&units=metric`;

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    return data.main.temp;
    return data.weather[0].description;
  } catch (error) {
    console.error('Failed to fetch weather data:', error);
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
      const temperature = await fetchData(capitalCity);
      const description = await fetchData(capitalCity);
      return { countryId, temperature, description};
    });

    const temperatureResults = await Promise.all(temperaturePromises);

    temperatureResults.forEach(({ countryId, temperature, description }) => {
      if (temperature !== null) {
        let fillColor;

        if (temperature < 0) {
          fillColor = '#EBA6FF'; // Extreme cold
        } else if (temperature < 10 && temperature >= 0) {
          fillColor = '#5881db'; // very cold
        } 
        else if (temperature <= 15){
          fillColor = '#6FE1E5' //cold
        }
        else if (temperature >= 15 && temperature < 18) {
          fillColor = '#FABF48'; // cool
        } else if (temperature >= 25 && temperature < 35) {
          fillColor = '#eb9e60'; // Warm
        } else if (temperature >= 35) {
          fillColor = '#ed5d47'; // HOT
        }
        else if (temperature >= 18 && temperature < 21){
          fillColor = '#aaf26b' // less warm
        }
        else if (temperature >= 21){
          fillColor = '#48FA70' // warmer
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
        const capitalCity = 'London'; // Replace with the actual capital city for the country

        if (capitalCity) {
          hoverTimeout = setTimeout(async () => {
            const apiKey = 'YOUR_API_KEY'; // Replace with your OpenWeatherMap API key
            const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${capitalCity}&appid=${apiKey}&units=metric`;

            try {
              const response = await fetch(apiUrl);
              const data = await response.json();

              if (data.main && data.main.temp) {
                tooltip.textContent = `Temp in ${capitalCity} is ${data.main.temp}°C`;
                tooltip.style.left = `${e.pageX}px`;
                tooltip.style.top = `${e.pageY}px`;
                tooltip.style.display = 'block';
              }
            } catch (error) {
              console.error('Failed to fetch weather data:', error);
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

