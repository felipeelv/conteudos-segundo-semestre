# 06 · Regras de produção

> Metodologia · Proposta de Atividades 2º Semestre · [índice](00-LEIA-ME.md)
> **Escopo:** produção dos dois conjuntos (sala e casa) para os 193 capítulos.

Os arquivos 01 a 05 dizem **o que** o material é e **como aplicá-lo**. Este diz **como produzi-lo** — e existe porque a geração capítulo a capítulo estava saindo repetitiva.

---

## 1. O diagnóstico da geração

A repetição não vem de falta de repertório. Vem de três buracos entre o repertório e o texto que o aluno lê:

| Buraco | Efeito na geração |
|---|---|
| **Falta a camada de item.** Os tipos são macro-tarefas. Entre "esta atividade é um MC" e o comando final não há nada especificado | O gerador preenche o vazio sozinho, e preenche sempre do mesmo jeito. 193 capítulos com a mesma cara |
| **A escolha do tipo está em prosa** (seção 2 do [`03-REPERTORIO.md`](03-REPERTORIO.md)) | Prosa se interpreta; tabela de decisão se executa. Interpretação converge para o tipo mais fácil de escrever |
| **Não há molde de saída** | Cada arquivo sai com estrutura própria. Nada é comparável, nada é revisável em lote |

> **Randômico puro não resolve — quebra.** Sortear livremente entre os 18 contradiz a regra do próprio repertório: *se a resposta esperada já está impressa no capítulo em forma quase idêntica, o tipo está errado*. Um sorteio cego coloca TAB em capítulo que já termina em tabela e LT em capítulo de datas decorativas.
>
> O que se quer é **variedade sob restrição**: sorteio dentro de um pool elegível, com travas de repetição e semente reprodutível.

---

## 2. As três camadas

Toda atividade é decidida em três níveis, nesta ordem. O nível 1 já existe; os níveis 2 e 3 são o que este arquivo acrescenta.

```
Nível 1 · TIPO      (19 códigos)         → o que a tarefa é          → 03-REPERTORIO
Nível 2 · ITEM      (60 formatos)        → como a tarefa é montada   → §5 deste arquivo
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
| OBJ | R14 | — | 2× por capítulo, fora do sorteio, sempre complementar |

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

**`OBJ` está fora do pool, e isso é regra, não omissão.** As duas objetivas de cada capítulo não competem com os dezoito tipos por vaga: elas se somam ao que o sorteio produziu, ao final da folha daquele capítulo. Nenhum marcador as libera e nenhum as proíbe — o que decide se uma `OBJ` cabe é a existência de **confusão conceitual típica** no conteúdo do capítulo, e essa leitura se faz na hora de escrever o item, não na hora de montar o pool. Se um capítulo não oferecer duas confusões distintas que rendam distratores honestos, **pare e pergunte** em vez de inventar distrator absurdo.

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
8. escrever as 2 OBJ do capítulo (§5, §7.1)    → aplicar trava T9
```

O passo 8 não sorteia nada: escolhe as duas confusões conceituais do capítulo e o item `OBJ` que melhor as expõe.

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
| T9 | **OBJ:** as duas do capítulo usam **itens diferentes entre si**, atacam **confusões conceituais diferentes**, e nenhuma delas é a atividade principal | duas objetivas do mesmo formato sobre o mesmo ponto é uma questão repetida, não duas |

Trava violada → re-sortear dentro do pool (máximo 5 tentativas). Esgotadas, aceitar a violação de menor peso nesta ordem de prioridade: **T8 > T7 > T9 > T2 > T1 > T6 > T5 > T4 > T3** — e registrar a exceção no rodapé do capítulo.

**T9 não se resolve por re-sorteio**, porque `OBJ` não é sorteado: resolve-se reescrevendo uma das duas sobre outra confusão do mesmo capítulo. Se não houver segunda confusão, o caso é de pergunta à coordenação (§3).

**T2 e T9 não colidem.** T2 mede concentração **entre as atividades principais** da disciplina, e `OBJ` nunca é principal — por isso duas objetivas em cada um dos 95 capítulos não empurram nenhum tipo para o teto de 40%.

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

Os 60 formatos, em 19 tipos. O sorteio do nível 2 acontece aqui.
Marcados com **✓conf** os itens que trazem conferência embutida — os únicos admissíveis para EX no caderno de casa. Os quatro de `OBJ` são todos ✓conf por construção: a conferência é a própria exigência de eliminar cada distrator por um motivo distinto.

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
| ESC.a | Explicação a destinatário-leitor nomeado (quem faltou à aula, um leitor de 8 anos), extensão fixa — destinatário conforme §8.3 |
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
| INV.d | Entrevista com roteiro fechado — **só no conjunto de sala** (§8.3); sujeita às regras de privacidade de [`05`](05-REGRAS-DE-APLICACAO.md) |

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

