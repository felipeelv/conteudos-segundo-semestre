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
│   ├── CADERNO/               ← ENTREGA · atividades de casa · Bloco 1 fechado
│   │   └── <Disciplina>/      ← 12 pastas
│   │       ├── <N>º Ano.md    ← FOLHA DO ALUNO · só questões
│   │       └── _ORGANIZACAO.md   ← grade, rodapé com seed, checagem, revisões
│   ├── ATIVIDADES/            ← A GERAR · atividades de sala · vazia
│   └── ACERVO/                ← consulta apenas · nunca imitar
│       ├── v1-ATIVIDADES/     ← descartado (geração repetitiva)
│       ├── v1-CADERNO/        ← descartado (geração repetitiva)
│       └── v2-plano-CADERNO/  ← superado, não descartado (ver abaixo)
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
| `ATIVIDADES/CADERNO/` | **Entrega** | Bloco 1 fechado. Escrever aqui a produção nova de casa |
| `ATIVIDADES/ATIVIDADES/` | **A gerar** | Vazia. Escrever aqui o conjunto de sala quando ele for produzido |
| `ATIVIDADES/ACERVO/` | **Consulta** | Ler se eu pedir. **Nunca usar como referência de estilo ou formato** |
| `EDITADOS/` | **Derivado** | Espelho em `.docx` do conteúdo. Não é fonte; se divergir do `.md`, o `.md` vence |
| `Física/`, `Operações/`, `Conteudo_docs/` | **Ignorar** | Nada |

> **Sobre o ACERVO.** Ele guarda duas coisas diferentes, e confundi-las estraga a produção:
>
> - `v1-ATIVIDADES/` e `v1-CADERNO/` foram **descartados** porque a geração saiu repetitiva. Se você se pegar copiando estrutura de lá, vai reproduzir exatamente o problema que o `06-PRODUCAO.md` existe para resolver.
> - `v2-plano-CADERNO/` **não foi descartado, foi superado**: são os 12 arquivos consolidados de onde os arquivos-ano foram minerados. Saíram de `CADERNO/` porque trazem grade de correção e gabarito, e quem imprimisse a pasta de entrega levaria isso junto. **São o único lugar onde ficam os 35 capítulos de Bloco 2 já produzidos** — é de lá que a produção do Bloco 2 vai minerar.

### Estado da produção — 12/08/2026

| Conjunto | Bloco | Estado | Onde |
|---|---|---|---|
| **Casa** | Bloco 1 | **fechado** · 95/95 capítulos · 47 arquivos-ano · **814 questões** — 624 sorteadas no formato §7.1 v2 + **190 objetivas justificadas** (`OBJ`, 2 por capítulo) | `CADERNO/<Disciplina>/` |
| **Casa** | Bloco 2 | parcial · 35 de 98 capítulos, em formato consolidado antigo | `ACERVO/v2-plano-CADERNO/` |
| **Sala** | ambos | **não produzido** · 0 de 193 | `ATIVIDADES/ATIVIDADES/` vazia |

Três pendências abertas, todas registradas nos `_ORGANIZACAO.md` de cada disciplina:

- **T8 é inverificável hoje.** A trava compara os tipos de sala e casa do mesmo capítulo, e o conjunto de sala não existe. É a trava de maior prioridade do §4.3 e está aberta nos 95 capítulos. Ao produzir sala, confrontar tipo a tipo com a seção 2 de cada `_ORGANIZACAO.md`.
- **Travas de distribuição violadas e herdadas** — T6 (mesmo item em capítulos consecutivos), T2/T1 (teto da questão principal), T3 (piso de cobertura), T5. Fechá-las exige **re-sortear tipo**, o que nenhuma revisão fez até agora por decisão explícita: revisão preserva tipo e rubrica.
- **O banco de verbos do §6 fechou em 22** com `redija` (texto), `leia` (fonte entregue) e `calcule` (`EX`/R1). Restava só produção visual em EF1 sem verbo próprio — `elabore` cobre. Se aparecer nova lacuna, **acrescente o verbo ao §6 antes de reescrever questão**: as três rodadas anteriores mostraram que reescrever para caber num banco incompleto piora o enunciado.
- **A folha e a grade podem sair de sincronia sem que ninguém perceba.** A checagem que confronta cada `Responda:` com o "Critério que decide a nota" achou 39 divergências em 624 questões — o caso mais comum foi `ESQ` sem pedir seta rotulada, quando R4 reserva 3 dos 10 pontos justamente a isso. **Ao reescrever qualquer enunciado, releia a linha dele na seção 2 do `_ORGANIZACAO.md`**: se o critério cobra algo que a folha deixou de pedir, o professor corrige por um critério que a folha não pede mais. E confira que o critério está **no `Responda:`**, não em algum lugar qualquer da questão: em `Português 8º Cap. 2 Q2` a grade dizia *"o terceiro exemplo é o que discrimina"* e a folha pedia o exemplo na execução, fora da entrega — divergência que a checagem de 12/08 não pegou porque só comparava o bloco com o critério.

