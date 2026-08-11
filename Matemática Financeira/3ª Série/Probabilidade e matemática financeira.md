# BL2_Capítulo 1 — Probabilidade e matemática financeira

> Toda a probabilidade do EM cabe em 5 ferramentas e toda a matemática financeira em 4 ideias. Diante de um problema real — um teste médico positivo, uma proposta de financiamento, três opções de investimento — como identificar em segundos qual ferramenta usar e aceitar o que o número disser?

---

## 1. Eventos, condicional e independência

As palavras do problema indicam qual relação probabilística precisa ser modelada.

### 1.1 Mapa de ferramentas

Cinco estruturas concentram os cálculos mais frequentes:

| Indício no enunciado | Ferramenta | Relação central |
|---|---|---|
| casos igualmente possíveis | clássica | $$P(A)=\frac{n(A)}{n(\Omega)}$$ |
| “ou”, com possível sobreposição | união | $$P(A\cup B)=P(A)+P(B)-P(A\cap B)$$ |
| “dado que” | condicional | $$P(A|B)=\frac{P(A\cap B)}{P(B)}$$ |
| evidência atualiza chance anterior | Bayes | $$P(A|B)=\frac{P(B|A)P(A)}{P(B)}$$ |
| $$k$$ sucessos em $$n$$ tentativas | binomial | $$P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$$ |

O complementar resolve “não ocorrer” ou “pelo menos um”:

$$P(\bar{A})=1-P(A)$$

Se $$A\cap B=\emptyset$$, os eventos são mutuamente exclusivos. Se forem independentes:

$$P(A\cap B)=P(A)P(B)$$

Numa partição $$A_1,\ldots,A_k$$, a probabilidade total é:

$$P(B)=\sum_iP(B|A_i)P(A_i)$$

Em 1937, **Bruno de Finetti** defendeu a probabilidade como grau coerente de crença diante da incerteza. Sua frase “a probabilidade não existe” criticava a ideia de uma chance separada do modelo e da informação, não o cálculo probabilístico.

### 1.2 Teste diagnóstico

**Resultado positivo hipotético**

Em 10.000 pessoas, a prevalência é 1%; sensibilidade e especificidade valem 95%.

| Grupo | Pessoas | Resultados positivos |
|---|---:|---:|
| Com a condição | 100 | 95 verdadeiros |
| Sem a condição | 9.900 | 495 falsos |

**Resolução:**

- **Passo 1:** Somar todos os positivos.

$$95+495=590$$

- **Passo 2:** Aplicar Bayes pela tabela.

$$P(\text{condicao}|+)=\frac{95}{590}\approx16{,}10\%$$

**Resposta:** cerca de 16,10% dos resultados positivos correspondem à condição; a baixa prevalência produz muitos falsos positivos no grupo maior.

> ⚠️ **Atenção:**
>
> Inverter a condição troca a pergunta: $$P(A|B)$$ geralmente não é igual a $$P(B|A)$$.

---

## 2. Juros simples e compostos

Variações sucessivas atuam sobre bases diferentes e, por isso, não devem ser apenas somadas.

### 2.1 Fatores e regimes

Um acréscimo ou desconto transforma o valor por um fator:

$$V_f=V_i(1\pm p)$$

A variação relativa é:

$$\Delta\%=\frac{V_f-V_i}{V_i}\cdot100$$

$$V_i$$ e $$V_f$$ são os valores inicial e final; $$p$$ é a taxa decimal.

Um aumento de 10% seguido de desconto de 10% produz:

$$100\cdot1{,}10\cdot0{,}90=99$$

A variação total é −1%, não zero.

Nos juros simples e compostos:

$$M_s=C(1+it)$$

$$M_c=C(1+i)^n$$

$$M$$ é o montante, $$C$$ o capital, $$i$$ a taxa por período e $$t$$ ou $$n$$, a quantidade de períodos. O regime simples cresce linearmente; o composto incorpora juros à base seguinte.

**Capital por 12 meses**

Considere R$ 1.000,00 a 2% ao mês.

**Resolução:**

- **Passo 1:** Calcular o regime simples.

