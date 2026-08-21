# Capítulo 1 — Fatoração e raízes de polinômios

> Como descobrir TODAS as raízes de um polinômio sem chutar valores? E o que os coeficientes já revelam sobre a soma e o produto das raízes, antes mesmo de encontrá-las?
---

## 1. Fatoração de polinômios

Decompor P(x) = aₙ·(x − r₁)·(x − r₂)·...·(x − rₙ).

### 1.1 Conceito e linguagem

A definição fica completa com estas relações:
- Fatorar por raiz conhecida + Briot-Ruffini para reduzir o grau.
- Fator comum e agrupamento como passos iniciais.

### 1.2 Procedimento e interpretação

**Fator comum e produto**

**Resolução:**

$$P(x)=x^2-5x+6$$

$$P(x)=(x-2)(x-3)$$

**Resposta:** a forma fatorada mostra os fatores lineares do polinômio.

Albert Girard (1595–1632) é a referência histórica deste tema matemático.
---

## 2. Multiplicidade de raízes

Fator (x − r)ᵏ: r é raiz de multiplicidade k.

### 2.1 Conceito e linguagem

Na leitura da notação, dois pontos são decisivos:
- Contagem total de raízes (com multiplicidade) = grau do polinômio.
- Distinção entre "número de raízes distintas" e "número de raízes com multiplicidade".

### 2.2 Procedimento e interpretação

**Raiz dupla**

**Resolução:**

$$P(x)=(x-2)^2(x+1)$$

$$m(2)=2$$

$$m(-1)=1$$

**Resposta:** a potência do fator indica a multiplicidade de cada raiz.

---

## 3. Relações de Girard

Soma das raízes = −aₙ₋₁/aₙ; produto = (−1)ⁿ·a₀/aₙ; somas de produtos intermediárias.

### 3.1 Conceito e linguagem

O procedimento preserva estas condições:
- Generalização das relações soma/produto do 2º grau para grau qualquer.
- Uso: obter informações sobre as raízes sem resolver a equação.

### 3.2 Procedimento e interpretação

**Soma e produto das raízes**

**Resolução:**

$$x^2-5x+6=0$$

$$x_1+x_2=5$$

$$x_1x_2=6$$

**Resposta:** as raízes 2 e 3 confirmam as relações de Girard.

---

## 4. Pesquisa de raízes racionais

Teorema das raízes racionais: se p/q é raiz, então p | a₀ e q | aₙ.

### 4.1 Conceito e linguagem

A definição fica completa com estas relações:
- Montar a lista finita de candidatos e testá-los (com Briot-Ruffini).
- Reduzir o polinômio a cada raiz encontrada até fatorar completamente.

### 4.2 Procedimento e interpretação

**Candidatos racionais**

**Resolução:**

$$P(x)=x^3-6x^2+11x-6$$

$$P(1)=0$$

$$P(x)=(x-1)(x-2)(x-3)$$

**Resposta:** testar divisores do termo independente encontra as três raízes inteiras.