**Um registro de método, da rodada de 13/08 — o tipo `OBJ`.** A rodada acrescentou 190 questões objetivas justificadas às 47 folhas, e quatro decisões dela valem para as próximas produções:

- **A objetiva não mede a letra.** Assinalar vale 2 dos 10 pontos de R14; os outros 8 estão na justificativa de por que cada distrator está errado. É isso que torna a questão autoverificável sem gabarito na folha e que a livra da checagem 1 — a alternativa correta pode ecoar o capítulo, mas **a razão pela qual as outras falham não está impressa em lugar nenhum**.
- **Quando a eliminação convergir, mude a pergunta, não o distrator.** Em *qual destas é fruto?*, as três erradas cairiam todas por "não vem do ovário da flor". A saída foi trocar o que o `Responda:` cobra — **que estrutura é cada uma** —, e o mesmo movimento se repetiu em seis disciplinas e em catorze das 56 objetivas de Português.
- **A faixa EF1 só tem três itens** (`OBJ.d` é reservado a EF2 e EM), e dois capítulos vizinhos com duas questões cada exigiriam quatro. **T6 é aritmeticamente inviável em EF1** — a violação está registrada nos `_ORGANIZACAO.md` de Ciências, Estudos Sociais, Matemática EF1 e Português, com o rodízio que a reduz a um item por fronteira.
- **Em conteúdo politicamente disputado, a objetiva fica no conceito que o capítulo define.** Geografia (conflitos contemporâneos) e Sociologia (movimentos sociais) não trazem nenhuma alternativa que peça ao aluno julgar quem tem razão: o risco é o **distrator indecidível** que §8.4 veta.

**Um registro de método, da rodada de 12/08.** A afirmação *"as 12 disciplinas estão no formato §7.1"* era verdadeira por disciplina e falsa por folha: **8 das 47 nunca haviam sido reformatadas** — Estudos Sociais 6º a 9º, Ciências 6º (parcial), 7º e 8º, e Filosofia 2ª —, somando 126 questões em parágrafo único, sem um único bloco `Responda:`. Duas dessas folhas tinham o defeito anotado no próprio `_ORGANIZACAO.md`; as quatro de Estudos Sociais, o maior bloco, não estavam registradas em lugar nenhum. **Contar por disciplina esconde o que falta; a unidade de verificação é a folha.**

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

> **Bloco 1 e Bloco 2 são os dois blocos do MESMO 3º bimestre** — Bloco 1 de 05/08 a 25/08, Bloco 2 de 27/08 a 18/09. Não são bimestres diferentes. Os 193 capítulos do escopo são todos do 3º bimestre, repartidos entre os dois blocos: **95 no Bloco 1 e 98 no Bloco 2**. Confundir isso faz a contagem de cobertura errar por um fator de dois.
>
> A linha 3 de cada `bl1_`/`bl2_` traz o tema e as datas do bloco — copie de lá, não invente. Os anexos só existem em **Estudos Sociais** (34 arquivos); nas outras 11 disciplinas o marcador M5 nunca liga.

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
| 1 | `ATIVIDADES/METODOLOGIA/03-REPERTORIO.md` | os 19 tipos, quando **não** usar cada um, os tipos dominantes da disciplina, e por que `OBJ` fica fora do sorteio |
| 2 | `ATIVIDADES/METODOLOGIA/04-RUBRICAS.md` | R1–R14, total sempre 10 — R14 é a da objetiva justificada |
| 3 | `ATIVIDADES/METODOLOGIA/06-PRODUCAO.md` | **o arquivo operacional**: marcadores, pool, sorteio, travas T1–T9, banco de verbos (§6), catálogo de **60 itens em 19 tipos** (§5), molde de saída (§7, com o molde de `OBJ` e a calibragem por faixa etária), as **14 checagens** (§8) — com §8.1 independência, §8.2 acessibilidade, §8.3 execução individual e §8.4 qualidade do distrator |
| 4 | `ATIVIDADES/METODOLOGIA/05-REGRAS-DE-APLICACAO.md` | quando o pedido envolver peso na nota, quantidade ou aplicação |

