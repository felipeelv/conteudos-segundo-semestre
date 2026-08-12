# 06 · Regras de produção

> Metodologia · Proposta de Atividades 2º Semestre · [índice](00-LEIA-ME.md)
> **Escopo:** produção dos dois conjuntos (sala e casa) para os 193 capítulos.

Os arquivos 01 a 05 dizem **o que** o material é e **como aplicá-lo**. Este diz **como produzi-lo** — e existe porque a geração capítulo a capítulo estava saindo repetitiva.

---

## 1. O diagnóstico da geração

A repetição não vem de falta de repertório. Vem de três buracos entre o repertório e o texto que o aluno lê:

| Buraco | Efeito na geração |
|---|---|
| **Falta a camada de item.** Os 18 tipos são macro-tarefas. Entre "esta atividade é um MC" e o comando final não há nada especificado | O gerador preenche o vazio sozinho, e preenche sempre do mesmo jeito. 193 capítulos com a mesma cara |
| **A escolha do tipo está em prosa** (seção 2 do [`03-REPERTORIO.md`](03-REPERTORIO.md)) | Prosa se interpreta; tabela de decisão se executa. Interpretação converge para o tipo mais fácil de escrever |
| **Não há molde de saída** | Cada arquivo sai com estrutura própria. Nada é comparável, nada é revisável em lote |

> **Randômico puro não resolve — quebra.** Sortear livremente entre os 18 contradiz a regra do próprio repertório: *se a resposta esperada já está impressa no capítulo em forma quase idêntica, o tipo está errado*. Um sorteio cego coloca TAB em capítulo que já termina em tabela e LT em capítulo de datas decorativas.
>
> O que se quer é **variedade sob restrição**: sorteio dentro de um pool elegível, com travas de repetição e semente reprodutível.

---

## 2. As três camadas

Toda atividade é decidida em três níveis, nesta ordem. O nível 1 já existe; os níveis 2 e 3 são o que este arquivo acrescenta.

```
Nível 1 · TIPO      (18 códigos)         → o que a tarefa é          → 03-REPERTORIO
Nível 2 · ITEM      (56 formatos)        → como a tarefa é montada   → §5 deste arquivo
Nível 3 · COMANDO   (banco de verbos)    → o que o aluno lê          → §6 deste arquivo
```

Dois MC podem ser tarefas completamente diferentes — "monte o mapa" e "este mapa tem duas setas sem rótulo e um conceito intruso" medem coisas distintas. **A variação que mais importa é a do nível 2, não a do nível 1.**

### Tipo → rubrica padrão

Mapeamento fixo. A rubrica sai do tipo, não do sorteio.

| Tipo | Rubrica padrão | Alternativa aceita | Observação |
|---|---|---|---|
| EX | R1 | — | |
| MC | R2 | — | |
| LT | R3 | — | |
| ESQ | R4 | — | |
| TAB | R10 | R2 | R10 com ajuste: *correção da informação* = critérios paralelos corretos |
| ESC | R5 | — | |
| RED | R6 | — | exige v2 ([`05`](05-REGRAS-DE-APLICACAO.md), regra 4) |
| RET | R6 se houver reescrita | R5 se entrega única | |
| FON | R7 | — | |
| INV | R8 | — | |
| ERR | R11 | — | |
| DEB | R9 | — | só no conjunto de sala |
| CASO | R12 | R5 | R12 com ajuste: *tradução* = leitura do caso; *interpretação* = justificativa da decisão |
| MOD | R12 | — | |
| VIS | R10 | — | |
| CONS | R10 | R1 | R10 com ajuste: *correção da informação* = correção da construção |
| ORA | R9 | — | só no conjunto de sala |
| POR | R13 | — | 1× por bimestre, na integradora |

---

## 3. Elegibilidade: do capítulo ao pool

Antes de sortear, ler o arquivo do capítulo e marcar quais dos onze marcadores estão presentes. Todos são detectáveis por leitura ou por `grep`.

