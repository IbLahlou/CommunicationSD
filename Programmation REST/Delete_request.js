const axios = require('axios');

// Make a DELETE request to remove a resource
axios.delete('https://api.example.com/posts/1')
  .then(response => {
    // Handle the response data
    console.log(response.data);
  })
  .catch(error => {
    // Handle errors
    console.error(error);
  });
