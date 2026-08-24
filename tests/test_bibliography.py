from __future__ import annotations

import unittest
from pathlib import Path


REPOSITORY = Path(__file__).parents[1]
BIBLIOGRAPHY = REPOSITORY / "docs" / "referencias" / "bibliografia.md"


class BibliographyTests(unittest.TestCase):
    def test_bibliography_documents_access_and_required_books(self) -> None:
        text = BIBLIOGRAPHY.read_text(encoding="utf-8")

        self.assertIn("OpenAthens", text)
        self.assertIn("O’Reilly Learning", text)
        self.assertIn("Fundamentals of Software Architecture", text)
        self.assertIn("The Software Architect Elevator", text)
        self.assertIn("Engenharia de Software Moderna", text)
        self.assertIn("https://www.oreilly.com/library-access/", text)

    def test_bibliography_is_linked_from_navigation_and_glossary(self) -> None:
        config = (REPOSITORY / "mkdocs.yml").read_text(encoding="utf-8")
        glossary = (
            REPOSITORY / "docs" / "referencias" / "glossario.md"
        ).read_text(encoding="utf-8")

        self.assertIn("referencias/bibliografia.md", config)
        self.assertIn("bibliografia.md", glossary)


if __name__ == "__main__":
    unittest.main()
