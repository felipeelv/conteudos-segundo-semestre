# Metodologia — Proposta de Atividades · 2º Semestre

> **Escopo:** 4º ano EF1 → 2ª série EM · 12 disciplinas · 47 conjuntos disciplina×ano · 193 capítulos, repartidos em **95 no Bloco 1 e 98 no Bloco 2** — os dois blocos do mesmo 3º bimestre.
> **Fora do escopo (por decisão):** Operações, Física e 3ª série EM.
> **Data:** 13/08/2026

---

## Organização das pastas

```
ATIVIDADES/
├── METODOLOGIA/   ← esta pasta: as decisões que valem para os dois conjuntos
├── CADERNO/       ← atividades de casa (sozinho, autocorreção, sem gabarito)
│   └── <Disciplina>/
│       ├── <N>º Ano.md       folha do aluno: título, cabeçalho, questões
│       └── _ORGANIZACAO.md   grade, rodapé com seed, checagem em lote, revisões
├── ATIVIDADES/    ← atividades de sala (professor, grupo, insumo, rubrica analítica)
└── ACERVO/        ← v1 descartada · v2-plano-CADERNO superada (fonte do Bloco 2)
```

Os dois conjuntos de atividades cobrem os **mesmos 193 capítulos** e **não se repetem**: quando uma atividade de sala pede troca entre duplas ou material fornecido pelo professor, a versão de casa resolve o mesmo conteúdo por outro caminho.

**Um arquivo por ano, não por disciplina.** O professor recebe a folha do ano que leciona e seleciona quais questões entram — por isso cada questão precisa ser respondível isoladamente (`06-PRODUCAO.md` §8.1) e usar só recurso que todo aluno tem (§8.2).

**Estado:** casa do Bloco 1 fechada (95 capítulos · **814 questões**, das quais **190 objetivas justificadas** — 2 por capítulo, tipo `OBJ`, rubrica R14) · casa do Bloco 2 parcial (35 capítulos, em `ACERVO/v2-plano-CADERNO/`) · sala não produzida.

---

## As seis peças desta pasta

| Arquivo | O que resolve | Quando abrir |
|---|---|---|
| `01-PROPOSTA.md` | O que este material é e o que ele não é · o **diagnóstico** dos 94 arquivos de conteúdo: o que eles favorecem, o que não permitem avaliar hoje, e o desequilíbrio de carga entre disciplinas | Antes de discutir qualquer atividade. É o argumento. |
| `02-BASE-DE-EVIDENCIA.md` | Por que cada tipo de tarefa foi escolhido: para que habilidade serve, qual a **limitação conhecida** e a referência com autor e ano | Quando alguém perguntar "por que não só exercício?" |
| `03-REPERTORIO.md` | Os **19 tipos** com código, quando usar e quando **não** usar · a distribuição dos tipos dominantes por disciplina | Ao desenhar ou trocar uma atividade |
| `04-RUBRICAS.md` | As **14 rubricas-modelo** (R1–R14), com critérios e pesos, total 10 — R14 é a da objetiva justificada | Ao corrigir, e ao entregar a rubrica ao aluno |
| `05-REGRAS-DE-APLICACAO.md` | Quantidade por bimestre · peso na nota · rubrica antes e não depois · comando verbatim · conteúdo religioso · correção amostral | Antes de aplicar o bimestre |
| `06-PRODUCAO.md` | **O arquivo operacional.** Marcadores · pool · sorteio com semente · travas (T1–T9) · **banco de 23 verbos** (§6) · catálogo de 60 itens em 19 tipos (§5) · molde da folha do aluno (§7.1, com o formato síntese → execução → `Responda:` → `Confira você mesmo:`, os **dois casos de marcador**, o complemento de localização no rótulo, a pergunta em dois tempos, os **subitens `a) b) c)` em lista Markdown** e o **molde de `OBJ`** com a calibragem por faixa etária — **três exemplos calibrados**: as transformações do 8º de Geometria, os climogramas da 1ª de Geografia e a objetiva da rodovia do 7º de Ciências) · as **14 checagens** (§8): §8.1 independência da questão · §8.2 acessibilidade do recurso · §8.3 execução individual · §8.4 qualidade do distrator | Ao gerar qualquer atividade. É o único que se abre com o teclado na mão |

---

## Índice dos arquivos de disciplina

A casa do Bloco 1 é **um arquivo por ano**, dentro da pasta da disciplina, mais um `_ORGANIZACAO.md` por disciplina. A sala ainda não existe.

| Disciplina | Anos | Caps. totais | Caps. Bl1 | Questões Bl1 | das quais `OBJ` | Casa — Bloco 1 |
|---|---|---:|---:|---:|---:|---|
| Biologia | 9º, 1ª, 2ª | 10 | 5 | 50 | 10 | `../CADERNO/Biologia/` |
| Ciências | 4º–8º | 21 | 10 | 84 | 20 | `../CADERNO/Ciências/` |
| Estudos Sociais | 4º–9º | 34 | 17 | 136 | 34 | `../CADERNO/Estudos Sociais/` |
| Filosofia | 1ª, 2ª | 4 | 2 | 20 | 4 | `../CADERNO/Filosofia/` |
| Geografia | 1ª, 2ª | 8 | 4 | 40 | 8 | `../CADERNO/Geografia/` |
| Geometria | 6º–9º, 1ª, 2ª | 12 | 6 | 48 | 12 | `../CADERNO/Geometria/` |
| História | 1ª, 2ª | 8 | 4 | 38 | 8 | `../CADERNO/História/` |
| Matemática EF1 | 4º, 5º | 18 | 8 | 72 | 16 | `../CADERNO/Matemática EF1/` |
| Matemática Financeira | 6º–9º, 1ª, 2ª | 12 | 6 | 48 | 12 | `../CADERNO/Matemática Financeira/` |
| Português | 4º–9º, 1ª, 2ª | 56 | 28 | 230 | 56 | `../CADERNO/Português/` |
| Química | 9º, 1ª, 2ª | 6 | 3 | 28 | 6 | `../CADERNO/Química/` |
| Sociologia | 1ª, 2ª | 4 | 2 | 20 | 4 | `../CADERNO/Sociologia/` |
| **Total** | **47 anos** | **193** | **95** | **814** | **190** | 47 arquivos-ano |

As instruções ao aluno que existiam na v1 — segurança, privacidade, materiais e as seis formas de conferir sozinho — estão em `../ACERVO/v1-CADERNO/CADERNO-00-Instrucoes.md` e **não foram reintroduzidas**: no formato atual, a conferência é embutida em cada questão de `EX`, como o §4 de [`03-REPERTORIO.md`](03-REPERTORIO.md) exige.

---

## Nota sobre esta pasta

Estes seis arquivos eram, até agora, as seções 1 a 7 de um único documento. Foram separados para que cada decisão possa ser revista sem mexer nas outras: a base de evidência muda quando aparece referência nova; o repertório muda quando um tipo se mostra inadequado; as rubricas mudam quando um critério não discrimina na correção; as regras de aplicação mudam a cada bimestre.

**A ordem de leitura, na primeira vez, é a numérica.** Depois, cada arquivo se abre sozinho.
