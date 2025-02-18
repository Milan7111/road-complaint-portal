// Initialize the map and set its view to Kathmandu (27.7172, 85.3240)
var map = L.map('map').setView([27.7172, 85.3240], 13);

// Add OpenStreetMap tiles (free)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);