### OBJ — questão objetiva justificada *(2 por capítulo, fora do sorteio)*
| Código | Formato |
|---|---|
| OBJ.a | **Situações paralelas:** cada alternativa é um caso concreto; só um satisfaz o conceito. As demais falham em **condições diferentes** do conceito **✓conf** |
| OBJ.b | **Caso + leituras:** um caso descrito no enunciado e alternativas que o interpretam. Pelo menos um distrator é desmentido pelo próprio caso, e os outros só caem pelo conceito **✓conf** |
| OBJ.c | **Afirmações sobre o mesmo fenômeno:** uma correta; as erradas são os erros que o conteúdo tipicamente produz — inversão de causa, generalização indevida, confusão entre dois termos vizinhos **✓conf** |
| OBJ.d | **Certa com justificativa errada:** duas alternativas chegam à mesma conclusão correta, e só uma a sustenta pela razão certa. O caso mais difícil — espelha `ERR.c` e é reservado a EF2 e EM **✓conf** |

**Como se escolhe entre os quatro.** `OBJ.a` cabe quando o conceito tem **condições** que o aluno aplica pela metade — exótica × invasora, fenômeno × catástrofe, dado × informação. `OBJ.b` cabe quando o capítulo permite construir um caso novo, e é o item que mais afasta a checagem 1, porque o caso não está impresso. `OBJ.c` é o mais direto e o que exige distratores mais bem pesquisados, porque sem erro típico documentado ele degenera em alternativa absurda. `OBJ.d` é o mais exigente e não entra em EF1.

**Quatro regras de escrita dos distratores, que valem para os quatro itens:**

| Regra | Por quê |
|---|---|
| Erro **plausível e típico**, nunca absurdo | distrator que ninguém marcaria não mede nada e reduz a questão a três alternativas |
| Alternativas de **comprimento parecido** | a mais longa e mais qualificada denuncia a resposta sem que o aluno pense no conceito |
| Cada errada cai por um **motivo diferente** | é o que a rubrica R14 mede e o que o `Confira você mesmo:` audita |
| Sem *"todas as anteriores"*, *"nenhuma das anteriores"*, *"apenas I e II"* | testam leitura de enunciado, não o conceito, e não rendem eliminação argumentada |

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
| leia | tomar conhecimento de fonte **entregue** — Anexo, trecho no enunciado | R7 | parar na leitura, sem o que extrair dela |
| analise | separar, na fonte, a afirmação, a prova e a lacuna | R7 | resumir a fonte em vez de examiná-la |
| calcule | executar a operação e apresentar o resultado com as etapas | R1 | entregar só o resultado, sem o caminho |
| elabore | produzir o artefato inteiro, do zero | R4, R10 | preencher um modelo já pronto |
| redija | produzir texto próprio, na extensão e para o destinatário que o comando fixa | R5, R6 | comando sem destinatário nem extensão, que rebaixa a tarefa a "escreva sobre" |
| assinale | escolher a alternativa que satisfaz o conceito **e sustentar a escolha eliminando as demais** | R14 | parar na letra, sem a eliminação — que é onde estão 8 dos 10 pontos |

**`assinale` é o verbo de `OBJ`, e o único do banco cuja entrega tem duas partes.** A síntese diz o que assinalar e **já anuncia a eliminação**: *"…e justifique por que cada uma das outras três está errada"*. Sem essa segunda metade na primeira frase, a questão vira múltipla escolha comum, o `Responda:` cobra o que o enunciado não pediu, e R14 mede algo que a folha não exige — o defeito exato que a segunda linha de §9.1 existe para pegar. `marque`, `escolha` e `indique` **não entram no banco**: os três param na seleção, e é justamente a parada na seleção que `OBJ` foi desenhado para impedir.

**Três verbos produzem, e o objeto decide qual.** `construa` produz figura **com instrumento** — compasso, transferidor, régua. `elabore` produz o artefato que dispensa instrumento — esquema, tabela, linha do tempo, história em quadrinhos. `redija` produz **texto**. Trocar um pelo outro descaracteriza o tipo, e os dois erros são simétricos: escrever *"desenhe"* onde cabe `construa` é exatamente o que a linha de `construa` nomeia como erro comum, e escrever *"escreva sobre"* onde cabe `redija` apaga o destinatário e a extensão sem os quais [`03`](03-REPERTORIO.md) §1 manda **não usar** `ESC` — a mesma exigência que a checagem 3 do §8 cobra.

`redija` é o verbo de `ESC` e de `RET`, e é ele que sustenta a substituição prescrita para a casa: onde o conteúdo pedia `DEB` e T7 o exclui, entra `ESC` com objeção obrigatória e leitor contrário nomeado **no texto** ([`03`](03-REPERTORIO.md) §3, destinatário conforme §8.3).

