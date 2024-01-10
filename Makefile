# Commands can be run trough `make <command>`
# .PHONY indicates that the target is not a file
# @ at the start of the command silence its output
# Comments after ## are used for help
# When run with no target shows help
# Syntax uses the following convention:
#  - https://www.thapaliya.com/en/writings/well-documented-makefiles/


.DEFAULT_GOAL := help

.PHONY: help
help:  ## display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

serve:  ## start the live-reloading docs server.
	@mkdocs serve

build: ## build the documentation site.
	@mkdocs build
