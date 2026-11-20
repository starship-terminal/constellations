# Browse the library through the Next.js app (make dev), and check the catalog before a commit.
# `make setup` once installs the site builder's and the capture tools' python dependencies
# (requirements.txt + tools/requirements-capture.txt) into .venv; everything else needs only
# python3 (lint-design-md also needs Node.js, and the app needs pnpm). `make dev PORT=9000`
# picks another port.

PYTHON ?= python3
PORT ?= 8800

.PHONY: help setup dev serve build docs scorecard grade check test brief design-md lint-design-md refero-dump refero-db clean web web-build

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

# Every gate runs even after an earlier one fails, so one run reports every problem; the
# target then fails, naming each gate that failed.
check: ## Validate catalog.json, the refero stores, and login-extracted; fail on a stale Brief, DESIGN.md, scorecard or Health section
	@failed=""; \
	for gate in "tools/catalog.py check" "tools/refero/check.py" "tools/brief.py --check" \
	            "tools/grade.py --check" "tools/gated.py --check" "tools/login_extracted.py --check"; do \
		$(PYTHON) $$gate || failed="$$failed  $$gate;"; \
	done; \
	if [ -n "$$failed" ]; then echo "make check: failed:$$failed" >&2; exit 1; fi

brief: ## Rewrite every package README's Brief from its catalog entry, tokens and README
	@$(PYTHON) tools/brief.py

design-md: brief ## Rewrite every Brief, then regenerate every package's DESIGN.md from its tokens and README
	@$(PYTHON) tools/catalog.py design-md

lint-design-md: ## Lint every DESIGN.md with Google's pinned linter (needs Node.js; runs npx in a temp dir)
	@$(PYTHON) tools/catalog.py design-md --lint

refero-dump: ## Rewrite refero/.dump/ (the text dump git merges) from refero/refero.db
	@$(PYTHON) tools/refero/dump.py dump

refero-db: ## Rebuild refero/refero.db from refero/.dump/ (after merging the dump), then rewrite the dump canonically
	@$(PYTHON) tools/refero/dump.py load

test: ## Run the tools' tests, then every package's own tests (every test_*.py and test_*.mjs under systems/<slug>/)
	@$(PYTHON) -m unittest discover -s tools -p 'test_*.py'
	@$(PYTHON) tools/package_tests.py

clean: ## Remove generated files
	rm -rf site web/data docs/scorecard refero/.work
