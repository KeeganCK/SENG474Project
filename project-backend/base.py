from flask import Flask
from flask import request
from flask_cors import CORS
from getTopTen import *
import requests

api = Flask(__name__)
CORS(api)

apiKey = 'BQDlJqtybu1dL1NrIyQuALMXZO9B84H8vIBnOpLWjmQsMUOtBGKpFm1B8s6j7nbx8Q3Njez929mlYHbEbWnNZqXBfaaIJYAis3Iv9uPAUCgRdWvFvaRQZvbHyxtxNA9rmLvE8k_BNatxNYN-aiVmwqhkruVlY5nYei3d6gZGNpDuzlxSd_xF1H2c0H1MZ1w'
BASE_URL = 'https://api.spotify.com/v1/'
headers = {
    'Authorization': 'Bearer {token}'.format(token=apiKey)
}



@api.route('/getArtist', methods=['POST'])
def my_profile():
    data = request.get_json()

    # wantedDict = get_recommendations(data['name'])
    # print(data['type'])
    matrix=CVectorizer()
    sim,reverse = EuDSim(matrix)
    wantedDict = get_recommendations(data['name'],sim,reverse)


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