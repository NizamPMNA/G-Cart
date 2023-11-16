 // An array of options
  var options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"];

  // Loop through the array and append an option for each item
  $.each(options, function(index, value) {
    $('#no_teams').append($('<option>', {
      value: 'option' + (index + 1), // You can set the value dynamically if needed
      text: value
    }));
  });