**`leia` e `localize` não são o mesmo verbo.** `localize` manda o aluno **encontrar** uma fonte que ele ainda não tem, e é o que `FON` usa nas onze disciplinas sem anexo. `leia` só cabe quando a fonte **já está na mão** — o Anexo de Estudos Sociais (M5), um trecho transcrito no próprio enunciado. Nesse caso, mandar *analisar* uma biografia no 4º ano cobra do aluno de nove anos um verbo de outra idade; `leia` abre a tarefa e o `Responda:` cobra o que extrair dela.

**Quando o dado precisa vir antes do comando.** Em questão de cálculo ou de leitura de tabela, o enunciado às vezes tem de apresentar a série, o caso ou a fonte **antes** de dizer o que fazer com eles. Aí a síntese pode abrir pelo dado — *"Considere a série 12, 15, 15, 18, 20 e 22"* — desde que o verbo do banco apareça no `Responda:` que fecha a questão. A checagem 2 do §8 se afere no verbo do comando, esteja ele na primeira frase ou no bloco de entrega.

---

## 7. Molde de saída

O arquivo de um capítulo tem **três partes, nesta ordem**: a folha do aluno, a grade de correção e o rodapé de produção. Só a primeira chega à mão do aluno.

### 7.1 Folha do aluno

Questões numeradas, na voz do aluno. **Sem campo de resposta, sem linha pontilhada, sem moldura** — o espaço para escrever é da folha impressa, não do arquivo.

A questão separa o que o aluno **faz** do que o aluno **pensa e entrega**. A execução vai em prosa compacta; a entrega intelectual vai em blocos rotulados em negrito — ela é o centro da questão e não pode ficar escondida entre instruções mecânicas, com o mesmo peso visual de "pegue a régua". Os dois extremos falham: o checklist de etapas rotuladas faz o aluno executar sem pensar, e o parágrafo único corrido mistura ação, registro e pergunta.

Estrutura, nesta ordem — os blocos 2, 4 e 6 só existem quando o item os tem:

1. **Enunciado-síntese.** A primeira frase, com o verbo do banco do §6, dando o arco completo da questão (construir → transformar → registrar) sem detalhar o como. **A checagem 2 do §8 se afere aqui** — os imperativos internos da execução (*trace*, *marque*, *percorra*) não são verbos de comando. Se a questão pede previsão, a síntese não pode revelar o resultado esperado.
2. **`Antes de começar, responda por escrito:`** — só quando o item tem previsão (INV). Em forma de pergunta e **antes da execução**: o palpite nasce antes do dado (R8).
3. **Execução.** Prosa corrida compacta: ações simples fundidas na mesma frase. Quando há duas ações de natureza distinta — reunir o dado e montar o produto com ele —, dois parágrafos curtos separam melhor que um só. Todas as especificações técnicas preservadas — medidas, quantidades, condições. A síntese resume; a execução carrega os números. **Marcador só em dois casos:** (a) sub-sequência técnica cuja ordem importa — as transformações aplicadas em sequência; (b) especificações paralelas de um mesmo produto — os requisitos verificáveis daquilo que o aluno constrói, como os elementos que o gráfico precisa ter. No caso (b) o marcador lista **o que conferir no produto pronto**, não o artefato montado: enumerar requisito continua sendo exigência, entregar cabeçalho de tabela ou caixa vazia é o artefato pronto que a tabela de proibições veta.
4. **`Registre:`** — só quando o aluno produz **várias observações** antes de concluir. Vale a repetição no tempo (três dias de contagem, uma semana de germinação) e vale a repetição em número (cinco objetos medidos, os trechos de um caminho contados, uma categoria por linha). Observação é dado bruto que o aluno produz, separado da conclusão — e o que decide o bloco é essa separação, não o calendário: uma resposta única não é registro, duas medidas já são. O bloco também não repete o que o `Antes de começar` já pediu: a previsão fica lá, e aqui entra só o que a execução produz.
5. **`Responda:`** — a entrega central, em forma de pergunta sempre que a pergunta funciona. Carrega extensão e destinatário quando o tipo os exige (ESC/RET — checagem 3), com destinatário conforme §8.3, e admite **complemento de localização** quando a questão gera produto na página: `Responda, abaixo dos gráficos:`. **Pergunta que comprime dois raciocínios abre nos dois tempos.** *Aponte o fator que explica a maior diferença* cobra duas coisas e pergunta uma só: o aluno tem de identificar a diferença antes de explicá-la, e quem responde direto o fator pula a etapa que a questão existe para exercitar. Escreve-se `qual é a maior diferença entre os dois climogramas, e que fator do clima a explica?`. Ao abrir o segundo tempo, **confira a linha da questão na grade**: se o critério só nomeia o fator, ele passa a nomear os dois — a folha e a grade mudam na mesma passada, sem tocar em tipo nem em rubrica.
6. **`Confira você mesmo:`** — só quando o item tem conferência embutida. Diz o que o erro **significa**, não apenas que ele existe.

