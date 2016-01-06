#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import logging.config
import json

LOGGING_CONF_FILE = 'logging.json'
DEFAULT_LOGGING_LVL = logging.INFO
path = LOGGING_CONF_FILE
value = os.getenv('LOG_CFG', None)
if value:
    path = value
if os.path.exists(path):
    with open(path, 'rt') as f:
        config = json.load(f)
    logging.config.dictConfig(config)
else:
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
logger = logging.getLogger(__name__)

from flask import Flask

PROJECT_DIR, PROJECT_MODULE_NAME = os.path.split(
    os.path.dirname(os.path.realpath(__file__))
)

FLASK_JSONRPC_PROJECT_DIR = os.path.join(PROJECT_DIR, os.pardir)
if os.path.exists(FLASK_JSONRPC_PROJECT_DIR) \
        and FLASK_JSONRPC_PROJECT_DIR not in sys.path:
    sys.path.append(FLASK_JSONRPC_PROJECT_DIR)

from flask_cors import CORS
from flask_jsonrpc import JSONRPC
from pymmrouting.routeplanner import MultimodalRoutePlanner
from pymmrouting.inferenceengine import RoutingPlanInferer

app = Flask(__name__)
cors = CORS(app)
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)
inferer = RoutingPlanInferer()
planner = MultimodalRoutePlanner()

@jsonrpc.method('mmrp.index')
def index():
    return u'Welcome using Multimodal Route Planner (mmrp) JSON-RPC API'


@jsonrpc.method('mmrp.echo')
def echo(input):
    logger.debug("input value: %s", input)
    return u'Receive {0}'.format(input)


@jsonrpc.method('mmrp.findMultimodalPaths')
def find_multimodal_paths(options):
    inferer.load_routing_options(options)
    plans = inferer.generate_routing_plan()
    results = planner.batch_find_path(plans)
    return results


@jsonrpc.method('mmrp.fails')
def fails(string):
    raise ValueError

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
