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


from google.cloud import storage

import os

# [START functions_copier]
def copier(data, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed.

    Args:
        data (dict): The Cloud Functions event payload.
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """

    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(data['bucket']))
    print('File: {}'.format(data['name']))
    print('Metageneration: {}'.format(data['metageneration']))
    print('Created: {}'.format(data['timeCreated']))
    print('Updated: {}'.format(data['updated']))
    PROJECT = os.environ['GCLOUD_PROJECT']
    print('project: {}'.format(PROJECT))

    # figure out input and output bucket name, object (blob) path
    input_bucket_name=data['bucket']
    input_blob_path='{}/{}'.format(input_bucket_name,data['name'])
    print('input_blob_path={}'.format(input_blob_path))
    output_bucket_name=os.environ['OUTPUT_BUCKET']
    # parse out customer_id
    customer_id=input_bucket_name.split(PROJECT+'-')[1]
    output_blob_path='{}/{}'.format(customer_id,data['name'])
    print('output_blob_path={}'.format(output_blob_path))

    storage_client = storage.Client()
    input_bucket = storage_client.get_bucket(input_bucket_name)
    output_bucket = storage_client.get_bucket(output_bucket_name)

    input_blob = input_bucket.get_blob(data['name'])
    if input_blob:
        output_blob = output_bucket.blob(output_blob_path)
        token = None
        while True:
            token, bytes_rewritten, total_bytes = output_blob.rewrite(
                input_blob, token=token)
            if token is None:
                break

# [END functions_copier]
