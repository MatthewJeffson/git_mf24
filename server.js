// server.js
import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

// Get the current directory (since __dirname is not available in ES modules)
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();

// Serve the static files from the dist directory
app.use('/static', express.static(path.join(__dirname, 'dist/static')));

// Handle SPA (Single Page Application) routing
app.get('*', function (req, res) {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

// Start the app by listening on the default Heroku port
const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});