```markdown
### Capítulo N — <título do capítulo>

**1.** <enunciado-síntese, verbo do banco §6>

<execução em prosa compacta; marcadores só onde a ordem importa>

**Responda:** <a pergunta central — com extensão e destinatário quando ESC/RET>

**Confira você mesmo:** <a verificação, e o que o erro significa>
```

Subitens `a) b) c)` continuam valendo quando a mesma tarefa se repete sobre vários objetos. **Cada subitem ocupa uma linha e termina em dois espaços** — a quebra dura do Markdown —, exceto o último do bloco, que é fechado pela linha em branco seguinte:

```markdown
a) <primeiro objeto>··
b) <segundo objeto>··
c) <terceiro objeto>
```

*(`··` representa os dois espaços, invisíveis no arquivo.)*

Sem eles, o Markdown funde as linhas num parágrafo único ao renderizar **e ao colar a folha no Google Docs**, e o aluno recebe a lista corrida. Os dois espaços viram `<br>`: o item fica numa linha própria **sem marcador e sem espaçamento de parágrafo**, que é como uma folha de questões se lê. Lista com `- ` resolveria o mesmo problema, mas imprime um bullet antes da letra — `• a)` —, redundante numa alternativa que já é rotulada.

> ⚠️ **Os dois espaços são invisíveis e frágeis.** Editor configurado para *trim trailing whitespace on save* os apaga sem avisar, e o defeito volta calado — o arquivo parece igual e a folha cola errada. Ao mexer numa folha, confira depois se as alternativas ainda terminam em dois espaços.

Exemplo calibrado — a questão de transformações do 8º ano de Geometria:

> **1.** Construa uma malha quadriculada, aplique a um triângulo três transformações em sequência e registre o que muda e o que permanece em cada uma.
>
> Trace no caderno uma malha de 1 cm — pelo menos doze quadrados de lado — e, nela, um triângulo com os três vértices sobre pontos da malha. Aplique nesta ordem:
>
> - translação de 4 quadrados à direita e 2 para cima;
> - reflexão por um eixo vertical da malha;
> - rotação de 90° em torno de um dos vértices.
>
> **Responda, em uma tabela que você mesmo elaborar:** o que mudou e o que permaneceu na figura em cada uma das três transformações?
>
> **Confira você mesmo:** meça os lados do triângulo inicial e os da última imagem — as três medidas têm de coincidir. Se não coincidirem, uma das transformações foi aplicada errado.

Note: montar a malha e traçar o triângulo são uma frase de prosa, não "Etapa 1" e "Etapa 2"; os marcadores sobrevivem só na sequência de transformações, porque ali a ordem importa; o registro virou `Responda:` em pergunta; a conferência diz o que o erro significa.

Segundo exemplo calibrado — a questão dos climogramas da 1ª série de Geografia, que mostra os outros três recursos: execução em dois parágrafos, marcador do caso (b) e `Responda:` em dois tempos.

> **1.** Elabore dois climogramas de cidades brasileiras de climas contrastantes, com dados que você mesmo reunir, e identifique a maior diferença entre eles e o fator do clima que a explica.
>
> Consulte um atlas, um livro didático ou uma fonte digital e reúna a temperatura média e a precipitação de cada um dos doze meses de duas cidades — uma da Amazônia ou do litoral, outra do interior do Nordeste, do planalto do Sudeste ou do Sul. Se a fonte já trouxer o climograma pronto, transcreva dela os valores mês a mês.
>
> Monte um climograma para cada cidade, com:
>
> - título que nomeie a cidade;
> - barras de precipitação em milímetros;
> - linha de temperatura em graus Celsius;
> - as mesmas escalas nos dois gráficos;
> - a indicação da fonte dos dados.
>
> **Responda, abaixo dos gráficos:** qual é a maior diferença entre os dois climogramas, e que fator do clima a explica?

Note: reunir os dados e montar o gráfico são ações de natureza distinta e ficam em parágrafos separados; os cinco marcadores não têm ordem obrigatória entre si — são o que se confere no climograma pronto, e é isso que os autoriza pelo caso (b); o `Responda:` ganhou localização porque o produto está na página, e abriu os dois tempos porque *apontar o fator que explica a diferença* cobrava a identificação da diferença sem nunca pedi-la.

#### O molde de `OBJ`

A objetiva usa o mesmo esqueleto, com um bloco a mais e uma restrição a mais. Ordem:

