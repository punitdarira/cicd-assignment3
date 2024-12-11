import azure.functions as func
import logging
 
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
 
@app.route(route="http_trigger1")
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Inside main function')
 
    return func.HttpResponse(
        "Hello World from Punit Darira",
        status_code=200
    )