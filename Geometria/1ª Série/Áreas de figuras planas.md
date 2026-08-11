# BL2_Capítulo 1 — Áreas de figuras planas

> Por que um paralelogramo inclinado tem a mesma fórmula de área que um retângulo e por que um triângulo ocupa exatamente a metade?

---

## 1. Conceito de área, retângulo e quadrado

Ladrilhos congruentes podem mudar de posição sem alterar a superfície total que ocupam.

### 1.1 Princípios fundamentais

A **área** mede uma extensão bidimensional. Duas propriedades sustentam seu cálculo:

- regiões congruentes possuem a mesma área;
- uma região dividida sem sobreposição tem área igual à soma das partes.

Escolhida uma unidade quadrada, um retângulo com base $$b$$ e altura $$h$$ comporta $$b\cdot h$$ unidades. Assim,

$$A=b\cdot h$$

No quadrado, as duas dimensões têm medida $$\ell$$:

$$A=\ell^2$$

### 1.2 Pontos de uma rede

Em 1899, o matemático **Georg Pick** (1859–1942) mostrou que um polígono com vértices em uma rede inteira pode ter sua área calculada por

$$A=I+\frac{B}{2}-1$$

<!-- tikz:inicio fig-01-teorema-de-pick-na-malha -->
![Polígono em rede inteira com oito pontos interiores e dez pontos de fronteira marcados de modos distintos](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/areas-de-figuras-planas/fig-01-teorema-de-pick-na-malha.png)
<!-- tikz:fim fig-01-teorema-de-pick-na-malha -->

em que $$I$$ é o número de pontos interiores e $$B$$, o de pontos na fronteira. A expressão ilustra a aditividade por meio de uma contagem discreta.

**Polígono na malha**

Um polígono possui 8 pontos interiores e 10 pontos na fronteira.

**Resolução:**

- **Passo 1:** Substituir as contagens.

$$A=8+\frac{10}{2}-1$$

- **Passo 2:** Efetuar as operações.

$$A=8+5-1$$

$$A=12\,\mathrm{u^2}$$

**Resposta:** o polígono ocupa 12 unidades quadradas.

> 🔢 **Padrão:**  
> Recortar e deslocar partes sem deformá-las preserva a área total.

---

## 2. Área do paralelogramo

Um cartão em forma de paralelogramo pode ser recortado e reorganizado como retângulo.

### 2.1 Demonstração por recomposição

Traçando uma altura, separa-se de uma extremidade um triângulo retângulo. Ao transladá-lo para a outra extremidade, obtém-se um retângulo de mesma base $$b$$ e mesma altura $$h$$. Não há perda, sobreposição nem deformação; pela invariância e pela aditividade, as áreas são iguais:

$$A=b\cdot h$$

<!-- tikz:inicio fig-02-demonstracao-da-area-do-paralelogramo -->
![Sequência de recorte e translação que transforma um paralelogramo em retângulo de mesma base e altura](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/areas-de-figuras-planas/fig-02-demonstracao-da-area-do-paralelogramo.png)
<!-- tikz:fim fig-02-demonstracao-da-area-do-paralelogramo -->

A inclinação altera a posição do recorte, mas não a quantidade de unidades quadradas. Em paralelogramos muito inclinados, o pé da altura pode ficar no prolongamento da base; a distância perpendicular entre as retas paralelas continua sendo $$h$$.

<!-- tikz:inicio fig-03-altura-interna-e-externa-no-paralelogramo -->
![Dois paralelogramos com alturas perpendiculares interna e externa medindo a mesma distância entre bases](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/areas-de-figuras-planas/fig-03-altura-interna-e-externa-no-paralelogramo.png)
<!-- tikz:fim fig-03-altura-interna-e-externa-no-paralelogramo -->

### 2.2 Aplicação da altura perpendicular

**Painel inclinado**

Um painel tem base de $$9\,\mathrm{m}$$, lado oblíquo de $$5\,\mathrm{m}$$ e altura de $$4\,\mathrm{m}$$.

**Resolução:**

- **Passo 1:** Identificar a medida perpendicular à base.

$$h=4\,\mathrm{m}$$

- **Passo 2:** Multiplicar base e altura.

$$A=9\cdot4$$

$$A=36\,\mathrm{m^2}$$

**Resposta:** o painel tem área de $$36\,\mathrm{m^2}$$.

O lado oblíquo não entra no cálculo porque não mede a distância entre as bases paralelas.

> ⚠️ **Atenção:**  
> No paralelogramo, a altura é perpendicular à base e não deve ser confundida com o lado inclinado.

---

## 3. Área do triângulo

Duas placas triangulares congruentes podem ser encaixadas para formar um paralelogramo.

### 3.1 Metade de uma figura conhecida

O paralelogramo formado pelas duas cópias tem base $$b$$, altura $$h$$ e área $$b\cdot h$$. Como as cópias são congruentes, cada triângulo ocupa metade:

$$A=\frac{b\cdot h}{2}$$

