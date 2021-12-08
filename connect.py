def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token
    response = requests.request()
    print ("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception (response.status_code, response.text)
    return response.json()
