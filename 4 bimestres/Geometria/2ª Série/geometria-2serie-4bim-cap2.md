# Capítulo 2 — Sólidos semelhantes

> Uma maquete na escala 1:50 de um prédio de 24.000 m³ tem volume de apenas 192 litros. Por que a redução do volume não é 50 vezes, mas 125.000 vezes?

---

## 1. Sólidos semelhantes: razão de semelhança

Uma maquete preserva a forma do prédio, embora nenhuma de suas medidas lineares permaneça com o tamanho real.

### 1.1 Forma e proporção

**Sólidos semelhantes** possuem a mesma forma e medidas correspondentes proporcionais. Um pode ser obtido do outro por ampliação ou redução uniforme, possivelmente acompanhada de deslocamento.

A razão de semelhança $$k$$ multiplica toda medida linear:

- aresta;
- raio;
- altura;
- geratriz;
- diagonal.

| Valor de $$k$$ | Efeito |
|---|---|
| $$k>1$$ | ampliação |
| $$0<k<1$$ | redução |
| $$k=1$$ | congruência |

Assim como na semelhança de triângulos, ângulos correspondentes permanecem congruentes e comprimentos correspondentes guardam a mesma razão.

### 1.2 Escala arquitetônica

Numa escala $$1:n$$, a maquete usa $$k=1/n$$.

**Altura de uma maquete**

Um prédio de $$30\,\mathrm{m}$$ é representado na escala 1:50. Determine a altura da maquete.

**Resolução:**

- **Passo 1:** Identificar a razão linear.

$$k=\frac{1}{50}$$

- **Passo 2:** Multiplicar a altura real por $$k$$.

$$h'=30\cdot\frac{1}{50}$$

$$h'=0{,}6\,\mathrm{m}$$

- **Passo 3:** Converter para centímetros.

$$0{,}6\,\mathrm{m}=60\,\mathrm{cm}$$

**Resposta:** a maquete terá $$60\,\mathrm{cm}$$ de altura; raios, arestas e demais medidas lineares também serão divididos por 50.

> ⚠️ **Atenção:**  
> A escala 1:50 significa dividir comprimentos por 50, não subtrair 50 unidades.

---

## 2. Medidas lineares, áreas e volumes

Ampliar uma caixa afeta uma direção no comprimento, duas na superfície e três no espaço ocupado.

### 2.1 Justificativa dimensional

Se toda medida linear é multiplicada por $$k$$, uma área, produto de duas medidas, recebe dois fatores; um volume, produto de três, recebe três:

$$\frac{L'}{L}=k$$

$$\frac{A'}{A}=k^2$$

$$\frac{V'}{V}=k^3$$

Essa regra vale para prismas, pirâmides, cilindros, cones e esferas. Num cubo com aresta triplicada, a área cresce 9 vezes e o volume, 27; numa esfera de raio dobrado, os fatores são 4 e 8.

Constantes próprias das fórmulas não alteram a comparação. Por exemplo, o fator $$4\pi$$ aparece nas duas áreas esféricas e se cancela na razão; restam apenas os quadrados dos raios. O mesmo ocorre com $$4\pi/3$$ nos volumes.

### 2.2 Verificação numérica

**Cubo ampliado**

Um cubo de aresta $$2\,\mathrm{cm}$$ é ampliado com $$k=3$$.

**Resolução:**

- **Passo 1:** Calcular a nova aresta.

$$a'=3\cdot2$$

$$a'=6\,\mathrm{cm}$$

- **Passo 2:** Comparar as áreas totais.

$$A=6\cdot2^2$$

$$A=24\,\mathrm{cm^2}$$

$$A'=6\cdot6^2$$

$$A'=216\,\mathrm{cm^2}$$

$$\frac{216}{24}=9$$

- **Passo 3:** Comparar os volumes.

$$V=2^3$$

$$V=8\,\mathrm{cm^3}$$

$$V'=6^3$$

$$V'=216\,\mathrm{cm^3}$$

$$\frac{216}{8}=27$$

**Resposta:** a aresta triplica, a área é multiplicada por $$3^2=9$$ e o volume por $$3^3=27$$.

> 🔢 **Padrão:**  
> Semelhança segue a sequência dimensional $$k\rightarrow k^2\rightarrow k^3$$.

---

## 3. Aplicações de sólidos semelhantes

Uma maquete completa exige escalas diferentes para altura, fachada, volume de concreto e capacidade interna.

### 3.1 Escala em três dimensões

Na escala 1:50:

$$k=\frac{1}{50}$$

$$k^2=\frac{1}{2500}$$

$$k^3=\frac{1}{125\,000}$$

Tinta e revestimento acompanham áreas; massa de material, capacidade e custo de concreto acompanham volumes, quando composição e preço unitário permanecem iguais.

A unidade também precisa acompanhar a dimensão: comprimentos permanecem em metros, fachadas em metros quadrados e espaços internos em metros cúbicos. Essa leitura impede aplicar a razão linear a uma grandeza tridimensional.

### 3.2 Maquete completa

**Modelo de um edifício**

Um prédio tem altura de $$30\,\mathrm{m}$$, fachada de $$800\,\mathrm{m^2}$$ e volume de $$24\,000\,\mathrm{m^3}$$.

**Resolução:**

- **Passo 1:** Reduzir a altura por $$k$$.

$$h'=\frac{30}{50}$$

$$h'=0{,}6\,\mathrm{m}$$

- **Passo 2:** Reduzir a fachada por $$k^2$$.

$$A'=\frac{800}{2500}$$

$$A'=0{,}32\,\mathrm{m^2}$$

- **Passo 3:** Reduzir o volume por $$k^3$$.

$$V'=\frac{24\,000}{125\,000}$$

$$V'=0{,}192\,\mathrm{m^3}$$

- **Passo 4:** Converter a capacidade.

$$0{,}192\,\mathrm{m^3}=192\,\mathrm{L}$$

**Resposta:** a maquete tem $$0{,}6\,\mathrm{m}$$ de altura, $$0{,}32\,\mathrm{m^2}$$ de fachada e $$192\,\mathrm{L}$$ de volume.

No **Programa de Erlangen** (1872), **Felix Klein (1849–1925)** caracterizou geometrias pelas propriedades preservadas por transformações. Na semelhança, a forma é invariante, mas o tamanho não.

> ⚠️ **Atenção:**  
> Aplicar apenas $$k$$ ao volume da maquete produziria um resultado dimensionalmente incorreto.