Os arquivos `01-PROPOSTA.md` e `02-BASE-DE-EVIDENCIA.md` são o argumento e a fundamentação — leia quando o pedido for justificar uma escolha, não para produzir.

**O `06-PRODUCAO.md` §9 tem o prompt de produção pronto.** Use-o em vez de improvisar um loop.

---

## 5. Regras rígidas de produção

1. **Um capítulo por vez, dentro do agente.** Cada capítulo é lido, marcado e sorteado isoladamente — nunca gerar a disciplina inteira num só passe de raciocínio. Em produção por workflow, o recorte é **um agente por disciplina**, e esse agente percorre os capítulos um a um; a validação vem depois, em agente separado, e não pode re-sortear tipo nem rubrica.
2. **O molde de saída de `06-PRODUCAO.md` §7 é obrigatório.** Sem seções extras, sem preâmbulo.
3. **O comando entre aspas é o texto final do aluno.** Nunca escrever *"peça que o aluno..."*.
4. **Se a resposta esperada já está impressa no capítulo em forma quase idêntica, o tipo está errado.** Re-sorteie.
5. **Sala e casa do mesmo capítulo não repetem tipo.** Os dois conjuntos cobrem os mesmos 193 capítulos por caminhos diferentes.
6. **Caderno de casa: sem gabarito na folha, sem DEB, sem ORA.** Todo bloco de exercício precisa de conferência embutida. O gabarito das `OBJ` é a única resposta registrada, e fica no `_ORGANIZACAO.md`.
7. **Nenhum dado inventado.** Se um item exige dado real e ele não existe, troque o item.
8. **Cada questão é independente** (`06-PRODUCAO.md` §8.1). O professor seleciona o que entra na folha, e nem tudo entra — uma questão que dependa de outra quebra quando a outra é descartada. Proibido *"a tabela que você construiu na questão 2"*.
9. **Só recurso que todo aluno tem** (§8.2): capítulo, caderno, lápis, material de geometria (régua, compasso, transferidor), calculadora comum, observação e raciocínio. Nada de termômetro, balança, cronômetro, celular, internet, impressora, deslocamento, compra ou **calculadora financeira**.
10. **Casa se faz sozinho** (§8.3). Nenhuma questão exige ação, resposta ou presença de outra pessoa — conversar, perguntar, entrevistar, pedir que confiram. `INV.d` (entrevista) só em sala, como `DEB` e `ORA`. Destinatário de escrita é **leitor hipotético** (*quem faltou à aula*, *um leitor que discorda*) e a palavra **"colega" não entra na folha de casa**.
11. **O verbo do comando sai do banco do §6 e é aferido no enunciado-síntese** (§7.1). `construa` produz figura com instrumento · `elabore`, artefato sem instrumento · `redija`, texto. Os imperativos internos da execução (*trace*, *marque*, *percorra*) não são verbos de comando.
12. **A folha separa fazer de entregar** (§7.1). Enunciado-síntese → execução em prosa compacta → `Responda:` em pergunta → `Confira você mesmo:`. Nunca etapas rotuladas ("Etapa 1 — a malha"), nunca a questão inteira em lista plana. **Marcador só em dois casos:** (a) sub-sequência cuja ordem importa — a construção com régua e compasso, a sequência de teclas da calculadora; (b) especificações paralelas de um mesmo produto — as colunas de uma tabela, os elementos que um mapa precisa ter. O marcador lista requisito verificável, nunca entrega o artefato montado.
13. **O `Responda:` admite complemento de localização e abre nos dois tempos** (§7.1). `Responda, abaixo dos gráficos:` quando a questão gera produto na página; e pergunta que comprime dois raciocínios se desdobra — *apontar o fator que explica a maior diferença* vira *qual é a maior diferença, e que fator a explica?*. Ao abrir o segundo tempo, a linha da grade acompanha na mesma passada.
14. **Toda folha traz 2 questões objetivas por capítulo** (`OBJ`, tipo 19), ao final do bloco daquele capítulo, numeradas em continuidade. Elas **não são sorteadas** e nunca são a atividade principal: escolhem-se duas confusões conceituais distintas do capítulo (T9). A síntese usa `assinale` e **anuncia a eliminação na primeira frase**; o `Responda:` cobra a letra **e** por que cada distrator está errado; o `Confira você mesmo:` aponta a estrutura das eliminações **sem revelar a letra**. Alternativas por faixa: **3 no EF1** (uma eliminação cobrada) · **4 no EF2 e no EM** (as três, com o tipo de erro nomeado no EM).
15. **O gabarito das `OBJ` vive na grade do `_ORGANIZACAO.md`, nunca na folha.** A linha traz a letra e o motivo de eliminação esperado de cada distrator — é a eliminação que decide 8 dos 10 pontos de R14.
16. **Rode as 14 checagens de `06-PRODUCAO.md` §8** antes de passar ao capítulo seguinte. A 14ª é a dos distratores (§8.4): erro plausível, motivo próprio para cada um, comprimento parecido, e nada de *"todas as anteriores"*.