1. **Enunciado-síntese** com `assinale`, dizendo o que se procura entre as alternativas **e** anunciando a eliminação. As duas metades são obrigatórias.
2. **Execução** — só em `OBJ.b`, e é o caso descrito em um parágrafo. Em `OBJ.a`, `OBJ.c` e `OBJ.d` não há execução: as alternativas vêm logo depois da síntese.
3. **As alternativas**, em `a) b) c) d)`, **uma por linha, cada uma terminada em dois espaços** — a quebra dura do §7.1 —, sem marcador de lista antes da letra. São os subitens que §7.1 já admite, não marcadores — a regra dos dois casos de marcador não se aplica a elas.
4. **`Responda:`** com as duas entregas na mesma pergunta: qual é a alternativa e por que cada uma das outras está errada.
5. **`Confira você mesmo:`** sempre presente — os quatro itens de `OBJ` são ✓conf. Ele **não revela a letra**: aponta a estrutura das eliminações, para o aluno auditar o próprio raciocínio.

**Calibragem por faixa, que é o que o pedido de "nível de cada aluno" significa aqui:**

| Faixa | Alternativas | Eliminação cobrada | Distratores |
|---|---:|---|---|
| EF1 · 4º–5º | 3 | **uma**, nomeada no `Responda:` | erro concreto e visível; frase de até 15 palavras; sem `OBJ.d` |
| EF2 · 6º–9º | 4 | as três | confusão entre termos vizinhos, condição aplicada pela metade, causa invertida |
| EM · 1ª–2ª | 4 | as três, **com o tipo de erro nomeado** | generalização indevida, conclusão certa por razão errada, condição necessária tomada por suficiente |

Exemplo calibrado de `OBJ` — 7º ano de Ciências, item `OBJ.b`:

> **7.** Assinale, entre as quatro alternativas, a que explica o que aconteceu com a população de uma espécie depois que uma rodovia dividiu a mata em que ela vivia, e justifique por que cada uma das outras três está errada.
>
> Uma rodovia foi aberta no meio de uma área de mata e a dividiu em dois fragmentos. Nenhum animal foi retirado nem caçado, e a mata dos dois lados continuou de pé. Alguns anos depois, a população da espécie que vivia ali havia diminuído nos dois fragmentos.
>
> a) A rodovia não pode ser a causa, porque nenhum animal foi retirado da mata quando ela foi aberta.  
> b) Os dois grupos, agora separados, encontram menos parceiros e resistem menos a doenças e a eventos locais.  
> c) Os dois grupos viraram espécies diferentes no momento em que a rodovia os separou.  
> d) O que reduziu a população foi a perda de vegetação provocada pela obra.
>
> **Responda:** qual é a alternativa correta, e por que cada uma das outras três está errada?
>
> **Confira você mesmo:** só uma das três erradas é desmentida pelo próprio caso; as outras duas só caem com o que o capítulo explica sobre populações isoladas. Se você descartou as três apenas relendo o caso, duas justificativas ainda não estão prontas.

Note: as quatro alternativas têm comprimento próximo, e a certa não é a mais longa; `d` cai pela leitura do caso, `a` e `c` só caem pelo conceito, e é essa assimetria que o `Confira você mesmo:` torna verificável sem entregar a letra.

**Oito a dez questões por capítulo:** as seis a oito sorteadas, sem repetir o par tipo+item, **mais as duas `OBJ` ao final**. Um mesmo tipo pode voltar uma segunda vez se o item for outro — `FON.a` (pesquisar a fonte) e `FON.c` (analisar o que a fonte não diz) são tarefas distintas.

Três proibições no enunciado:

| Não escrever | Por quê |
|---|---|
| Instrução de andaime — *"você escolhe"*, *"pode ser qualquer um"*, *"não precisa ser"* | conversa sobre a tarefa, não é a tarefa. O enunciado exige; não negocia |
| Artefato pronto para preencher — tabela com cabeçalho dado, esquema com caixas vazias | o aluno **constrói** a tabela e o esquema. Entregá-los prontos rebaixa TAB e ESQ a preenchimento |
| *"peça que o aluno…"*, *"o professor entrega…"* | o texto é lido pelo aluno; instrução ao professor vai para a grade |
| Rótulo de tempo — *"⏱ 50 min"*, *"30 min"* | tempo estimado é gestão de aula, não tarefa. Vai para a grade, se for para algum lugar |
| Rótulo de lugar — *"🏠 em casa"* | o arquivo já diz de que conjunto é. Dizer ao aluno onde ele está é ruído |
| Lista de material quando o material é o garantido do §8.2 | régua, compasso, transferidor, lápis e calculadora comum são pressupostos. Listá-los sugere que poderiam faltar |
| Etapas rotuladas — *"Etapa 1 — a malha"* — ou a questão inteira em lista numerada plana | efeito checklist: a pergunta central fica com o mesmo peso visual da instrução mecânica, e o aluno executa sem pensar |
| Previsão ou conferência inventada, que o item sorteado não tem | conteúdo sem lastro no sorteio. Os blocos rotulados existem quando o item os tem — não por decoração |
| Imperativo no `Responda:` quando a forma de pergunta funciona | a pergunta define a entrega melhor que a ordem |
| `Responda:` que cobra dois raciocínios e pergunta um só | *o fator que explica a maior diferença* faz o aluno identificar a diferença sem nunca pedir que ele a declare. Os dois tempos, explícitos |
| Perder especificação técnica ao compactar a execução | a síntese resume; quem carrega medidas, quantidades e condições é a execução |
| **OBJ:** síntese que manda assinalar sem mandar justificar | vira múltipla escolha comum, e R14 passa a medir o que a folha não pede |
| **OBJ:** `Confira você mesmo:` que entrega a letra, ou diz "confira no capítulo" | o primeiro é gabarito na folha; o segundo não confere nada |
| **OBJ:** alternativa mais longa e mais qualificada que as outras | denuncia a resposta pela forma, sem passar pelo conceito |
| **OBJ:** *"todas as anteriores"*, *"nenhuma das anteriores"*, *"apenas I e II"* | testam leitura de enunciado e não rendem eliminação argumentada |

