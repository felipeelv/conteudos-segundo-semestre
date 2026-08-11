# Financeira — 1ª Série · Bloco 2

> **3º Bimestre — Medidas de dispersão e probabilidade** · Bloco 2 (27/08–18/09)

**Capítulos deste bloco**

2. **Probabilidade e educação financeira** (3 aulas)

---

# BL2_Capítulo 1 — Probabilidade e educação financeira

> Numa turma de 30 alunos, 18 jogam esporte, 12 tocam instrumento e 6 fazem os dois. Sorteando um aluno, qual a chance de ser esportista OU músico? Por que 18 + 12 = 30 (100%) está errado — e o que isso tem a ver com decidir onde investir seu dinheiro?

---

## 1. Conceitos fundamentais de probabilidade

Antes de calcular uma chance, é necessário definir quais resultados pertencem ao experimento.

### 1.1 Espaço e eventos

Um **experimento aleatório** possui resultado incerto. O **espaço amostral** $$\Omega$$ reúne todos os resultados possíveis; um evento é qualquer subconjunto de $$\Omega$$.

| Evento | Característica | Probabilidade |
|---|---|---:|
| Simples | um resultado | depende do experimento |
| Composto | dois ou mais resultados | depende do experimento |
| Certo | coincide com $$\Omega$$ | 1 |
| Impossível | conjunto vazio $$\emptyset$$ | 0 |

Toda probabilidade obedece a:

$$0\leq P(E)\leq1$$

$$P(\Omega)=1$$

O evento complementar $$\bar{A}$$ reúne tudo o que não pertence a $$A$$:

$$P(\bar{A})=1-P(A)$$

Em 1657, **Christiaan Huygens** publicou *De Ratiociniis in Aleae*, primeiro tratado impresso de probabilidade. Ele formalizou ideias iniciadas por Pascal e Fermat e introduziu o valor esperado, sem que esse conceito seja necessário neste capítulo.

### 1.2 Duas interpretações

Em espaços equiprováveis, a probabilidade clássica é:

$$P(E)=\frac{n(E)}{n(\Omega)}$$

Nessa expressão, $$n(E)$$ é a quantidade de casos favoráveis e $$n(\Omega)$$, o total de casos possíveis.

**Complementar no dado**

Calcule a chance de não sair 6 num dado comum.

**Resolução:**

- **Passo 1:** Calcular o evento “sair 6”.

$$P(A)=\frac{1}{6}$$

- **Passo 2:** Usar o complementar.

$$P(\bar{A})=1-\frac{1}{6}=\frac{5}{6}$$

$$\frac{5}{6}\approx0{,}8333=83{,}33\%$$

**Resposta:** cinco das seis faces não são 6; portanto, a chance é aproximadamente 83,33%.

Quando não há simetria conhecida, a frequência observada estima a probabilidade:

$$P(E)\approx\frac{f_a}{n}$$

Aqui, $$f_a$$ é o número de ocorrências e $$n$$, a quantidade de ensaios. A estimativa depende dos dados observados.

> 🔢 **Padrão:**
>
> A probabilidade clássica parte de resultados equiprováveis; a frequentista parte da repetição observada.

---

## 2. Cálculo em situações

Quando dois grupos se sobrepõem, somar suas quantidades conta a interseção duas vezes.

### 2.1 Regra da adição

Para eventos quaisquer:

$$P(A\cup B)=P(A)+P(B)-P(A\cap B)$$

$$A\cup B$$ representa “$$A$$ ou $$B$$”; $$A\cap B$$ representa a ocorrência conjunta.

**Esporte ou instrumento**

Numa turma de 30 alunos, 18 praticam esporte, 12 tocam instrumento e 6 fazem ambos.

**Resolução:**

- **Passo 1:** Calcular a quantidade presente na união.

$$n(A\cup B)=18+12-6=24$$

- **Passo 2:** Dividir pelo total.

