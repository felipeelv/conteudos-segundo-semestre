# CLAUDE.md — conteudos-segundo-semestre

> Raiz do conteúdo didático do 2º semestre de 2026 · Colégio Eleve
> **Leia este arquivo antes de qualquer tarefa nesta pasta.**

---

## 1. O que é esta pasta

O **conteúdo pronto** dos capítulos do 2º semestre, mais a metodologia e os cadernos de atividades derivados dele.

O conteúdo é **100% expositivo**: nenhum capítulo contém exercício, atividade ou proposta de trabalho. Isso não é uma falha a corrigir dentro dos capítulos — é o pressuposto do projeto. As atividades vivem em pasta separada e são **geradas a partir** dos capítulos, nunca inseridas neles.

### Escopo

| Em escopo | Fora de escopo — **não produzir, não ler, não sugerir** |
|---|---|
| 4º ano EF1 → 2ª série EM · 12 disciplinas · 193 capítulos | **Física** · **Operações** · **3ª série EM** |

As pastas `Física/` e `Operações/` existem no disco e estão fora por decisão. Se uma tarefa parecer exigi-las, **pare e pergunte**.

### As 12 disciplinas em escopo

| Disciplina | Anos | Caps. |
|---|---|---|
| Biologia | 9º, 1ª, 2ª | 10 |
| Ciências | 4º–8º | 21 |
| Estudos Sociais | 4º–9º | 34 |
| Filosofia | 1ª, 2ª | 4 |
| Geografia | 1ª, 2ª | 8 |
| Geometria | 6º–9º, 1ª, 2ª | 12 |
| História | 1ª, 2ª | 8 |
| Matemática EF1 | 4º, 5º | 18 |
| Matemática Financeira | 6º–9º, 1ª, 2ª | 12 |
| Português | 4º–9º, 1ª, 2ª | 56 |
| Química | 9º, 1ª, 2ª | 6 |
| Sociologia | 1ª, 2ª | 4 |

---

## 2. Mapa da pasta e status de cada diretório

```
conteudos-segundo-semestre/
├── CLAUDE.md                  ← este arquivo
│
├── <Disciplina>/              ← FONTE CANÔNICA · 12 pastas em escopo
│   └── <N>º Ano/  ou  <N>ª Série/
│       ├── bl1_<Disciplina>_<ano>.md     inventário do bloco 1
│       ├── bl2_<Disciplina>_<ano>.md     inventário do bloco 2
│       ├── <Título do capítulo>.md        ← UNIDADE DE PRODUÇÃO
│       └── <Título do capítulo> — Anexo.md   ← insumo de FON (marcador M5)
│
├── ATIVIDADES/
│   ├── METODOLOGIA/           ← REGRA · única fonte de decisão (arquivos 00–06)
│   ├── ATIVIDADES/            ← A GERAR · atividades de sala
│   ├── CADERNO/               ← A GERAR · atividades de casa
│   └── ACERVO/                ← MATERIAL DESCARTADO · consulta apenas
│       ├── v1-ATIVIDADES/
│       └── v1-CADERNO/
│
├── EDITADOS/                  ← MESMO conteúdo em .docx · saída para impressão
├── Física/                    ← FORA DE ESCOPO
├── Operações/                 ← FORA DE ESCOPO
└── Conteudo_docs/             ← OBSOLETA · ignorar por completo
```

### Status — o que cada um autoriza

| Diretório | Status | O que pode fazer |
|---|---|---|
| `<Disciplina>/` | **Fonte canônica** | Ler. **Nunca editar.** Nunca inserir atividade dentro de capítulo |
| `ATIVIDADES/METODOLOGIA/` | **Regra** | Ler sempre antes de produzir. Editar só quando o pedido for explicitamente sobre metodologia |
| `ATIVIDADES/ATIVIDADES/` e `ATIVIDADES/CADERNO/` | **A gerar** | Escrever a produção nova aqui |
| `ATIVIDADES/ACERVO/` | **Descartado** | Consultar se eu pedir. **Nunca usar como referência de estilo ou formato** — este material foi rejeitado |
| `EDITADOS/` | **Derivado** | Espelho em `.docx` do conteúdo. Não é fonte; se divergir do `.md`, o `.md` vence |
| `Física/`, `Operações/`, `Conteudo_docs/` | **Ignorar** | Nada |

> **Sobre o ACERVO:** os cadernos anteriores foram descartados porque a geração saiu repetitiva. Eles ficam guardados para consulta pontual, não para imitação. Se você se pegar copiando estrutura de lá, o resultado vai reproduzir exatamente o problema que o `06-PRODUCAO.md` existe para resolver.

---

## 3. Anatomia de um capítulo

Exemplo real — `Estudos Sociais/7º Ano/`:

```
bl1_EstudosSociais_7ano.md
bl2_EstudosSociais_7ano.md
Cruzadas e crise do feudalismo.md
Cruzadas e crise do feudalismo — Anexo.md
Mundo islâmico.md
Mundo islâmico — Anexo.md
...
```