| # | Marcador no capítulo | Como detectar | **Libera** | **Proíbe** |
|---|---|---|---|---|
| M1 | Exemplo resolvido com `Passo 1/2/3` + `Resposta` | `grep -c "Passo 1"` | ERR · MOD · CONS | EX espelhado no exemplo |
| M2 | Subseção termina em tabela comparativa | linha iniciada por `|` no fim de seção | MC · CASO · ESQ | TAB com os mesmos critérios |
| M3 | 5+ datas em seções distantes | `grep -oE "[0-9]{3,4} ?(a\.C\.)?"` | **LT (avaliar primeiro)** | — |
| M4 | Definição em negrito isolada (`**X** é...`) | `grep -E "^\*\*[A-ZÁ-Ú]"` | ESC · MC · CASO | — |
| M5 | Anexo com fonte, citação ou biografia | pasta de anexos da disciplina | **FON** | — |
| M6 | Fenômeno observável com material de casa | leitura | INV | — |
| M7 | Conteúdo espacial (região, fluxo, relevo, planta) | leitura | VIS | — |
| M8 | Processo, etapa, ciclo | leitura | ESQ | TAB |
| M9 | Tese com contraponto legítimo | leitura | DEB (sala) · ESC.c (casa) | EX |
| M10 | Figura pronta em TikZ (Geometria) | `grep "tikz"` | CONS | EX espelhado na figura |
| M11 | Conteúdo metalinguístico (Português) | leitura | EX · RET | INV |

**Fórmula do pool:**

```
pool = (dominantes da disciplina em 03 §3)
     ∪ (tipos liberados pelos marcadores presentes)
     − (tipos proibidos pelos marcadores presentes)
     − (DEB, ORA, se conjunto = CASA)
```

Se o pool ficar com menos de 3 tipos, o capítulo vai para revisão manual — não force o sorteio.

---

## 4. Algoritmo de sorteio

### 4.1 Semente

Determinística, por capítulo:

```python
import random, hashlib

def rng(disciplina, ano, cap, conjunto):
    chave = f"{disciplina}|{ano}|{cap}|{conjunto}"
    semente = int(hashlib.sha256(chave.encode()).hexdigest()[:8], 16)
    return random.Random(semente)
```

Variedade reprodutível: re-rodar a disciplina inteira devolve exatamente o mesmo resultado. Se um capítulo sair ruim, muda-se só ele (acrescentando `|v2` à chave) sem mexer nos outros.

### 4.2 Ordem de decisão

```
1. montar o pool (§3)
2. sortear TIPO da atividade principal        → aplicar travas T1, T2, T3, T8
3. sortear 2 TIPOS complementares do pool      → aplicar trava T4
4. sortear ITEM de cada tipo (§5)              → aplicar trava T6
5. derivar RUBRICA do tipo (§2)                → aplicar trava T5
6. sortear VERBO compatível com a rubrica (§6)
7. escrever o comando verbatim e os insumos
```

### 4.3 Travas

| # | Trava | Por quê |
|---|---|---|
| T1 | Tipo da principal ≠ tipo da principal dos capítulos vizinhos (janela 2) | evita bloco monótono |
| T2 | Nenhum tipo passa de **40%** das principais da disciplina — exceto **EX** em Matemática EF1 e Português, teto **55%** | preserva o desequilíbrio deliberado de [`03`](03-REPERTORIO.md) §4 sem deixá-lo virar monocultura |
| T3 | Cada tipo dominante listado em [`03`](03-REPERTORIO.md) §3 aparece **ao menos 1×** por ano | piso de cobertura |
| T4 | As 2 complementares têm tipos ≠ do principal e ≠ entre si | três formas diferentes por capítulo |
| T5 | No máximo 2 capítulos consecutivos com a mesma rubrica | facilita a correção variada e evita R1 em cadeia |
| T6 | Mesmo item (ex.: `EX.a`) não repete em capítulos consecutivos da disciplina | é aqui que mora a repetição percebida |
| T7 | **Casa:** DEB e ORA fora do pool; todo EX usa item com conferência embutida (`EX.a`, `EX.c`, `EX.d`) | [`03`](03-REPERTORIO.md) §4, caderno sem gabarito |
| T8 | Sala e casa do **mesmo capítulo** têm tipos diferentes | [`00-LEIA-ME.md`](00-LEIA-ME.md): "não se repetem" |

