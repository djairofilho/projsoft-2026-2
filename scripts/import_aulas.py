"""Importa PDFs de aulas sem sobrescrever anotações existentes."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import unicodedata
from pathlib import Path

import yaml
from pypdf import PdfReader


PDF_DESTINATION = Path("docs/assets/pdfs/2026-2")
NOTES_DESTINATION = Path("docs/aulas")
MANIFEST_PATH = Path("data/aulas.yml")


def sha256(path: Path) -> str:
    """Calcula o SHA-256 de um arquivo sem carregá-lo inteiro na memória."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def slugify(value: str) -> str:
    """Converte um título em um nome seguro e estável para URL."""
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", ascii_value.lower()).strip("-")


def title_from_stem(stem: str) -> str:
    """Transforma nomes comuns do Blackboard em títulos de apresentação."""
    cleaned = re.sub(r"\s+", " ", stem.replace("_", " ")).strip()
    match = re.match(r"(?i)^aula\s*(\d+)\s*[-–—]\s*(.+)$", cleaned)
    if not match:
        return cleaned

    number, topic = match.groups()
    if topic.isupper():
        topic = topic.capitalize()
    return f"Aula {int(number):02d} — {topic}"


def load_manifest(path: Path) -> dict:
    if not path.exists():
        return {"aulas": []}
    with path.open("r", encoding="utf-8") as stream:
        data = yaml.safe_load(stream) or {}
    data.setdefault("aulas", [])
    return data


def save_manifest(path: Path, manifest: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        yaml.safe_dump(
            manifest,
            stream,
            allow_unicode=True,
            sort_keys=False,
            width=100,
        )


def scaffold_note(path: Path, title: str, pdf_name: str) -> None:
    """Cria uma página inicial somente quando a aula ainda não possui notas."""
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    body = f"""# {title}

[Baixar o PDF original](../assets/pdfs/2026-2/{pdf_name}){{ .md-button }}

## Objetivos

- Registrar os objetivos desta aula.

## Resumo

Adicione aqui um resumo do material.

## Conceitos-chave

- Conceito a revisar.

## Perguntas de revisão

1. Qual é a principal ideia desta aula?
"""
    path.write_text(body, encoding="utf-8", newline="\n")


def unique_destination(directory: Path, slug: str, digest: str) -> Path:
    candidate = directory / f"{slug}.pdf"
    if not candidate.exists() or sha256(candidate) == digest:
        return candidate
    return directory / f"{slug}-{digest[:8]}.pdf"


def import_pdfs(source: Path, repo_root: Path) -> tuple[int, int]:
    """Importa PDFs novos e retorna as quantidades importada e ignorada."""
    if not source.is_dir():
        raise ValueError(f"Diretório de origem não encontrado: {source}")

    manifest_path = repo_root / MANIFEST_PATH
    manifest = load_manifest(manifest_path)
    lessons = manifest["aulas"]
    known_hashes = {lesson["source_hash"] for lesson in lessons}
    next_order = max((int(lesson["order"]) for lesson in lessons), default=0) + 1

    pdf_destination = repo_root / PDF_DESTINATION
    notes_destination = repo_root / NOTES_DESTINATION
    pdf_destination.mkdir(parents=True, exist_ok=True)
    notes_destination.mkdir(parents=True, exist_ok=True)

    imported = 0
    skipped = 0
    for source_pdf in sorted(source.glob("*.pdf"), key=lambda item: item.name.lower()):
        digest = sha256(source_pdf)
        if digest in known_hashes:
            skipped += 1
            continue

        title = title_from_stem(source_pdf.stem)
        slug = slugify(source_pdf.stem)
        destination = unique_destination(pdf_destination, slug, digest)
        shutil.copy2(source_pdf, destination)

        note_path = notes_destination / f"{slug}.md"
        scaffold_note(note_path, title, destination.name)
        pages = len(PdfReader(source_pdf).pages)
        lessons.append(
            {
                "order": next_order,
                "title": title,
                "slug": slug,
                "source_file": destination.name,
                "source_hash": digest,
                "pages": pages,
                "published": False,
            }
        )
        known_hashes.add(digest)
        next_order += 1
        imported += 1

    lessons.sort(key=lambda lesson: int(lesson["order"]))
    save_manifest(manifest_path, manifest)
    return imported, skipped


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Importa novos PDFs do Blackboard para o material de estudo."
    )
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="Diretório local que contém os PDFs baixados.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    try:
        imported, skipped = import_pdfs(args.source.resolve(), repo_root)
    except ValueError as error:
        print(error)
        return 2
    print(f"Importados: {imported}; já existentes: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
