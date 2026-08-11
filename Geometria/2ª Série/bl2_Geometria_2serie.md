# Geometria — 2ª Série · Bloco 2

> **3º Bimestre — Cilindros e cones** · Bloco 2 (27/08–18/09)

**Capítulos deste bloco**

2. **Cones** (6 aulas)

---

# BL2_Capítulo 1 — Cones

> Qual deve ser o formato de uma folha plana para que ela se transforme em um chapéu cônico sem sobras nem aberturas?

---

## 1. Definição e elementos do cone

Ao girar um triângulo retângulo em torno de um de seus catetos, sua hipotenusa varre uma superfície cônica.

<!-- tikz:inicio fig-01-geracao-do-cone-por-rotacao -->
![Triângulo retângulo girando em torno de um cateto enquanto a hipotenusa gera a superfície de um cone](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cones/fig-01-geracao-do-cone-por-rotacao.png)
<!-- tikz:fim fig-01-geracao-do-cone-por-rotacao -->

### 1.1 Duas descrições equivalentes

O cone pode ser entendido como um **sólido de revolução** ou como uma pirâmide de base circular. No cone reto, seus elementos são:

- **vértice:** ponto de encontro das geratrizes;
- **base:** círculo de raio $$r$$;
- **eixo:** reta que liga o vértice ao centro da base;
- **altura $$h$$:** distância perpendicular do vértice ao plano da base;
- **geratriz $$g$$:** segmento do vértice à circunferência da base.

<!-- tikz:inicio fig-02-elementos-do-cone -->
![Cone reto com vértice, base, eixo, raio r, altura h e geratriz g identificados](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cones/fig-02-elementos-do-cone.png)
<!-- tikz:fim fig-02-elementos-do-cone -->

Uma secção pelo eixo revela um triângulo retângulo de catetos $$h$$ e $$r$$ e hipotenusa $$g$$. Portanto,

$$g^2=h^2+r^2$$

### 1.2 Relação fundamental

**Cone de sinalização**

Um cone reto possui raio de $$5\,\mathrm{cm}$$ e altura de $$12\,\mathrm{cm}$$.

**Resolução:**

- **Passo 1:** Aplicar o teorema de Pitágoras.

$$g^2=12^2+5^2$$

- **Passo 2:** Somar os quadrados.

$$g^2=144+25$$

$$g^2=169$$

- **Passo 3:** Obter a raiz positiva.

$$g=13\,\mathrm{cm}$$

**Resposta:** a geratriz mede $$13\,\mathrm{cm}$$.

> ⚠️ **Atenção:**  
> A geratriz é a hipotenusa do triângulo gerador e, por isso, é maior que a altura e o raio.

---

## 2. Classificação dos cones

Um cone de trânsito permanece reto; uma pilha cônica deformada pode ter o vértice deslocado em relação ao centro da base.

### 2.1 Eixo e secção meridiana

No **cone reto**, o eixo é perpendicular ao plano da base. No **cone oblíquo**, ele é inclinado. Uma secção meridiana de um cone reto contém o eixo e produz um triângulo isósceles de base $$2r$$, altura $$h$$ e lados iguais a $$g$$.

<!-- tikz:inicio fig-03-cone-reto-e-obliquo -->
![Comparação entre cone reto de eixo perpendicular à base e cone oblíquo de eixo inclinado](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cones/fig-03-cone-reto-e-obliquo.png)
<!-- tikz:fim fig-03-cone-reto-e-obliquo -->

O **cone equilátero** é o caso em que essa secção é um triângulo equilátero. Logo,

$$g=2r$$

$$h=r\sqrt{3}$$

<!-- tikz:inicio fig-04-seccao-meridiana-do-cone-equilatero -->
![Secção meridiana equilátera de um cone com base dois r, lados g e altura r raiz de três](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cones/fig-04-seccao-meridiana-do-cone-equilatero.png)
<!-- tikz:fim fig-04-seccao-meridiana-do-cone-equilatero -->

O geômetra grego **Menecmo** (c. 380–c. 320 a.C.) percebeu que cortes planos em cones geravam curvas distintas, origem histórica do estudo das cônicas.

### 2.2 Caso equilátero

**Cone decorativo**

Um cone equilátero possui raio de $$4\,\mathrm{cm}$$.

**Resolução:**

- **Passo 1:** Calcular a geratriz.

$$g=2\cdot4$$

$$g=8\,\mathrm{cm}$$

- **Passo 2:** Calcular a altura.

$$h=4\sqrt{3}\,\mathrm{cm}$$

**Resposta:** a geratriz mede $$8\,\mathrm{cm}$$ e a altura, $$4\sqrt{3}\,\mathrm{cm}$$.

