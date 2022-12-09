from flask import Flask
from flask import request
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

apiKey = 'BQAsi1HBztyFtprA5TndqVhk7X68_fGm_dFExEzomGimnagjtQrMbDS01egWmDJBQ9FSUpwQNqGMrF9lJ_2wR2EF2uMq7bDStFs562QreaKzmCV9-W6eoEGMPWGDAdLkfjE9cxAB-0tjsLUG313G3vT8C_v6hQqJLnLy4e5tvcaj3mu0PDwZll0qmlL1L9k'
tempId = '6sfUgwUTFjy1SNF2uWOcPp'
@api.route('/getArtist', methods=['POST'])
def my_profile():
    data = request.get_json()
    print(data['name'])

    
    
    response_body = {
        "name": data['name']
    }

    return response_body