
// Create the map object with center and zoom level.
let map = L.map('mapid').setView([30, 30], 2);

 // We create the tile layer that will be the background of our map.
let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY
});

// Add 'streets' tile layer to the map
streets.addTo(map);

// Accessing The airport GeoJSON URL
let airportData = "https://raw.githubusercontent.com/mwalbers1/Data-Analytics-Bootcamp/Mapping_Geo_JSON/mapping-earthquakes/mapping-geoJSON-points/static/json/majorAirports.json";

// Get GeoJSON data
d3.json(airportData).then(function(data) {
  console.log(data);
  
  //Creating a GeoJSON layer with the retrieved data
  L.geoJson(data, {
    onEachFeature: function(features, layer) {
      layer.bindPopup("<h2>Airport Code: " + features.properties.faa + "<hr>" + features.properties.name);
    }
  }).addTo(map);
});
