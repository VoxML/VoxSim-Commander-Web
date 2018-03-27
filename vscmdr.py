from flask import Flask, render_template, request
import json

initialized = False
app = Flask(__name__)

status = {
    "input" : "",
    "question" : "",
    "utter" : "",
    "clicked" : ""
    }
status_str = ""

@app.route('/init', methods=['POST'])
def init():
    global initialized
    global json
    initialized = True
    return str(initialized)

@app.route('/server', methods=['GET', 'POST'])
def server():
    global status
    global status_str
    if request.method == 'GET':
        data = status_str
        #print data
        return data
    elif request.method == 'POST':
        status = request.get_json(silent=True)
        status_str = str(json.dumps(request.get_json(silent=True)))
        print status_str
        return render_template('VSCommander.html',s=status)

@app.route('/', methods=['GET', 'POST'])
def index():
    global status
    global status_str
    if request.method == 'POST':
        status = request.get_json(silent=True)
        status_str = str(json.dumps(status))
        print status_str
        print status['clicked']
        return render_template('VSCommander.html',s=status)
    else:
        return render_template('VSCommander.html',s=status)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description=__doc__
                                     )
    parser.add_argument(
                         '-p', '--port',
                         default=8220,
                         type=int,
                         action='store',
                         nargs='?',
                         help='Specify port number to run the app.'
                         )
    args = parser.parse_args()
    app.run(port=args.port)