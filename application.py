from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Replace these with your actual Azure ML endpoint details
#AZURE_ML_ENDPOINT = "https://your-azure-ml-endpoint.azurewebsites.net/api/v1/score"
#AZURE_ML_KEY = "your-azure-ml-api-key"
AZURE_ML_ENDPOINT = "https://aml-imperialbrand-ib.uksouth.inference.ml.azure.com/score"
AZURE_ML_KEY = "NtpIyqtbgohBK0CmbUfzsEhhbvzzJzLG"

#@app.route('/performance/<outlet>', methods=['POST'])
@app.route('/performance', methods=['POST'])
def performance():
    # Check the Content-Type header
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Request must have Content-Type: application/json'}), 400
   
    # Get the input parameter from the request
    try:
      input_data = request.get_json()
      #parameter = input_data['parameter']
      if 'outlet' not in input_data:
            return jsonify({'error': 'Request must contain a "parameter" field'}), 400
      outlet = input_data['outlet']
    except (KeyError, TypeError):
      return jsonify({'error': 'Request must contain a valid JSON payload with a "parameter" field'}), 400
    # Prepare the request data for the Azure ML endpoint
    '''
    data = {
        "data": [
            {
                "parameter": parameter
            }
        ]
    }
    '''
    data =  {
                "outlet": "Esso Tankstelle outlet"
            }
    '''
    data =  {
                "outlet": outlet
            }
    '''
    print(data)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {AZURE_ML_KEY}'
    }
    print(headers)
    # Call the Azure ML endpoint
    print(AZURE_ML_ENDPOINT)
    response = requests.post(AZURE_ML_ENDPOINT, headers=headers, data=json.dumps(data))
    print(response.status_code)
    # Check the response status code
    if response.status_code == 200:
        # Return the prediction result
        return jsonify(response.json())
    else:
        # Return an error message
        return jsonify({'error': 'Failed to get performance information from Azure ML endpoint'}), 500

@app.route('/distribution', methods=['POST'])
def distribution():
    # Check the Content-Type header
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Request must have Content-Type: application/json'}), 400
    # Get the input parameter from the request
    input_data = request.get_json()
    #parameter = input_data['parameter']
    outlet = input_data['outlet']

    # Prepare the request data for the Azure ML endpoint
    '''
    data = {
        "data": [
            {
                "parameter": parameter
            }
        ]
    }
    '''
    data =  {
                "outlet": "Esso Tankstelle outlet"
            }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {AZURE_ML_KEY}'
    }

    # Call the Azure ML endpoint
    response = requests.post(AZURE_ML_ENDPOINT, headers=headers, data=json.dumps(data))

    # Check the response status code
    if response.status_code == 200:
        # Return the prediction result
        return jsonify(response.json())
    else:
        # Return an error message
        return jsonify({'error': 'Failed to get prediction from Azure ML endpoint'}), 500

@app.route('/shelfavailability', methods=['POST'])
def shelfavailability():
    # Check the Content-Type header
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Request must have Content-Type: application/json'}), 400
    # Get the input parameter from the request
    input_data = request.get_json()
    #parameter = input_data['parameter']
    outlet = input_data['outlet']

    # Prepare the request data for the Azure ML endpoint
    '''
    data = {
        "data": [
            {
                "parameter": parameter
            }
        ]
    }
    '''
    data =  {
                "outlet": "Esso Tankstelle outlet"
            }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {AZURE_ML_KEY}'
    }

    # Call the Azure ML endpoint
    response = requests.post(AZURE_ML_ENDPOINT, headers=headers, data=json.dumps(data))

    # Check the response status code
    if response.status_code == 200:
        # Return the prediction result
        return jsonify(response.json())
    else:
        # Return an error message
        return jsonify({'error': 'Failed to get prediction from Azure ML endpoint'}), 500

@app.route('/reconnect', methods=['POST'])
def reconnect():
    # Check the Content-Type header
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Request must have Content-Type: application/json'}), 400
    # Get the input parameter from the request
    input_data = request.get_json()
    #parameter = input_data['parameter']
    outlet = input_data['outlet']

    # Prepare the request data for the Azure ML endpoint
    '''
    data = {
        "data": [
            {
                "parameter": parameter
            }
        ]
    }
    '''
    data =  {
                "outlet": "Esso Tankstelle outlet"
            }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {AZURE_ML_KEY}'
    }

    # Call the Azure ML endpoint
    response = requests.post(AZURE_ML_ENDPOINT, headers=headers, data=json.dumps(data))

    # Check the response status code
    if response.status_code == 200:
        # Return the prediction result
        return jsonify(response.json())
    else:
        # Return an error message
        return jsonify({'error': 'Failed to get prediction from Azure ML endpoint'}), 500
if __name__ == '__main__':
    app.run(debug=True)