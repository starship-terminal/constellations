# Browse the library's docs site (gallery, scorecard, docs), and check the catalog before a commit.
# `make setup` once installs the pinned Zensical into .venv; everything else needs only python3
# (lint-design-md also needs Node.js). `make serve PORT=9000` picks another port.

PYTHON ?= python3
PORT ?= 8800

.PHONY: help setup serve build docs scorecard grade check test brief design-md lint-design-md clean

help: ## List the targets
	@grep -E '^[a-z-]+:.*## ' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  make %-14s %s\n", $$1, $$2}'

setup: ## Create .venv with the pinned Zensical (once per machine)
	uv venv -q --python 3.13 .venv && uv pip install -q --python .venv/bin/python -r requirements.txt

serve: ## Build the gallery, scorecard and docs site and serve it on 127.0.0.1 (PORT, default 8800)
	@$(PYTHON) tools/catalog.py serve --port $(PORT)

build: ## Write the gallery's data and screenshot thumbnails into docs/gallery/
	@$(PYTHON) tools/catalog.py build

docs: ## Generate the scorecard pages and build the docs site into site/ (strict)
	@$(PYTHON) tools/scorecard.py && .venv/bin/zensical build --clean --strict

scorecard: ## Validate the scorecard's audit data
	@$(PYTHON) tools/scorecard.py --check

grade: ## Re-grade the scripted criteria into a new audit snapshot, then rewrite every README's Health section
	@$(PYTHON) tools/grade.py --write && $(PYTHON) tools/scorecard.py --check

check: ## Validate catalog.json against the packages; fail on a stale Brief, DESIGN.md, scorecard or Health section
	@$(PYTHON) tools/catalog.py check
	@$(PYTHON) tools/brief.py --check
	@$(PYTHON) tools/grade.py --check

brief: ## Rewrite every package README's Brief from its catalog entry, tokens and README
	@$(PYTHON) tools/brief.py

design-md: brief ## Rewrite every Brief, then regenerate every package's DESIGN.md from its tokens and README
	@$(PYTHON) tools/catalog.py design-md

lint-design-md: ## Lint every DESIGN.md with Google's pinned linter (needs Node.js; runs npx in a temp dir)
	@$(PYTHON) tools/catalog.py design-md --lint

test: ## Run the tools' tests
	@$(PYTHON) -m unittest discover -s tools -p 'test_*.py'

clean: ## Remove generated files
	rm -rf site docs/gallery/data.json docs/gallery/thumbs docs/scorecard zensical.toml
