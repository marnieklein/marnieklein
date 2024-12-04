from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_legislators():
    with open('legislators-current.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def find_representatives_by_state_and_district(state, district):
    legislators = load_legislators()
    matching_legislators = []

    for legislator in legislators:
        # Ensure state and district exist
        legislator_state = legislator.get('state', '').strip().upper()
        legislator_district = legislator.get('district', '').strip()

        # Check if state matches and district is empty or matches
        if state and district and legislator_state == state.strip().upper():
            if not legislator_district or legislator_district == district.strip():
                matching_legislators.append(legislator)

    return matching_legislators

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    state = request.form.get('state', '').strip().upper()
    district = request.form.get('district', '').strip()

    valid_states = {'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS',
                    'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY',
                    'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV',
                    'WI', 'WY'}

    if state not in valid_states:
        return render_template('index.html', error="Please provide a valid state abbreviation.")

    if not district.isdigit() or int(district) <= 0:
        return render_template('index.html', error="Please provide a valid district number.")

    matching_legislators = find_representatives_by_state_and_district(state, district)

    return render_template('index.html', legislators=matching_legislators, state=state, district=district)

if __name__ == '__main__':
    app.run(debug=True)
