#!/usr/bin/env bash
INPUT_BUCKET=pso-victory-dev-8f039964-e2bb-11e8-b17e-1700de069414
OUTPUT_BUCKET=pso-victory-dev-data
gcloud beta functions deploy copier --runtime python37 \
--set-env-vars OUTPUT_BUCKET=${OUTPUT_BUCKET} \
--trigger-resource ${INPUT_BUCKET} \
--trigger-event google.storage.object.finalize