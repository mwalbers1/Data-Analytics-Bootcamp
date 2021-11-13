
// Create the map object with a center and zoom level.
let map = L.map("mapid").setView([37.6213, -122.3790], 5);

 // We create the tile layer that will be the background of our map.
let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY
});

// Coordinates for each point to be used in the line.
let line = [
  [33.9416, -118.4085],
  [37.6213, -122.3790],
  [40.7899, -111.9791],
  [47.4502, -122.3088]
];

// Create a polyline using the line coordinates.
L.polyline(line, {
  color: "yellow"
}).addTo(map);

// We create the tile layer that will be the background of our map.
// let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/dark-v10/tiles/{z}/{x}/{y}?access_token={accessToken}', {
//   attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//   maxZoom: 18,
//   accessToken: API_KEY
// });


// Then we add our 'graymap' tile layer to the map.
streets.addTo(map);

// An array containing each city's location, state, and population.
//cityData = cities;

// add marker for each city onto map
// cityData.forEach(city => L.marker(city.location)
//   .bindPopup("<h1>" + city.city + "</h1> <hr> <h3>Population " + city.population + "</h3>")
//   .addTo(map)
// );

// circle for each city onto map
// cityData.forEach(city => L.circleMarker(city.location, {
//   radius: (city.population - 200000) / 100000,
//   color: "orange",
//   weight: "4"
// }).addTo(map));


// Add circle to the map
// L.circle([34.0522, -118.2437], {
//   radius: 10000
// }).addTo(map);

// Add a circle to the map with L.circleMaker
// L.circleMarker([34.0522, -118.2437], {
//   radius: 75,
//   color: "black",
//   fillColor: '#ffffa1'
// }).addTo(map);
