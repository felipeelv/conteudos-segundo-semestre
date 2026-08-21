# Capítulo 1 — Esferas

> Uma bola de futebol tem cerca de 5.300 cm³; a Terra, 1,08 × 10²¹ m³. As duas obedecem às mesmas fórmulas. Por que o volume cresce tão rapidamente quando o raio aumenta?

---

## 1. Esfera: definição e elementos

Uma bola preenchida e sua película externa não representam o mesmo objeto geométrico.

### 1.1 Lugar geométrico no espaço

**Esfera** é o conjunto dos pontos do espaço cuja distância ao centro $$O$$ é menor ou igual a $$r$$. **Superfície esférica** reúne apenas os pontos cuja distância é exatamente $$r$$.

| Objeto | Condição para um ponto $$P$$ |
|---|---|
| esfera | $$OP\leq r$$ |
| superfície esférica | $$OP=r$$ |

Os elementos fundamentais são:

- centro $$O$$;
- raio $$r$$, do centro à superfície;
- diâmetro $$d=2r$$, que atravessa o centro.

Essa é a primeira definição de sólido por uma propriedade satisfeita por todos os seus pontos, e não por uma lista de faces.

### 1.2 Sólido de revolução

A rotação completa de um semicírculo em torno de seu diâmetro gera uma esfera. O arco gera a superfície; a região semicircular gera o sólido preenchido.

**Modelo de um globo**

Um globo tem diâmetro de $$24\,\mathrm{cm}$$. Determine o raio e classifique pontos a $$8\,\mathrm{cm}$$ e $$12\,\mathrm{cm}$$ do centro.

**Resolução:**

- **Passo 1:** Dividir o diâmetro por 2.

$$r=\frac{24}{2}$$

$$r=12\,\mathrm{cm}$$

- **Passo 2:** Comparar a primeira distância com o raio.

$$8\,\mathrm{cm}<12\,\mathrm{cm}$$

- **Passo 3:** Comparar a segunda distância.

$$12\,\mathrm{cm}=12\,\mathrm{cm}$$

**Resposta:** o raio mede $$12\,\mathrm{cm}$$; o primeiro ponto está no interior da esfera e o segundo, na superfície esférica.

> ⚠️ **Atenção:**  
> “Esfera” inclui o interior; “superfície esférica” designa somente a casca.

---

## 2. Área da superfície esférica

Cobrir uma bola com material mede sua casca, não o espaço interno que ela comporta.

### 2.1 Relação de Arquimedes

**Arquimedes de Siracusa (c. 287–212 a.C.)** demonstrou em *Sobre a Esfera e o Cilindro*, por volta de 225 a.C., que:

$$A=4\pi r^2$$

Uma esfera de raio $$r$$ cabe exatamente num cilindro equilátero de mesmo raio e altura $$2r$$. A área lateral desse cilindro é:

$$A_l=2\pi r\cdot2r$$

$$A_l=4\pi r^2$$

Portanto, a superfície esférica tem a mesma área da superfície lateral do cilindro circunscrito. O expoente 2 confirma que se trata de área.

### 2.2 Escalas reais

**Revestimento de uma bola oficial**

Uma bola tem diâmetro de $$21{,}65\,\mathrm{cm}$$. Calcule sua área usando $$\pi\approx3{,}14$$.

**Resolução:**

- **Passo 1:** Obter o raio.

$$r=\frac{21{,}65}{2}$$

$$r=10{,}825\,\mathrm{cm}$$

- **Passo 2:** Aplicar a fórmula.

$$A=4\cdot3{,}14\cdot(10{,}825)^2$$

- **Passo 3:** Calcular a aproximação.

$$A\approx1471{,}79\,\mathrm{cm^2}$$

**Resposta:** a superfície da bola mede aproximadamente $$1471{,}79\,\mathrm{cm^2}$$.

Com raio médio de $$6371\,\mathrm{km}$$, a Terra possui cerca de 510 milhões de quilômetros quadrados de superfície pelo mesmo modelo.

