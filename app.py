import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def healthcheck():
    return "Alive"


@app.route("/test", methods=["GET", "POST"])
def test():
    req_data = {}
    app.logger.info('Testing')
    req_data['method'] = request.method
    req_data['headers'] = dict(request.headers)
    req_data['data'] = json.loads(request.data)
    req_data['args'] = request.args
    req_data['form'] = request.form
    req_data['endpoint'] = request.endpoint
    req_data['remote_addr'] = request.remote_addr
    req_data['scheme'] = request.scheme
    req_data['server'] = request.server
    req_data['root_path'] = request.root_path
    req_data['path'] = request.path
    req_data['shallow'] = request.shallow
    req_data['view_args'] = request.view_args
    req_data['_parsed_content_type'] = request._parsed_content_type
    req_data['content_length'] = request.content_length
    req_data['files'] = request.files
    req_data['query_string'] = request.query_string.decode("utf-8")
    req_data['_cached_data'] = request._cached_data.decode("utf-8")
    req_data['url_rule'] = str(request.url_rule)
    req_data['stream'] = str(request.stream)

    return jsonify(req_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
