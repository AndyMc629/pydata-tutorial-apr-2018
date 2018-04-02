export GCS_JOB_DIR=gs://pydata_april_2018/cloudml-census/census_20180402_170044
gcloud ml-engine models create census --regions europe-west1
export MODEL_BINARIES=$GCS_JOB_DIR/export/census/1522684876
gcloud ml-engine versions create v1 --model census --origin $MODEL_BINARIES --runtime-version 1.4
