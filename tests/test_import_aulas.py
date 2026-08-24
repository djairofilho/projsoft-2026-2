from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

import yaml
from pypdf import PdfWriter


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "import_aulas.py"
SPEC = importlib.util.spec_from_file_location("import_aulas", SCRIPT_PATH)
assert SPEC and SPEC.loader
import_aulas = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(import_aulas)


def create_pdf(path: Path) -> None:
    writer = PdfWriter()
    writer.add_blank_page(width=300, height=300)
    with path.open("wb") as stream:
        writer.write(stream)


class ImportAulasTests(unittest.TestCase):
    def test_slugify_preserves_readable_portuguese_slug(self) -> None:
        self.assertEqual(
            import_aulas.slugify("Aula 05 — Observabilidade"),
            "aula-05-observabilidade",
        )

    def test_import_is_idempotent_and_does_not_overwrite_notes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source = root / "entrada"
            repository = root / "repositorio"
            source.mkdir()
            repository.mkdir()
            create_pdf(source / "Aula 05 - Observabilidade.pdf")

            imported, skipped = import_aulas.import_pdfs(source, repository)
            self.assertEqual((imported, skipped), (1, 0))

            note = repository / "docs/aulas/aula-05-observabilidade.md"
            note.write_text("Notas revisadas\n", encoding="utf-8")

            imported, skipped = import_aulas.import_pdfs(source, repository)
            self.assertEqual((imported, skipped), (0, 1))
            self.assertEqual(note.read_text(encoding="utf-8"), "Notas revisadas\n")

            manifest_path = repository / "data/aulas.yml"
            manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(len(manifest["aulas"]), 1)
            self.assertEqual(manifest["aulas"][0]["pages"], 1)
            self.assertFalse(manifest["aulas"][0]["published"])


if __name__ == "__main__":
    unittest.main()
