from webapp2 import RequestHandler
import os
import jinja2
from google.appengine.api import mail


class YumSearchRequestHandler(RequestHandler):
    # define how to get to template folder for all html src
    template_directory = os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)),
        'templates'
    )

    jinja_environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_directory)
    )

    def render(self, template, **kwargs):
        jinja_template = self.jinja_environment.get_template(template)
        html_from_template = jinja_template.render(kwargs)

        self.response.out.write(html_from_template)

    def json_response(self, status_code=200, **kwargs):
        from json import dumps

        self.response.status = status_code
        self.response.headers['Content-type'] = 'application/javascript'
        self.response.out.write(dumps(kwargs))

    @classmethod
    def send_email2(cls, to, subject, message, content, status):

        email_object = mail.EmailMessage(
            sender='noreply@openair-154101.appspotmail.com',
            subject='File checker notification - %s' % subject,
            to=to
        )

        email_parameters = {
            'message': message,
            'url': content,
            'status': status,
        }

        html_from_template = cls.jinja_environment.get_template('email/email.html').render(email_parameters)

        email_object.html = html_from_template
        email_object.send()