Trava violada → re-sortear dentro do pool (máximo 5 tentativas). Esgotadas, aceitar a violação de menor peso nesta ordem de prioridade: **T8 > T7 > T2 > T1 > T6 > T5 > T4 > T3** — e registrar a exceção no rodapé do capítulo.

### 4.4 Calibragem de tempo, não de quantidade

Regra já fixada em [`01`](01-PROPOSTA.md) §2.5 e que o gerador precisa obedecer:

| Capítulos no ano | Tempo da principal | Caráter |
|---|---|---|
| 2–3 | 60–90 min | maior, integradora, produto único |
| 4–6 | 40–50 min | média |
| 7–9 | 20–30 min | curta e encadeada — o resultado de uma alimenta a seguinte |

Desvios já registrados que o gerador **não** deve tentar corrigir: Estudos Sociais com 1 atividade de casa por capítulo; Português reorganizado em 24 conjuntos didáticos.

---

## 5. Catálogo de itens

Os 56 formatos, em 18 tipos. O sorteio do nível 2 acontece aqui.
Marcados com **✓conf** os itens que trazem conferência embutida — os únicos admissíveis para EX no caderno de casa.

### EX — exercício / prática de recuperação
| Código | Formato |
|---|---|
| EX.a | Bloco graduado em 3 níveis (direto → com obstáculo → invertido), com conferência ao final **✓conf** |
| EX.b | Bloco curto + **1 item que a tabela do capítulo não responde** (o "porquê") |
| EX.c | Cadeia: o resultado do item *n* é o insumo do item *n+1*; se a cadeia não fecha, há erro atrás **✓conf** |
| EX.d | Par contrastante: dois enunciados quase idênticos em que uma palavra muda a operação **✓conf** |

### MC — mapa mental / conceitual
| Código | Formato |
|---|---|
| MC.a | Lista fechada de 8–12 conceitos dada; **toda linha precisa de rótulo** |
| MC.b | Lista com 2 conceitos intrusos, a descartar **e justificar** |
| MC.c | Mapa-esqueleto com conceitos prontos e **setas sem rótulo** — o aluno só nomeia as relações |

### LT — linha do tempo
| Código | Formato |
|---|---|
| LT.a | Marcos dados; **frase de nexo causal obrigatória entre cada par consecutivo** |
| LT.b | Marcos embaralhados, incluindo 2 fora do recorte, a descartar com justificativa |
| LT.c | Duas faixas paralelas (ex.: política / social) com 3 ligações cruzadas obrigatórias |

### ESQ — esquema / fluxograma / ciclo
| Código | Formato |
|---|---|
| ESQ.a | Converter texto corrido do capítulo em fluxograma com setas rotuladas |
| ESQ.b | Esquema com **uma etapa removida**: identificar qual falta e inseri-la |
| ESQ.c | Ciclo com entradas e saídas nomeadas + "o que acontece se parar em X" |

### TAB — tabela construída pelo aluno
| Código | Formato |
|---|---|
| TAB.a | Tabela com **um critério novo**, ausente do capítulo |
| TAB.b | Tabela de contraste + linha final "onde as duas se parecem" |
| TAB.c | Preencher a partir de **3 casos concretos**, não de definições |

### ESC — escrita curta
| Código | Formato |
|---|---|
| ESC.a | Explicação a destinatário nomeado (colega que faltou, irmão de 8 anos), extensão fixa |
| ESC.b | Verbete de 5 linhas com 3 termos obrigatórios |
| ESC.c | Parágrafo com **objeção obrigatória**: "alguém poderia dizer que… mas…" |
| ESC.d | Texto em 1ª pessoa de um personagem, com 3 fatos verificáveis no capítulo |

### RED — produção de gênero com reescrita
| Código | Formato |
|---|---|
| RED.a | Ciclo completo: produção → devolutiva pela rubrica → versão 2 |
| RED.b | Texto-modelo defeituoso fornecido: apontar as falhas, depois produzir o próprio |

### RET — retextualização
| Código | Formato |
|---|---|
| RET.a | Mudança de gênero (notícia → verbete; norma → cartaz) |
| RET.b | Mudança de registro + **quadro do que mudou e por quê** |
| RET.c | Mesmo conteúdo para dois interlocutores diferentes, lado a lado |

