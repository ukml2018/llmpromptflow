from flask import Flask, request, jsonify
import requests
import json
import urllib
import ssl
import os
#import time

app = Flask(__name__)

# Replace these with your actual Azure ML endpoint details
#AZURE_ML_ENDPOINT = "https://your-azure-ml-endpoint.azurewebsites.net/api/v1/score"
#AZURE_ML_KEY = "your-azure-ml-api-key"
AZURE_ML_ENDPOINT = "https://aml-imperialbrand-ib.uksouth.inference.ml.azure.com/score"
AZURE_ML_KEY = "NtpIyqtbgohBK0CmbUfzsEhhbvzzJzLG"

@app.route('/summary/<store_id>', methods=['GET'])
def summary(store_id):
  #p=allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
  ssl._create_default_https_context = ssl._create_unverified_context
  print(store_id)
  data = {
    "category": "Summary",
    "outlet":store_id
  }

  body = str.encode(json.dumps(data))

  url = 'https://aml-imperialbrand-ib.uksouth.inference.ml.azure.com/score'
  # Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
  api_key = 'NtpIyqtbgohBK0CmbUfzsEhhbvzzJzLG'
  if not api_key:
      raise Exception("A key should be provided to invoke the endpoint")

  # The azureml-model-deployment header will force the request to go to a specific deployment.
  # Remove this header to have the request observe the endpoint traffic rules
  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'aml-imperialbrand-ib-9' }

  req = urllib.request.Request(url, body, headers)

  try:
      response = urllib.request.urlopen(req)
      #time.sleep(80)
      result = response.read()
      print(result)
      return result
      
  except urllib.error.HTTPError as error:
      print("The request failed with status code: " + str(error.code))
    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
      print(error.info())
      print(error.read().decode("utf8", 'ignore'))
      return jsonify({'error': 'Failed to get Summary information from Azure ML endpoint'}), 500

@app.route('/performance/<store_id>', methods=['GET'])
#def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
#    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
#        ssl._create_default_https_context = ssl._create_unverified_context
#allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
def performance(store_id):
  #p=allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
  ssl._create_default_https_context = ssl._create_unverified_context
  print(store_id)
  data = {
    "category": "performance",
    "outlet":store_id
  }

  body = str.encode(json.dumps(data))

  url = 'https://aml-imperialbrand-ib.uksouth.inference.ml.azure.com/score'
  # Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
  api_key = 'NtpIyqtbgohBK0CmbUfzsEhhbvzzJzLG'
  if not api_key:
      raise Exception("A key should be provided to invoke the endpoint")

  # The azureml-model-deployment header will force the request to go to a specific deployment.
  # Remove this header to have the request observe the endpoint traffic rules
  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'aml-imperialbrand-ib-9' }

  req = urllib.request.Request(url, body, headers)

  try:
      print("inside try")
      #response = urllib.request.urlopen(req, timeout=30)
      response = urllib.request.urlopen(req)
      #time.sleep(30)
      print("Waited for 30 sec")
      result = response.read()
      print(result)
      return result
        
  except urllib.error.HTTPError as error:
      try:
        print("inside except try")
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'aml-imperialbrand-ib-4' }
        req = urllib.request.Request(url, body, headers)  
        response = urllib.request.urlopen(req)
        result = response.read()
        print(result)
        return result
      except urllib.error.HTTPError as error:
        print("inside except")
        print("The request failed with status code: " + str(error.code))
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))
        return jsonify({'error': 'Failed to get performance information from Azure ML endpoint'}), 500

#Sasanka's code
@app.route('/conversationalAI', methods=['GET'])
def conversationalAI():
  #p=allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
  ssl._create_default_https_context = ssl._create_unverified_context
  data = {  "question": "Esso Tankstelle outlet",
            "chat_history": []
         }

  body = str.encode(json.dumps(data))

  url = 'https://dbcmirepibmibgaipoc.uksouth.inference.ml.azure.com/score'
  # Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
  api_key = 'wdw3ssgTgianzh27TCZ7URMSsTDEreff'
  if not api_key:
      raise Exception("A key should be provided to invoke the endpoint")

  # The azureml-model-deployment header will force the request to go to a specific deployment.
  # Remove this header to have the request observe the endpoint traffic rules
  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'dbcmirepibmibgaipoc-1' }

  req = urllib.request.Request(url, body, headers)

  try:
      response = urllib.request.urlopen(req)
      result = response.read()
      print(result)
      return result
      
  except urllib.error.HTTPError as error:
      print("The request failed with status code: " + str(error.code))
    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
      print(error.info())
      print(error.read().decode("utf8", 'ignore'))
      return jsonify({'error': 'Failed to get ConversationalAL flow information from Azure ML endpoint'}), 500

