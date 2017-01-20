from framework.request_handler import YumSearchRequestHandler


class CheckerActivation(YumSearchRequestHandler):
    def post(self):

        message = self.request.get('message')

        json_response = {}

        if message:
            # success
            if message == "Activate":
                json_response.update({
                    'title': 'Activated'
                })
            elif message == "Deactivated":
                json_response.update({
                    'title': 'Deativated'
                })
            self.json_response(**json_response)
        else:
            # failure
            status = 400
            json_response.update({
                'title': 'Undefined activation request'
            })
            self.json_response(status_code=status, **json_response)
