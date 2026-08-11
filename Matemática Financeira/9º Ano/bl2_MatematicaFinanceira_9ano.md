# Financeira — 9º Ano · Bloco 2

> **3º Bimestre — Educação financeira e probabilidade** · Bloco 2 (27/08–18/09)

**Capítulos deste bloco**

2. **Probabilidade: dependência e independência** (3 aulas)

---

# BL2_Capítulo 1 — Probabilidade: dependência e independência

> Você tira uma carta de copas do baralho e NÃO a devolve. A chance de a segunda carta ser copas ainda é 1/4? E se você joga uma moeda 5 vezes e dá cara nas 5, a próxima tem mais chance de ser coroa “para compensar”?

---

## 1. Eventos independentes

O resultado de uma moeda não altera as faces disponíveis em um dado separado.

### 1.1 Independência e produto

Dois eventos são **independentes** quando a ocorrência de um não modifica a probabilidade do outro.

Isso ocorre geralmente em:

- experimentos físicos separados;
- lançamentos sucessivos de moedas ou dados;
- sorteios com reposição do item retirado.

Para eventos independentes:

$$P(A \cap B)=P(A)\cdot P(B)$$

Nessa expressão, $$A\cap B$$ significa que os dois eventos ocorrem.

Em *Foundations of the Theory of Probability*, de 1933, **Andrey Kolmogorov** deu base axiomática moderna à probabilidade e rigor à definição de independência. Os axiomas formais não são necessários para aplicar a regra do produto.

**Cara e face 6**

Uma moeda equilibrada e um dado comum são lançados.

**Resolução:**

- **Passo 1:** Registrar as probabilidades separadas.

$$P(A)=\frac{1}{2}$$

$$P(B)=\frac{1}{6}$$

- **Passo 2:** Multiplicar.

$$P(A\cap B)=\frac{1}{2}\cdot\frac{1}{6}=\frac{1}{12}$$

$$\frac{1}{12}\approx0{,}0833=8{,}33\%$$

**Resposta:** cara e face 6 ocorrem juntas em aproximadamente 8,33% dos pares possíveis.

### 1.2 Sequências e memória

Para três caras seguidas:

$$P(C_1\cap C_2\cap C_3)=\left(\frac{1}{2}\right)^3=\frac{1}{8}=12{,}5\%$$

O mesmo produto se estende a mais eventos independentes.

Cinco caras anteriores não aumentam a chance de coroa no sexto lançamento:

$$P(\text{coroa no sexto})=\frac{1}{2}=50\%$$

A **falácia do apostador** é acreditar numa compensação obrigatória após uma sequência. A moeda não guarda memória dos resultados passados.

> ⚠️ **Atenção:**
>
> Uma sequência improvável pode ocorrer sem alterar a probabilidade da tentativa independente seguinte.

---

## 2. Eventos dependentes

Retirar uma carta sem devolvê-la reduz o baralho e modifica a chance seguinte.

### 2.1 Espaço amostral reduzido

Eventos são **dependentes** quando a ocorrência do primeiro altera as possibilidades do segundo.

Em extrações sem reposição:

- a primeira carta é retirada entre 52;
- a segunda é retirada entre 51;
- a composição restante depende da primeira retirada.

A notação $$P(B|A)$$ significa “probabilidade de $$B$$ dado que $$A$$ ocorreu”. A regra geral é:

$$P(A\cap B)=P(A)\cdot P(B|A)$$

Se os eventos forem independentes, então $$P(B|A)=P(B)$$ e a fórmula volta à regra do produto.

### 2.2 Duas cartas de copas

O diagrama representa as primeiras ramificações do sorteio sem reposição:

```text
1ª carta
├─ copas: 13/52
│  ├─ copas: 12/51
│  └─ outro naipe: 39/51
└─ outro naipe: 39/52
   ├─ copas: 13/51
   └─ outro naipe: 38/51
```

**Duas copas sem reposição**

**Resolução:**

- **Passo 1:** Calcular a chance da primeira carta ser copas.

$$P(A)=\frac{13}{52}=\frac{1}{4}=25\%$$

- **Passo 2:** Atualizar a chance após uma carta de copas sair.

$$P(B|A)=\frac{12}{51}=\frac{4}{17}\approx23{,}53\%$$

- **Passo 3:** Multiplicar os ramos.

$$P(A\cap B)=\frac{13}{52}\cdot\frac{12}{51}$$

$$P(A\cap B)=\frac{1}{17}\approx0{,}0588=5{,}88\%$$

**Resposta:** a segunda chance cai de 25% para cerca de 23,53%; a chance de ambas serem copas é aproximadamente 5,88%.

Como referência, a definição é:

$$P(A|B)=\frac{P(A\cap B)}{P(B)}$$

Thomas Bayes estudou como novas informações atualizam probabilidades, mas seu teorema completo exige outro tratamento. Além disso, $$P(A|B)$$ e $$P(B|A)$$ geralmente representam perguntas diferentes.

> 🔢 **Padrão:**
>
> Sem reposição, cada ramo usa o total e a composição que restaram após a etapa anterior.

---

## 3. Aplicações de probabilidade

Antes de calcular, é preciso decidir se o primeiro resultado altera ou não o seguinte.

### 3.1 Escolher a regra

O contexto identifica a relação entre os eventos:

| Situação | Relação | Regra |
|---|---|---|
| moeda e dado | independente | produto das probabilidades fixas |
| sorteio com reposição | independente | produto das probabilidades fixas |
| duas meias sem reposição | dependente | atualizar o segundo ramo |
| dois alunos sem repetir | dependente | reduzir o total após o primeiro |

**Duas meias pretas**

Uma gaveta possui 4 meias pretas e 2 brancas; duas são retiradas sem reposição.

**Resolução:**

- **Passo 1:** Registrar a primeira chance.

$$P(A)=\frac{4}{6}$$

- **Passo 2:** Atualizar a segunda chance.

$$P(B|A)=\frac{3}{5}$$

- **Passo 3:** Multiplicar.

$$P(A\cap B)=\frac{4}{6}\cdot\frac{3}{5}=\frac{2}{5}=40\%$$

**Resposta:** a chance de retirar duas meias pretas é 40%; a segunda retirada depende da primeira.

Uma previsão de 70% de chuva informa incerteza relevante para uma decisão, não certeza de que choverá.

### 3.2 Frequência e grandes números

Quando as chances teóricas são desconhecidas, a frequência observada oferece uma estimativa:

$$P(E)\approx\frac{n_{ocorridos}}{n_{ensaios}}$$

Num exemplo hipotético, a face 6 apareceu 132 vezes em 600 lançamentos:

$$P(6)\approx\frac{132}{600}=0{,}22=22\%$$

O resultado sugere diferença em relação aos 16,67% de um dado equilibrado, mas não prova sozinho que o dado seja viciado.

A **lei dos grandes números**, em sentido intuitivo, explica por que a frequência tende a se aproximar da probabilidade quando os ensaios aumentam. Sete caras em dez lançamentos correspondem a 70%; 503 em mil correspondem a 50,3%, muito mais perto dos 50% teóricos.

Abraham de Moivre aplicou probabilidades a seguros no século XVIII. No século XX, cadeias de Andrey Markov permitiram modelar sequências dependentes e inspiraram aplicações como o PageRank, sem que suas matrizes sejam necessárias aqui.

> ⚠️ **Atenção:**
>
> Frequência observada estima uma probabilidade; ela não garante o resultado da próxima tentativa.
