from framework.request_handler import YumSearchRequestHandler
from models.emails import Email


class AddEmail(YumSearchRequestHandler):

    def post(self):

        email = self.request.get('email')
        # message = self.request.get('message')

        json_response = {'pipi': email}

        if email:
            # success
            json_response = Email.add_email(email)
            created = json_response['created']

            if created:
                self.send_email2(str(email), 'Congrats!', 'You were added as supervisor', email,
                                 'will now get notifications of file changes')

            self.json_response(**json_response)
        else:
            # failure
            status = 400
            json_response.update({
                'title': 'Not a valid email format'
            })
            self.json_response(status_code=status, **json_response)

