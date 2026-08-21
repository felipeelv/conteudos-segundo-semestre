# Capítulo 2 — Análise crítica e pesquisa

> Um gráfico mostra uma cotação passando de R$ 5,80 para R$ 6,00, mas o desenho parece indicar que ela dobrou. Como um dado verdadeiro pode sustentar uma impressão falsa?

---

## 1. Análise crítica de gráficos

### 1.1 Escala e proporção visual

Um eixo vertical iniciado em 5,80 amplia visualmente a diferença até 6,00. A variação percentual real é:

**Resolução:**

- **Passo 1:** Calcular a diferença: $6{,}00-5{,}80=0{,}20$.
- **Passo 2:** Dividir pelo valor inicial.

$$
\frac{0{,}20}{5{,}80}\cdot100\approx3{,}45\%
$$

**Resposta:** a alta é de aproximadamente 3,45%, embora um eixo truncado possa fazê-la parecer muito maior.

Começar o eixo em zero costuma preservar a proporção em gráficos de barras. Em gráficos de linha, um recorte pode ser útil para mostrar pequenas oscilações, desde que a interrupção seja explícita. Uma escala logarítmica também precisa ser identificada, pois distâncias iguais representam multiplicações, não acréscimos iguais.

Escolher apenas o intervalo que sustenta uma tese é **cherry picking**. O número não muda, mas o período escolhido esconde parte da trajetória.

### 1.2 Outras distorções e checklist

Gráficos 3D alteram a percepção pela perspectiva. Em pictogramas, dobrar altura e largura quadruplica a área do desenho, embora o dado apenas tenha dobrado. Darrell Huff popularizou a análise dessas manipulações em *How to Lie with Statistics* (1954).

Antes de aceitar a mensagem visual, convém verificar:

- fonte, período e unidade;
- título neutro e categorias comparáveis;
- escala uniforme e interrupções declaradas;
- proporção entre valores e formas;
- uso do zero quando ele é necessário para a comparação.

> ⚠️ **Atenção:** um gráfico pode usar números corretos e ainda induzir uma conclusão desproporcional.

---

## 2. Leitura crítica de estatísticas

### 2.1 Percentual, base e contexto

Uma manchete como “os casos aumentaram 100%” parece alarmante, mas pode descrever a passagem de 1 para 2 casos. O aumento relativo é realmente 100%; o aumento absoluto é de apenas um caso. As duas informações são necessárias.

**Resolução:**

- **Passo 1:** Identificar a base inicial: 1 caso.
- **Passo 2:** Calcular a mudança: $2-1=1$ caso.
- **Passo 3:** Comparar a mudança com a base.

$$
\frac{2-1}{1}\cdot100=100\%
$$

**Resposta:** houve aumento de um caso, equivalente a 100% da base inicial.

Período, fonte, população, tamanho da amostra e ponto de comparação formam o contexto. “Crescimento de 0,1%” pode ser descrito como avanço ou estabilidade, conforme o histórico e a incerteza; o dado isolado não decide a interpretação. Hans Rosling tornou-se referência na comunicação de estatísticas ao mostrar como intuições podem falhar quando ignoram séries completas e proporções.

### 2.2 Correlação não prova causa

Duas variáveis variarem juntas indica **correlação**, não necessariamente causalidade. Vendas de sorvete e ocorrências de afogamento podem subir no verão sem que sorvete cause afogamentos. A temperatura é uma **variável de confusão** que influencia ambas.

Também pode haver causa reversa: em vez de $A$ causar $B$, talvez $B$ influencie $A$. Para sustentar uma explicação causal, é preciso considerar mecanismo, ordem temporal, comparação adequada e fatores alternativos. Ler criticamente não significa rejeitar números, mas limitar a conclusão ao que o método permite.

> 🔢 **Em resumo:** pergunte “quanto?”, “em relação a quê?”, “em qual período?” e “por qual mecanismo?”.

---

## 3. Amostragem e pesquisa amostral

### 3.1 Representatividade e viés

Na amostragem aleatória simples, todos têm possibilidade conhecida de seleção. Na sistemática, escolhe-se um início e uma posição a cada intervalo. Na estratificada, preservam-se grupos relevantes. Se uma população de 1.000 pessoas tem 600 no grupo A e uma amostra terá 100, a parcela proporcional é:

**Resolução:**

- **Passo 1:** Usar $n_i=n\cdot\dfrac{N_i}{N}$.

$$
n_A=100\cdot\frac{600}{1\,000}=60
$$

- **Passo 2:** Reservar as 40 posições restantes aos demais grupos, segundo suas proporções.

**Resposta:** o grupo A deve ocupar 60 posições da amostra proporcional.

Em 1936, uma pesquisa da revista *Literary Digest* recebeu milhões de respostas, mas sua lista e a participação voluntária favoreceram certos eleitores. George Gallup usou uma amostra muito menor e melhor planejada. O episódio mostra que tamanho não elimina **viés de seleção**.

Pesquisas por conveniência e enquetes abertas não sustentam generalização. A margem de erro tende a diminuir com amostras maiores e bem selecionadas, mas aqui ela é interpretada qualitativamente, sem fórmula.

### 3.2 Método e relatório

Uma pesquisa amostral completa articula seis etapas:

| Etapa | Conteúdo |
|---|---|
| pergunta-problema | define o que se quer conhecer |
| planejamento | delimita população, amostra e variáveis |
| coleta | padroniza instrumento, período e unidade |
| tabulação | organiza frequências e categorias |
| análise | combina medidas e gráficos adequados |
| relatório | apresenta método, resultados e limitações |

Jerzy Neyman formalizou fundamentos da amostragem representativa e estratificada no século XX. Declarar limitações não enfraquece um relatório: informa até onde suas conclusões podem chegar. Uma amostra pode ser pequena demais para certos recortes, excluir um grupo ou acumular não respostas. O relatório honesto registra esses limites e evita transformar descrição da amostra em certeza sobre toda a população.

> ⚠️ **Atenção:** uma pesquisa é tão confiável quanto a seleção, a coleta e a transparência de seu relatório.