### FON — análise de fonte
| Código | Formato |
|---|---|
| FON.a | Fonte única + roteiro: autoria · data · finalidade · **o que a fonte não diz** |
| FON.b | Duas fontes divergentes: decidir qual sustenta qual afirmação |
| FON.c | Gráfico ou tabela + uma pergunta que o dado **não** responde |

### INV — investigação
| Código | Formato |
|---|---|
| INV.a | Experimento com **controle** e previsão escrita antes de medir **✓conf** |
| INV.b | Medição repetida 3× + registro da variação **✓conf** |
| INV.c | Levantamento no ambiente (rua, casa, feed, conta de luz) com categorias fechadas antes |
| INV.d | Entrevista com roteiro fechado — sujeita às regras de privacidade de [`05`](05-REGRAS-DE-APLICACAO.md) |

### ERR — análise de erro
| Código | Formato |
|---|---|
| ERR.a | Resolução alheia com **1 erro plausível**, a localizar e explicar |
| ERR.b | Duas resoluções com respostas plausíveis; só uma correta |
| ERR.c | Resolução **certa com justificativa errada** — o caso mais difícil |

### DEB — debate *(só sala)*
| Código | Formato |
|---|---|
| DEB.a | Júri simulado com papéis e ficha de evidência preenchida antes |
| DEB.b | Debate com **troca de lado obrigatória** na metade |
| DEB.c | Mesa com posição **atribuída por sorteio**, não escolhida |

### CASO — estudo de caso
| Código | Formato |
|---|---|
| CASO.a | Caso com dado numérico + critério explícito de decisão |
| CASO.b | Caso com **dado insuficiente**: dizer o que falta e por quê |
| CASO.c | Mesma decisão sob dois critérios → duas respostas igualmente defensáveis |

### MOD — modelagem / projeto
| Código | Formato |
|---|---|
| MOD.a | Situação real com dado **coletado pelo aluno** |
| MOD.b | Modelo dado + teste de limite: "até onde ele vale?" |
| MOD.c | Dois planos comparados sob o mesmo modelo |

### VIS — produção visual
| Código | Formato |
|---|---|
| VIS.a | Croqui ou mapa com legenda e título obrigatórios |
| VIS.b | Infográfico de 1 página: 3 dados + 1 conclusão escrita |
| VIS.c | HQ de 4 quadros com o conceito correto no terceiro |
| VIS.d | Perfil, corte ou mapa de fluxos |

### CONS — construção geométrica
| Código | Formato |
|---|---|
| CONS.a | Construção com régua e compasso + justificativa da propriedade usada |
| CONS.b | Planificação → montagem → verificação de medida **✓conf** |
| CONS.c | Malha: transformar a figura e registrar o que mudou e o que permaneceu **✓conf** |

### ORA — oralidade *(só sala)*
| Código | Formato |
|---|---|
| ORA.a | Explicação gravada de 90 s para leigo |
| ORA.b | Seminário-relâmpago: 5 min, 1 slide |
| ORA.c | Podcast em dupla a partir de uma pergunta-guia |

### POR — portfólio
| Código | Formato |
|---|---|
| POR.a | Seleção justificada de 3 evidências + o que mudou entre elas |
| POR.b | Revisão de uma atividade anterior **com a rubrica na mão** |

---

## 6. Banco de verbos do comando

[`05`](05-REGRAS-DE-APLICACAO.md) §5 fixa que o texto entre aspas vai verbatim para o aluno. O verbo precisa combinar com a rubrica — caso contrário a tarefa pede uma coisa e a correção mede outra.

