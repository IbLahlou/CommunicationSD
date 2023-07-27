const axios = require('axios');

// Data to send in the request body
const data = {
  title: 'Updated Post',
  content: 'This is the updated content of the post.'
};

// Make a PUT request to update an existing resource
axios.put('https://api.example.com/posts/1', data)
  .then(response => {
    // Handle the response data
    console.log(response.data);
  })
  .catch(error => {
    // Handle errors
    console.error(error);
  });
