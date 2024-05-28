import logging
import json

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        operation = req_body.get('operation')
        x = req_body.get('x')
        y = req_body.get('y')
    except ValueError:
        return func.HttpResponse(
             "Invalid input",
             status_code=400
        )

    if not operation or x is None or y is None:
        return func.HttpResponse(
             "Please pass an operation and two numbers (x and y) in the request body",
             status_code=400
        )

    if operation == 'add':
        result = x + y
    elif operation == 'subtract':
        result = x - y
    else:
        return func.HttpResponse(
             "Invalid operation. Please use 'add' or 'subtract'.",
             status_code=400
        )

    return func.HttpResponse(
        json.dumps({"result": result}),
        mimetype="application/json",
        status_code=200
    )
