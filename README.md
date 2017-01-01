# mmrp-jsonrpc

JSON RPC style API for Multimodal Route Planning

## Introduction

The API is hosted on [luliu.me] (http://luliu.me), the URL is:

http://luliu.me/mmrp/api/v1

## Sample usage

The API service provides two methods accepting POST requests: 

- `mmrp.index`: return a welcome message
- `mmrp.findMultimodalPaths`: do the multimodal route planning with given routing options

### Sample request on `mmrp.index`

Send a request via curl:

```bash
curl -i -X POST  -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "mmrp.index", "params": {}, "id": "1"}' http://luliu.me/mmrp/api/v1
```

Response:

```bash
HTTP/1.1 200 OK
Date: Sat, 13 Jun 2015 10:55:30 GMT
Server: Apache/2.4.7 (Ubuntu)
Content-Type: application/json
Content-Length: 111

{
  "id": "1", 
  "jsonrpc": "2.0", 
  "result": "Welcome using Multimodal Route Planner (mmrp) JSON-RPC API"
}
```

### Sample request on `mmrp.findMultimodalPaths`

Both the request and response are too long to write here. The request can be found in `sample_request.sh`. And the response containing the feasible multimodal paths as well as switch points is in the `sample_response.json`.

## Dependencies

- Flask-JSONRPC
- pymmrouting

## Contact

- Lu LIU
- nudtlliu#gmail.com

## Acknowledgements

Thanks for the support of National Natural Science Foundation of China (NSFC) project "Data model and algorithms in socially-enabled multimodal route planning service" (No. 41301431) of which I am the project leader.
