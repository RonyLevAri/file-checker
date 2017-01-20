# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from webapp2 import WSGIApplication
from webapp2 import Route

app = WSGIApplication(
    routes=[
        Route('/', handler='como.home.Home'),
        Route('/activate', handler='como.activation.CheckerActivation'),
        Route('/actionfile', handler='como.actionfile.AddFile'),
        Route('/addmail', handler='como.add_email.AddEmail'),
        Route('/_checker/loadfiles', handler='como.file_checker.LoadFiles'),
    ]
)