<!-- tikz:inicio fig-04-duas-copias-do-triangulo -->
![Duas cópias congruentes de um triângulo formando um paralelogramo de base b e altura h](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/areas-de-figuras-planas/fig-04-duas-copias-do-triangulo.png)
<!-- tikz:fim fig-04-duas-copias-do-triangulo -->

Cada triângulo possui três pares possíveis de base e altura. A altura correspondente deve ser perpendicular à reta da base; qualquer par produz a mesma área. No triângulo retângulo, os catetos já formam esse par.

<!-- tikz:inicio fig-05-tres-pares-de-base-e-altura -->
![Mesmo triângulo com cada um dos três pares de base e altura correspondente destacado separadamente](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/areas-de-figuras-planas/fig-05-tres-pares-de-base-e-altura.png)
<!-- tikz:fim fig-05-tres-pares-de-base-e-altura -->

A igualdade entre os três produtos $$b\cdot h$$ expressa geometricamente que a região medida permanece a mesma, embora sua descrição mude.

### 3.2 Caso equilátero

No triângulo equilátero, a altura divide a base ao meio. O teorema de Pitágoras fornece

$$h=\frac{\ell\sqrt{3}}{2}$$

<!-- tikz:inicio fig-06-altura-do-triangulo-equilatero -->
![Triângulo equilátero de lado l dividido em dois triângulos retângulos com base l sobre dois](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/areas-de-figuras-planas/fig-06-altura-do-triangulo-equilatero.png)
<!-- tikz:fim fig-06-altura-do-triangulo-equilatero -->

e, por substituição,

$$A=\frac{\ell^2\sqrt{3}}{4}$$

**Peça equilátera**

Uma peça tem lado de $$6\,\mathrm{cm}$$.

**Resolução:**

- **Passo 1:** Calcular a altura.

$$h=\frac{6\sqrt{3}}{2}$$

$$h=3\sqrt{3}\,\mathrm{cm}$$

- **Passo 2:** Calcular a área.

$$A=\frac{6\cdot3\sqrt{3}}{2}$$

$$A=9\sqrt{3}\,\mathrm{cm^2}$$

**Resposta:** a área é $$9\sqrt{3}\,\mathrm{cm^2}$$, aproximadamente $$15{,}6\,\mathrm{cm^2}$$.

> 🔢 **Padrão:**  
> Trocar a base exige trocar também a altura correspondente.

---

## 4. Área do losango

As duas diagonais de um losango dividem a figura em quatro triângulos retângulos.

### 4.1 Dedução pelas diagonais

As diagonais são perpendiculares e cortam-se ao meio. Cada triângulo interno tem catetos $$D/2$$ e $$d/2$$, portanto sua área é

$$A_1=\frac{D\cdot d}{8}$$

Somando os quatro triângulos,

$$A=4\cdot\frac{D\cdot d}{8}$$

$$A=\frac{D\cdot d}{2}$$

<!-- tikz:inicio fig-07-losango-em-quatro-triangulos -->
![Losango dividido em quatro triângulos retângulos de catetos D sobre dois e d sobre dois](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/areas-de-figuras-planas/fig-07-losango-em-quatro-triangulos.png)
<!-- tikz:fim fig-07-losango-em-quatro-triangulos -->

Como o losango também é um paralelogramo, sua área pode ser calculada por $$b\cdot h$$. Os dois caminhos devem coincidir quando as medidas pertencem à mesma figura.

Essa coerência permite escolher o conjunto de dados disponível: diagonais favorecem a primeira fórmula; base e altura favorecem a segunda.

Nenhuma medida é redundante.

### 4.2 Aplicação em uma peça

**Vitral em losango**

As diagonais de um vitral medem $$10\,\mathrm{dm}$$ e $$6\,\mathrm{dm}$$.

**Resolução:**

- **Passo 1:** Multiplicar as diagonais.

$$10\cdot6=60\,\mathrm{dm^2}$$

- **Passo 2:** Dividir o produto por 2.

$$A=\frac{60}{2}$$

$$A=30\,\mathrm{dm^2}$$

**Resposta:** o vitral ocupa $$30\,\mathrm{dm^2}$$.

O comprimento do lado não é necessário quando as duas diagonais são conhecidas.

> ⚠️ **Atenção:**  
> Na fórmula do losango, $$D$$ e $$d$$ representam diagonais inteiras, não suas metades.

---

## 5. Área do trapézio

Duas telhas trapezoidais iguais podem ser giradas e unidas pelas laterais.

### 5.1 Demonstração por duplicação

As duas cópias formam um paralelogramo de base $$B+b$$ e altura $$h$$. Sua área é $$(B+b)\cdot h$$. Como cada trapézio ocupa metade da figura composta,

$$A=\frac{(B+b)\cdot h}{2}$$

<!-- tikz:inicio fig-08-duplicacao-do-trapezio -->
![Dois trapézios congruentes invertidos compondo um paralelogramo de base B mais b e altura h](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/areas-de-figuras-planas/fig-08-duplicacao-do-trapezio.png)
<!-- tikz:fim fig-08-duplicacao-do-trapezio -->

