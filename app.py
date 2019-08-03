from flask import Flask, abort
from flask import request
import randos
app = Flask(__name__)
@app.route('/')
def index():
    # key = request.args.get('key', None)
    # with open('keys.json') as app_key:
    #     config = json.load(app_key)
    # if key == config['key']:
    return randos.random_number()
    # else:
    #     return abort(403)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)