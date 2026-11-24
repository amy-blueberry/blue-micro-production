#!/bin/bash
set -euo pipefail
# First-time provisioning only. Do not rerun on an existing deployment.
# Enable compute.googleapis.com, iap.googleapis.com and cloudresourcemanager.googleapis.com first.
gc() { gcloud "$@" --project=bumpp-intelligence-prod --account=devops@houseofblueberry.com --quiet; }
gc compute networks create intelligence --subnet-mode=custom
gc compute networks subnets create intelligence-east --network=intelligence --region=us-east1 --range=10.20.0.0/24
gc compute firewall-rules create intelligence-iap-ssh --network=intelligence --allow=tcp:22 --source-ranges=35.235.240.0/20 --target-tags=intelligence
gc compute firewall-rules create intelligence-lb --network=intelligence --allow=tcp:8080 --source-ranges=35.191.0.0/16,130.211.0.0/22 --target-tags=intelligence
gc compute disks create intelligence-data --zone=us-east1-b --size=20GB --type=pd-balanced
gc compute instances create intelligence-1 --zone=us-east1-b --machine-type=e2-small --subnet=intelligence-east --tags=intelligence --image-family=debian-12 --image-project=debian-cloud --boot-disk-size=20GB --boot-disk-type=pd-balanced --disk=name=intelligence-data,device-name=intelligence-data,mode=rw,boot=no,auto-delete=no --no-service-account --no-scopes --shielded-secure-boot
gc compute addresses create intelligence-web --global --ip-version=IPV4
gc compute instance-groups unmanaged create intelligence --zone=us-east1-b
gc compute instance-groups unmanaged add-instances intelligence --zone=us-east1-b --instances=intelligence-1
gc compute instance-groups unmanaged set-named-ports intelligence --zone=us-east1-b --named-ports=http:8080
gc compute health-checks create http intelligence --port=8080 --request-path=/healthz
gc compute backend-services create intelligence --global --load-balancing-scheme=EXTERNAL_MANAGED --protocol=HTTP --port-name=http --health-checks=intelligence --timeout=120s
gc compute backend-services add-backend intelligence --global --instance-group=intelligence --instance-group-zone=us-east1-b
gc compute backend-services update intelligence --global --iap=enabled
gc iap web add-iam-policy-binding --resource-type=backend-services --service=intelligence --member=user:devops@houseofblueberry.com --role=roles/iap.httpsResourceAccessor
gc compute url-maps create intelligence --default-service=intelligence
gc compute ssl-certificates create intelligence --domains=intelligence.bumpp.gg --global
gc compute target-https-proxies create intelligence --url-map=intelligence --ssl-certificates=intelligence
gc compute forwarding-rules create intelligence-https --global --load-balancing-scheme=EXTERNAL_MANAGED --address=intelligence-web --target-https-proxy=intelligence --ports=443
gc compute addresses describe intelligence-web --global --format='value(address)'
gc compute backend-services describe intelligence --global --format='value(id)'