| Verbo | Exige do aluno | Rubricas compatíveis | Erro comum |
|---|---|---|---|
| descreva | enumerar o observável | R8, R10 | usado onde se queria explicação causal |
| explique | dizer o mecanismo | R5, R4, R11 | aceita paráfrase do capítulo |
| justifique | apresentar razão sustentada | R5, R9, R11, R12 | vira opinião sem conceito |
| compare | aplicar critérios paralelos | R2, R10 | vira lista de diferenças soltas |
| classifique | aplicar critério a casos | R2, R10 | critério não explicitado |
| ordene | estabelecer sequência | R3, R4 | cronologia sem nexo |
| relacione | nomear a ligação | R2, R3 | conectar sem rotular |
| decida | escolher e defender sob critério | R12, R9 | decidir sem citar o dado |
| prove | encadear dedução | R1, R10 (CONS) | verificar um caso e chamar de prova |
| construa | produzir com instrumento | R10 | desenhar à mão livre |
| meça / registre | coletar dado fiel | R8 | registrar só o resultado bonito |
| preveja | escrever palpite **antes** | R8 | preencher depois de ver o resultado |
| reescreva | adequar a gênero/registro | R6 | copiar com sinônimos |
| diagnostique | localizar e nomear o erro | R11 | corrigir sem explicar |
| avalie | julgar sob critério dado | R7, R13 | elogiar ou reprovar sem critério |
| pesquise | buscar dado fora do capítulo e registrar a referência | R7, R8 | entregar o dado sem dizer de onde veio |
| localize | encontrar uma fonte que atenda a critérios dados | R7 | trazer o primeiro resultado que apareceu |
| analise | separar, na fonte, a afirmação, a prova e a lacuna | R7 | resumir a fonte em vez de examiná-la |
| elabore | produzir o artefato inteiro, do zero | R4, R10 | preencher um modelo já pronto |

---

## 7. Molde de saída

O arquivo de um capítulo tem **três partes, nesta ordem**: a folha do aluno, a grade de correção e o rodapé de produção. Só a primeira chega à mão do aluno.

### 7.1 Folha do aluno

Questões numeradas, na voz do aluno. **Sem campo de resposta, sem linha pontilhada, sem moldura** — o espaço para escrever é da folha impressa, não do arquivo. Cada questão é um enunciado fechado que já diz o que entregar.

```markdown
### Capítulo N — <título do capítulo>

**1.** <enunciado, verbo do banco §6>

**2.** <enunciado>

**3.** <enunciado, com subitens quando a mesma tarefa se repete sobre vários objetos:>

a) <objeto>
b) <objeto>
c) <objeto>
```

**Seis a oito questões por capítulo**, sem repetir o par tipo+item. Um mesmo tipo pode voltar uma segunda vez se o item for outro — `FON.a` (pesquisar a fonte) e `FON.c` (analisar o que a fonte não diz) são tarefas distintas.

Três proibições no enunciado:

| Não escrever | Por quê |
|---|---|
| Instrução de andaime — *"você escolhe"*, *"pode ser qualquer um"*, *"não precisa ser"* | conversa sobre a tarefa, não é a tarefa. O enunciado exige; não negocia |
| Artefato pronto para preencher — tabela com cabeçalho dado, esquema com caixas vazias | o aluno **constrói** a tabela e o esquema. Entregá-los prontos rebaixa TAB e ESQ a preenchimento |
| *"peça que o aluno…"*, *"o professor entrega…"* | o texto é lido pelo aluno; instrução ao professor vai para a grade |

### 7.2 Grade de correção

No fim do arquivo, separada por `---`. É o que o professor usa e o aluno não recebe.

```markdown
| Questão | Tipo | Rubrica | Critério que decide a nota |
|---|---|---|---|
| 1 | ESQ | R4 | <o ajuste, quando houver> |
```

### 7.3 Rodapé de produção

Uma linha por capítulo, depois da grade:

`**Cap. N** · Marcadores: M2, M4 · Pool: MC, CASO, ESQ, ESC · Seed: <hash8>`

É o que permite auditar por que cada tipo foi escolhido e re-sortear com reprodutibilidade.

**Integradora do ano** usa o mesmo molde, acrescentando uma questão de `POR`.

### 7.4 Variante do conjunto de sala

A folha do aluno é a mesma: questões numeradas, sem campo, sem andaime. O conjunto de sala acrescenta **uma única linha** antes da questão 1, porque a tarefa depende de três coisas que a casa não tem:

`**Formato:** duplas · **Tempo:** 50 min · **O professor entrega:** <insumo>`

Nada mais de instrução ao professor entra no corpo das questões — o resto vai para a grade de correção. E `DEB` e `ORA`, que T7 exclui da casa, voltam ao pool.

