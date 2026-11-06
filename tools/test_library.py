"""Tests for server/library.py, the tool layer behind the chat and MCP.
web/lib/chat/library.ts is its twin; a fix here lands there too. Run with
`make test`."""
import importlib.util
import unittest
from pathlib import Path

SERVER = Path(__file__).resolve().parent.parent / "server"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, SERVER / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


library = _load("agent_library_test", "library.py")


class HandoffPromptTest(unittest.TestCase):
    def test_paths_are_relative_to_the_library_home(self):
        prompt = library.call("handoff_prompt", {"slug": "linear"})["prompt"]
        self.assertNotIn(str(library.ROOT.resolve()), prompt)
        self.assertIn("$DESIGN_SYSTEMS_HOME/systems/linear/README.md", prompt)
        self.assertIn("$DESIGN_SYSTEMS_HOME/systems/linear/tokens.json", prompt)
        self.assertIn("$DESIGN_SYSTEMS_HOME/systems/linear/screenshots/", prompt)


if __name__ == "__main__":
    unittest.main()
