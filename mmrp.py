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
        and not FLASK_JSONRPC_PROJECT_DIR in sys.path:
    sys.path.append(FLASK_JSONRPC_PROJECT_DIR)

from flask_jsonrpc import JSONRPC
from pymmrouting.routeplanner import MultimodalRoutePlanner
from pymmrouting.inferenceengine import RoutingPlanInferer

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

@jsonrpc.method('App.index')
def index():
    return u'Welcome using Multimodal Route Planner (mmrp) JSON-RPC API'

@jsonrpc.method('App.inferRoutingPlans')
def infer_routing_plans(options):
    logger.info("infer_routing_plans called")
    logger.debug("argument options passed in is: %s", options)
    inferer = RoutingPlanInferer()
    inferer.load_routing_options_from_string(options)
    plans = inferer.generate_routing_plan()
    return json.dumps(plans)

@jsonrpc.method('App.findMultimodalPaths')
def find_multimodal_paths(options):
    inferer = RoutingPlanInferer()
    inferer.load_routing_options_from_string(options)
    plans = inferer.generate_routing_plan()
    planner = MultimodalRoutePlanner()
    rough_results = planner.batch_find_path(plans)
    results = planner.refine_results(rough_results)
    return json.dumps(results)

@jsonrpc.method('App.notify')
def notify(string):
    pass

@jsonrpc.method('App.fails')
def fails(string):
    raise ValueError


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
