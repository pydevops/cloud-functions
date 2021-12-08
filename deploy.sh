#!/usr/bin/env bash
set -euo pipefail
INPUT_BUCKET=pso-victory-dev-8f039964-e2bb-11e8-b17e-1700de069414
OUTPUT_BUCKET=pso-victory-dev-data

gcloud beta functions deploy copier --runtime python39 \
--set-env-vars OUTPUT_BUCKET=${OUTPUT_BUCKET} \
--trigger-resource ${INPUT_BUCKET} \
--trigger-event google.storage.object.finalize \
--timeout=540
#--memory=2048MB

# Testing
#gsutil -o GSUtil:parallel_composite_upload_threshold=150M cp 1g gs://${INPUT_BUCKET}