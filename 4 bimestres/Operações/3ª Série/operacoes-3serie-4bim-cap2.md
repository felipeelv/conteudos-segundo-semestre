# Capítulo 2 — Forma trigonométrica e fórmula de De Moivre

> Calcular (1 + i)¹⁰⁰ na forma algébrica é quase impossível; na forma trigonométrica é trivial. Como uma mudança de 'lente' torna potências gigantescas fáceis?
---

## 1. Módulo e argumento de um complexo

Módulo ρ = √(a² + b²); argumento θ (ângulo com o eixo real).

### 1.1 Conceito e linguagem

A definição fica completa com estas relações:
- cos θ = a/ρ; sen θ = b/ρ; argumento principal em [0, 2π).
- Cuidado com o quadrante ao obter θ.

### 1.2 Procedimento e interpretação

**Módulo e ângulo**

**Resolução:**

$$z=1+i$$

$$|z|=\sqrt2$$

$$\arg z=45^\circ$$

**Resposta:** o complexo fica no primeiro quadrante, a 45 graus do eixo real.

Abraham de Moivre (1667–1754) é a referência histórica deste tema matemático.
---

## 2. Forma trigonométrica (polar)

z = ρ·(cos θ + i·sen θ); dedução via plano polar.

### 2.1 Conceito e linguagem

Na leitura da notação, dois pontos são decisivos:
- Conversão algébrica ↔ trigonométrica, nos dois sentidos.
- O complexo como vetor (tamanho + direção).

### 2.2 Procedimento e interpretação

**Forma polar**

**Resolução:**

$$z=1+i$$

$$|z|=\sqrt2$$

$$z=\sqrt2(\cos45^\circ+i\sin45^\circ)$$

**Resposta:** módulo e argumento localizam o complexo no plano.

---

## 3. Multiplicação e divisão na forma trigonométrica

Multiplicar: multiplicar módulos e somar argumentos.

### 3.1 Conceito e linguagem

O procedimento preserva estas condições:
- Dividir: dividir módulos e subtrair argumentos.
- Interpretação geométrica (rotação + dilatação).

### 3.2 Procedimento e interpretação

**Quociente polar**

**Resolução:**

$$z_1=6\mathrm{cis}(80^\circ)$$

$$z_2=2\mathrm{cis}(20^\circ)$$

$$\frac{z_1}{z_2}=3\mathrm{cis}(60^\circ)$$

**Resposta:** no quociente, módulos dividem e argumentos subtraem.

---

## 4. Fórmula de De Moivre (potências)

zⁿ = ρⁿ·(cos nθ + i·sen nθ); demonstração por indução.

### 4.1 Conceito e linguagem

A definição fica completa com estas relações:
- Cálculo de potências altas (ex.: (1 + i)⁸, (1 + i)¹⁰⁰).
- Comparação com a expansão binomial (o ganho da forma polar).

### 4.2 Procedimento e interpretação

**Potência polar**

**Resolução:**

$$z=2(\cos30^\circ+i\sin30^\circ)$$

$$z^3=8(\cos90^\circ+i\sin90^\circ)$$

$$z^3=8i$$

**Resposta:** De Moivre eleva o módulo e multiplica o argumento.

---

## 5. Raízes n-ésimas de um número complexo

As n raízes n-ésimas: ρ^(1/n) com argumentos (θ + 2kπ)/n, k = 0, ..., n−1.

### 5.1 Conceito e linguagem

Na leitura da notação, dois pontos são decisivos:
- Distribuição das raízes em um polígono regular no plano.
- Exemplos (raízes cúbicas da unidade; raízes quadradas de complexos).

### 5.2 Procedimento e interpretação

**Raízes cúbicas de 8**

**Resolução:**

$$z^3=8$$

$$z_1=2$$

$$z_2=-1+\sqrt3i$$

- **Passo 4:** Conferir no modelo original.

$$z_3=-1-\sqrt3i$$

**Resposta:** as três raízes têm módulo 2 e argumentos separados por 120 graus.

---

## 6. Representação geométrica e aplicações

As raízes e potências no plano de Argand-Gauss.

### 6.1 Conceito e linguagem

O procedimento preserva estas condições:
- Aplicações: fasores em corrente alternada; rotações em computação gráfica.
- Menção à identidade de Euler e^(iθ) = cos θ + i·sen θ como "joia" (apresentação).

### 6.2 Procedimento e interpretação

**Rotação por multiplicação**

**Resolução:**

$$z=2$$

$$w=i$$

$$zw=2i$$

**Resposta:** multiplicar por i gira o ponto 90 graus em torno da origem.

