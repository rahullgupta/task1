from urllib import response
from matplotlib.pyplot import get
import requests

URL = "https://www.flickr.com/services/rest"

response = requests.get(URL)

key = "9d9bdf9c8dfccefad9cdeec801bdf22c"

if(response.status_code == 200):
    params = {
        "api_key": key,
        "method": "flickr.photos.getPopular",
        "user_id": "134493066@N06"
    }
    print(requests.get(URL, params).text);
