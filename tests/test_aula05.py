from __future__ import annotations

import unittest
from pathlib import Path


REPOSITORY = Path(__file__).parents[1]
LESSON = REPOSITORY / "docs" / "aulas" / "aula-05-redes-docker.md"


class DockerNetworksLessonTests(unittest.TestCase):
    def test_lesson_covers_the_original_lab_flow(self) -> None:
        text = LESSON.read_text(encoding="utf-8")

        self.assertIn('class="pdf-preview"', text)
        self.assertIn("aula-05-redes-docker.pdf", text)
        self.assertIn("docker network create", text)
        self.assertIn("postgres-aula:5432", text)
        self.assertIn("${DB_HOST:localhost}", text)
        self.assertIn("Parte 4: levar para a máquina AWS", text)
        self.assertGreaterEqual(text.count("```mermaid"), 2)

    def test_lesson_is_linked_from_navigation_and_indexes(self) -> None:
        expected = "aulas/aula-05-redes-docker.md"
        config = (REPOSITORY / "mkdocs.yml").read_text(encoding="utf-8")
        home = (REPOSITORY / "docs" / "index.md").read_text(encoding="utf-8")
        lesson_index = (
            REPOSITORY / "docs" / "aulas" / "index.md"
        ).read_text(encoding="utf-8")

        self.assertIn(expected, config)
        self.assertIn(expected, home)
        self.assertIn("aula-05-redes-docker.md", lesson_index)


if __name__ == "__main__":
    unittest.main()
