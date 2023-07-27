// Import Axios (Node.js environment) or use the global Axios object (browser)
const axios = require('axios');

// Make a GET request to fetch data from the API
axios.get('https://api.example.com/posts')
  .then(response => {
    // Handle the response data
    console.log(response.data);
  })
  .catch(error => {
    // Handle errors
    console.error(error);
  });
