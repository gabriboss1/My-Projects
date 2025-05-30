const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow () {
  const win = new BrowserWindow({
    width: 900,
    height: 720,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'), // Optional, for IPC
      nodeIntegration: true,
      contextIsolation: false,
    }
  });

  // For production, use 'build/index.html'
  win.loadURL('http://localhost:3000'); // Dev: React runs on localhost
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});
