#!/usr/bin/env python3
"""Compara a produção do 4º bimestre com os blueprints autoritativos.

Uso:
    python3 "4 bimestres/auditar-escopo.py"
    python3 "4 bimestres/auditar-escopo.py" --validar

O modo padrão confere completude, contagem e numeração. Com ``--validar``,
executa também o validador oficial de cada disciplina em todos os capítulos.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TARGET_ROOT = ROOT / "4 bimestres"
SOURCE_ROOT = Path(
    "/Users/feliperosamini/Reorganizacao-2026-2Semestre/disciplinas"
)


@dataclass(frozen=True)
class Discipline:
    source: str
    target: str
    validator_dir: str
    slug: str


DISCIPLINES = (
    Discipline("Biologia", "Biologia", "Biologia", "biologia"),
    Discipline("Ciencias", "Ciências", "Ciencias", "ciencias"),
    Discipline(
        "Estudos Sociais", "Estudos Sociais", "Estudos Sociais", "estudos-sociais"
    ),
    Discipline("Filosofia", "Filosofia", "Filosofia", "filosofia"),
    Discipline("Financeira", "Matemática Financeira", "Financeira", "financeira"),
    Discipline("Fisica", "Física", "Fisica", "fisica"),
    Discipline("Geografia", "Geografia", "Geografia", "geografia"),
    Discipline("Geometria", "Geometria", "Geometria", "geometria"),
    Discipline("Historia", "História", "Historia", "historia"),
    Discipline(
        "Matematica EF1", "Matemática EF1", "Matematica EF1", "matematica-ef1"
    ),
    Discipline("Operacoes", "Operações", "Operacoes", "operacoes"),
    Discipline("Portugues", "Português", "Portugues", "portugues"),
    Discipline("Quimica", "Química", "Quimica", "quimica"),
    Discipline("Sociologia", "Sociologia", "Sociologia", "sociologia"),
)

YEAR_DIRS = {
    "4ano": "4º Ano",
    "5ano": "5º Ano",
    "6ano": "6º Ano",
    "7ano": "7º Ano",
    "8ano": "8º Ano",
    "9ano": "9º Ano",
    "1serie": "1ª Série",
    "2serie": "2ª Série",
    "3serie": "3ª Série",
}

CAP_HEADING = re.compile(
    r"^## .*?CAPÍTULO\s+(\d+)\b.*?\((\d+)\s+aulas?\)",
    re.IGNORECASE,
)
AULA_BLUEPRINT = re.compile(r"^\*\*Aula\s+(\d+)\b", re.IGNORECASE)
AULA_TARGET = re.compile(r"^##\s+(\d+)\.\s+")
SUBSECTION_TARGET = re.compile(r"^###\s+(\d+)\.(\d+)\s+")
CAP_FILE = re.compile(r"-4bim-cap(\d+)\.md$", re.IGNORECASE)
CAP_TITLE_TARGET = re.compile(
    r"^#\s+(?:BL\d+_)?Capítulo\s+(\d+)\s+—\s+\S",
    re.IGNORECASE,
)
PLACEHOLDER_PATTERNS = (
    re.compile(r"(?:\[TODO\]|\bTODO\s*:)", re.IGNORECASE),
    re.compile(r"\bFIXME\b", re.IGNORECASE),
    re.compile(r"\bPLACEHOLDER\b", re.IGNORECASE),
    re.compile(r"conteúdo\s+a\s+desenvolver", re.IGNORECASE),
    re.compile(r"registrar\s+a\s+etapa\s+matemática\s+correspondente", re.IGNORECASE),
    re.compile(r"esse\s+enunciado\s+identifica\s+os\s+dados", re.IGNORECASE),
    re.compile(r"a\s+representação\s+deixa\s+visível\s+o\s+que\s+muda", re.IGNORECASE),
    re.compile(r"dois\s+aspectos\s+completam", re.IGNORECASE),
    re.compile(r"o\s+registro\s+de\s+.+?\s+explicita\s+quais\s+valores", re.IGNORECASE),
    re.compile(r"o\s+recorte\s+exige\s+ainda", re.IGNORECASE),
    re.compile(r"essa\s+configuração\s+torna\s+medidas,\s+posições", re.IGNORECASE),
    re.compile(r"a\s+figura\s+deve\s+conservar\s+os\s+elementos\s+essenciais", re.IGNORECASE),
    re.compile(r"aplicar\s+a\s+relação\s+geométrica\s+com\s+as\s+unidades", re.IGNORECASE),
    re.compile(r"o\s+resultado\s+descreve\s+a\s+medida\s+da\s+configuração", re.IGNORECASE),
    re.compile(r"a\s+decisão\s+começa\s+pelo\s+dado\s+observado", re.IGNORECASE),
    re.compile(r"resume\s+a\s+relação\s+principal\s+sem\s+apagar\s+o\s+contexto", re.IGNORECASE),
    re.compile(r"organizar\s+os\s+valores\s+e\s+efetuar\s+a\s+operação\s+indicada", re.IGNORECASE),
    re.compile(r"a\s+conta\s+ganha\s+sentido\s+quando\s+é\s+comparada", re.IGNORECASE),
    re.compile(r"a\s+contribuição\s+técnica\s+deve\s+ser\s+lida\s+em\s+seu\s+contexto", re.IGNORECASE),
    re.compile(r"que\s+resultado\s+os\s+dados\s+de\s+.+?\s+determinam\?", re.IGNORECASE),
    re.compile(r"domínio,\s+sinais\s+e\s+substituições\s+devem\s+ser\s+conferidos", re.IGNORECASE),
    re.compile(r"escrever\s+o\s+modelo\s+de\s+", re.IGNORECASE),
    re.compile(r"substituir\s+ou\s+transformar\s+os\s+valores", re.IGNORECASE),
    re.compile(r"obter\s+e\s+interpretar\s+o\s+resultado", re.IGNORECASE),
    re.compile(r"o\s+conceito\s+de\s+.+?\s+só\s+informa\s+algo\s+quando", re.IGNORECASE),
    re.compile(r"o\s+resultado\s+deve\s+ser\s+comparado\s+com\s+a\s+referência", re.IGNORECASE),
    re.compile(r"nele,\s+as\s+medidas\s+e\s+posições\s+necessárias\s+aparecem\s+antes\s+da\s+fórmula", re.IGNORECASE),
    re.compile(r"a\s+unidade\s+informa\s+qual\s+grandeza\s+foi\s+medida", re.IGNORECASE),
)


@dataclass
class ExpectedChapter:
    discipline: Discipline
    year_key: str
    chapter: int
    claimed_lessons: int
    lesson_numbers: list[int]
    blueprint: Path

    @property
    def year_dir(self) -> str:
        return YEAR_DIRS[self.year_key]


def blueprint_chapters(
    discipline: Discipline, year_key: str, blueprint: Path
) -> list[ExpectedChapter]:
    chapters: list[ExpectedChapter] = []
    current: ExpectedChapter | None = None

    for line in blueprint.read_text(encoding="utf-8").splitlines():
        cap_match = CAP_HEADING.match(line)
        if cap_match:
            if current is not None:
                chapters.append(current)
            current = ExpectedChapter(
                discipline=discipline,
                year_key=year_key,
                chapter=int(cap_match.group(1)),
                claimed_lessons=int(cap_match.group(2)),
                lesson_numbers=[],
                blueprint=blueprint,
            )
            continue

        aula_match = AULA_BLUEPRINT.match(line)
        if aula_match and current is not None:
            current.lesson_numbers.append(int(aula_match.group(1)))

    if current is not None:
        chapters.append(current)
    return chapters


def load_expected() -> tuple[list[ExpectedChapter], list[str]]:
    expected: list[ExpectedChapter] = []
    errors: list[str] = []

    for discipline in DISCIPLINES:
        bp_root = SOURCE_ROOT / discipline.source / "blueprints"
        if not bp_root.is_dir():
            errors.append(f"Blueprints ausentes: {bp_root}")
            continue

        for year_path in sorted(path for path in bp_root.iterdir() if path.is_dir()):
            year_key = year_path.name
            if year_key not in YEAR_DIRS:
                continue
            for filename in ("4bim-bloco1.md", "4bim-bloco23.md"):
                blueprint = year_path / filename
                if not blueprint.is_file():
                    errors.append(f"Blueprint ausente: {blueprint}")
                    continue
                expected.extend(blueprint_chapters(discipline, year_key, blueprint))

    seen: set[tuple[str, str, int]] = set()
    for chapter in expected:
        key = (chapter.discipline.target, chapter.year_key, chapter.chapter)
        if key in seen:
            errors.append(
                "Capítulo duplicado nos blueprints: "
                f"{chapter.discipline.target}/{chapter.year_key}/cap{chapter.chapter}"
            )
        seen.add(key)

        expected_sequence = list(range(1, chapter.claimed_lessons + 1))
        if chapter.lesson_numbers != expected_sequence:
            errors.append(
                f"Blueprint inconsistente: {chapter.blueprint} cap{chapter.chapter}: "
                f"declarou {chapter.claimed_lessons}, encontrou {chapter.lesson_numbers}"
            )

    return expected, errors


def target_chapter_files(year_dir: Path) -> dict[int, list[Path]]:
    result: dict[int, list[Path]] = {}
    if not year_dir.is_dir():
        return result
    for path in sorted(year_dir.glob("*.md")):
        if path.name.endswith("-anexo.md"):
            continue
        match = CAP_FILE.search(path.name)
        if match:
            result.setdefault(int(match.group(1)), []).append(path)
    return result


def inspect_target(
    path: Path, expected_chapter: int, expected_lessons: int
) -> list[str]:
    errors: list[str] = []
    lessons: list[int] = []
    current_lesson: int | None = None
    text = path.read_text(encoding="utf-8")

    title_numbers = [
        int(match.group(1))
        for line in text.splitlines()
        if (match := CAP_TITLE_TARGET.match(line))
    ]
    if title_numbers != [expected_chapter]:
        errors.append(
            f"Título: {path}: esperado Capítulo {expected_chapter}, "
            f"encontrado {title_numbers or 'nenhum H1 válido'}"
        )

    for line_number, line in enumerate(
        text.splitlines(), start=1
    ):
        aula_match = AULA_TARGET.match(line)
        if aula_match:
            current_lesson = int(aula_match.group(1))
            lessons.append(current_lesson)
            continue
        subsection_match = SUBSECTION_TARGET.match(line)
        if subsection_match and current_lesson is not None:
            subsection_lesson = int(subsection_match.group(1))
            if subsection_lesson != current_lesson:
                errors.append(
                    f"Numeração interna: {path}:{line_number}: "
                    f"aula {current_lesson}, subtítulo {subsection_match.group(0).strip()}"
                )

    expected_sequence = list(range(1, expected_lessons + 1))
    if lessons != expected_sequence:
        errors.append(
            f"Aulas: {path}: esperado {expected_sequence}, encontrado {lessons}"
        )

    if re.search(r"\n---\s*\n---\s*\n", text):
        errors.append(f"Separador horizontal duplicado: {path}")

    for pattern in PLACEHOLDER_PATTERNS:
        matches = pattern.findall(text)
        if matches:
            errors.append(
                f"Texto genérico/placeholder em {path}: padrão "
                f"{pattern.pattern!r} ({len(matches)} ocorrência(s))"
            )
    return errors


def run_validator(discipline: Discipline, path: Path) -> tuple[bool, str]:
    validator = ROOT / discipline.validator_dir / "validar-capitulo.py"
    process = subprocess.run(
        [
            sys.executable,
            str(validator),
            str(path),
            "--disciplina",
            discipline.slug,
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return process.returncode == 0, process.stdout


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--validar",
        action="store_true",
        help="executa também o validador oficial de cada disciplina",
    )
    args = parser.parse_args()

    expected, errors = load_expected()
    expected_by_group: dict[tuple[str, str], dict[int, ExpectedChapter]] = {}
    for chapter in expected:
        key = (chapter.discipline.target, chapter.year_key)
        expected_by_group.setdefault(key, {})[chapter.chapter] = chapter

    produced_chapters = 0
    produced_lessons = 0
    validators_passed = 0

    for (target_name, year_key), chapter_map in sorted(expected_by_group.items()):
        discipline = next(d for d in DISCIPLINES if d.target == target_name)
        year_dir = TARGET_ROOT / target_name / YEAR_DIRS[year_key]
        actual = target_chapter_files(year_dir)

        for chapter_number, expected_chapter in sorted(chapter_map.items()):
            matches = actual.get(chapter_number, [])
            if not matches:
                errors.append(
                    f"Arquivo ausente: {target_name}/{YEAR_DIRS[year_key]}/cap{chapter_number}"
                )
                continue
            if len(matches) > 1:
                errors.append(
                    f"Arquivos duplicados para {target_name}/{YEAR_DIRS[year_key]}/"
                    f"cap{chapter_number}: {matches}"
                )
                continue

            path = matches[0]
            produced_chapters += 1
            produced_lessons += expected_chapter.claimed_lessons
            errors.extend(
                inspect_target(
                    path,
                    expected_chapter.chapter,
                    expected_chapter.claimed_lessons,
                )
            )

            if discipline.target == "Estudos Sociais":
                annex = path.with_name(path.stem + "-anexo.md")
                if not annex.is_file():
                    errors.append(f"Anexo ausente: {annex}")

            if args.validar:
                ok, output = run_validator(discipline, path)
                if ok:
                    validators_passed += 1
                else:
                    tail = "\n".join(output.splitlines()[-25:])
                    errors.append(f"Validador reprovou {path}:\n{tail}")

        extras = sorted(set(actual) - set(chapter_map))
        for chapter_number in extras:
            errors.append(
                f"Capítulo extra: {target_name}/{YEAR_DIRS[year_key]}/"
                f"cap{chapter_number}: {actual[chapter_number]}"
            )

    expected_chapters = len(expected)
    expected_lessons = sum(chapter.claimed_lessons for chapter in expected)
    print(f"Blueprints: {expected_chapters} capítulos / {expected_lessons} aulas")
    print(f"Produção:  {produced_chapters} capítulos / {produced_lessons} aulas")
    if args.validar:
        print(f"Validadores aprovados: {validators_passed}/{produced_chapters}")

    if errors:
        print(f"\nFALHAS ({len(errors)}):")
        for error in errors:
            print(f"- {error}")
        return 1

    if args.validar:
        print("\nAUDITORIA APROVADA: escopo completo, numerado e validado.")
    else:
        print("\nAUDITORIA APROVADA: escopo completo, numerado e sem placeholders.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