> 🔢 **Padrão:**  
> Apenas o cone reto pode ser equilátero, pois a classificação depende de sua secção meridiana simétrica.

---

## 3. Área lateral do cone

Ao abrir a lateral de um chapéu cônico, obtém-se um setor circular, e não um círculo completo.

### 3.1 Planificação e dedução

O setor tem raio $$g$$. Seu arco deve coincidir com a circunferência da base, de comprimento $$2\pi r$$. Se $$\alpha$$ é o ângulo central do setor,

$$\frac{\alpha}{360^\circ}=\frac{2\pi r}{2\pi g}$$

$$\frac{\alpha}{360^\circ}=\frac{r}{g}$$

A área do setor é a mesma da superfície lateral:

$$A_L=\frac{\alpha}{360^\circ}\cdot\pi g^2$$

Substituindo a razão anterior,

$$A_L=\pi rg$$

<!-- tikz:inicio fig-05-planificacao-da-area-lateral -->
![Superfície lateral do cone aberta em setor circular de raio g e arco de comprimento dois pi r](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cones/fig-05-planificacao-da-area-lateral.png)
<!-- tikz:fim fig-05-planificacao-da-area-lateral -->

A planificação preserva comprimentos: a geratriz permanece como raio do setor e a borda circular torna-se seu arco. Por isso, modificar o raio da base também modifica o ângulo necessário.

### 3.2 Recorte de fabricação

**Chapéu cônico**

Um chapéu tem raio da base de $$7\,\mathrm{cm}$$ e geratriz de $$21\,\mathrm{cm}$$.

**Resolução:**

- **Passo 1:** Determinar o ângulo do setor.

$$\alpha=360^\circ\cdot\frac{7}{21}$$

$$\alpha=120^\circ$$

- **Passo 2:** Calcular a área lateral.

$$A_L=\pi\cdot7\cdot21$$

$$A_L=147\pi\,\mathrm{cm^2}$$

**Resposta:** o recorte é um setor de raio $$21\,\mathrm{cm}$$, ângulo $$120^\circ$$ e área $$147\pi\,\mathrm{cm^2}$$.

> ⚠️ **Atenção:**  
> Na planificação, o raio do setor é a geratriz do cone, enquanto seu arco é o contorno da base.

---

## 4. Área total do cone

Revestir um cone fechado exige material para a superfície curva e para sua base circular.

### 4.1 Soma das superfícies

A base possui área

$$A_B=\pi r^2$$

e a superfície lateral possui área

$$A_L=\pi rg$$

Somando regiões que não se sobrepõem,

$$A_T=A_L+A_B$$

$$A_T=\pi r(g+r)$$

<!-- tikz:inicio fig-06-planificacao-da-area-total -->
![Planificação do cone fechado com setor lateral de raio g e círculo da base de raio r separados](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cones/fig-06-planificacao-da-area-total.png)
<!-- tikz:fim fig-06-planificacao-da-area-total -->

No cone equilátero, $$g=2r$$; portanto, $$A_L=2\pi r^2$$ e $$A_T=3\pi r^2$$. Quando o problema fornece altura e raio, a geratriz deve ser calculada antes da área.

Em fabricação, a superfície solicitada determina quais parcelas entram: um cone fechado inclui base e lateral; um cone sem base utiliza somente a lateral. A sequência segura é identificar as superfícies, encontrar medidas ausentes e então somar suas áreas.

Isso evita parcelas indevidas.

### 4.2 Revestimento completo

**Embalagem cônica**

Uma embalagem fechada possui raio de $$3\,\mathrm{cm}$$ e altura de $$4\,\mathrm{cm}$$.

**Resolução:**

- **Passo 1:** Calcular a geratriz.

$$g^2=4^2+3^2$$

$$g=5\,\mathrm{cm}$$

- **Passo 2:** Calcular a área total.

$$A_T=\pi\cdot3\cdot(5+3)$$

$$A_T=24\pi\,\mathrm{cm^2}$$

**Resposta:** o revestimento completo ocupa $$24\pi\,\mathrm{cm^2}$$.

> 🔢 **Padrão:**  
> Área total inclui a base; recipientes abertos podem exigir apenas a área lateral.

---

## 5. Volume do cone

Três recipientes cônicos iguais enchem um cilindro com a mesma base e a mesma altura.

### 5.1 Um terço do cilindro

Pelo princípio de Cavalieri, o cone possui o mesmo volume de uma pirâmide de base circular e igual altura. Por isso,

$$V=\frac{1}{3}\pi r^2h$$

