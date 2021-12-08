def create_headers(bearer_token):
    headers = {"Authorization": "Bear{}".format(bearer_token)}
    return headers
