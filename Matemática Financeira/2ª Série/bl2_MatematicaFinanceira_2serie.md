# Financeira — 2ª Série · Bloco 2

> **3º Bimestre — Probabilidade condicional e crédito** · Bloco 2 (27/08–18/09)

**Capítulos deste bloco**

2. **Crédito e financiamentos** (3 aulas)

---

# BL2_Capítulo 1 — Crédito e financiamentos

> Uma casa de R$ 300 mil financiada em 30 anos pela Tabela Price custa, ao final, mais de R$ 1 milhão — R$ 750 mil só de juros. E uma dívida de R$ 1.000 no rotativo do cartão dobra em 5 meses. Como a mesma matemática dos juros compostos constrói patrimônio de um lado e destrói orçamento do outro?

---

## 1. Financiamentos e empréstimos

Uma prestação combina juros e amortização.

### 1.1 Juros e amortização

$$PMT_k=J_k+A_k$$

$$J_k=SD_{k-1}\cdot i$$

$$PMT_k$$ é a prestação; $$J_k$$, os juros; $$A_k$$, a amortização; $$SD_{k-1}$$, o saldo anterior; e $$i$$, a taxa. Somente $$A_k$$ reduz o saldo.

Na Price, a prestação é fixa:

$$PMT=\frac{P\cdot i\cdot(1+i)^n}{(1+i)^n-1}$$

$$P$$ é o principal e $$n$$, o número de prestações.

Em 1771, **Richard Price** formalizou anuidades; o sistema francês passou a levar seu nome.

### 1.2 Price × SAC

**Casa hipotética em dois sistemas**

Considere R$ 300.000,00 a 0,94% ao mês por 360 meses, sem custos adicionais.

**Resolução:**

- **Passo 1:** Calcular a prestação, com duas casas decimais.

$$PMT=\frac{300\,000\cdot0{,}0094\cdot(1{,}0094)^{360}}{(1{,}0094)^{360}-1}$$

$$PMT\approx\mathrm{R\$}\,2\,920{,}62$$

- **Passo 2:** Calcular a amortização constante do SAC.

$$A=\frac{P}{n}$$

$$A=\frac{300\,000}{360}\approx\mathrm{R\$}\,833{,}33$$

$$PMT_k=A+SD_{k-1}\cdot i$$

- **Passo 3:** Comparar cinco períodos, em reais.

| Mês | Saldo Price | Juros Price | Amort. Price | Parcela Price | Saldo SAC | Juros SAC | Parcela SAC |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 300.000,00 | 2.820,00 | 100,62 | 2.920,62 | 300.000,00 | 2.820,00 | 3.653,33 |
| 2 | 299.899,38 | 2.819,05 | 101,57 | 2.920,62 | 299.166,67 | 2.812,17 | 3.645,50 |
| 3 | 299.797,81 | 2.818,10 | 102,52 | 2.920,62 | 298.333,33 | 2.804,33 | 3.637,66 |
| 4 | 299.695,29 | 2.817,14 | 103,48 | 2.920,62 | 297.500,00 | 2.796,50 | 3.629,83 |
| 5 | 299.591,81 | 2.816,16 | 104,46 | 2.920,62 | 296.666,67 | 2.788,67 | 3.622,00 |

- **Passo 4:** Comparar os totais aproximados.

$$T_{Price}=\mathrm{R\$}\,1\,051\,423{,}20$$

$$J_{Price}=\mathrm{R\$}\,751\,423{,}20$$

$$T_{SAC}=\mathrm{R\$}\,809\,010{,}00$$

$$J_{SAC}=\mathrm{R\$}\,509\,010{,}00$$

Aqui, $$T$$ é o total pago e $$J$$, os juros.

**Resposta:** a Price começa menor, mas amortiza lentamente; o SAC começa maior e reduz o saldo mais depressa.

O **Custo Efetivo Total (CET)** inclui seguros, tarifas e tributos e pode superar a taxa contratual.

> ⚠️ **Atenção:**
>
> Uma parcela menor não significa financiamento mais barato quando prazo, juros e CET são diferentes.

---

## 2. Crédito e endividamento

Pagar integralmente a fatura e financiar seu saldo são operações financeiramente diferentes.

### 2.1 Fatura e rotativo

