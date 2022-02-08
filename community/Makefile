GOLANG_IMAGE=golang:1.12
LABEL_SYNC_IMAGE=gcr.io/k8s-prow/label_sync:latest
export GO111MODULE=on
export GOPROXY?=https://proxy.golang.org

default: \
	generate \

reset-docs:
	git checkout HEAD -- ./sig-list.md ./sig-*/README.md ./wg-*/README.md

generate-sig-files:
	podman run --rm --volume $(shell pwd):/workdir:Z quay.io/open-services-group/community-tooling:v0.1.0-dev

label-sync:
	podman run --rm -v $(shell pwd):/community:Z $(LABEL_SYNC_IMAGE) --action docs --config /community/labels.yaml --docs-template /community/labels.md.tmpl --docs-output /community/labels.md

verify:
	@hack/verify.sh

verify-dockerized:
	podman run --rm -v $(shell pwd):/go/src/app:Z $(GOLANG_IMAGE) make -C /go/src/app verify

test:
	go test -v ./generator/...

test-dockerized:
	podman run --rm -v $(shell pwd):/go/src/app:Z $(GOLANG_IMAGE) make -C /go/src/app test

.PHONY: default reset-docs generate generate-dockerized verify test test-dockerized
