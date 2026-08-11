# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é este repositório

Repositório de **conteúdo didático**, não de software. Material do **3º bimestre / 2º semestre de 2026** do Colégio Eleve, em Markdown, do 4º ano do EF1 à 3ª série do EM — 14 disciplinas, 283 capítulos, 500 arquivos `.md`.

**Não há build, testes, linter, gerenciador de pacotes nem CI.** Não procure `package.json`, `Makefile`, `requirements.txt` — não existem, e não devem ser criados sem pedido explícito. A verificação aqui é de **consistência textual** (ver [Verificações](#verificações)).

Tudo está em **português brasileiro**: conteúdo, nomes de arquivo, nomes de pasta e mensagens de commit. Escreva em português.

## As quatro árvores

| Árvore | O que é | Editar? |
|---|---|---|
| `<Disciplina>/<Ano ou Série>/` | **Fonte canônica.** Todo o Markdown de conteúdo. | Sim |
| `ATIVIDADES/` | Sistema de proposta de atividades (metodologia + sala + casa). | Sim |
| `EDITADOS/<DISCIPLINA> EDITADO - OK/<GRADE>/` | Só atalhos `.gdoc` para o Google Drive — a esteira de revisão editorial. | Não |
| `Conteudo_docs/<Disciplina>/<Ano>/3º Bimestre/` | Par `.md` + `.gdoc` da versão exportada para o Google Docs (hoje só Estudos Sociais). | Ver abaixo |

Nomes de série divergem entre as árvores: o conteúdo usa `4º Ano`…`9º Ano` e `1ª Série`…`3ª Série`; `EDITADOS/` usa `4ANO`…`9ANO` e `1EM`/`2EM`/`3EM`.

Arquivos `.gdoc` são ponteiros JSON do Google Drive (`{"doc_id": …}`), não documentos. O próprio conteúdo avisa: *"NÃO EDITE ESTE ARQUIVO. TODAS AS ALTERAÇÕES FEITAS SERÃO PERDIDAS."*

O `.md` dentro de `Conteudo_docs/` **não** é cópia do canônico — é a variante preparada para o Google Docs: sem o cabeçalho de bloco (começa direto no título do capítulo como `#`) e com os *callouts* achatados em uma linha só. Alterar o canônico não propaga para lá.

## A arquitetura central: bloco = cabeçalho + capítulos concatenados

Cada pasta `<Disciplina>/<Ano>/` contém dois tipos de `.md`, e **o mesmo texto vive nos dois**:

```
Geografia/1ª Série/
├── bl1_Geografia_1serie.md   ← BLOCO: cabeçalho + Clima + Ciclo hidrológico, verbatim
├── bl2_Geografia_1serie.md   ← BLOCO: cabeçalho + Hidrografia + Biomas e solos
├── Clima.md                  ← CAPÍTULO avulso
├── Ciclo hidrológico e bacias hidrográficas.md
├── Hidrografia - rios, usos e bacias brasileiras.md
└── Biomas e solos.md
```

O arquivo de bloco é a compilação: cabeçalho do bloco, `---`, e então o corpo de cada capítulo daquele bloco copiado **literalmente**, separado por `---`.

> **Consequência prática, e a principal armadilha do repositório:** editar um capítulo exige aplicar a mesma edição dentro do arquivo `bl*` correspondente, e vice-versa. Não há geração automática. Quatro pares já estão dessincronizados hoje (`Física/1ª Série`, `Física/2ª Série`, `Geometria/6º Ano`) — rode a verificação antes e depois de mexer.

### Nomenclatura

**Bloco:** `bl<1|2>_<DisciplinaSemAcentoNemEspaço>_<Nano|Nserie>.md`
`bl1_Geografia_1serie.md` · `bl2_EstudosSociais_9ano.md` · `bl1_MatematicaFinanceira_7ano.md` · `bl1_Fisica_6ano.md`

**Capítulo:** o nome do arquivo é o título que aparece depois do travessão no `#`. Quando o título tem `:` ou `—`, o nome do arquivo troca por ` - ` (limitação de sistema de arquivos):

```
# BL1_Capítulo 1 — Origens de Roma: Monarquia e República
→ Origens de Roma - Monarquia e República.md
```

**Anexo:** `<Título> — Anexo.md`, com `# Anexo — BL1_Capítulo N: <Título>`. Só Estudos Sociais tem anexos (34, um por capítulo), e eles **não** entram nos arquivos de bloco.

## Convenções de escrita

### Cabeçalho de bloco

```markdown
# Geografia — 1ª Série · Bloco 1

> **3º Bimestre — Clima, hidrografia e biomas** · Bloco 1 (05/08–25/08)

**Capítulos deste bloco**

1. **Clima** (7 aulas)
2. **Ciclo hidrológico e bacias hidrográficas** (2 aulas)

---
```

As datas são fixas no bimestre inteiro: **Bloco 1 = 05/08–25/08**, **Bloco 2 = 27/08–18/09**.

### Corpo do capítulo

`#` título · citação-gancho (uma pergunta que abre o assunto) · `---` · seções `## N.` e subseções `### N.M`, numeradas e sequenciais · `---` entre seções de topo. Termos técnicos entram em **negrito** na primeira ocorrência.

### Callouts

Vocabulário fechado — reutilize, não invente rótulo novo:

`⚠️ **Atenção**` · `🔢 **Padrão**` · `💭 **Você já pensou nisso?**` · `🔎 **Curiosidade**` · `💡 **Dica**` · `📌 **Aplicação prática**` · `⚡ **Física no Dia a Dia**`

Convivem **duas** formas. Siga a que o arquivo já usa:

```markdown
> 🔎 **Curiosidade:** Torricelli criou o barômetro de mercúrio em 1643.
```
```markdown
> 🔎 **Curiosidade:**
>
> Cerca de 45% da população brasileira se declarou parda no Censo de 2022.
```

A forma de uma linha domina em Geografia, História, Filosofia e Sociologia; a de três linhas, em Estudos Sociais, Geometria e Matemática Financeira.

### Matemática

`$$…$$` para fórmula **e** para símbolo no meio da frase — não use `$…$`. Resoluções seguem o padrão `**Resolução:**` → `- **Passo 1:** …` → `**Resposta:** …`. Decimal com vírgula protegida: `16{,}7`.

### Imagens

Quase todas vêm de um repositório externo, `felipeelv/imagens-tikz`, envoltas em marcadores de origem:

```markdown
<!-- tikz:inicio fig-01-equilibrio-estatico-e-dinamico -->
![Comparação entre corpo em repouso e corpo em MRU, ambos com resultante nula](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/leis-de-newton/fig-01-equilibrio-estatico-e-dinamico.png)
<!-- tikz:fim fig-01-equilibrio-estatico-e-dinamico -->
```

Só Matemática EF1, Geometria, Física e Química têm figuras. A URL às vezes aponta para `main`, às vezes para um SHA fixo — as duas formas estão em uso e é justamente onde bloco e capítulo mais divergem. O `alt` é sempre uma frase descritiva completa em português, não um rótulo.

Exceção única: `Geometria/6º Ano/bl1_Geometria_6ano.md` usa arquivos locais em `imagens/bl1-geometria-6ano/` (par `.svg` + `.png`, o Markdown referencia o `.png`), junto de um `bl1_Geometria_6ano_com_imagens.docx`.

### Anexos (Estudos Sociais)

Três seções `##` fixas, sempre nesta ordem: **`Enquanto isso…`** (contexto lateral) · **`E para hoje…`** (versículo bíblico + leitura ética) · **`Esse foi o "cara"`** (perfil biográfico terminado em `🏛️ **Legado:**`). O eixo bíblico é deliberado nos anexos e igualmente deliberado **fora** deles.

## O sistema ATIVIDADES

Subprojeto próprio, com metodologia declarada. Leia `ATIVIDADES/METODOLOGIA/00-LEIA-ME.md` antes de tocar em qualquer atividade.

```
ATIVIDADES/
├── METODOLOGIA/   00-LEIA-ME · 01-PROPOSTA · 02-BASE-DE-EVIDENCIA · 03-REPERTORIO · 04-RUBRICAS · 05-REGRAS-DE-APLICACAO
├── ATIVIDADES/    atividades de sala — um arquivo por disciplina
└── CADERNO/       atividades de casa — um arquivo por disciplina, mesmo nome-base
```

Os dois conjuntos cobrem os **mesmos 193 capítulos** e **não se repetem**: onde a versão de sala pede troca entre duplas ou insumo do professor, a de casa resolve o mesmo conteúdo por outro caminho.

**Fora do escopo por decisão:** Operações, Física e 3ª série EM — existem como conteúdo, não têm atividades. Não "complete" essa lacuna sem pedido.

Ao escrever ou editar uma atividade:

- **Tipo** vem dos 18 códigos de `03-REPERTORIO.md` (`EX`, `MC`, `LT`, `ESQ`, `TAB`, `ESC`, `RED`, `RET`, `FON`, `INV`, `ERR`, `DEB`, `CASO`, `MOD`, `VIS`, `CONS`, `ORA`, `POR`). A coluna que decide é *"quando **não** usar"*.
- **Rubrica** é referenciada por código (`R1`–`R13`, total sempre 10) de `04-RUBRICAS.md`. Descreva só o **ajuste** local; nunca reescreva a rubrica inteira dentro do arquivo de disciplina.
- **O texto entre aspas é o comando literal do aluno.** Trocar o verbo (*descreva* / *explique* / *justifique* / *decida* / *prove*) troca a tarefa e a rubrica que a avalia.
- Toda atividade de casa termina em **Confira você mesmo** — uma das seis formas de autocorreção de `CADERNO/CADERNO-00-Instrucoes.md` — e em ficha de autoavaliação. Não há gabarito no caderno, por desenho.
- Referências entre arquivos são caminhos relativos (`../METODOLOGIA/04-RUBRICAS.md`). Mantenha-os válidos.

## Verificações

Não há suíte de testes. Estas duas checagens cobrem o que costuma quebrar.

**Bloco × capítulo em sincronia** — a mais importante, rode sempre que editar conteúdo:

```bash
python3 - <<'PY'
import pathlib, re
for ch in sorted(pathlib.Path('.').glob('*/*/*.md')):
    if ch.parts[0] in {'ATIVIDADES','Conteudo_docs','EDITADOS'}: continue
    if ch.name.startswith('bl') or 'Anexo' in ch.name: continue
    m = re.match(r'# (BL\d)_', ch.read_text().splitlines()[0])
    if not m: print('SEM CABEÇALHO BL:', ch); continue
    bl = list(ch.parent.glob(m.group(1).lower() + '_*.md'))
    if len(bl) != 1: print('BLOCO AMBÍGUO:', ch); continue
    if ch.read_text().strip() not in bl[0].read_text():
        print('DESSINCRONIZADO:', ch)
PY
```

**Nome de arquivo × título do H1:**

```bash
python3 - <<'PY'
import pathlib, re
for f in sorted(pathlib.Path('.').glob('*/*/*.md')):
    if f.parts[0] in {'ATIVIDADES','Conteudo_docs','EDITADOS'} or f.name.startswith('bl'): continue
    h = f.read_text().splitlines()[0]
    m = re.match(r'# BL\d_Capítulo \d+ — (.+)$', h) or re.match(r'# Anexo — BL\d_Capítulo \d+: (.+)$', h)
    if not m: print('H1 FORA DO PADRÃO:', f, '|', h); continue
    want = m.group(1) + (' — Anexo' if 'Anexo' in f.name else '')
    if f.stem != want and f.stem != re.sub(r'\s*[:—]\s*', ' - ', want):
        print('NOME ≠ TÍTULO:', f, '|', h)
PY
```

## Particularidades do ambiente

**Índice do git vazio ao abrir a sessão.** Em container novo o repositório pode aparecer em `HEAD` destacado com o índice vazio — `git status` então lista **todos os 910 arquivos como deletados**, mesmo estando no disco. Não commite isso. Reconstrua o índice a partir do `HEAD`, sem tocar no working tree:

```bash
git reset -q HEAD    # depois disso, git status fica limpo
```

**Um caminho longo demais para o Linux.** `EDITADOS/PORTUGUÊS EDITADO - OK/4ANO/BL2_CAP1,CAP2,CAP3 E CAP4_OK/BL2_Capítulo 1 — …` tem nome de arquivo de 261 bytes e estoura o limite de 255 do sistema de arquivos: está no `HEAD` mas nunca chega ao disco, e o `git reset` acima imprime `File name too long` para ele. É esperado. Não remova a entrada do índice para "resolver".

**Acentos e caracteres especiais em caminhos** são a regra, não a exceção. Cite sempre os caminhos no shell, e prefira Glob/Grep/Read a `find | while read`.
