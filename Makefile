# Browse the library through the Next.js app (make dev), and check the catalog before a commit.
# `make setup` once installs the site builder's and the capture tools' python dependencies
# (requirements.txt + tools/requirements-capture.txt) into .venv; everything else needs only
# python3 (lint-design-md also needs Node.js, and the app needs pnpm). `make dev PORT=9000`
# picks another port.

PYTHON ?= python3
PORT ?= 8800

.PHONY: help setup dev serve build docs scorecard grade check test brief design-md lint-design-md clean web web-build

help: ## List the targets
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-14s %s\n", $$1, $$2}'

setup: ## Create .venv with the site builder's and capture tools' dependencies (once per machine)
	uv venv -q --python 3.13 .venv && uv pip install -q --python .venv/bin/python -r requirements.txt -r tools/requirements-capture.txt

dev: ## Run the Next.js app (web/) on 127.0.0.1 and open the gallery and the scorecard (PORT, default 8800)
	@./scripts/dev.sh --port $(PORT)

serve: web ## Alias for `make web`

build: ## Write the app's data and screenshot thumbnails into web/data/
	@$(PYTHON) tools/catalog.py build

web: build ## Run the Next.js app (web/) in dev mode on 127.0.0.1 (PORT, default 8800)
	@pnpm --dir web exec next dev -H 127.0.0.1 -p $(PORT)

web-build: ## Build the Next.js app for production (web/.next, or $$NEXT_DIST_DIR under web/)
	@pnpm --dir web build

docs: ## Generate the scorecard pages and build the docs site into site/
	@$(PYTHON) tools/scorecard.py && $(if $(filter file,$(origin PYTHON)),$(if $(wildcard .venv/bin/python),.venv/bin/python,$(PYTHON)),$(PYTHON)) tools/site.py

scorecard: ## Validate the scorecard's audit data
	@$(PYTHON) tools/scorecard.py --check

grade: ## Re-grade the scripted criteria into a new audit snapshot, then rewrite every README's Health section
	@$(PYTHON) tools/grade.py --write && $(PYTHON) tools/scorecard.py --check

check: ## Validate catalog.json and the refero stores; fail on a stale Brief, DESIGN.md, scorecard or Health section
	@$(PYTHON) tools/catalog.py check
	@$(PYTHON) tools/refero/check.py
	@$(PYTHON) tools/brief.py --check
	@$(PYTHON) tools/grade.py --check
	@$(PYTHON) tools/gated.py --check

brief: ## Rewrite every package README's Brief from its catalog entry, tokens and README
	@$(PYTHON) tools/brief.py

design-md: brief ## Rewrite every Brief, then regenerate every package's DESIGN.md from its tokens and README
	@$(PYTHON) tools/catalog.py design-md

lint-design-md: ## Lint every DESIGN.md with Google's pinned linter (needs Node.js; runs npx in a temp dir)
	@$(PYTHON) tools/catalog.py design-md --lint

test: ## Run the tools' tests, then every package's own tests (systems/*/tools/test_*.py)
	@$(PYTHON) -m unittest discover -s tools -p 'test_*.py'
	@$(PYTHON) tools/package_tests.py

clean: ## Remove generated files
	rm -rf site web/data docs/scorecard refero/.work
