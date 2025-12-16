#!/usr/bin/env node
/**
 * Simple local development server with custom 404.html support
 * Mimics GitHub Pages behavior for testing clean URLs locally
 *
 * Usage: node server.js
 */

const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 8000;
const ROOT_DIR = __dirname;

const MIME_TYPES = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'text/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
};

function getMimeType(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  return MIME_TYPES[ext] || 'application/octet-stream';
}

function serveFile(res, filePath) {
  fs.readFile(filePath, (err, content) => {
    if (err) {
      serve404(res);
    } else {
      res.writeHead(200, { 'Content-Type': getMimeType(filePath) });
      res.end(content);
    }
  });
}

function serve404(res) {
  const notFoundPath = path.join(ROOT_DIR, '404.html');
  fs.readFile(notFoundPath, (err, content) => {
    if (err) {
      // Fallback if 404.html doesn't exist
      res.writeHead(404, { 'Content-Type': 'text/html' });
      res.end('<h1>404 Not Found</h1>');
    } else {
      res.writeHead(404, { 'Content-Type': 'text/html' });
      res.end(content);
    }
  });
}

const server = http.createServer((req, res) => {
  let filePath = path.join(ROOT_DIR, req.url === '/' ? 'index.html' : req.url);

  // Handle directory URLs (e.g., /blog -> /blog/index.html)
  if (req.url.endsWith('/') && req.url !== '/') {
    filePath = path.join(filePath, 'index.html');
  }

  fs.stat(filePath, (err, stats) => {
    if (!err && stats.isFile()) {
      // File exists, serve it
      serveFile(res, filePath);
    } else if (!err && stats.isDirectory()) {
      // Directory exists, try index.html
      const indexPath = path.join(filePath, 'index.html');
      serveFile(res, indexPath);
    } else {
      // File doesn't exist - serve 404.html (mimics GitHub Pages)
      serve404(res);
    }
  });
});

server.listen(PORT, () => {
  console.log(`\n🚀 Server running at http://localhost:${PORT}/`);
  console.log(`📁 Serving files from: ${ROOT_DIR}`);
  console.log(`✨ Custom 404.html support enabled\n`);
  console.log(`Try these URLs to test clean URLs:`);
  console.log(`  - http://localhost:${PORT}/blog/welcome (clean URL)`);
  console.log(`  - http://localhost:${PORT}/blog/welcome.html (with extension)\n`);
  console.log('Press Ctrl+C to stop\n');
});