$$M_s=1000(1+0{,}02\cdot12)=\mathrm{R\$}\,1\,240{,}00$$

- **Passo 2:** Calcular o composto.

$$M_c=1000(1{,}02)^{12}\approx\mathrm{R\$}\,1\,268{,}24$$

**Resposta:** o composto supera o simples em R$ 28,24 porque cada mês atualiza a base de juros.

### 2.2 Taxas equivalentes e reais

Taxas equivalentes produzem o mesmo fator acumulado:

$$1+i_a=(1+i_m)^{12}$$

Para 2% ao mês:

$$i_a=(1{,}02)^{12}-1\approx26{,}82\%\text{ ao ano}$$

A taxa nominal apenas declara uma referência; a efetiva mede o fator realmente acumulado no período.

A relação de Fisher apresenta a taxa real:

$$1+i_{real}=\frac{1+i_{nominal}}{1+\pi}$$

$$\pi$$ representa a inflação no mesmo intervalo. Com rendimento nominal hipotético de 10% e inflação de 4,64%:

$$i_{real}=\frac{1{,}10}{1{,}0464}-1\approx5{,}12\%$$

O poder de compra cresce aproximadamente 5,12%, antes de custos e impostos.

> 🔢 **Padrão:**
>
> Taxas só podem ser comparadas diretamente quando usam o mesmo período e o mesmo regime de capitalização.

---

## 3. Financiamentos e investimentos

Fluxos em datas distintas devem ser comparados numa mesma data.

### 3.1 Valor presente e amortização

$$VP=\frac{VF}{(1+i)^n}$$

$$VP$$ é o valor presente; $$VF$$, o futuro; $$i$$, a taxa; e $$n$$, o prazo.

Três descontos usam bases diferentes:

| Regime | Valor presente |
|---|---|
| Comercial simples | $$VP=N(1-dn)$$ |
| Racional simples | $$VP=\frac{N}{1+in}$$ |
| Composto | $$VP=\frac{N}{(1+i)^n}$$ |

$$N$$ é o valor nominal futuro e $$d$$, a taxa de desconto comercial.

Na Price, $$PMT$$ é constante. No SAC:

$$A=\frac{P}{n}$$

$$A$$ é constante e as prestações diminuem. A comparação exige total pago, perfil e CET.

### 3.2 VPL, TIR e contexto de 2026

$$VPL=-I_0+\sum_{k=1}^{n}\frac{FC_k}{(1+r)^k}$$

$$I_0$$ é o investimento inicial, $$FC_k$$ o fluxo no período $$k$$ e $$r$$ a taxa mínima de comparação.

**Projeto hipotético de dois anos**

Considere investimento inicial de R$ 1.000,00, retornos anuais de R$ 600,00 e taxa de 10% ao ano.

**Resolução:**

- **Passo 1:** Trazer os fluxos ao presente.

$$VPL=-1000+\frac{600}{1{,}10}+\frac{600}{(1{,}10)^2}$$

$$VPL\approx\mathrm{R\$}\,41{,}32$$

**Resposta:** o VPL positivo em R$ 41,32 indica retorno acima da taxa de 10% ao ano, dadas as projeções adotadas.

A **TIR** zera o VPL. Em fluxos convencionais, TIR maior que $$r$$ confirma o critério; mudanças de sinal exigem cautela.

Em junho de 2026, a Selic era 14,25% ao ano e o IPCA em 12 meses, 4,64%. A comparação de aplicações considerava:

| Modalidade | Regra | Retorno líquido depende de |
|---|---|---|
| Poupança | TR + 0,5% ao mês | data de aniversário; isenção de IR para pessoa física |
| CDB | taxa contratada, muitas vezes ligada ao CDI | IR, liquidez e risco do emissor |
| Tesouro Selic | remuneração vinculada à Selic | IR, custos e preço no resgate antecipado |

Os dados situam o cenário, sem recomendar produtos; taxas e condições mudam.

> ⚠️ **Atenção:**
>
> VPL depende da taxa e dos fluxos estimados; resultado positivo não elimina erro de projeção nem risco.
