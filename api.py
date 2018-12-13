from argparse import ArgumentParser

from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route("/teas")
def teas():
    tealist = {
        'Lord': {
            'name': 'Thé des Lords',
            'type': 'Earl Grey'
        },
        'Hammam': {
            'name': 'Thé du Hammam',
            'type': 'Thé vert'
        }
    }
    return jsonify(tealist)


def main():
    arg_parser = ArgumentParser(description="Tea Infused Service")
    arg_parser.add_argument(
        "-p", "--port",
        dest="port",
        type=int,
        default=5000,
        help="Port for Flask")
    arg = arg_parser.parse_args()
    app.run(host='0.0.0.0', port=arg.port)


if __name__ == '__main__':
    main()