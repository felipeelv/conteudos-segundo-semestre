# Capítulo 1 — Probabilidade: consolidação

> Se ambos os pais têm traço falciforme e planejam quatro filhos, qual é a probabilidade de nenhum ter doença falciforme? E de pelo menos um ter a doença?

---

## 1. Problemas de probabilidade

### 1.1 Contagem e experimentos compostos

Quando os resultados elementares são equiprováveis,

$$
P=\frac{casos\ favoraveis}{casos\ totais}.
$$

Uma mão de cinco cartas pode ser escolhida de $C(52,5)$ modos. A probabilidade de todas serem de copas é:

$$
P=\frac{C(13,5)}{C(52,5)}.
$$

A combinação é adequada porque a ordem das cartas na mão não importa; um arranjo seria usado se posições distintas alterassem o resultado. Pierre de Fermat e Blaise Pascal combinaram contagem e probabilidade, em 1654, ao estudar a divisão do prêmio de um jogo interrompido.

Em retiradas **com reposição**, as probabilidades permanecem iguais e as tentativas podem ser independentes. Se a chance de uma peça azul é $1/3$, duas retiradas azuis têm probabilidade $(1/3)^2=1/9$. Sem reposição, a primeira retirada altera a segunda. Duas cartas de copas consecutivas, sem devolver a primeira, têm:

$$
P=\frac{13}{52}\cdot\frac{12}{51}.
$$

### 1.2 Modelo binomial

A distribuição binomial descreve $n$ tentativas independentes, cada uma com dois resultados técnicos — sucesso e fracasso — e probabilidade de sucesso constante $p$:

$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}.
$$

**Situação hipotética:** uma peça tem probabilidade $p=0{,}2$ de falhar, e cinco peças independentes são observadas. Qual a chance de exatamente duas falharem?

**Resolução:**

- **Passo 1:** Identificar $n=5$ e $k=2$.
- **Passo 2:** Substituir na fórmula.

$$
P(X=2)=\binom{5}{2}(0{,}2)^2(0{,}8)^3
$$

$$
P(X=2)=10\cdot0{,}04\cdot0{,}512=0{,}2048
$$

**Resposta:** a probabilidade é 20,48%.

> ⚠️ **Atenção:** a fórmula binomial exige independência e probabilidade constante entre tentativas.

---

## 2. Aplicações de probabilidade

### 2.1 Genética e controle de qualidade

No modelo mendeliano simplificado $Aa\times Aa$, o quadrado de Punnett produz $AA$, $Aa$, $Aa$ e $aa$. Se $aa$ representa a doença autossômica recessiva, cada gestação tem probabilidade $1/4$ de doença e $3/4$ de não apresentar a doença. Gestações distintas são modeladas como independentes.

**Resolução:**

- **Passo 1:** Calcular a chance de nenhum dos quatro filhos ter a doença.

$$
P(X=0)=\left(\frac{3}{4}\right)^4=\frac{81}{256}\approx31{,}64\%
$$

- **Passo 2:** Usar o evento complementar para “pelo menos um”.

$$
P(X\geq1)=1-\frac{81}{256}=\frac{175}{256}\approx68{,}36\%
$$

**Resposta:** as probabilidades são aproximadamente 31,64% para nenhum e 68,36% para pelo menos um com a doença. Cada gestação mantém 25%; resultados anteriores não alteram a próxima.

No controle de qualidade, se a taxa hipotética de defeito é 2% e dez itens independentes são inspecionados:

$$
P(X\geq1)=1-(0{,}98)^{10}\approx18{,}29\%.
$$

Um critério de aceitar ou rejeitar lote transforma essa probabilidade em decisão, mas depende de a taxa e a independência representarem o processo real.

### 2.2 Jogos, risco e incerteza

Em jogos, resultados equiprováveis permitem calcular risco. Um prêmio de R$ 100,00 com chance de $1/100$ contribui com R$ 1,00 para uma média ponderada intuitiva; isso não significa receber R$ 1,00 em cada tentativa. Se o bilhete custa mais, o retorno médio é desfavorável, ainda que alguém possa ganhar.

**Risco** envolve probabilidades estimáveis; **incerteza** aparece quando elas são desconhecidas ou instáveis. Antes de aplicar um modelo, é necessário conferir reposição, independência, equiprobabilidade e constância de $p$. Loterias, genética e controle industrial usam estruturas parecidas, mas suas hipóteses e consequências não são intercambiáveis.

> ⚠️ **Atenção:** probabilidade descreve padrões de muitas situações; não prevê o resultado individual.
