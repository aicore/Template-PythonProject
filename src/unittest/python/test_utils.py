import json
import pathlib


def _get_test_resource_file_path(file_name):
    return pathlib.Path(__file__).parent.parent.absolute()\
        .joinpath('test_resources')\
        .joinpath(file_name)


def load_json_test_resource(json_file_name):
    file_path = _get_test_resource_file_path(json_file_name)
    f = open(file_path, "r")
    data = json.loads(f.read())
    f.close()
    return data
