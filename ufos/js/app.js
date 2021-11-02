// from data.js
const tableData = data;

// get table references
var tbody = d3.select("tbody");

// get filter input references
let date_field = d3.select("#datetime");
let city_field = d3.select("#city");
let state_field = d3.select("#state");
let country_field = d3.select("#country");
let shape_field = d3.select("#shape");

function buildTable(data) {
  // First, clear out any existing data
  tbody.html("");

  // Next, loop through each object in the data
  // and append a row and cells for each value in the row
  data.forEach((dataRow) => {
    // Append a row to the table body
    let row = tbody.append("tr");

    // Loop through each field in the dataRow and add
    // each value as a table cell (td)
    Object.values(dataRow).forEach((val) => {
      let cell = row.append("td");
      cell.text(val);
    });
  });
}

// 1. Create a variable to keep track of all the filters as an object.
var filters = [];

function addFilterObject(id, value) {
  /********************************************************* 
    Add filterObject varable with the filter id and value passed into function. Then
    push filter object into filters array.
  ***********************************************************/

  // search for array index for the filter field equal to id parameter
  found = filters.findIndex(function(val, index) {
    if (val.id == id)
      return true;
  });

  // Return if filters already contains filter ojbect for id parameter
  if (found != -1)
    return;

  let filterObject = {};

   // 4c. Save the id of the filter that was changed as a variable.
   filterObject["id"] = id;
      
   // 4b. Save the value that was changed as a variable.
   filterObject["value"] = value;

   // 5. If a filter value was entered then add that filterId and value to the filters list
   filters.push(filterObject);
}

// 3. Use this function to update the filters. 
function updateFilters() {
    
    let date = d3.select("#datetime").property("value");
    let city = d3.select("#city").property("value");
    let state = d3.select("#state").property("value");
    let country = d3.select("#country").property("value");
    let shape = d3.select("#shape").property("value");

    // 4a. Save the element that was changed as a variable.
    if (date) {
      addFilterObject("datetime", date);
    }
    if (city) {
      addFilterObject("city", city);
    }
    if (state) {
      addFilterObject("state", state);
    }
    if (country) {
      addFilterObject("country", country);
    }
    if (shape) {
      addFilterObject("shape", shape);
    }
    
    if ((!date) && (!city) && (!state) && (!country) && (!shape)) {
      // clear filter from the filters object.
      filters = [];
    }
  
    // 6. Call function to apply all filters and rebuild the table
    filterTable();
  }
  
  // 7. Use this function to filter the table when data is entered.
  function filterTable() {
  
    // 8. Set the filtered data to the tableData.
    filteredData = tableData;
  
    console.log(filters);

    // 9. Loop through all of the filters and keep any data that matches the filter values
    for (var filter in filters) {
      let filterId = filters[filter].id;
      let filterValue = filters[filter].value;

      if (filterId == 'datetime') {
        filteredData = filteredData.filter(row => row.datetime === filterValue);
      }
      if (filterId == 'city') {
        filteredData = filteredData.filter(row => row.city === filterValue);
      }
      if (filterId == 'state') {
        filteredData = filteredData.filter(row => row.state === filterValue);
      }
      if (filterId == 'country') {
        filteredData = filteredData.filter(row => row.country === filterValue);
      }
      if (filterId == 'shape') {
        filteredData = filteredData.filter(row => row.shape === filterValue);
      }      
    }
  
    // 10. Finally, rebuild the table using the filtered data
    buildTable(filteredData);
  }

  function handleChange(event) {
    /****************************************************
      This method is triggered on change event on filter fields
    ****************************************************/

    var target_id = d3.event.target.id;
    var target_value = d3.event.target.value;

    // search for array index for the filter field with target id
    found = filters.findIndex(function(val, index) {
      if (val.id == target_id)
        return true;
    });

    //console.log(target_id);
    //console.log(found);

    if (found != -1) {
      if (target_value == '') {
        // remove filter object from filters array at found index
        filters.splice(found, 1);
      }
      else {
        // update value to filter on in filters array
        filters[found] = target_value;
      }
    }
  }

  // 2. Attach an event to listen for changes to each filter
  d3.selectAll("#filter-btn").on("click", updateFilters);
  
  // Attach change events for each filter field
  date_field.on("change", handleChange);
  city_field.on("change", handleChange);
  state_field.on("change", handleChange);
  country_field.on("change", handleChange);
  shape_field.on("change", handleChange);

  // Build the table when the page loads
  buildTable(tableData);