#@app.route('/performance/<outlet>', methods=['POST'])
@app.route('/performance_old', methods=['POST'])
def performance_old():
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
        'Authorization': f'Bearer {AZURE_ML_KEY}',
        'azureml-model-deployment': 'aml-imperialbrand-ib-4' 
    }
    print(headers)
    # Call the Azure ML endpoint
    print(AZURE_ML_ENDPOINT)
    response = requests.post(AZURE_ML_ENDPOINT, headers=headers, data=json.dumps(data) )
    print(response.status_code)
    # Check the response status code
    if response.status_code == 200:
        # Return the prediction result
        return jsonify(response.json())
    else:
        # Return an error message
        return jsonify({'error': 'Failed to get performance information from Azure ML endpoint'}), 500

@app.route('/distribution/<store_id>', methods=['GET'])
def distribution(store_id):
  #p=allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
  ssl._create_default_https_context = ssl._create_unverified_context
  print(store_id)
  data = {
    "category": "Distribution",
    "outlet":store_id
  }

  body = str.encode(json.dumps(data))

  url = 'https://aml-imperialbrand-ib.uksouth.inference.ml.azure.com/score'
  # Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
  api_key = 'NtpIyqtbgohBK0CmbUfzsEhhbvzzJzLG'
  if not api_key:
      raise Exception("A key should be provided to invoke the endpoint")

  # The azureml-model-deployment header will force the request to go to a specific deployment.
  # Remove this header to have the request observe the endpoint traffic rules
  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'aml-imperialbrand-ib-8' }

  req = urllib.request.Request(url, body, headers)

  try:
      response = urllib.request.urlopen(req)
      result = response.read()
      print(result)
      return result
      
  except urllib.error.HTTPError as error:
      print("The request failed with status code: " + str(error.code))
    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
      print(error.info())
      print(error.read().decode("utf8", 'ignore'))
      return jsonify({'error': 'Failed to get distribution information from Azure ML endpoint'}), 500

@app.route('/shelfavailability/<store_id>', methods=['GET'])
def shelfavailability(store_id):
  #p=allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
  ssl._create_default_https_context = ssl._create_unverified_context
  print(store_id)
  data = {
    "category": "shelfavailability",
    "outlet":store_id
  }

  body = str.encode(json.dumps(data))

  url = 'https://aml-imperialbrand-ib.uksouth.inference.ml.azure.com/score'
  # Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
  api_key = 'NtpIyqtbgohBK0CmbUfzsEhhbvzzJzLG'
  if not api_key:
      raise Exception("A key should be provided to invoke the endpoint")

  # The azureml-model-deployment header will force the request to go to a specific deployment.
  # Remove this header to have the request observe the endpoint traffic rules
  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'aml-imperialbrand-ib-8' }

  req = urllib.request.Request(url, body, headers)

  try:
      response = urllib.request.urlopen(req)
      result = response.read()
      print(result)
      return result
      
  except urllib.error.HTTPError as error:
      print("The request failed with status code: " + str(error.code))
    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
      print(error.info())
      print(error.read().decode("utf8", 'ignore'))
      return jsonify({'error': 'Failed to get Shelf-Availability information from Azure ML endpoint'}), 500

@app.route('/reconnect/<store_id>', methods=['GET'])
def reconnect(store_id):
  #p=allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.
  ssl._create_default_https_context = ssl._create_unverified_context
  print(store_id)
  data = {
    "category": "Reconnect",
    "outlet":store_id
  }

  body = str.encode(json.dumps(data))

  url = 'https://aml-imperialbrand-ib.uksouth.inference.ml.azure.com/score'
  # Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
  api_key = 'NtpIyqtbgohBK0CmbUfzsEhhbvzzJzLG'
  if not api_key:
      raise Exception("A key should be provided to invoke the endpoint")

  # The azureml-model-deployment header will force the request to go to a specific deployment.
  # Remove this header to have the request observe the endpoint traffic rules
  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'aml-imperialbrand-ib-8' }

  req = urllib.request.Request(url, body, headers)

  try:
      response = urllib.request.urlopen(req)
      result = response.read()
      print(result)
      return result
      
  except urllib.error.HTTPError as error:
      print("The request failed with status code: " + str(error.code))
    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
      print(error.info())
      print(error.read().decode("utf8", 'ignore'))
      return jsonify({'error': 'Failed to get Reconnect information from Azure ML endpoint'}), 500
if __name__ == '__main__':
    app.run(debug=True,port=8888)
