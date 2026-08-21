# Capítulo 1 — Geometria plana e espacial

> Como um topógrafo mede a área de uma fazenda triangular do outro lado de um rio sem atravessá-lo — e quanto espaço fica vazio dentro de uma caixa cúbica que comporta exatamente uma bola?

---

## 1. Geometria plana: áreas, perímetros e relações métricas

Uma praça composta combina contornos, regiões e relações internas que precisam ser tratadas por grandezas diferentes.

### 1.1 Formulário justificado

Áreas decorrem de decomposição ou rearranjo; perímetros somam somente o contorno externo.

| Figura | Área |
|---|---|
| triângulo | $$A=\frac{bh}{2}$$ |
| equilátero | $$A=\frac{l^2\sqrt{3}}{4}$$ |
| retângulo/paralelogramo | $$A=bh$$ |
| trapézio | $$A=\frac{(B+b)h}{2}$$ |
| losango | $$A=\frac{Dd}{2}$$ |
| polígono regular | $$A=\frac{Pa_p}{2}$$ |
| círculo | $$A=\pi r^2$$ |

No círculo, o perímetro é $$2\pi r$$. Relações métricas completam as medidas:

$$a^2=b^2+c^2$$

$$b^2=am$$

$$c^2=an$$

$$h^2=mn$$

$$bc=ah$$

Na circunferência, potência de ponto iguala produtos: cordas $$PA\cdot PB=PC\cdot PD$$ e secante-tangente $$PA\cdot PB=PT^2$$.

### 1.2 Figura composta

**Praça com extremidade semicircular**

Um retângulo de $$10\,\mathrm{m}$$ por $$6\,\mathrm{m}$$ recebe, no lugar de um lado menor, um semicírculo de raio $$3\,\mathrm{m}$$. Use $$\pi\approx3{,}14$$.

**Resolução:**

- **Passo 1:** Somar as áreas.

$$A=10\cdot6+\frac{3{,}14\cdot3^2}{2}$$

$$A=74{,}13\,\mathrm{m^2}$$

- **Passo 2:** Somar três lados retos e o arco.

$$P=10+10+6+3{,}14\cdot3$$

$$P=35{,}42\,\mathrm{m}$$

**Resposta:** a praça ocupa $$74{,}13\,\mathrm{m^2}$$ e possui contorno de $$35{,}42\,\mathrm{m}$$.

**Bernhard Riemann (1826–1866)** mostrou em 1854 que a geometria euclidiana é um caso de uma teoria mais ampla; estas relações pertencem ao modelo euclidiano plano.

> ⚠️ **Atenção:**  
> Numa figura composta, segmentos internos de decomposição não pertencem ao perímetro externo.

---

## 2. Trigonometria: aplicações

Um topógrafo mede dois lados acessíveis e o ângulo entre eles para determinar uma região além do rio.

### 2.1 Três relações complementares

Para um triângulo qualquer:

$$S=\frac{1}{2}bc\cdot\mathrm{sen}\,A$$

$$\frac{a}{\mathrm{sen}\,A}=\frac{b}{\mathrm{sen}\,B}=\frac{c}{\mathrm{sen}\,C}=2R$$

$$a^2=b^2+c^2-2bc\cos A$$

A área nasce de base vezes altura, com $$h=c\cdot\mathrm{sen}\,A$$. A escolha depende dos dados:

Na medição indireta, o desenho precisa registrar qual ângulo está entre os lados conhecidos e qual lado se opõe a cada ângulo. Essa correspondência evita trocar termos entre as leis e permite conferir se o maior lado enfrenta o maior ângulo.

| Dados | Ferramenta |
|---|---|
| 2 lados e ângulo entre eles | Lei dos Cossenos |
| 2 ângulos e 1 lado | Lei dos Senos |
| 2 lados e ângulo entre eles para área | seno na área |

### 2.2 Fazenda triangular

**Levantamento sem atravessar o rio**

Duas divisas acessíveis medem $$200\,\mathrm{m}$$ e $$300\,\mathrm{m}$$, formando $$60^{\circ}$$.

**Resolução:**

- **Passo 1:** Calcular o terceiro lado pela Lei dos Cossenos.

$$a^2=200^2+300^2-2\cdot200\cdot300\cdot\cos60^{\circ}$$

$$a^2=70\,000\,\mathrm{m^2}$$

$$a=100\sqrt{7}\,\mathrm{m}$$

- **Passo 2:** Calcular a área pelo seno.

$$S=\frac{1}{2}\cdot200\cdot300\cdot\frac{\sqrt{3}}{2}$$

$$S=15\,000\sqrt{3}\,\mathrm{m^2}$$

- **Passo 3:** Converter a aproximação para hectares.

$$S\approx25\,980\,\mathrm{m^2}$$

$$S\approx2{,}598\,\mathrm{ha}$$

**Resposta:** a terceira divisa mede $$100\sqrt{7}\,\mathrm{m}$$ e a área é aproximadamente $$2{,}598\,\mathrm{ha}$$.