---

## 6. Nunca faça

- **Não editar capítulo em `<Disciplina>/`.** Nem para corrigir, nem para inserir atividade. Se encontrar erro no conteúdo, **reporte, não conserte**.
- **Não acrescentar camada devocional às atividades.** Os capítulos tratam temas religiosos **como conteúdo** (hebreus e monoteísmo, Tomás de Aquino, cristianismo em Roma, religião em Marx). As atividades os tratam analiticamente. Decisão explícita — `05-REGRAS-DE-APLICACAO.md` §6.
- **Não usar `v1-ATIVIDADES/` nem `v1-CADERNO/` como modelo.** Aquele material foi rejeitado. `v2-plano-CADERNO/` é caso diferente: serve para **minerar conteúdo já aprovado**, não para copiar formato — o formato vigente é o dos arquivos-ano.
- **Não pôr grade, rubrica, tipo, seed ou instrução ao professor no arquivo-ano.** A folha do aluno tem título, cabeçalho e questões. Todo o resto vai para o `_ORGANIZACAO.md`.
- **Não rotular tempo nem lugar na folha** — nada de *"⏱ 50 min"*, nada de *"🏠 em casa"* (`06-PRODUCAO.md` §7.4). Duração é gestão de aula e vai para a grade; o conjunto já está no caminho do arquivo. **Linha de material só quando há material a declarar**, e nunca para listar o que o §8.2 já garante.
- **Não tocar em `Física/`, `Operações/`, `Conteudo_docs/`.**
- **Não criar arquivo sem aprovação prévia.** Apresente o resumo do que será criado e aguarde. Aprovado o plano, um workflow pode escrever o lote inteiro — o que a regra veda é começar a escrever sem o plano aprovado.
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
5. **Todo ajuste de regra, formato ou estrutura atualiza, na mesma entrega, toda a documentação que o cita** — este `CLAUDE.md`, o `00-LEIA-ME.md`, o `06-PRODUCAO.md` e os `_ORGANIZACAO.md` afetados — e termina com commit e push. Regra que vive só na conversa não existe: a próxima sessão produz pelo que está escrito.

Respostas diretas: problema → análise → solução. Sintético sem perder profundidade. Aponte limitação, trade-off e alternativa melhor — não concorde por padrão. Se faltar informação para avaliar algo, **diga em vez de presumir**.

Entregáveis vão para `/mnt/user-data/outputs/` quando gerados fora do repositório.
