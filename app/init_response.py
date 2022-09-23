import request
import control_response


def init():
    response = request.request_brou()
    final_response = control_response.control(response)

    return final_response

