from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path

import yaml
from pypdf import PdfReader


REPOSITORY = Path(__file__).parents[1]
MANIFEST = REPOSITORY / "data" / "aulas.yml"
PDF_DIRECTORY = REPOSITORY / "docs" / "assets" / "pdfs" / "2026-2"
IGNORED_PARTS = {".git", ".venv", "site", "__pycache__"}
TEXT_SUFFIXES = {".md", ".py", ".txt", ".yml", ".yaml"}
PATTERN_SUBLESSONS = {
    "aula-02-padroes-fundamentais.md": (
        3,
        "aula-02-padroes-complementares.md",
    ),
    "aula-02-padroes-complementares.md": (
        3,
        "aula-02-padroes-fundamentais.md",
    ),
}
SUPPLEMENTAL_LESSONS = {
    "aula-01-requisitos-qualidade.md": (
        "aula-01-introducao.md",
        "aula-01-decisoes-arquiteturais.md",
        0,
    ),
    "aula-01-decisoes-arquiteturais.md": (
        "aula-01-introducao.md",
        "aula-01-requisitos-qualidade.md",
        0,
    ),
    "aula-04-testes-erros.md": (
        "aula-04-confiabilidade.md",
        "aula-04-entrega-observabilidade.md",
        6,
    ),
    "aula-04-entrega-observabilidade.md": (
        "aula-04-confiabilidade.md",
        "aula-04-testes-erros.md",
        2,
    ),
}


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repository_files() -> list[Path]:
    return [
        path
        for path in REPOSITORY.rglob("*")
        if path.is_file() and not IGNORED_PARTS.intersection(path.parts)
    ]


class PublicContentTests(unittest.TestCase):
    def test_manifest_matches_published_pdfs(self) -> None:
        manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
        lessons = manifest["aulas"]
        self.assertEqual(len(lessons), 5)
        self.assertEqual(len({lesson["slug"] for lesson in lessons}), 5)

        for lesson in lessons:
            with self.subTest(lesson=lesson["slug"]):
                pdf = PDF_DIRECTORY / lesson["source_file"]
                self.assertTrue(pdf.is_file())
                self.assertEqual(file_hash(pdf), lesson["source_hash"])
                self.assertEqual(len(PdfReader(pdf).pages), lesson["pages"])
                self.assertTrue(lesson["published"])

    def test_lessons_embed_their_source_pdf(self) -> None:
        manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))

        for lesson in manifest["aulas"]:
            with self.subTest(lesson=lesson["slug"]):
                note = REPOSITORY / "docs" / "aulas" / f"{lesson['slug']}.md"
                text = note.read_text(encoding="utf-8")
                self.assertIn('class="pdf-preview"', text)
                self.assertIn(lesson["source_file"], text)
                self.assertNotIn("Perguntas de revisão", text)

    def test_pattern_sublessons_have_guided_examples_and_diagrams(self) -> None:
        for filename, (minimum_diagrams, peer) in PATTERN_SUBLESSONS.items():
            with self.subTest(sublesson=filename):
                path = REPOSITORY / "docs" / "aulas" / filename
                text = path.read_text(encoding="utf-8")
                self.assertGreaterEqual(text.count("```mermaid"), minimum_diagrams)
                self.assertGreaterEqual(text.count("```java"), 4)
                self.assertIn("### Antes", text)
                self.assertIn("### Depois", text)
                self.assertIn("Quando usar", text)
                self.assertIn("Quando não usar", text)
                self.assertIn("Custo introduzido", text)
                self.assertNotIn('class="pdf-preview"', text)
                self.assertIn("aula-02-manutenibilidade.md", text)
                self.assertIn(peer, text)

    def test_supplemental_lessons_are_linked_and_self_contained(self) -> None:
        config = (REPOSITORY / "mkdocs.yml").read_text(encoding="utf-8")

        for filename, (parent, peer, minimum_java) in SUPPLEMENTAL_LESSONS.items():
            with self.subTest(sublesson=filename):
                path = REPOSITORY / "docs" / "aulas" / filename
                text = path.read_text(encoding="utf-8")
                parent_text = (path.parent / parent).read_text(encoding="utf-8")

                self.assertIn("```mermaid", text)
                self.assertGreaterEqual(text.count("```java"), minimum_java)
                self.assertNotIn('class="pdf-preview"', text)
                self.assertIn(parent, text)
                self.assertIn(peer, text)
                self.assertIn(filename, parent_text)
                self.assertIn(f"aulas/{filename}", config)

    def test_docker_lessons_form_a_guided_sequence(self) -> None:
        docker = (
            REPOSITORY / "docs" / "aulas" / "aula-03-docker.md"
        ).read_text(encoding="utf-8")
        aws = (
            REPOSITORY / "docs" / "aulas" / "aula-03-tutorial-aws.md"
        ).read_text(encoding="utf-8")

        self.assertIn("```mermaid", docker)
        self.assertIn("```mermaid", aws)
        self.assertIn("aula-03-tutorial-aws.md", docker)
        self.assertIn("aula-03-docker.md", aws)
        self.assertIn("VERSAO_ANTERIOR", aws)

    def test_mkdocs_configures_native_mermaid_fences(self) -> None:
        config = (REPOSITORY / "mkdocs.yml").read_text(encoding="utf-8")
        self.assertIn("name: mermaid", config)
        self.assertIn("pymdownx.superfences.fence_code_format", config)

    def test_repository_has_no_operational_secrets(self) -> None:
        forbidden_names = {"maquina.txt", "maquinas_geral.csv"}
        ipv4 = re.compile(r"(?<!\d)(?:\d{1,3}\.){3}\d{1,3}(?!\d)")

        for path in repository_files():
            with self.subTest(path=path.relative_to(REPOSITORY)):
                self.assertNotIn(path.name.lower(), forbidden_names)
                self.assertNotIn(path.suffix.lower(), {".pem", ".key", ".p12", ".pfx"})
                content = path.read_bytes()
                private_key_marker = b"BEGIN " + b"PRIVATE KEY"
                rsa_key_marker = b"BEGIN RSA " + b"PRIVATE KEY"
                self.assertNotIn(private_key_marker, content)
                self.assertNotIn(rsa_key_marker, content)
                if path.suffix.lower() in TEXT_SUFFIXES:
                    text = content.decode("utf-8")
                    self.assertIsNone(ipv4.search(text))
                    mojibake_artifacts = (
                        chr(0x0007),
                        chr(0x00C3),
                        chr(0x00C2),
                        chr(0xFFFD),
                    )
                    for artifact in mojibake_artifacts:
                        self.assertNotIn(artifact, text)


if __name__ == "__main__":
    unittest.main()
