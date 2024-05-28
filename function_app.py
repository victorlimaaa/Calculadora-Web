import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger1")
def http_trigger1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    operation = req.params.get('operation')
    x_str = req.params.get('x')
    y_str = req.params.get('y')

    try:
        x = float(x_str)
        y = float(y_str)
    except:
        return func.HttpResponse(f"Invalid values. Please adjust number formats.",status_code=400)

    if operation == 'add':
        result = x + y
    elif operation == 'subtract':
        result = x - y
    else:
        return func.HttpResponse("Invalid operation. Please use 'add' or 'subtract'.",status_code=400)

    return func.HttpResponse( f"Resultado: {result}", status_code=200)
