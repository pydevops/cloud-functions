## deploy the cloud function
Please configure it accordingly in your GCP project, then run
```
./deploy.sh
```

## Note
* Each cloud function can have only one trigger resource, i.e. bucket.
* Cloud function uses the timeout 540s.
* use GCS's rewrite API: 
    * [Object rewrite](https://cloud.google.com/storage/docs/json_api/v1/objects/rewrite)
* Tested with up to 10g file size:
  * 100m: 462ms
  * 1g: 30,262 ms 
  * 10g: 327,745 ms


## testing a file upload
with size desired
```
INPUT_BUCKET=pso-victory-dev-8f039964-e2bb-11e8-b17e-1700de069414
(OSX) mkfile -n 100m 100m
gsutil cp 100m gs://${INPUT_BUCKET}

(OSX) mkfile -n 1g 1g
gsutil -o GSUtil:parallel_composite_upload_threshold=200M cp 1g gs://${INPUT_BUCKET}
```
