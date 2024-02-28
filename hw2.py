from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch US Population data from the provided API endpoint
    api_endpoint = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
    response = requests.get(api_endpoint)

    if response.status_code == 200:
        data = response.json()
        # Extract population data
        population_data = data["data"]
    else:
        population_data = [{'Year': 'N/A', 'Population': 'N/A'}]

    # Render the HTML template with the population data
    return render_template('index.html', population_data=population_data)

if __name__ == '__main__':
    app.run(debug=True)
