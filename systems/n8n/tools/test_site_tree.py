"""Local checks for the 2026-11-22 public site-tree capture."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHOTS = ROOT / "screenshots"

REQUIRED = [
    "home-light-1440.png",
    "home-light-390.png",
    "footer-light-1440.png",
    "menu-product-light-1440.png",
    "menu-use-cases-light-1440.png",
    "features-light-1440.png",
    "ai-agents-light-1440.png",
    "mcp-light-1440.png",
    "nod-light-1440.png",
    "integrations-light-1440.png",
    "workflows-light-1440.png",
    "itops-light-1440.png",
    "secops-light-1440.png",
    "rag-light-1440.png",
    "lead-automation-light-1440.png",
    "crm-light-1440.png",
    "oem-light-1440.png",
    "case-studies-light-1440.png",
    "enterprise-light-1440.png",
    "pricing-light-1440.png",
    "support-light-1440.png",
    "careers-light-1440.png",
    "partners-light-1440.png",
    "contact-light-1440.png",
    "press-light-1440.png",
    "brandguidelines-light-1440.png",
    "status-light-1440.png",
    "docs-light-1440.png",
    "changelog-light-1440.png",
    "report-light-1440.png",
    "vs-light-1440.png",
    "education-light-1440.png",
    "sap-light-1440.png",
    "imprint-light-1440.png",
    "security-light-1440.png",
    "privacy-light-1440.png",
    "legal-light-1440.png",
    "learn-light-1440.png",
    "login-light-1440.png",
    "register-light-1440.png",
]


def test_site_tree_dated():
    text = (ROOT / "site-tree.md").read_text()
    assert "2026-11-22" in text
    assert "https://n8n.io/" in text
    assert "catalog.json" not in text or "left alone" in (ROOT / "README.md").read_text()


def test_login_review_not_started():
    data = json.loads((ROOT / "login-review.json").read_text())
    assert data["slug"] == "n8n"
    assert data["signed_in"] is False
    assert data["login_extracted"] == "not-started"
    assert data["wall"]["continue_not_clicked"] is True
    assert data["wall"]["sign_in_not_clicked"] is True


def test_screenshots_present():
    missing = [name for name in REQUIRED if not (SHOTS / name).is_file()]
    assert missing == []


def test_people_pages_not_saved():
    names = {p.name for p in SHOTS.glob("*.png")}
    for banned in ("creators", "forum", "blog", "events", "experts", "vulnerability"):
        assert not any(banned in name for name in names)
