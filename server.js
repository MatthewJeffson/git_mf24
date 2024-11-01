// server.js
const express = require('express');
const path = require('path');
const app = express();

// Serve the static files from the dist/static directory
app.use('/static', express.static(path.join(__dirname, 'dist/static')));

// Handle SPA (Single Page Application) routing
app.get('*', function(req, res) {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

// Start the app by listening on the default Heroku port
const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});