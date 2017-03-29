# Copyright 2017 ZTE Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
import logging
import threading
import traceback
import sys

from lcm.pub.vimapi import adaptor

logger = logging.getLogger(__name__)

class ResCreateThread(threading.Thread):
    """
    Create resource
    """
    def __init__(self, req_data):
        threading.Thread.__init__(self)
        self.data = req_data

    def run(self):
        try:
            adaptor.create_vim_res(self.data, self.do_notify)
        except:
            logger.error(traceback.format_exc())
            logger.error(str(sys.exc_info()))
            
    def do_notify(self, res_type, ret):
        logger.debug('ret of [%s] is %s', res_type, str(ret))

class ResDeleteThread(threading.Thread):
    """
    Delete resource
    """
    def __init__(self, req_data):
        threading.Thread.__init__(self)
        self.data = req_data

    def run(self):
        try:
            adaptor.delete_vim_res(self.data, self.do_notify)
        except:
            logger.error(traceback.format_exc())
            logger.error(str(sys.exc_info()))
            
    def do_notify(self, res_type, res_id):
        logger.debug('Delete %s(%s)', res_type, res_id)
