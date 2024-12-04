// Checks for valid input to form (correct state abbreviation and district number)

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const stateInput = document.querySelector('#state');
    const districtInput = document.querySelector('#district');
    const validStates = new Set(['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS',
                                'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY',
                                'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV',
                                'WI', 'WY']);

    form.onsubmit = function(event) {
      const state = stateInput.value.trim().toUpperCase();
      const district = districtInput.value.trim();

      if (!validStates.has(state)) {
        alert("Please enter a valid state abbreviation.");
        event.preventDefault();
        return false;
      }

      if (!district.match(/^\d+$/) || parseInt(district) <= 0) {
        alert("Please enter a valid district number for the district.");
        event.preventDefault();
        return false;
      }

      return true;
    };
  });