A fatura reúne compras até o fechamento e vence depois. Comprar logo após o fechamento costuma ampliar o prazo até o pagamento; isso só evita juros se a fatura for quitada integralmente.

O saldo não pago entra no **crédito rotativo**, limitado a 30 dias, ou pode ser parcelado. Em maio de 2026, a taxa média mensal do rotativo para pessoas físicas foi 15,09%, segundo a série 25477 do Banco Central.

**Dívida hipotética no rotativo**

Considere R$ 1.000,00 a 15,09% ao mês, sem pagamentos intermediários.

**Resolução:**

- **Passo 1:** Modelar a evolução matemática.

$$S_n=S_0(1+i)^n$$

$$S_0$$ é o saldo inicial, $$S_n$$ o saldo após $$n$$ meses e $$i$$ a taxa mensal decimal.

| Mês | Saldo matemático |
|---:|---:|
| 0 | R$ 1.000,00 |
| 1 | R$ 1.150,90 |
| 2 | R$ 1.324,71 |
| 3 | R$ 1.524,64 |
| 4 | R$ 1.754,49 |
| 5 | R$ 2.019,24 |

- **Passo 2:** Calcular a taxa anual equivalente.

$$i_{anual}=(1+0{,}1509)^{12}-1$$

$$i_{anual}\approx4{,}4007=440{,}07\%$$

**Resposta:** sem limite legal, a dívida ultrapassaria o dobro no quinto mês. Desde 2024, juros e encargos do rotativo e do parcelamento da fatura não podem superar 100% do principal; para R$ 1.000,00, esse componente fica limitado a R$ 1.000,00.

### 2.2 Endividamento e proteção

Comprometimento acima de 30% da renda funciona como alerta, não diagnóstico universal. Renda instável e despesas essenciais mudam a capacidade de pagamento.

A Lei nº 14.181/2021 define **superendividamento** como a impossibilidade manifesta de a pessoa consumidora, de boa-fé, pagar suas dívidas de consumo sem comprometer o mínimo existencial.

> ⚠️ **Atenção:**
>
> O limite legal de encargos reduz o crescimento máximo, mas não transforma o rotativo em crédito barato.

---

## 3. Uso consciente do crédito

O custo do crédito precisa ser comparado com a urgência, as alternativas e o impacto no orçamento.

### 3.1 Comparar propostas

O CET reúne o custo completo na mesma taxa. Prazo maior pode reduzir a parcela e elevar o total pago.

**Parcelamento anunciado como “sem juros”**

Um produto custa R$ 2.000,00 à vista ou dez parcelas de R$ 220,00.

**Resolução:**

- **Passo 1:** Somar as parcelas.

$$10\cdot\mathrm{R\$}\,220{,}00=\mathrm{R\$}\,2\,200{,}00$$

- **Passo 2:** Comparar com o preço à vista.

$$\frac{2200-2000}{2000}\cdot100=10\%$$

**Resposta:** o parcelamento custa R$ 200,00 a mais, diferença de 10%; a expressão “sem juros” não elimina um possível custo embutido.

Uma troca de dívida só reduz custo quando o novo CET e o total final são menores, sem alongamento que anule a economia.

### 3.2 Estratégias e renegociação

Duas estratégias priorizam dívidas de formas distintas:

| Estratégia | Prioridade | Efeito principal |
|---|---|---|
| Bola de neve | menor saldo | libera uma dívida mais cedo |
| Avalanche | maior CET | minimiza juros sob as mesmas condições |

Considere R$ 500,00 a 2% ao mês e R$ 2.000,00 a 10% ao mês. A primeira gera R$ 10,00 de juros no mês; a segunda, R$ 200,00. A avalanche ataca o custo maior, enquanto a bola de neve encerra primeiro o saldo menor.

Renegociação pode alterar taxa, prazo e encargos. Campanhas podem anunciar grandes percentuais de desconto sobre saldos antigos, mas a comparação deve usar valor final, número de parcelas e CET; desconto não é universal nem necessariamente recai sobre o principal.

Matematicamente, amortizar uma dívida cujo CET supera o retorno líquido de uma aplicação reduz uma despesa maior; a decisão também precisa preservar gastos essenciais e liquidez para imprevistos.

> 🔢 **Padrão:**
>
> Comparar crédito exige CET, total pago e prazo — nunca apenas o valor da parcela.
