"""Automated tests for the hello module."""

import subprocess
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from hello import greeting  # noqa: E402


class HelloTest(unittest.TestCase):
    def test_greeting(self) -> None:
        self.assertEqual(greeting(), "Hello, World!")

    def test_command_line_output(self) -> None:
        result = subprocess.run(
            [sys.executable, str(PROJECT_ROOT / "hello.py")],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.stdout, "Hello, World!\n")


if __name__ == "__main__":
    unittest.main()
