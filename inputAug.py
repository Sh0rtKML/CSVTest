#Inputs for the request
from imports import *
bearer_token = auth()
headers = create_headers(bearer_token)
keyword = "isis OR isis-k OR #isis OR #isis_k or iskp or khorasan lang:en"
start_time = '2021-08-19T00:00:01.000Z'
end_time = '2021-09-02T00:00:01.000Z'
max_results = 200

