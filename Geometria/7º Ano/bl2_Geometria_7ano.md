# Geometria — 7º Ano · Bloco 2

> **3º Bimestre — Circunferência, área e perímetro** · Bloco 2 (27/08–18/09)

**Capítulos deste bloco**

2. **Área e perímetro** (3 aulas)

---

# BL2_Capítulo 1 — Área e perímetro

> Tinta se compra por área; moldura, por perímetro. E a pizza de 40 cm custa o dobro da de 30 cm — mas oferece o dobro de área?

---

## 1. O que área e perímetro medem

Uma quadra usa tinta na superfície e tela ao longo de seu contorno.

### 1.1 Dimensões diferentes

O **perímetro** é uma medida linear; a **área** mede uma superfície bidimensional.

| Grandeza | Operação | Unidade |
|---|---|---|
| perímetro | somar os lados | m |
| área | aplicar a expressão da figura | m² |

Figuras com o mesmo perímetro podem ter áreas diferentes. Um retângulo de $$1\,\mathrm{m}$$ por $$9\,\mathrm{m}$$ e um quadrado de lado $$5\,\mathrm{m}$$ têm perímetro de $$20\,\mathrm{m}$$, mas áreas de $$9\,\mathrm{m^2}$$ e $$25\,\mathrm{m^2}$$.

<!-- tikz:inicio fig-01-mesmo-perimetro-areas-diferentes -->
![Retângulo de um por nove metros e quadrado de lado cinco metros com mesmo perímetro e áreas diferentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/7ano/area-e-perimetro/fig-01-mesmo-perimetro-areas-diferentes.png)
<!-- tikz:fim fig-01-mesmo-perimetro-areas-diferentes -->

### 1.2 Conversões e expressões

Cada degrau entre unidades quadradas vale 100, pois duas dimensões são convertidas:

$$1\,\mathrm{m^2}=10\,000\,\mathrm{cm^2}$$

$$1\,\mathrm{km^2}=1\,000\,000\,\mathrm{m^2}$$

$$1\,\mathrm{ha}=10\,000\,\mathrm{m^2}$$

Uma expressão de área relaciona medidas da figura. Antes de aplicá-la, todas devem estar na mesma unidade.

Assim ficam comparáveis entre si.

**Placa e moldura**

Uma placa retangular mede $$1{,}2\,\mathrm{m}$$ por $$0{,}8\,\mathrm{m}$$.

**Resolução:**

- **Passo 1:** Calcular o perímetro.

$$P=2\cdot(1{,}2+0{,}8)$$

$$P=4\,\mathrm{m}$$

- **Passo 2:** Calcular a área.

$$A=1{,}2\cdot0{,}8$$

$$A=0{,}96\,\mathrm{m^2}$$

**Resposta:** a moldura mede $$4\,\mathrm{m}$$ e a placa ocupa $$0{,}96\,\mathrm{m^2}$$.

> ⚠️ **Atenção:**  
> Somar lados produz comprimento; multiplicar dimensões compatíveis produz área.

---

## 2. Área de quadriláteros e triângulos

Um terreno deve ser reconhecido antes que suas medidas entrem numa fórmula.

### 2.1 Quadriláteros

Decomposição e recomposição justificam as expressões principais:

| Figura | Área | Relação visual |
|---|---|---|
| quadrado | $$A=\ell^2$$ | lados iguais |
| retângulo | $$A=b\cdot h$$ | linhas por colunas |
| paralelogramo | $$A=b\cdot h$$ | recorte forma retângulo |
| losango | $$A=\frac{D\cdot d}{2}$$ | quatro triângulos pelas diagonais |
| trapézio | $$A=\frac{(B+b)\cdot h}{2}$$ | duas cópias formam paralelogramo |

No paralelogramo, um recorte triangular deslocado completa um retângulo de mesma base e altura.

<!-- tikz:inicio fig-02-recomposicao-do-paralelogramo -->
![Recorte triangular deslocado de um lado do paralelogramo para formar um retângulo de mesma área](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/7ano/area-e-perimetro/fig-02-recomposicao-do-paralelogramo.png)
<!-- tikz:fim fig-02-recomposicao-do-paralelogramo -->

No losango, as diagonais perpendiculares organizam quatro triângulos internos.

<!-- tikz:inicio fig-03-losango-em-quatro-triangulos -->
![Losango dividido por diagonais perpendiculares em quatro triângulos retângulos](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/7ano/area-e-perimetro/fig-03-losango-em-quatro-triangulos.png)
<!-- tikz:fim fig-03-losango-em-quatro-triangulos -->

