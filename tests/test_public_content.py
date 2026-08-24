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
                    mojibake_artifacts = (chr(0x00C3), chr(0x00C2), chr(0xFFFD))
                    for artifact in mojibake_artifacts:
                        self.assertNotIn(artifact, text)


if __name__ == "__main__":
    unittest.main()