---

## 8. Critérios de rejeição

Antes de aceitar um capítulo gerado, doze checagens. Qualquer **não** manda re-sortear ou reescrever.

| # | Pergunta | Se falhar |
|---|---|---|
| 1 | A resposta esperada está impressa no capítulo em forma quase idêntica? | trocar o tipo |
| 2 | O verbo do comando bate com a rubrica? (§6) | trocar o verbo |
| 3 | O comando define destinatário e extensão, quando é ESC/RET? | reescrever o comando |
| 4 | Os insumos existem sem preparo extra do professor? | trocar o item |
| 5 | **Casa:** há mecanismo de conferência declarado? | trocar o item por um **✓conf** |
| 6 | **Casa:** há previsão escrita antes de medir, quando é INV? | inserir o palpite |
| 7 | O tipo repete o do capítulo vizinho ou o do par sala/casa? | re-sortear (T1, T8) |
| 8 | O tempo bate com a faixa da disciplina? (§4.4) | recalibrar |
| 9 | O enunciado tem instrução de andaime — *"você escolhe"*, *"pode ser qualquer"*, *"não precisa ser"*? | reescrever o enunciado (§7.1) |
| 10 | O artefato pedido — tabela, esquema, linha do tempo — vem pronto para preencher? | reescrever: quem constrói é o aluno (§7.1) |
| 11 | A questão depende de outra questão para ser respondida? | reescrever autossuficiente (§8.1) |
| 12 | A questão exige recurso que não todo aluno tem? | trocar o item (§8.2) |

Checagem em lote, por disciplina, ao final: nenhum tipo acima do teto de T2; todos os dominantes de [`03`](03-REPERTORIO.md) §3 presentes ao menos 1×.

### 8.1 Independência da questão

O professor seleciona quais questões entram na folha, e nem todas entram. Uma questão que depende de outra quebra quando a outra é descartada. Portanto **cada questão precisa ser respondível isoladamente**, sem que nenhuma outra tenha sido feita.

| Não escrever | Escrever |
|---|---|
| *"Analise a tabela que você construiu na questão 2"* | *"Construa uma tabela que compare X e Y e analise…"* — a questão recria o próprio objeto |
| *"Com base no esquema anterior…"* | enunciar de novo o que o esquema mostrava |
| *"Repita o procedimento do item anterior para…"* | enunciar o procedimento inteiro |

Duas questões **podem** tratar do mesmo conteúdo. O que não podem é compartilhar um objeto construído: cada uma carrega a própria premissa, mesmo ao custo de repetir uma frase de contexto.

### 8.2 Acessibilidade do recurso

Os recursos garantidos a todo aluno são: **o capítulo, o caderno, lápis ou caneta, o material escolar de geometria — régua, compasso e transferidor —, calculadora comum, e a própria observação e raciocínio**. Uma questão que exija qualquer coisa além disso exclui parte da turma e precisa ser trocada.

| Não exigir | Por quê | Substituir por |
|---|---|---|
| Termômetro, balança, trena, fita métrica, cronômetro | instrumento de medida que a escola não pede na lista | comparação qualitativa, estimativa justificada, ou dado fornecido no enunciado |
| **Calculadora financeira** (teclas PV, FV, PMT, i, n) | não está na lista de material | calculadora comum, com o roteiro de cálculo explicitado no enunciado |
| Celular, computador, internet, aplicativo, câmera | acesso desigual | fonte impressa **ou** digital **ou** o acervo da escola, à escolha |
| Impressora, recorte de revista ou jornal | consumível que a família paga | o aluno constrói o artefato ou transcreve |
| Visita a local, entrevista com especialista, compra | custo, deslocamento e disponibilidade | observação do próprio cotidiano ou caso descrito no enunciado |
| Item específico dentro de casa | nem toda casa tem | objeto de uma lista ampla, ou dado fornecido no enunciado |

Três consequências que decidem a redação do comando:

