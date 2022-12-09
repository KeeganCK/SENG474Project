from flask import Flask
from flask import request
from flask_cors import CORS
from getTopTen import *
import requests

api = Flask(__name__)
CORS(api)

apiKey = 'BQBYoZkUjE005tW9gnxhs4UDuzC4ZqYe42KAxPbkXBVLMPcluMms4sPYBCI5j1xN_5ivmlWhU4Dj3Qz7r78-PKNhUmC4XkLEh4INvCiTNB5NHAY8OhnK5dbU5ehg8Z1WRNG1MIDLNFhs-EVXr2bKzV0Ao9Bahzs0qJzsHG9w-0bGILp5YNE_CmLsa9WyaCg'
BASE_URL = 'https://api.spotify.com/v1/'
headers = {
    'Authorization': 'Bearer {token}'.format(token=apiKey)
}



@api.route('/getArtist', methods=['POST'])
def my_profile():
    data = request.get_json()

    wantedDict = get_recommendations(data['name'])

    topTenArray = []
    topten = wantedDict['top10']
    i=0
    for id in topten:
        r = requests.get(BASE_URL + 'artists/' + id, headers=headers)
        rData = r.json()
        tempDict = {
            'name': rData['name'],
            'image': rData['images'][2]['url'],
            'url': rData['external_urls']['spotify'],
            'score': wantedDict['scores'][i],
            'position': i+1
        }
        topTenArray.append(tempDict)
        i+=1
    
    topTenSpotArray = []
    id = wantedDict['mainId']
    r = requests.get(BASE_URL + 'artists/' + id + '/related-artists', headers=headers)
    rData = r.json()
    i = 0
    for entry in rData['artists']:
        if i >= 10:
            break
        tempDict = {
            'name': entry['name'],
            'image': entry['images'][2]['url'],
            'url': entry['external_urls']['spotify'],
            'position': i+1
        }
        topTenSpotArray.append(tempDict)
        i+=1
    
    response_body = {
        "data": topTenArray,
        "spotifyData": topTenSpotArray
    }

    return response_body