Outra dedução traça uma diagonal e separa o trapézio em dois triângulos de mesma altura. A soma de suas áreas é

$$A=\frac{B\cdot h}{2}+\frac{b\cdot h}{2}$$

$$A=\frac{(B+b)\cdot h}{2}$$

<!-- tikz:inicio fig-09-trapezio-decomposto-em-triangulos -->
![Trapézio dividido por uma diagonal em dois triângulos com bases B e b e altura comum h](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/areas-de-figuras-planas/fig-09-trapezio-decomposto-em-triangulos.png)
<!-- tikz:fim fig-09-trapezio-decomposto-em-triangulos -->

Assim, duplicação e decomposição conduzem à mesma expressão.

O argumento completa uma cadeia dedutiva: retângulos justificam paralelogramos; paralelogramos justificam triângulos; e triângulos, reunidos de modos diferentes, justificam losangos e trapézios.

Cada etapa preserva áreas mensuráveis.

### 5.2 Aplicação em uma cobertura

**Telha trapezoidal**

Uma peça tem bases paralelas de $$14\,\mathrm{cm}$$ e $$8\,\mathrm{cm}$$, com altura de $$5\,\mathrm{cm}$$.

**Resolução:**

- **Passo 1:** Somar as bases.

$$14+8=22\,\mathrm{cm}$$

- **Passo 2:** Multiplicar pela altura.

$$22\cdot5=110\,\mathrm{cm^2}$$

- **Passo 3:** Dividir por 2.

$$A=\frac{110}{2}$$

$$A=55\,\mathrm{cm^2}$$

**Resposta:** a área da peça é $$55\,\mathrm{cm^2}$$.

> 🔢 **Padrão:**  
> A altura do trapézio mede a distância perpendicular entre as bases paralelas.

---

## 6. Polígonos regulares e círculo

Um mosaico regular pode ser dividido em triângulos com vértice no centro.

### 6.1 Do polígono ao círculo

Em um polígono regular de $$n$$ lados, o **apótema** $$a$$ é a distância do centro a um lado. Os $$n$$ triângulos internos têm base total igual ao perímetro $$p=n\cdot\ell$$ e altura $$a$$:

$$A=\frac{p\cdot a}{2}$$

<!-- tikz:inicio fig-10-poligono-regular-em-triangulos -->
![Polígono regular dividido em triângulos centrais com lado l e apótema a identificados](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/areas-de-figuras-planas/fig-10-poligono-regular-em-triangulos.png)
<!-- tikz:fim fig-10-poligono-regular-em-triangulos -->

À medida que o número de lados cresce, o polígono aproxima um círculo: o apótema tende ao raio e o perímetro, ao comprimento $$2\pi r$$. Assim,

$$A=\pi r^2$$

<!-- tikz:inicio fig-11-poligonos-aproximando-o-circulo -->
![Sequência de polígonos regulares com mais lados aproximando uma circunferência e apótema tendendo ao raio](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/areas-de-figuras-planas/fig-11-poligonos-aproximando-o-circulo.png)
<!-- tikz:fim fig-11-poligonos-aproximando-o-circulo -->

Partes circulares também resultam de composição e subtração:

| Região | Área |
|---|---|
| setor | $$\frac{\theta}{360^\circ}\cdot\pi r^2$$ |
| segmento | área do setor menos área do triângulo |
| coroa | $$\pi(R^2-r^2)$$ |

<!-- tikz:inicio fig-12-setor-e-segmento-circular -->
![Mesmo arco delimitando um setor e um segmento circular com o triângulo que deve ser subtraído](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/areas-de-figuras-planas/fig-12-setor-e-segmento-circular.png)
<!-- tikz:fim fig-12-setor-e-segmento-circular -->

O arco de um setor mede $$\frac{\theta}{360^\circ}\cdot2\pi r$$.

<!-- tikz:inicio fig-13-coroa-circular -->
![Dois círculos concêntricos de raios R e r com somente a coroa entre eles destacada](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/areas-de-figuras-planas/fig-13-coroa-circular.png)
<!-- tikz:fim fig-13-coroa-circular -->

### 6.2 Faixa circular

**Trecho de pista**

Uma faixa circular tem raios externo e interno de $$38\,\mathrm{m}$$ e $$36{,}5\,\mathrm{m}$$. Use $$\pi\approx3{,}14$$.

**Resolução:**

- **Passo 1:** Calcular a diferença dos quadrados.

$$38^2-36{,}5^2=111{,}75\,\mathrm{m^2}$$

- **Passo 2:** Multiplicar por $$\pi$$.

$$A=3{,}14\cdot111{,}75$$

$$A=350{,}895\,\mathrm{m^2}$$

**Resposta:** a faixa ocupa aproximadamente $$350{,}9\,\mathrm{m^2}$$.

> ⚠️ **Atenção:**  
> A coroa circular exige subtrair os quadrados dos raios, não apenas os próprios raios.
