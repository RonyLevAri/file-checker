from framework.request_handler import YumSearchRequestHandler
from google.appengine.api import taskqueue
from models.checked_files import CheckedFiles


class LoadFiles(YumSearchRequestHandler):

    def get(self):

        queue = taskqueue.Queue('checker')
        files = CheckedFiles.get_all_menaged_files()

        for a_file in files:

            # self.json_response(**{'url': a_file.url, 'message': 'automated task'})
            task = taskqueue.Task(url='/actionfile', params={'url': a_file.url, 'message': 'automated task'})
            queue.add(task)