<!-- tikz:inicio fig-07-tres-cones-preenchem-um-cilindro -->
![Três porções cônicas equivalentes preenchendo um cilindro de mesma base e altura](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cones/fig-07-tres-cones-preenchem-um-cilindro.png)
<!-- tikz:fim fig-07-tres-cones-preenchem-um-cilindro -->

O cilindro correspondente tem volume $$\pi r^2h$$; assim, o fator $$1/3$$ expressa que três cones completam esse cilindro. A fórmula usa a altura perpendicular $$h$$, não a geratriz $$g$$.

Volume mede o espaço tridimensional ocupado. Como $$1\,\mathrm{cm^3}=1\,\mathrm{mL}$$, o resultado também pode representar a capacidade interna de recipientes quando as medidas fornecidas são internas.

Medidas externas descrevem outro volume.

### 5.2 Capacidade de uma casquinha

**Casquinha cônica**

Uma casquinha possui raio interno de $$3\,\mathrm{cm}$$ e altura de $$10\,\mathrm{cm}$$.

**Resolução:**

- **Passo 1:** Elevar o raio ao quadrado.

$$3^2=9\,\mathrm{cm^2}$$

- **Passo 2:** Substituir na fórmula.

$$V=\frac{1}{3}\cdot\pi\cdot9\cdot10$$

- **Passo 3:** Simplificar.

$$V=30\pi\,\mathrm{cm^3}$$

$$V\approx94{,}2\,\mathrm{cm^3}$$

**Resposta:** a casquinha comporta aproximadamente $$94{,}2\,\mathrm{cm^3}$$, equivalentes a $$94{,}2\,\mathrm{mL}$$.

> ⚠️ **Atenção:**  
> Medidas lineares geram volume em unidades cúbicas após a aplicação da fórmula.

---

## 6. Tronco de cone

Um balde tem duas bases circulares de tamanhos diferentes e laterais inclinadas, formando um tronco de cone.

### 6.1 Elementos e fórmulas

O tronco é a porção entre a base de um cone e uma secção paralela a ela. Seus elementos são raio maior $$R$$, raio menor $$r$$, altura $$h$$ e geratriz $$g$$. A secção meridiana fornece

<!-- tikz:inicio fig-08-elementos-do-tronco-de-cone -->
![Tronco de cone reto com raio maior R, raio menor r, altura h e geratriz g identificados](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cones/fig-08-elementos-do-tronco-de-cone.png)
<!-- tikz:fim fig-08-elementos-do-tronco-de-cone -->

$$g^2=h^2+(R-r)^2$$

<!-- tikz:inicio fig-09-triangulo-gerador-do-tronco -->
![Secção lateral do tronco isolando triângulo retângulo de catetos h e R menos r e hipotenusa g](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cones/fig-09-triangulo-gerador-do-tronco.png)
<!-- tikz:fim fig-09-triangulo-gerador-do-tronco -->

Suas medidas de superfície e capacidade são calculadas por

$$A_L=\pi g(R+r)$$

$$V=\frac{\pi h}{3}(R^2+Rr+r^2)$$

O termo $$Rr$$ preserva no cálculo a relação entre o cone completo e a parte retirada.

Se o problema fornecer o cone original e o cone retirado, a semelhança entre suas secções permite reconstruir medidas correspondentes antes de aplicar essas expressões.

<!-- tikz:inicio fig-10-tronco-como-cone-recortado -->
![Cone completo cortado por plano paralelo à base com o pequeno cone retirado e o tronco restante](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cones/fig-10-tronco-como-cone-recortado.png)
<!-- tikz:fim fig-10-tronco-como-cone-recortado -->

### 6.2 Balde sem tampa

**Tronco cônico**

Um balde possui $$R=5\,\mathrm{dm}$$, $$r=2\,\mathrm{dm}$$ e $$h=4\,\mathrm{dm}$$.

**Resolução:**

- **Passo 1:** Calcular a geratriz.

$$g^2=4^2+(5-2)^2$$

$$g=5\,\mathrm{dm}$$

- **Passo 2:** Calcular a área lateral.

$$A_L=\pi\cdot5\cdot(5+2)$$

$$A_L=35\pi\,\mathrm{dm^2}$$

- **Passo 3:** Calcular o volume.

$$V=\frac{4\pi}{3}(25+10+4)$$

$$V=52\pi\,\mathrm{dm^3}$$

**Resposta:** a área lateral é $$35\pi\,\mathrm{dm^2}$$ e o volume, $$52\pi\,\mathrm{dm^3}$$.

> 🔢 **Padrão:**  
> No tronco, a diferença $$R-r$$ ocupa o lugar do raio no triângulo retângulo associado à geratriz.
