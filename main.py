from flask_json import FlaskJSON, as_json
from flask_cors import CORS, cross_origin
import uuid
from flask import Flask, redirect, url_for, request, make_response, send_file, jsonify
app = Flask(__name__)
cors = CORS(app)
json = FlaskJSON(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_AS_ASCII'] = False
app.config['JSON_ADD_STATUS'] = False

def errors(func):
    def wrapper(*args, **kwargs):

        try:
                original_result = func(*args, **kwargs)

        except Exception  as err:
            print(err)
            original_result = {"success": False,
                               "exception": {
                                "message": str(err)
                               }
                               }
        return original_result
    return wrapper

usedPass = {'admin': 'password123',
            'lena': 'Roomster13'}

@app.route('/user/register', methods=['GET'])
@cross_origin()
@as_json
@errors
def auth():
    # check parameters
    nickname = request.args.get('nickname')
    password = request.args.get('password')
    try:

        if (usedPass[nickname] != password):
            raise Exception()
        else:
            newUuid = uuid.uuid4() #random token
            response = {'success': True,
                        'exception': None,
                        'nickname': nickname,
                        'accessToken': newUuid}
            return response, 200
    except Exception as err:
        raise Exception("Nickname or password is incorrect")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)

