# BL2_Capítulo 1 — Áreas de figuras planas

> Um terreno em formato de L não tem uma fórmula própria. Como calcular sua área usando apenas figuras conhecidas?

---

## 1. Áreas de quadriláteros

Uma quadra, uma placa e um terreno podem ter formas diferentes, mas a área de cada um depende de medidas perpendiculares.

### 1.1 Escolha da expressão

Antes do cálculo, é preciso reconhecer a figura e identificar suas medidas.

| Quadrilátero | Área | Medidas necessárias |
|---|---|---|
| quadrado | $$A=\ell^2$$ | lado $$\ell$$ |
| retângulo | $$A=b\cdot h$$ | base e altura |
| paralelogramo | $$A=b\cdot h$$ | base e altura perpendicular |
| losango | $$A=\frac{D\cdot d}{2}$$ | diagonais |
| trapézio | $$A=\frac{(B+b)\cdot h}{2}$$ | bases paralelas e altura |

No paralelogramo e no trapézio, o lado inclinado não substitui a altura.

<!-- tikz:inicio fig-01-altura-no-paralelogramo-e-trapezio -->
![Paralelogramo e trapézio com a altura perpendicular diferenciada do lado inclinado](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/8ano/areas-de-figuras-planas/fig-01-altura-no-paralelogramo-e-trapezio.png)
<!-- tikz:fim fig-01-altura-no-paralelogramo-e-trapezio -->

No losango, a expressão usa as diagonais, não os lados.

<!-- tikz:inicio fig-02-diagonais-do-losango -->
![Losango com diagonais perpendiculares D e d identificadas e lados sem medida](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/8ano/areas-de-figuras-planas/fig-02-diagonais-do-losango.png)
<!-- tikz:fim fig-02-diagonais-do-losango -->

A unidade final é quadrada porque a superfície possui duas dimensões independentes.

### 1.2 Aplicação em um terreno

**Lote trapezoidal**

Um lote tem bases paralelas de $$18\,\mathrm{m}$$ e $$10\,\mathrm{m}$$, separadas por uma altura de $$8\,\mathrm{m}$$.

**Resolução:**

- **Passo 1:** Somar as bases.

$$18+10=28\,\mathrm{m}$$

- **Passo 2:** Multiplicar pela altura.

$$28\cdot8=224\,\mathrm{m^2}$$

- **Passo 3:** Dividir por 2.

$$A=\frac{224}{2}$$

$$A=112\,\mathrm{m^2}$$

**Resposta:** o lote tem área de $$112\,\mathrm{m^2}$$.

> ⚠️ **Atenção:**  
> Todas as medidas devem estar na mesma unidade antes da aplicação da fórmula.

---

## 2. Área do triângulo

Uma tesoura corta um paralelogramo por sua diagonal e produz dois triângulos congruentes.

### 2.1 Metade de um paralelogramo

Como os dois triângulos ocupam juntos a área $$b\cdot h$$, cada um ocupa a metade:

$$A=\frac{b\cdot h}{2}$$

<!-- tikz:inicio fig-03-triangulo-metade-do-paralelogramo -->
![Duas cópias congruentes do triângulo compondo um paralelogramo de mesma base e altura](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/8ano/areas-de-figuras-planas/fig-03-triangulo-metade-do-paralelogramo.png)
<!-- tikz:fim fig-03-triangulo-metade-do-paralelogramo -->

Qualquer lado pode ser escolhido como base, desde que seja usada a altura correspondente. Essa altura é sempre perpendicular à reta que contém a base. Em um triângulo obtusângulo, ela pode ficar fora da figura e encontrar o prolongamento de um lado.

<!-- tikz:inicio fig-04-tres-pares-de-base-e-altura -->
![Mesmo triângulo apresentado com três escolhas de base e suas alturas perpendiculares correspondentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/8ano/areas-de-figuras-planas/fig-04-tres-pares-de-base-e-altura.png)
<!-- tikz:fim fig-04-tres-pares-de-base-e-altura -->

Em uma malha quadriculada, a contagem de quadrados inteiros e de partes complementares permite verificar o resultado da fórmula.

<!-- tikz:inicio fig-05-triangulo-na-malha-quadriculada -->
![Triângulo em malha quadriculada dentro de um retângulo cujas partes complementares permitem conferir a área](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/8ano/areas-de-figuras-planas/fig-05-triangulo-na-malha-quadriculada.png)
<!-- tikz:fim fig-05-triangulo-na-malha-quadriculada -->

### 2.2 Medida de uma cobertura

**Telhado triangular**

A face triangular de um telhado tem base de $$12\,\mathrm{m}$$ e altura perpendicular de $$7\,\mathrm{m}$$.

**Resolução:**

- **Passo 1:** Multiplicar base e altura.

$$12\cdot7=84\,\mathrm{m^2}$$

- **Passo 2:** Dividir o produto por 2.

$$A=\frac{84}{2}$$

$$A=42\,\mathrm{m^2}$$

**Resposta:** a face do telhado tem área de $$42\,\mathrm{m^2}$$.

Outra escolha de base e altura correspondente produziria a mesma área, pois a região triangular não se altera.

> 🔢 **Padrão:**  
> A base e a altura de um triângulo formam sempre um par perpendicular.

---

## 3. Composição e decomposição de figuras

Uma planta em formato de L pode ser tratada como a união de retângulos ou como um retângulo maior do qual se retirou uma parte.

### 3.1 Duas estratégias equivalentes

Em uma decomposição, as partes devem cobrir toda a figura sem lacunas nem sobreposições. Depois, suas áreas são somadas:

$$A_{total}=A_1+A_2+\cdots$$

Quando a figura possui um recorte, pode ser mais simples subtrair:

$$A_{figura}=A_{externo}-A_{recorte}$$

<!-- tikz:inicio fig-06-duas-decomposicoes-da-sala-em-l -->
![Sala em formato de L com dimensões oito por seis metros e recorte três por dois resolvida por duas decomposições](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/8ano/areas-de-figuras-planas/fig-06-duas-decomposicoes-da-sala-em-l.png)
<!-- tikz:fim fig-06-duas-decomposicoes-da-sala-em-l -->

O matemático **Thabit ibn Qurra** (c. 836–901), ligado à Casa da Sabedoria de Bagdá, preservou obras gregas e desenvolveu raciocínios baseados na decomposição e recomposição de figuras.

### 3.2 Área, rendimento e perda

**Piso de uma sala em L**

Uma sala ocupa um retângulo de $$8\,\mathrm{m}$$ por $$6\,\mathrm{m}$$, com um recorte de $$3\,\mathrm{m}$$ por $$2\,\mathrm{m}$$. Cada caixa cobre $$2\,\mathrm{m^2}$$ e a compra deve incluir $$10\%$$ de perda.

**Resolução:**

- **Passo 1:** Calcular a área externa.

$$8\cdot6=48\,\mathrm{m^2}$$

- **Passo 2:** Subtrair o recorte.

$$48-3\cdot2=42\,\mathrm{m^2}$$

- **Passo 3:** Incluir a margem de perda.

$$42\cdot1{,}10=46{,}2\,\mathrm{m^2}$$

- **Passo 4:** Dividir pelo rendimento e arredondar para cima.

$$\frac{46{,}2}{2}=23{,}1$$

**Resposta:** devem ser compradas 24 caixas de piso.

> ⚠️ **Atenção:**  
> Quantidades inteiras de embalagens são arredondadas para cima para garantir material suficiente.
