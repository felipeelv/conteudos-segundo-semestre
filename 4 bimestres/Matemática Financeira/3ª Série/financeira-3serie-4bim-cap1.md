# Capítulo 1 — Leitura de dados e contextos

> Uma tabela traz notas com pesos, um gráfico corta o eixo e uma manchete afirma que o preço “subiu 200%”. O que os dados dizem antes de qualquer conclusão?

---

## 1. Estatística e probabilidade em contextos

### 1.1 Dado, medida e apresentação

Ler uma tabela começa por título, unidade, fonte, período, categorias e total. Em gráficos, também se verificam escala e origem dos eixos. Um eixo truncado pode ampliar visualmente diferenças pequenas; omitir o período pode esconder uma tendência anterior.

Cada medida central responde a uma pergunta. A média considera todos os valores; a mediana resiste a extremos; a moda indica o mais frequente. Com pesos, usa-se:

$$
\bar{x}_p=\frac{\sum x_iw_i}{\sum w_i}.
$$

**Situação hipotética:** uma avaliação vale 6 e tem peso 2; outra vale 8 e tem peso 3.

**Resolução:**

- **Passo 1:** Somar os produtos: $6\cdot2+8\cdot3=36$.
- **Passo 2:** Somar os pesos: $2+3=5$.

$$
\bar{x}_p=\frac{36}{5}=7{,}2
$$

**Resposta:** a média ponderada é 7,2; a nota de peso maior influencia mais o resultado.

“Aumento de 200%” significa acrescentar duas vezes o valor inicial: o resultado final é três vezes a base. Sem informar a base, o percentual não revela a magnitude absoluta.

### 1.2 Probabilidade e contagem

Na probabilidade clássica,

$$
P(E)=\frac{n(E)}{n(\Omega)},
$$

desde que os resultados sejam equiprováveis. Em um lote com 100 peças, das quais 4 são defeituosas, o sorteio de uma peça tem probabilidade $4/100=4\%$ de defeito.

O princípio fundamental da contagem multiplica etapas. Uma senha com duas letras e três algarismos, admitindo repetição, possui:

$$
26^2\cdot10^3=676000
$$

possibilidades. George Pólya enfatizou compreender o problema antes de planejar o cálculo. Aqui, isso significa identificar se há equiprobabilidade, reposição, restrição ou ordem.

> ⚠️ **Atenção:** fonte, recorte e hipótese fazem parte do dado; removê-los altera o sentido da conclusão.

---

## 2. Matemática financeira em contextos

### 2.1 Porcentagens encadeadas

Um acréscimo ou desconto transforma o valor inicial $V_i$ por um fator:

$$
V_f=V_i(1\pm p).
$$

A variação percentual é:

$$
\Delta\%=\frac{V_f-V_i}{V_i}\cdot100.
$$

Variações sucessivas não são somadas. Se um preço de R$ 100,00 aumenta 20% e depois cai 20%:

**Resolução:**

- **Passo 1:** Aplicar o aumento: $100\cdot1{,}20=120$.
- **Passo 2:** Aplicar o desconto sobre a nova base: $120\cdot0{,}80=96$.
- **Passo 3:** Comparar com o início: $(96-100)/100=-4\%$.

**Resposta:** o preço final é R$ 96,00, uma queda total de 4%.

### 2.2 Juros e proposta comercial

Nos juros simples, o acréscimo por período é calculado sobre o capital inicial:

$$
M=C(1+it).
$$

Nos compostos, cada período incorpora os juros acumulados:

$$
M=C(1+i)^n.
$$

Um contrato que diz “2% ao mês sobre o saldo acumulado” descreve capitalização composta; “2% ao mês sempre sobre o capital inicial” descreve juros simples.

Considere um produto de R$ 1.000,00 com 10% de desconto à vista ou três parcelas mensais de R$ 330,00.

**Resolução:**

- **Passo 1:** À vista: $1000\cdot0{,}90=900$.
- **Passo 2:** Parcelado: $3\cdot330=990$.
- **Passo 3:** Diferença: $990-900=90$, ou 10% do preço à vista.

**Resposta:** o parcelamento custa R$ 90,00 a mais. Se a primeira parcela vence em um mês, a taxa que iguala o valor presente das três parcelas a R$ 900,00 é aproximadamente 4,9% ao mês.

Comparar propostas exige mesma data de referência, total pago, taxas, encargos e efeito sobre o orçamento. “Sem juros” não elimina a diferença quando há desconto à vista.

> 🔢 **Em resumo:** percentuais dependem da base, e valores em datas diferentes dependem de uma taxa de comparação.