> 🔢 **Padrão:**  
> A modelagem topográfica substitui uma medida inacessível por lados e ângulos observáveis.

---

## 3. Geometria espacial: prismas e pirâmides

Um silo com corpo prismático e cobertura piramidal exige somar volumes calculados por fatores diferentes.

### 3.1 Bases, alturas e superfícies

Prismas repetem a área da base em toda altura; pirâmides afunilam até o ápice e ocupam um terço do prisma correspondente:

| Sólido | Volume |
|---|---|
| prisma | $$V=A_bh$$ |
| paralelepípedo | $$V=abc$$ |
| cubo | $$V=a^3$$ |
| pirâmide | $$V=\frac{A_bh}{3}$$ |

No paralelepípedo, Pitágoras em três direções produz $$d=\sqrt{a^2+b^2+c^2}$$; no cubo, $$d=a\sqrt{3}$$. O tetraedro regular é pirâmide de quatro faces equiláteras.

A área total soma base ou bases e faces laterais. Num prisma reto, $$A_l=P_bh$$. Numa pirâmide regular, as faces triangulares podem ser somadas por $$A_l=P_bg/2$$, com $$g$$ como apótema lateral.

No tronco de pirâmide, de altura $$h$$ e bases de áreas $$A_1$$ e $$A_2$$:

$$V=\frac{h}{3}(A_1+A_2+\sqrt{A_1A_2})$$

### 3.2 Silo composto

**Corpo e cobertura**

Um silo tem prisma de base quadrada com lado $$4\,\mathrm{m}$$ e altura $$6\,\mathrm{m}$$; a cobertura é piramidal, com a mesma base e altura $$3\,\mathrm{m}$$.

**Resolução:**

- **Passo 1:** Calcular a base.

$$A_b=4^2$$

$$A_b=16\,\mathrm{m^2}$$

- **Passo 2:** Calcular o corpo prismático.

$$V_p=16\cdot6$$

$$V_p=96\,\mathrm{m^3}$$

- **Passo 3:** Calcular a cobertura.

$$V_c=\frac{16\cdot3}{3}$$

$$V_c=16\,\mathrm{m^3}$$

- **Passo 4:** Somar.

$$V=96+16$$

$$V=112\,\mathrm{m^3}$$

**Resposta:** o conjunto possui volume geométrico de $$112\,\mathrm{m^3}$$.

> ⚠️ **Atenção:**  
> Prismas e pirâmides com a mesma base e altura têm volumes na razão 3 para 1.

---

## 4. Geometria espacial: cilindros, cones e esferas

Uma bola ajustada a uma caixa cúbica ocupa pouco mais da metade do volume disponível.

### 4.1 Corpos redondos e semelhança

As fórmulas decorrem das bases, das planificações e do Princípio de Cavalieri:

| Sólido | Área lateral | Volume |
|---|---|---|
| cilindro | $$2\pi rh$$ | $$\pi r^2h$$ |
| cone | $$\pi rg$$ | $$\frac{1}{3}\pi r^2h$$ |
| esfera | $$4\pi r^2$$ | $$\frac{4}{3}\pi r^3$$ |

No cone reto, $$g^2=h^2+r^2$$. O tronco de cone com raios $$R$$ e $$r$$ tem volume $$V=\pi h(R^2+Rr+r^2)/3$$ e área lateral $$A_l=\pi(R+r)g$$.

O cilindro equilátero satisfaz $$h=2r$$. Em sólidos semelhantes, medidas lineares variam por $$k$$, áreas por $$k^2$$ e volumes por $$k^3$$.

### 4.2 Inscrição e espaço vazio

Uma esfera inscrita num cubo tem $$r=a/2$$; um cubo inscrito em esfera tem $$r=a\sqrt{3}/2$$. A inscrição de cone em esfera é lida pela secção axial, que relaciona raio, altura e geratriz.

**Bola dentro de uma caixa**

Uma esfera de raio $$10\,\mathrm{cm}$$ está inscrita num cubo de aresta $$20\,\mathrm{cm}$$. Use $$\pi\approx3{,}14$$.

**Resolução:**

- **Passo 1:** Calcular o cubo.

$$V_c=20^3$$

$$V_c=8000\,\mathrm{cm^3}$$

- **Passo 2:** Calcular a esfera.

$$V_e=\frac{4}{3}\cdot3{,}14\cdot10^3$$

$$V_e\approx4186{,}67\,\mathrm{cm^3}$$

- **Passo 3:** Calcular o vazio.

$$V_v=8000-4186{,}67$$

$$V_v\approx3813{,}33\,\mathrm{cm^3}$$

**Resposta:** ficam vazios aproximadamente $$3813{,}33\,\mathrm{cm^3}$$; a esfera ocupa a fração $$\pi/6$$, cerca de 52,3% do cubo.

> 🔢 **Padrão:**  
> Inscrição transforma relações espaciais em medidas obtidas numa secção central.