### 7.2 Grade de correção

No fim do arquivo, separada por `---`. É o que o professor usa e o aluno não recebe.

```markdown
| Questão | Tipo | Rubrica | Critério que decide a nota |
|---|---|---|---|
| 1 | ESQ | R4 | <o ajuste, quando houver> |
```

**`OBJ` é o único tipo cuja linha carrega gabarito**, e ele vive aqui — nunca na folha. A linha traz a letra **e** o motivo de eliminação esperado de cada distrator, porque é a eliminação que decide 8 dos 10 pontos:

```markdown
| 7 | OBJ.b | R14 | letra **b**; **d** cai pelo caso (a mata continuou de pé), **a** e **c** pelo conceito de população isolada. A letra sozinha vale 2 dos 10 |
```

Justificativa que descarta dois distratores pelo mesmo argumento não fecha o critério — está em [`04`](04-RUBRICAS.md), R14.

### 7.3 Rodapé de produção

Uma linha por capítulo, depois da grade:

`**Cap. N** · Marcadores: M2, M4 · Pool: MC, CASO, ESQ, ESC · Seed: <hash8>`

É o que permite auditar por que cada tipo foi escolhido e re-sortear com reprodutibilidade.

**Integradora do ano** usa o mesmo molde, acrescentando uma questão de `POR`.

### 7.4 Linha de material

Uma folha **pode** trazer uma linha antes da questão 1, e ela carrega **só material**:

`**Material:** <o que o aluno precisa ter na mesa>`

Três condições, todas obrigatórias:

1. **Só quando há material a declarar.** Se a tarefa roda com o que o §8.2 garante — capítulo, caderno, lápis, régua, compasso, transferidor, calculadora comum — **a linha não existe**. Listar o garantido sugere que poderia faltar.
2. **Sem tempo e sem lugar.** Nada de *"⏱ 50 min"*, nada de *"🏠 em casa"*. Duração é gestão de aula e vai para a grade de correção; o conjunto a que a folha pertence já está no caminho do arquivo.
3. **O material declarado tem de ser possível para todo aluno** (§8.2). A linha não é licença para exigir tesoura, papel-cartão, papelão, cola, barbante ou papel quadriculado impresso. Se o material não é garantido e não é fornecido pela escola, **o item está errado, não a linha** — troque o item.

### 7.5 Variante do conjunto de sala

A folha do aluno é a mesma: questões numeradas, sem campo, sem andaime, e a linha de material de §7.4 sob as mesmas três condições.

O que a sala tem e a casa não: **`DEB` e `ORA` voltam ao pool**, porque T7 só os exclui da casa. E o insumo que o professor entrega, o formato de agrupamento e a duração prevista **vão para a grade de correção** — não para o corpo da folha. O aluno lê a tarefa; o professor lê a logística.

---

## 8. Critérios de rejeição

Antes de aceitar um capítulo gerado, catorze checagens. Qualquer **não** manda re-sortear ou reescrever.

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
| 13 | **Casa:** a questão exige ação, resposta ou presença de outra pessoa? | reescrever para execução solitária, ou trocar o item (§8.3) |
| 14 | **OBJ:** cada distrator é erro plausível, cai por motivo próprio, e as alternativas têm comprimento parecido? | reescrever os distratores (§8.4) |

Checagem em lote, por disciplina, ao final: nenhum tipo acima do teto de T2; todos os dominantes de [`03`](03-REPERTORIO.md) §3 presentes ao menos 1×; **duas `OBJ` em cada capítulo, com itens distintos dentro do capítulo** (T9).

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

### 8.3 Execução individual

O caderno de casa é feito **sozinho**. Nenhuma questão pode exigir ação, resposta, presença ou permissão de outra pessoa — conversar, perguntar, entrevistar, pedir que alguém confira, ler para alguém ouvir, medir alguém. A dinâmica entre alunos existe, mas pertence à sala, onde o professor a conduz; embutida numa questão de casa, ela compromete a execução de quem não tem o interlocutor disponível na hora de fazer.

Três consequências:

- **`INV.d` (entrevista com roteiro) sai do pool da casa.** Só no conjunto de sala — mesmo regime de `DEB` e `ORA` (T7).
- **O destinatário de `ESC`/`RET` continua obrigatório (checagem 3), mas é leitor hipotético do texto, nunca tarefa de comunicação real.** Escreve-se *para quem faltou à aula*, *para um leitor que sustenta a posição contrária*, *para quem ainda não estudou o assunto*. Ninguém precisa existir nem estar presente para a questão ser feita.
- **A palavra "colega" não entra na folha de casa.** No enunciado de erro (`ERR`), o personagem é *um estudante*. Pessoa como objeto de análise ou personagem de problema — *"Alguém deixou a porta aberta"*, *"uma pessoa que cuida de um familiar doente"* — não é interação e segue permitida, assim como a pergunta metalinguística (*"pergunte ao verbo: quem?"*).

### 8.4 Qualidade do distrator

A múltipla escolha falha por um caminho que nenhum outro tipo tem: **a questão parece pronta mesmo quando não mede nada**. Quatro alternativas alinhadas dão aparência de rigor, e o defeito só aparece quando se pergunta o que cada errada exige do aluno para ser descartada. A checagem 14 é essa pergunta, feita distrator a distrator.

| Defeito | Como se reconhece | O que fazer |
|---|---|---|
| **Distrator absurdo** | ninguém da turma marcaria; o aluno chega à resposta por exclusão sem usar o conceito | trocar por um erro que o conteúdo realmente produz — os registrados nas seções de revisão dos `_ORGANIZACAO.md` são a melhor fonte |
| **Distrator redundante** | dois caem pelo mesmo argumento | reescrever um dos dois atacando outra condição do conceito |
| **Pista de forma** | a certa é a mais longa, a mais qualificada, ou a única com vocabulário do capítulo | igualar comprimento e registro entre as quatro |
| **Distrator só verbal** | erra por uma palavra trocada, sem erro de raciocínio atrás | reescrever como afirmação inteira e coerente que chega à conclusão errada |
| **Distrator indecidível** | defensável com o que o capítulo traz; não é errado, é discutível | ou tornar o caso mais específico, ou trocar o distrator — questão objetiva não comporta ambiguidade legítima |

**A pergunta que fecha a checagem:** *se um aluno marcasse esta alternativa, que erro de raciocínio ele teria cometido?* Sem resposta clara e escrevível, o distrator não serve — e é essa resposta que vira o critério da linha na grade (§7.2).

---

## 9. Prompt de produção

O recorte é **um agente por disciplina**, e esse agente percorre os capítulos um a um. Validação e auditoria vêm depois, em agentes separados, e **não podem re-sortear tipo nem rubrica** — corrigem formulação.

```
Você vai produzir o arquivo de atividades de <DISCIPLINA>, conjunto <SALA|CASA>.

LEIA ANTES, NESTA ORDEM:
  METODOLOGIA/03-REPERTORIO.md   (tipos e distribuição da disciplina)
  METODOLOGIA/04-RUBRICAS.md     (R1–R14)
  METODOLOGIA/06-PRODUCAO.md     (este arquivo — obedeça §3 a §8)
  o arquivo-ano de referência já aprovado, como calibre de registro

PARA CADA CAPÍTULO, NESTA ORDEM:
  1. Leia o capítulo e marque os marcadores M1–M11 (§3).
  2. Monte o pool. Se ficar com menos de 3 tipos, pare e me pergunte.
  3. Sorteie tipo, itens e verbo com a semente de §4.1 e as travas de §4.3.
  4. Escreva 6 a 8 questões no molde de §7.1 — enunciado-síntese com verbo do
     banco §6 · execução em prosa compacta · Responda: em pergunta · e os blocos
     Antes de começar / Registre / Confira você mesmo SÓ quando o item os tem.
  4b. Escreva as 2 OBJ do capítulo, ao final, numeradas em continuidade. Não
     sorteie: identifique duas confusões conceituais DIFERENTES do capítulo e
     escolha o item de §5 que expõe cada uma (T9). Alternativas conforme a
     faixa etária (§7.1), síntese com `assinale` anunciando a eliminação,
     Responda: com as duas entregas, Confira você mesmo: sem revelar a letra.
  5. Monte a grade de correção (§7.2) — a linha de OBJ carrega a letra e o
     motivo de eliminação de cada distrator — e o rodapé de produção (§7.3).
  6. Rode as 14 checagens de §8 e corrija antes de passar ao próximo.

REGRAS RÍGIDAS:
  - Um capítulo por vez dentro do agente. Não trate a disciplina inteira num só
    passe de raciocínio.
  - O enunciado é o texto final do aluno. Não escreva "peça que o aluno...".
  - Sem campo de resposta, sem linha pontilhada, sem moldura: só o enunciado.
  - Sem instrução de andaime ("você escolhe", "pode ser qualquer").
  - Sem etapas rotuladas ("Etapa 1 — a malha") e sem a questão em lista plana.
  - Tabela, esquema e linha do tempo são CONSTRUÍDOS pelo aluno, nunca entregues prontos.
  - Não invente dado numérico nem texto-fonte: se a questão exige uma notícia ou um
    trecho de livro, ou o aluno localiza a fonte, ou o item entra na lista de fontes a
    providenciar. Nunca escreva uma fonte fictícia.
  - Não acrescente camada devocional (05 §6).
  - CASA: sem gabarito NA FOLHA, sem DEB, sem ORA, sem INV.d, EX só com item
    ✓conf, e nada que exija outra pessoa (§8.3). O gabarito das OBJ vai para a
    grade do _ORGANIZACAO.md, nunca para o arquivo-ano.
  - OBJ: distrator plausível, motivo de eliminação próprio para cada um,
    alternativas de comprimento parecido, e nada de "todas as anteriores" (§8.4).
  - Subitens e alternativas a) b) c) d): um por linha, cada linha terminada em
    DOIS ESPACOS (quebra dura), menos a ultima do bloco. Sem marcador "- " antes
    da letra. Sem os dois espacos o bloco se funde num paragrafo so ao renderizar
    e ao colar no Google Docs.
  - Ao final da disciplina, imprima a tabela de checagem em lote (§8).
```

