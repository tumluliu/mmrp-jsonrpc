#!/bin/bash
curl -i -X POST  -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "App.inferRoutingPlans", "params": [{ "available_public_modes": ["suburban", "underground", "tram"], "can_use_taxi": false, "has_bicycle": false, "has_motorcycle": false, "has_private_car": false, "need_parking": false, "objective": "fastest", "source": { "type": "coordinate", "value": { "x": 11.5682, "y": 48.1500, "srid": 4326 } }, "target": { "type": "coordinate", "value": { "x": 11.5038, "y": 48.1583, "srid": 4326 } } }], "id": "1"}' http://localhost:5000/api
#curl -i -X POST  -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "App.echo", "params": [ {"Hi": "liulu"} ], "id": "1"}' http://localhost:5000/api
