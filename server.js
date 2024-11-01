// server.js
import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();

// Serve static files from the "dist" directory
app.use(express.static(path.join(__dirname, 'dist')));

// Serve static assets from the "static" directory
app.use('/static', express.static(path.join(__dirname, 'dist/static')));

// Serve images from the "image_store" directory
app.use('/image_store', express.static(path.join(__dirname, 'dist/image_store')));

// Handle SPA (Single Page Application) routing
app.get('*', function (req, res) {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});