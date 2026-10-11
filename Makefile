# Browse the library as a gallery, and check the catalog before a commit.
# Needs only python3 (lint-design-md also needs Node.js). `make serve PORT=9000` picks another port.

PYTHON ?= python3
PORT ?= 8800

.PHONY: help serve build check test design-md lint-design-md clean

help: ## List the targets
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-14s %s\n", $$1, $$2}'

serve: ## Build the gallery and serve it on 127.0.0.1 (PORT, default 8800)
	@$(PYTHON) tools/catalog.py serve --port $(PORT)

build: ## Write site/data.json and the screenshot thumbnails
	@$(PYTHON) tools/catalog.py build

check: ## Validate catalog.json against the packages on disk, including that every DESIGN.md is current
	@$(PYTHON) tools/catalog.py check

design-md: ## Regenerate every package's DESIGN.md from its tokens and README
	@$(PYTHON) tools/catalog.py design-md

lint-design-md: ## Lint every DESIGN.md with Google's pinned linter (needs Node.js; runs npx in a temp dir)
	@$(PYTHON) tools/catalog.py design-md --lint

test: ## Run the catalog tool's tests
	@$(PYTHON) -m unittest discover -s tools -p 'test_*.py'

clean: ## Remove generated gallery files
	rm -rf site/data.json site/thumbs
