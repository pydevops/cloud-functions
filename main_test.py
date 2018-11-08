# Copyright 2018, Google, LLC.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mock

import main
import os

def test_mover():
        event = {
            'bucket': 'pso-victory-dev-8f039964-e2bb-11e8-b17e-1700de069414',
            'name': 'foo',
            'metageneration': 'some-metageneration',
            'timeCreated': '0',
            'updated': '0'
        }
        context = mock.MagicMock()
        context.event_id = 'some-id'
        context.event_type = 'gcs-event'
        os.environ['GCLOUD_PROJECT']='pso-victory-dev'
        os.environ['OUTPUT_BUCKET']='pso-victory-dev-data'
        main.mover(event, context)

        # out, _ = capsys.readouterr()

        # assert 'some-bucket' in out
        # assert 'some-id' in out

if __name__ == '__main__':
    test_mover()