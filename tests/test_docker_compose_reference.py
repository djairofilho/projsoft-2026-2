from __future__ import annotations

import unittest
from pathlib import Path


REPOSITORY = Path(__file__).parents[1]
REFERENCE = REPOSITORY / "docs" / "referencias" / "docker-compose.md"


class DockerComposeReferenceTests(unittest.TestCase):
    def test_reference_covers_topology_configuration_and_lifecycle(self) -> None:
        text = REFERENCE.read_text(encoding="utf-8")

        self.assertIn("```yaml", text)
        self.assertIn("services:", text)
        self.assertIn("DB_HOST: postgres", text)
        self.assertIn("healthcheck:", text)
        self.assertIn("condition: service_healthy", text)
        self.assertIn("volumes:", text)
        self.assertIn("docker compose config", text)
        self.assertIn("docker compose up -d", text)
        self.assertIn("docker compose down", text)
        self.assertIn(".env.example", text)
        self.assertNotIn('class="pdf-preview"', text)

    def test_reference_is_linked_from_course_navigation(self) -> None:
        expected = "referencias/docker-compose.md"
        config = (REPOSITORY / "mkdocs.yml").read_text(encoding="utf-8")
        home = (REPOSITORY / "docs" / "index.md").read_text(encoding="utf-8")
        docker = (
            REPOSITORY / "docs" / "referencias" / "docker.md"
        ).read_text(encoding="utf-8")
        lesson = (
            REPOSITORY / "docs" / "aulas" / "aula-05-redes-docker.md"
        ).read_text(encoding="utf-8")
        glossary = (
            REPOSITORY / "docs" / "referencias" / "glossario.md"
        ).read_text(encoding="utf-8")

        self.assertIn(expected, config)
        self.assertIn(expected, home)
        self.assertIn("docker-compose.md", docker)
        self.assertIn("docker-compose.md", lesson)
        self.assertIn("docker-compose.md", glossary)


if __name__ == "__main__":
    unittest.main()