| Arquivo | Papel |
|---|---|
| `bl1_` / `bl2_` | Consolidação do bloco. Use para **inventariar escopo e ordem dos capítulos** |
| `<Título>.md` | **A unidade de produção.** É este arquivo que se lê para marcar M1–M11 (`06-PRODUCAO.md` §3) |
| `<Título> — Anexo.md` | Fonte, citação ou biografia prontas. **A presença do anexo liga o marcador M5 e libera o tipo FON** |

Padrão interno do capítulo, estável em todas as disciplinas:

```
# BLn_Capítulo N — Título
> pergunta-gancho
## 1. Seção numerada
### 1.1 Subseção
   texto expositivo + lista + tabela comparativa + box
```

Boxes em circulação: `💡 Dica` · `⚠️ Atenção` · `📌 Aplicação prática` · `🔎 Curiosidade` · `💭 Você já pensou nisso?` · `⏸️ Pare e pense` · `🔍 Conexão` · `🔢 Padrão`.

---

## 4. Ordem de leitura antes de produzir

Nunca comece a gerar sem ter lido, nesta ordem:

| # | Arquivo | Por quê |
|---|---|---|
| 1 | `ATIVIDADES/METODOLOGIA/03-REPERTORIO.md` | os 18 tipos, quando **não** usar cada um, e os tipos dominantes da disciplina |
| 2 | `ATIVIDADES/METODOLOGIA/04-RUBRICAS.md` | R1–R13, total sempre 10 |
| 3 | `ATIVIDADES/METODOLOGIA/06-PRODUCAO.md` | **o arquivo operacional**: marcadores, pool, sorteio, travas, catálogo de 48 itens, molde de saída, checagens |
| 4 | `ATIVIDADES/METODOLOGIA/05-REGRAS-DE-APLICACAO.md` | quando o pedido envolver peso na nota, quantidade ou aplicação |

Os arquivos `01-PROPOSTA.md` e `02-BASE-DE-EVIDENCIA.md` são o argumento e a fundamentação — leia quando o pedido for justificar uma escolha, não para produzir.

**O `06-PRODUCAO.md` §9 tem o prompt de produção pronto.** Use-o em vez de improvisar um loop.

---

## 5. Regras rígidas de produção

1. **Um capítulo por vez.** Nunca gerar o arquivo de uma disciplina inteira de uma vez.
2. **O molde de saída de `06-PRODUCAO.md` §7 é obrigatório.** Sem seções extras, sem preâmbulo.
3. **O comando entre aspas é o texto final do aluno.** Nunca escrever *"peça que o aluno..."*.
4. **Se a resposta esperada já está impressa no capítulo em forma quase idêntica, o tipo está errado.** Re-sorteie.
5. **Sala e casa do mesmo capítulo não repetem tipo.** Os dois conjuntos cobrem os mesmos 193 capítulos por caminhos diferentes.
6. **Caderno de casa: sem gabarito, sem DEB, sem ORA.** Todo bloco de exercício precisa de conferência embutida.
7. **Nenhum dado inventado.** Se um item exige dado real e ele não existe, troque o item.
8. **Rode as 8 checagens de `06-PRODUCAO.md` §8** antes de passar ao capítulo seguinte.

---

## 6. Nunca faça

- **Não editar capítulo em `<Disciplina>/`.** Nem para corrigir, nem para inserir atividade. Se encontrar erro no conteúdo, **reporte, não conserte**.
- **Não acrescentar camada devocional às atividades.** Os capítulos tratam temas religiosos **como conteúdo** (hebreus e monoteísmo, Tomás de Aquino, cristianismo em Roma, religião em Marx). As atividades os tratam analiticamente. Decisão explícita — `05-REGRAS-DE-APLICACAO.md` §6.
- **Não usar o ACERVO como modelo.**
- **Não tocar em `Física/`, `Operações/`, `Conteudo_docs/`.**
- **Não criar arquivo sem aprovação prévia.** Apresente o resumo do que será criado e aguarde. Um arquivo por vez.
- **Não gerar exemplos ou documentos não solicitados.**
- **Não editar `EDITADOS/` para "sincronizar"** sem eu pedir.

---

## 7. Convenções de nome

- Pastas e arquivos usam **acentos e espaços** (`Estudos Sociais`, `Matemática EF1`, `7º Ano`). Sempre entre aspas em qualquer comando de shell.
- O separador do anexo é **travessão com espaços** (`—`, U+2014), não hífen: `Mundo islâmico — Anexo.md`.
- Séries do EM aparecem como `1ª`, `2ª` — ordinal feminino.
- Ao escrever arquivos novos, seguir o padrão já existente da pasta de destino.

---

## 8. Fluxo de trabalho comigo

1. Entender o pedido
2. Apresentar plano **breve**
3. Aguardar aprovação
4. Executar

Respostas diretas: problema → análise → solução. Sintético sem perder profundidade. Aponte limitação, trade-off e alternativa melhor — não concorde por padrão. Se faltar informação para avaliar algo, **diga em vez de presumir**.

Entregáveis vão para `/mnt/user-data/outputs/` quando gerados fora do repositório.