No trapézio, duas cópias invertidas formam um paralelogramo de base $$B+b$$.

<!-- tikz:inicio fig-04-duplicacao-do-trapezio -->
![Duas cópias de um trapézio formando um paralelogramo cuja base mede B mais b](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/7ano/area-e-perimetro/fig-04-duplicacao-do-trapezio.png)
<!-- tikz:fim fig-04-duplicacao-do-trapezio -->

O matemático persa **Al-Khwarizmi** (c. 780–c. 850) tratou áreas de quadriláteros em sua obra sobre álgebra e geometria prática, usada em agrimensura e divisão de heranças.

### 2.2 Triângulos

Dois triângulos congruentes formam um paralelogramo, portanto:

$$A=\frac{b\cdot h}{2}$$

<!-- tikz:inicio fig-05-dois-triangulos-formam-paralelogramo -->
![Dois triângulos congruentes unidos para formar um paralelogramo de base b e altura h](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/7ano/area-e-perimetro/fig-05-dois-triangulos-formam-paralelogramo.png)
<!-- tikz:fim fig-05-dois-triangulos-formam-paralelogramo -->

Qualquer lado pode ser escolhido como base, desde que a altura correspondente seja perpendicular. Num triângulo obtusângulo, essa altura pode encontrar o prolongamento da base; no retângulo, os catetos já são perpendiculares.

**Vitral em losango**

As diagonais de um vitral medem $$1{,}2\,\mathrm{m}$$ e $$0{,}8\,\mathrm{m}$$.

**Resolução:**

- **Passo 1:** Multiplicar as diagonais.

$$1{,}2\cdot0{,}8=0{,}96$$

- **Passo 2:** Dividir por 2.

$$A=\frac{0{,}96}{2}$$

$$A=0{,}48\,\mathrm{m^2}$$

**Resposta:** o vitral tem área de $$0{,}48\,\mathrm{m^2}$$.

> 🔢 **Padrão:**  
> A altura usada nas áreas é sempre perpendicular à base escolhida.

---

## 3. Área do círculo e figuras compostas

Uma pizza maior cresce em duas direções, não apenas ao longo do diâmetro.

### 3.1 Do círculo ao quase-retângulo

Ao cortar um círculo em setores estreitos e alterná-los, forma-se uma figura próxima de um retângulo. Sua base tende a metade do comprimento da circunferência, $$\pi r$$, e sua altura é $$r$$:

$$A=\pi r\cdot r$$

$$A=\pi r^2$$

<!-- tikz:inicio fig-06-circulo-reorganizado-em-quase-retangulo -->
![Setores de um círculo alternados para aproximar um retângulo de base pi r e altura r](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/7ano/area-e-perimetro/fig-06-circulo-reorganizado-em-quase-retangulo.png)
<!-- tikz:fim fig-06-circulo-reorganizado-em-quase-retangulo -->

Como o raio está ao quadrado, duplicá-lo quadruplica a área.

**Duas pizzas**

Compare pizzas de diâmetros $$30\,\mathrm{cm}$$ e $$40\,\mathrm{cm}$$ usando $$\pi\approx3{,}14$$.

**Resolução:**

- **Passo 1:** Calcular a área da pizza menor, de raio $$15\,\mathrm{cm}$$.

$$A_1=3{,}14\cdot15^2$$

$$A_1=706{,}5\,\mathrm{cm^2}$$

- **Passo 2:** Calcular a área da maior, de raio $$20\,\mathrm{cm}$$.

$$A_2=3{,}14\cdot20^2$$

$$A_2=1\,256\,\mathrm{cm^2}$$

- **Passo 3:** Comparar.

$$\frac{A_2}{A_1}\approx1{,}78$$

**Resposta:** a pizza de 40 cm tem cerca de 78% mais área, não o dobro.

### 3.2 Composição e equivalência

Uma figura composta é calculada por partes simples:

- somar regiões que não se sobrepõem;
- subtrair recortes ou vazios;
- manter todas as medidas na mesma unidade.

<!-- tikz:inicio fig-07-composicao-e-subtracao-de-areas -->
![Mesma figura em formato de L dividida por soma de retângulos e por subtração de um recorte](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/7ano/area-e-perimetro/fig-07-composicao-e-subtracao-de-areas.png)
<!-- tikz:fim fig-07-composicao-e-subtracao-de-areas -->

Formas diferentes podem ter áreas equivalentes quando uma é obtida por recortes e deslocamentos da outra, sem perda nem sobreposição.

> ⚠️ **Atenção:**  
> A área do círculo é $$\pi r^2$$; elevar também o número $$\pi$$ ao quadrado altera indevidamente a medida.
