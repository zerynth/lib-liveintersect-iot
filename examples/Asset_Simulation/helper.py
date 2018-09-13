import json


def load_asset_conf():
    """
load_asset_conf from asset.config.json
    """
    confstream = open('resource://asset.config.json')
    conf = ''
    while True:
        line = confstream.readline()
        if not line:
            break
        conf += line
    return json.loads(conf)
    
