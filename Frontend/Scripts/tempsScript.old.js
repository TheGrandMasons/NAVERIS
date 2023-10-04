async function fetchTemperatureData(capitalCity) {
  const apiKey = 'ebc79dbb8dbbc5b4fc767069c24982e8';
  const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${capitalCity}&appid=${apiKey}&units=metric`;

  try {
      const response = await fetch(apiUrl);
      const data = await response.json();
      return data.main.temp; 
  } catch (error) {
      console.error('failed to fetch data 555', error);
      return 0; //xd (should be null)
  }
}

async function updateCountryColors() {
  try {
      const response = await fetch('/Scripts/countryData.json'); 
      if (!response.ok) {
          throw new Error('Failed to fetch country capitals data');
      }
      const countryData = await response.json();   // << el bta3 da (await) ana msh fahmo kwayes wala howa wala async.

      for (const countryId in countryData) {
          const capitalCity = countryData[countryId];
          const temperature = await fetchTemperatureData(capitalCity);
          
          if (temperature !== null) {

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
      }
  } catch (error) {
      console.error('Error fetching country capitals data:', error);
  }
}
// new one has hover and loads temp data at once, this one loaded countries one by one and took time