- **Construção geométrica usa instrumento.** Com compasso e transferidor garantidos, o verbo é `construa` — que §6 define como *produzir com instrumento* e cujo erro comum é justamente *desenhar à mão livre*. Circunferência traçada a compasso, ângulo medido a transferidor. Reserve `elabore` para o artefato que não pede instrumento: esquema, tabela, história em quadrinhos.
- **Aritmética pesada é aceitável, roteiro obrigatório.** Com calculadora comum, uma questão pode pedir potências sucessivas ou raiz. O que o enunciado precisa dar é o **roteiro**: qual conta, em que ordem, quantas vezes. O que ele não pode pressupor é tecla financeira que resolva o problema num passo.
- **`INV` e `FON` seguem válidos.** `INV`: o aluno prevê e depois **observa** — instrumento só se for régua, compasso ou transferidor. `FON`: o enunciado aceita fonte impressa, digital ou do acervo da escola, sem exigir uma delas.

---

## 9. Prompt de produção

Para rodar no Claude Code, uma disciplina por vez.

```
Você vai produzir o arquivo de atividades de <DISCIPLINA>, conjunto <SALA|CASA>.

LEIA ANTES, NESTA ORDEM:
  METODOLOGIA/03-REPERTORIO.md   (tipos e distribuição da disciplina)
  METODOLOGIA/04-RUBRICAS.md     (R1–R13)
  METODOLOGIA/06-PRODUCAO.md     (este arquivo — obedeça §3 a §8)

PARA CADA CAPÍTULO, NESTA ORDEM:
  1. Leia o capítulo e marque os marcadores M1–M11 (§3).
  2. Monte o pool. Se ficar com menos de 3 tipos, pare e me pergunte.
  3. Sorteie tipo, itens e verbo com a semente de §4.1 e as travas de §4.3.
  4. Escreva 6 a 8 questões no molde de §7.1, uma por tipo sorteado.
  5. Monte a grade de correção (§7.2) e o rodapé de produção (§7.3).
  6. Rode as 10 checagens de §8 e corrija antes de passar ao próximo.

REGRAS RÍGIDAS:
  - Um capítulo por vez. Não gere o arquivo inteiro de uma vez.
  - O enunciado é o texto final do aluno. Não escreva "peça que o aluno...".
  - Sem campo de resposta, sem linha pontilhada, sem moldura: só o enunciado.
  - Sem instrução de andaime ("você escolhe", "pode ser qualquer").
  - Tabela, esquema e linha do tempo são CONSTRUÍDOS pelo aluno, nunca entregues prontos.
  - Não invente dado numérico nem texto-fonte: se a questão exige uma notícia ou um
    trecho de livro, ou o aluno localiza a fonte, ou o item entra na lista de fontes a
    providenciar. Nunca escreva uma fonte fictícia.
  - Não acrescente camada devocional (05 §6).
  - CASA: sem gabarito, sem DEB, sem ORA, EX só com item ✓conf.
  - Ao final da disciplina, imprima a tabela de checagem em lote (§8).
```

---

## 10. Decisões adotadas por padrão

Três parâmetros foram fixados sem consulta prévia. São os primeiros a revisar se o resultado não agradar:

| Decisão | Valor adotado | Alternativa |
|---|---|---|
| **Teto de concentração (T2)** | 40% geral · 55% para EX em Mat. EF1 e Português | 33%/50% deixa mais variado, mas fragiliza a fluência procedimental |
| **Unidade de sorteio** | capítulo | sortear por ano, distribuindo os tipos antes, dá controle melhor da cobertura e pior da adequação capítulo a capítulo |
| **Complementares** | tipos sorteados, distintos do principal | fixar as complementares como sempre EX + ESC economiza produção e reduz muito a variedade |

---

## Para onde ir daqui

| Se você quer | Abra |
|---|---|
| O argumento e o diagnóstico | [`01-PROPOSTA.md`](01-PROPOSTA.md) |
| A justificativa de cada tipo | [`02-BASE-DE-EVIDENCIA.md`](02-BASE-DE-EVIDENCIA.md) |
| Os 18 tipos e a distribuição | [`03-REPERTORIO.md`](03-REPERTORIO.md) |
| Os critérios de correção | [`04-RUBRICAS.md`](04-RUBRICAS.md) |
| Peso, quantidade e aplicação | [`05-REGRAS-DE-APLICACAO.md`](05-REGRAS-DE-APLICACAO.md) |
