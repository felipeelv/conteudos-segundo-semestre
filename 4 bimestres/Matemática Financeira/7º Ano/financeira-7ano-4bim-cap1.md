# Capítulo 1 — Juros simples

> Você empresta R$ 200 a um amigo e ele combina pagar “mais 10%” depois de 2 meses. Qual é o capital, qual é a taxa, qual é o tempo — e quanto ele paga no total?

---

## 1. Conceitos e cálculo dos juros simples

Nos juros simples, o acréscimo de cada período é calculado sempre sobre o capital inicial.

### 1.1 Cinco grandezas

Uma operação de juros simples relaciona:

- **capital** $$C$$ — valor inicial;
- **taxa** $$i$$ — porcentagem cobrada ou recebida por período;
- **tempo** $$t$$ — quantidade de períodos;
- **juros** $$J$$ — acréscimo produzido;
- **montante** $$M$$ — capital acrescido dos juros.

As fórmulas são:

$$J=C\cdot i\cdot t$$

$$M=C+J=C(1+i\cdot t)$$

Taxa e tempo precisam usar a mesma unidade. Uma taxa de 3% ao mês combina com meses; uma taxa de 12% ao ano combina com anos. Antes do cálculo, a porcentagem vira decimal:

$$10\%=\frac{10}{100}=0{,}10$$

### 1.2 O empréstimo de R$ 200,00

**Pagamento depois de dois meses**

Capital de R$ 200,00, taxa de 10% ao mês e prazo de dois meses.

**Resolução:**

- **Passo 1:** Registrar as grandezas.

$$C=200 \qquad i=0{,}10 \qquad t=2$$

- **Passo 2:** Calcular os juros.

$$J=200\cdot0{,}10\cdot2$$

$$J=\mathrm{R\$}\,40{,}00$$

- **Passo 3:** Calcular o montante.

$$M=200+40$$

$$M=\mathrm{R\$}\,240{,}00$$

**Resposta:** o capital é R$ 200,00, a taxa é 10% ao mês, o tempo é dois meses, os juros são R$ 40,00 e o total pago é R$ 240,00.

Em juros simples, o acréscimo mensal é constante:

| Mês | Juros acumulados | Montante |
|---:|---:|---:|
| 0 | R$ 0,00 | R$ 200,00 |
| 1 | R$ 20,00 | R$ 220,00 |
| 2 | R$ 40,00 | R$ 240,00 |

**Leonardo Fibonacci** apresentou problemas de cálculo comercial no *Liber Abaci*, de 1202. O sistema indo-arábico divulgado na obra tornou operações de juros e câmbio muito mais práticas na Europa.

> ⚠️ **Atenção:**  
> Escrever 10% como $$i=10$$ multiplica o resultado por cem; na fórmula, usa-se $$i=0{,}10$$.

---

## 2. Aplicações e tomada de decisão

O custo ou rendimento muda com capital, taxa e prazo; comparar propostas exige manter iguais as demais condições.

### 2.1 Duas taxas para o mesmo prazo

Considere dois empréstimos hipotéticos de R$ 500,00 por três meses, ambos em juros simples.

**Comparação de custos**

| Proposta | Taxa mensal | Prazo |
|---|---:|---:|
| A | 2% ao mês | 3 meses |
| B | 6% ao mês | 3 meses |

**Resolução:**

- **Passo 1:** Calcular os juros da proposta A.

$$J_A=500\cdot0{,}02\cdot3$$

$$J_A=\mathrm{R\$}\,30{,}00$$

$$M_A=500+30=\mathrm{R\$}\,530{,}00$$

- **Passo 2:** Calcular os juros da proposta B.

$$J_B=500\cdot0{,}06\cdot3$$

$$J_B=\mathrm{R\$}\,90{,}00$$

$$M_B=500+90=\mathrm{R\$}\,590{,}00$$

**Resposta:** com capital e prazo iguais, a taxa maior torna B R$ 60,00 mais cara que A. O exemplo explica o mecanismo, sem recomendar produto ou instituição.

### 2.2 Preço à vista e total parcelado

Uma oferta hipotética anuncia R$ 900,00 à vista ou dez parcelas de R$ 100,00.

$$10\cdot\mathrm{R\$}\,100{,}00=\mathrm{R\$}\,1\,000{,}00$$

$$\mathrm{R\$}\,1\,000{,}00-\mathrm{R\$}\,900{,}00=\mathrm{R\$}\,100{,}00$$

**Resposta:** o parcelamento custa R$ 100,00 a mais que o preço à vista. Mesmo que a propaganda diga “sem juros”, os dois preços precisam ser comparados; a diferença pode representar custo do prazo.

Comprar agora, esperar ou formar uma reserva não é decisão puramente aritmética: urgência, renda e risco importam. Daniel Kahneman mostrou que ganhos imediatos e palavras como “promoção” influenciam escolhas. Reconhecer o impulso ajuda a separar desejo, necessidade e capacidade de pagamento, sem julgar quem precisa recorrer a crédito.

> 🔢 **Padrão:**  
> Comparação financeira usa o total pago, o mesmo prazo e as mesmas condições, não apenas o tamanho da parcela.
