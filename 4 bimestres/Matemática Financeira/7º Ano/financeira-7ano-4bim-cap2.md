# Capítulo 2 — Probabilidade

> Você sabe que P(cara) = 1/2. Mas se jogar a moeda 10 vezes, sairão exatamente 5 caras? E em 100 vezes? E em 1000 — o que muda?

---

## 1. Conceitos básicos e probabilidade clássica

Um experimento aleatório possui resultados conhecidos, mas seu resultado individual não pode ser previsto com certeza.

### 1.1 Espaço amostral e evento

O **espaço amostral** $$\Omega$$ reúne todos os resultados possíveis. Um **evento** $$A$$ é um subconjunto de resultados de interesse.

No lançamento de duas moedas, usando C para cara e K para coroa:

$$\Omega=\{CC,\ CK,\ KC,\ KK\}$$

O evento “exatamente uma cara” é:

$$A=\{CK,\ KC\}$$

Quando todos os resultados são equiprováveis:

$$P(A)=\frac{n(A)}{n(\Omega)}$$

$$P(A)=\frac{2}{4}=\frac{1}{2}=50\%$$

Toda probabilidade fica entre zero e um:

$$0\leq P(A)\leq1$$

### 1.2 Soma de dois dados

Dois dados distinguíveis produzem $$6\cdot6=36$$ pares ordenados. Para soma 7, os casos favoráveis são:

$$A=\{(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)\}$$

**Soma igual a 7**

**Resolução:**

- **Passo 1:** Contar os seis casos favoráveis.

$$n(A)=6$$

- **Passo 2:** Dividir pelos 36 resultados possíveis.

$$P(A)=\frac{6}{36}=\frac{1}{6}\approx16{,}67\%$$

**Resposta:** a soma 7 ocorre em aproximadamente 16,67% dos pares possíveis.

Para soma 2, apenas $$(1,1)$$ é favorável:

$$P(\text{soma 2})=\frac{1}{36}\approx2{,}78\%$$

Assim, soma 7 é seis vezes mais provável que soma 2. A comparação depende de listar pares, não apenas os totais de 2 a 12.

> ⚠️ **Atenção:**  
> A fórmula clássica exige resultados com a mesma chance; sem equiprobabilidade, contar casos não basta.

---

## 2. Experimentos e simulações

Uma simulação repete um processo aleatório e registra quantas vezes o evento acontece.

### 2.1 Planejamento e frequência relativa

Quatro elementos definem a simulação:

- pergunta investigada;
- espaço amostral;
- evento de interesse;
- quantidade de repetições.

A frequência relativa observada é:

$$f_r=\frac{n_{ocorrencias}}{n_{tentativas}}$$

Considere resultados hipotéticos já registrados para lançamentos de uma moeda:

| Tentativas | Caras | $$f_r$$ de caras |
|---:|---:|---:|
| 10 | 7 | 70% |
| 100 | 54 | 54% |
| 1.000 | 503 | 50,3% |

Em dez tentativas, uma diferença de duas caras altera a frequência em 20 pontos percentuais. Em mil, duas ocorrências alteram apenas 0,2 ponto. Por isso, amostras maiores oscilam proporcionalmente menos.

### 2.2 A ideia de Monte Carlo

**Stanisław Ulam** formulou, em 1946, uma estratégia para aproximar probabilidades difíceis por repetições aleatórias. O Método de Monte Carlo hoje apoia modelos em física, previsão do tempo e tecnologia.

Os dados da tabela permitem calcular cada frequência:

$$f_{r,10}=\frac{7}{10}=0{,}70$$

$$f_{r,100}=\frac{54}{100}=0{,}54$$

$$f_{r,1000}=\frac{503}{1000}=0{,}503$$

**Resposta:** os valores experimentais se aproximaram dos 50% teóricos conforme aumentou o número de tentativas, sem precisar atingir exatamente 50%.

> 🔢 **Padrão:**  
> Uma simulação informa quantas repetições foram feitas e como o evento foi contado.

---

## 3. Probabilidade e frequência

A probabilidade teórica descreve o modelo; a frequência relativa descreve o resultado observado.

### 3.1 Lei dos Grandes Números

Intuitivamente, a **Lei dos Grandes Números** afirma que a frequência relativa tende a se aproximar da probabilidade teórica quando o experimento é repetido muitas vezes.

O contraste precisa preservar duas ideias:

| Poucas repetições | Muitas repetições |
|---|---|
| oscilações proporcionais grandes | oscilações proporcionais menores |
| resultado pode ficar longe do teórico | frequência tende a se aproximar |
| não permite prever o próximo caso | também não prevê o caso individual |

Num sorteio equiprovável de um número entre 1 e 60, cada número tem:

$$P=\frac{1}{60}\approx0{,}0167=1{,}67\%$$

Em muitos sorteios, frequências tendem a se aproximar desse percentual, mas pequenas diferenças históricas não tornam um número “atrasado” ou “mais quente”.

### 3.2 A moeda não tem memória

Depois de cinco caras seguidas, a chance de cara no sexto lançamento continua:

$$P(\text{cara})=\frac{1}{2}$$

Esperar que a coroa se torne mais provável apenas para “equilibrar” a sequência é a **falácia do apostador**. A aproximação de longo prazo ocorre pelo conjunto crescente de resultados, não por uma correção obrigatória no próximo lance.

Quando um dado pode estar viciado, a simetria não garante equiprobabilidade. Nesse caso, muitas observações ajudam a estimar as chances de cada face, e a frequência experimental passa a ser evidência sobre o processo real.

> ⚠️ **Atenção:**  
> Uma sequência passada não altera a probabilidade do próximo resultado quando os lançamentos são independentes.