> ⚠️ **Atenção:**  
> Substituir o diâmetro no lugar do raio multiplica indevidamente a área por 4.

---

## 3. Volume da esfera

Um reservatório esférico armazena matéria em todo o interior, por isso sua medida envolve três dimensões.

### 3.1 A relação dois para três

Considere a esfera inscrita num cilindro equilátero de raio $$r$$ e altura $$2r$$. O cilindro possui volume:

$$V_c=\pi r^2\cdot2r$$

$$V_c=2\pi r^3$$

Por comparação de secções no Princípio de Cavalieri, Arquimedes demonstrou que o volume da esfera corresponde a $$2/3$$ desse cilindro:

$$V_e=\frac{2}{3}\cdot2\pi r^3$$

$$V_e=\frac{4}{3}\pi r^3$$

Essa relação entre esfera e cilindro foi a descoberta geométrica escolhida para a tumba de Arquimedes. O expoente 3 indica que dobrar indevidamente o raio pelo diâmetro multiplicaria o resultado por 8.

### 3.2 Capacidade esférica

**Tanque esférico**

Um tanque tem raio interno de $$1{,}5\,\mathrm{m}$$. Calcule a capacidade usando $$\pi\approx3{,}14$$.

**Resolução:**

- **Passo 1:** Aplicar a fórmula do volume.

$$V=\frac{4}{3}\cdot3{,}14\cdot(1{,}5)^3$$

- **Passo 2:** Calcular o volume.

$$V=14{,}13\,\mathrm{m^3}$$

- **Passo 3:** Converter para litros.

$$14{,}13\cdot1000=14\,130\,\mathrm{L}$$

**Resposta:** o tanque comporta geometricamente aproximadamente $$14\,130\,\mathrm{L}$$.

Comparações entre gota, bola, planeta e estrela refletem o mesmo crescimento cúbico; por isso pequenos aumentos de raio geram grandes variações de volume.

> 🔢 **Padrão:**  
> Área esférica cresce com $$r^2$$, enquanto volume esférico cresce com $$r^3$$.

---

## 4. Partes da esfera, secções e posições relativas

Cortar uma laranja ou separar um fuso de globo evidencia partes planas e curvas diferentes.

### 4.1 Partes e secções

Quatro partes recebem nomes específicos:

- **calota** — porção determinada por um plano, com $$A=2\pi rh$$;
- **segmento esférico** — sólido entre dois planos paralelos;
- **fuso esférico** — faixa da superfície entre dois semicírculos máximos, com $$A=\pi r^2\alpha/90$$;
- **cunha esférica** — sólido correspondente ao fuso.

Toda secção plana de uma esfera é um círculo. Se o plano está a distância $$d$$ do centro, Pitágoras fornece o raio $$\rho$$ da secção:

$$\rho=\sqrt{r^2-d^2}$$

Quando $$d=0$$, surge um círculo máximo, como o equador; com $$0<d<r$$, surge um círculo menor, como um paralelo.

### 4.2 Plano e esfera

| Distância ao centro | Posição do plano |
|---|---|
| $$d<r$$ | secante |
| $$d=r$$ | tangente |
| $$d>r$$ | externa |

**Corte de um modelo terrestre**

Uma esfera de raio $$10\,\mathrm{cm}$$ é cortada por um plano a $$6\,\mathrm{cm}$$ do centro.

**Resolução:**

- **Passo 1:** Classificar o plano.

$$6\,\mathrm{cm}<10\,\mathrm{cm}$$

- **Passo 2:** Calcular o raio da secção.

$$\rho=\sqrt{10^2-6^2}$$

$$\rho=8\,\mathrm{cm}$$

**Resposta:** o plano é secante e produz um círculo de raio $$8\,\mathrm{cm}$$.

Eratóstenes estimou a circunferência terrestre por volta de 240 a.C. comparando sombras em localidades distintas, obtendo valor próximo de $$40\,000\,\mathrm{km}$$.

> ⚠️ **Atenção:**  
> Uma secção da esfera é um círculo preenchido, e sua borda é uma circunferência.
