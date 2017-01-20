from framework.request_handler import YumSearchRequestHandler
from models.checked_files import CheckedFiles
from models.emails import Email
import logging


class AddFile(YumSearchRequestHandler):

    def post(self):

        url = self.request.get('url')
        message = self.request.get('message')

        json_response = {}

        if url and message:
            # success 
            json_response = CheckedFiles.add_new_file(url)
            has_changed_lately = json_response['has_changed_lately']
            add_request = message == 'Add new file path to manage'

            if has_changed_lately or add_request:
                subject = "File was added!"
                message = "The file you requested was added for supervision"
                status = 'File was added at %s' % str(json_response['last_checked'])
                if not add_request:
                    subject = "File changed!"
                    message = "A supervised file had been changed!"
                    status = 'File was changed according to last check at %s' % str(json_response['last_checked'])

                emails = Email.query().fetch()
                for a_mail in emails:
                    self.send_email2(str(a_mail.email), subject, message, 'File URL: %s' % url, status)

                log = 'url: %s check has completed at: %s change status: %s ' % (str(url), str(json_response['last_checked']), str(has_changed_lately))
                logging.info(log)
            self.json_response(**json_response)
        else:
            # failure
            status = 400
            json_response.update({
                'title': 'Undefined activation request'
            })
            self.json_response(status_code=status, **json_response)
