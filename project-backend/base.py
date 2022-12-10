from flask import Flask
from flask import request
from flask_cors import CORS
from getTopTen import *
import requests

api = Flask(__name__)
CORS(api)

apiKey = 'BQCatyFVkL-q4U_32jV-l10mnQvjUqBpUNanWUCOieED3adQvSrNZ2pXn211q8iTim7LtI07ZjkdIhwzs_ShhBpHPXgQydq9ITQ2qxJQUupRNI2EV-wut4H4GRfR_ocRId_HyAUV95DaFveL-m_97vVWWe-Eqh1DbKHhjIWA8PJLlHnYmrSRYOhq-Qfgm_0'
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

        tempDict = {}
        if len(rData['images']) > 0:
            tempDict = {
                'name': rData['name'],
                'image': rData['images'][1]['url'],
                'url': rData['external_urls']['spotify'],
                'score': wantedDict['scores'][i],
                'position': i+1
            }
        else:
            tempDict = {
                'name': rData['name'],
                'image': rData['images'],
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

        tempDict = {}
        if len(entry['images']) > 0:
            tempDict = {
                'name': entry['name'],
                'image': entry['images'][1]['url'],
                'url': entry['external_urls']['spotify'],
                'position': i+1
            }
        else:
            tempDict = {
                'name': entry['name'],
                'image': entry['images'],
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