### 9.1 O que a produção por agente não pega sozinha

Quatro rodadas de produção mostraram que o agente que escreve e o agente que valida erram nos mesmos pontos cegos. Três verificações precisam vir **de fora** do par produtor/validador:

| Verificação | Por que escapa | Como fazer |
|---|---|---|
| **Contagem e integridade** — arquivos, capítulos, questões, medidas, restrições, conferências, ordem dos blocos, rótulos, resíduos | o validador confia no relato do produtor, e a auditoria costuma amostrar | script determinístico comparando cada arquivo com sua versão em `git HEAD`. Roda em segundos, cobre 100% e não depende de orçamento |
| **Folha × grade** — o `Responda:` ainda pede o que o "Critério que decide a nota" mede? | exige ler as duas fontes lado a lado; ninguém faz por iniciativa | agente dedicado, uma disciplina por vez, com a seção 2 do `_ORGANIZACAO.md` na mão |
| **A própria ferramenta de verificação** | regex com falso positivo produz alarme que consome mais tempo que o defeito real | conferir cada achado no texto antes de agir. Alarme falso comum: contagem em vez de presença, regex sem `re.I`, parser que junta capítulos homônimos |

O caso que justifica a segunda linha: na reformatação de 2026-08-12, **39 de 624 questões** tinham deixado de pedir o que a rubrica media — o padrão mais frequente foi `ESQ` sem exigir seta rotulada, com R4 reservando 3 dos 10 pontos exatamente a isso.

---

## 10. Decisões adotadas por padrão

Três parâmetros foram fixados sem consulta prévia. São os primeiros a revisar se o resultado não agradar:

| Decisão | Valor adotado | Alternativa |
|---|---|---|
| **Teto de concentração (T2)** | 40% geral · 55% para EX em Mat. EF1 e Português | 33%/50% deixa mais variado, mas fragiliza a fluência procedimental |
| **Unidade de sorteio** | capítulo | sortear por ano, distribuindo os tipos antes, dá controle melhor da cobertura e pior da adequação capítulo a capítulo |
| **Complementares** | tipos sorteados, distintos do principal | fixar as complementares como sempre EX + ESC economiza produção e reduz muito a variedade |
| **Quantidade de `OBJ`** | 2 por capítulo, em todos os 95 | 1 por capítulo cobre menos confusões; 3 ou mais desequilibra a folha em favor da objetiva |
| **`OBJ` fora do sorteio** | fixa, complementar, ao final da folha do capítulo | sortear `OBJ` como os outros dezoito a faria desaparecer em capítulos onde ela é justamente o que falta, e disputaria a vaga da principal |
| **Peso da letra em R14** | 2 de 10 | 3 ou 4 tornam o chute lucrativo numa questão de 4 alternativas; 0 torna a marcação decorativa |

---

## Para onde ir daqui

| Se você quer | Abra |
|---|---|
| O argumento e o diagnóstico | [`01-PROPOSTA.md`](01-PROPOSTA.md) |
| A justificativa de cada tipo | [`02-BASE-DE-EVIDENCIA.md`](02-BASE-DE-EVIDENCIA.md) |
| Os 19 tipos e a distribuição | [`03-REPERTORIO.md`](03-REPERTORIO.md) |
| Os critérios de correção | [`04-RUBRICAS.md`](04-RUBRICAS.md) |
| Peso, quantidade e aplicação | [`05-REGRAS-DE-APLICACAO.md`](05-REGRAS-DE-APLICACAO.md) |