$$P(A\cup B)=\frac{24}{30}=\frac{4}{5}=0{,}8=80\%$$

**Resposta:** a chance é 80%; somar 18 e 12 sem descontar 6 produziria 100% porque os mesmos alunos seriam contados duas vezes.

### 2.2 Exclusividade e ordens de grandeza

Eventos **mutuamente exclusivos** não ocorrem juntos:

$$A\cap B=\emptyset$$

Nesse caso, a interseção vale zero e as probabilidades podem ser somadas diretamente.

**Copas ou rei**

Num baralho comum, há 13 cartas de copas, 4 reis e 1 rei de copas.

**Resolução:**

- **Passo 1:** Descontar a carta contada nos dois eventos.

$$P(A\cup B)=\frac{13}{52}+\frac{4}{52}-\frac{1}{52}$$

$$P(A\cup B)=\frac{16}{52}=\frac{4}{13}\approx30{,}77\%$$

**Resposta:** a chance é aproximadamente 30,77%; copas e reis não são exclusivos porque o rei de copas pertence aos dois grupos.

Uma aposta simples da Mega-Sena corresponde a uma entre 50.063.860 combinações:

$$P(E)=\frac{1}{50\,063\,860}\approx0{,}000002\%$$

O evento é possível, mas sua ordem de grandeza mostra uma chance individual extremamente pequena.

> ⚠️ **Atenção:**
>
> O conectivo “ou” inclui a sobreposição, exceto quando os eventos são comprovadamente mutuamente exclusivos.

---

## 3. Educação financeira e decisões

Uma taxa nominal não revela sozinha ganho real, risco e custo.

### 3.1 Comparação situada em 2026

Em junho de 2026, a meta Selic era 14,25% ao ano, segundo o Banco Central, e o IPCA acumulado em 12 meses era 4,64%, segundo o IBGE.

Os mecanismos de renda fixa diferem:

| Modalidade | Regra de remuneração | Comparação exige observar |
|---|---|---|
| Poupança | TR + 0,5% ao mês | data de aniversário e isenção de IR para pessoa física |
| CDB | taxa contratada, geralmente ligada ao CDI | impostos, liquidez e risco do emissor |
| Tesouro Selic | título vinculado à Selic | impostos e oscilação no resgate antecipado |

O retorno real pode ser estimado por:

$$r_{real}\approx r_{nom}-i_{infl}$$

$$r_{real}$$ é a taxa real, $$r_{nom}$$ a nominal e $$i_{infl}$$ a inflação no mesmo período.

**Rendimento hipotético de 10% ao ano**

**Resolução:**

- **Passo 1:** Descontar a inflação de 4,64% em 12 meses.

$$r_{real}\approx10\%-4{,}64\%=5{,}36\%$$

**Resposta:** o aumento estimado do poder de compra seria 5,36% no período, antes de impostos e custos.

### 3.2 Risco, horizonte e crédito

Renda fixa define uma remuneração; renda variável oscila. Risco inclui perda, iliquidez ou inadimplência do emissor.

Uma decisão estruturada considera:

- retorno líquido e real;
- risco e liquidez;
- horizonte e objetivo;
- tributação, taxas e garantias aplicáveis.

No crédito, o **Custo Efetivo Total (CET)** reúne juros, tarifas, tributos e encargos. Comprometer até 30% da renda é apenas referência: despesas essenciais e estabilidade da renda mudam a capacidade de pagamento.

Uma reserva de emergência cobre imprevistos e exige acesso rápido.

Nos juros compostos:

$$M=C(1+i)^n$$

$$M$$ é o montante, $$C$$ o capital, $$i$$ a taxa decimal por período e $$n$$ a quantidade de períodos. Cada período incorpora os juros à base seguinte.

> ⚠️ **Atenção:**
>
> Rentabilidade passada ou taxa anunciada não elimina riscos, custos nem a necessidade de comparar prazos equivalentes.
