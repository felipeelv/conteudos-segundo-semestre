# Capítulo 1 — Relações métricas no triângulo retângulo

> Por que o esquadro tradicional do pedreiro — uma corda com 12 nós igualmente espaçados dobrada em 3 + 4 + 5 — garante um ângulo reto perfeito, sem esquadro de metal e sem medidor de ângulo?

---

## 1. Teorema de Pitágoras: enunciado e demonstração

Uma viga diagonal divide uma moldura retangular em triângulos nos quais as áreas dos quadrados construídos sobre os lados se relacionam.

### 1.1 Enunciado e semelhança

Num triângulo retângulo, $$a$$ é a hipotenusa, lado oposto ao ângulo reto e maior medida; $$b$$ e $$c$$ são os catetos. O teorema afirma:

$$a^2=b^2+c^2$$

Dele seguem as formas para uma medida desconhecida:

$$a=\sqrt{b^2+c^2}$$

$$b=\sqrt{a^2-c^2}$$

A altura relativa à hipotenusa cria dois triângulos semelhantes ao original pelo caso AA. Se as projeções dos catetos são $$m$$ e $$n$$, a semelhança produz $$b^2=am$$ e $$c^2=an$$. Somando:

$$b^2+c^2=a(m+n)$$

Como $$m+n=a$$, obtém-se $$b^2+c^2=a^2$$.

### 1.2 O trapézio de Garfield

**James A. Garfield (1831–1881)** publicou em 1876 uma demonstração por áreas. Dois triângulos retângulos congruentes formam um trapézio com um triângulo central de área $$a^2/2$$.

**Área calculada por dois caminhos**

As bases do trapézio medem $$b$$ e $$c$$, e sua altura mede $$b+c$$.

**Resolução:**

- **Passo 1:** Calcular a área pela fórmula do trapézio.

$$A=\frac{(b+c)(b+c)}{2}$$

- **Passo 2:** Somar as três áreas internas.

$$A=\frac{bc}{2}+\frac{bc}{2}+\frac{a^2}{2}$$

- **Passo 3:** Igualar e simplificar.

$$(b+c)^2=2bc+a^2$$

$$b^2+c^2=a^2$$

**Resposta:** as duas decomposições da mesma área demonstram o Teorema de Pitágoras.

> 🔢 **Padrão:**  
> Demonstrações diferentes podem revelar a mesma relação por invariantes distintos: semelhança ou área.

---

## 2. Aplicações, ternos pitagóricos e recíproca

Uma corda marcada em 3, 4 e 5 partes fecha um triângulo cuja maior abertura é rigorosamente reta.

### 2.1 Ternos e aplicações

**Terno pitagórico** é um trio de inteiros positivos que satisfaz $$a^2=b^2+c^2$$. Casos frequentes são:

| Catetos | Hipotenusa |
|---|---:|
| 3 e 4 | 5 |
| 5 e 12 | 13 |
| 8 e 15 | 17 |
| 7 e 24 | 25 |

Se todas as medidas forem multiplicadas pelo mesmo fator, surge outro terno. A construção civil usa 3-4-5; telas 16:9, quadras e escadas produzem diagonais pelo mesmo teorema.

**Diagonal de uma quadra**

Uma quadra retangular mede $$28\,\mathrm{m}$$ por $$15\,\mathrm{m}$$.

**Resolução:**

- **Passo 1:** Aplicar Pitágoras.

$$d^2=28^2+15^2$$

$$d^2=1009\,\mathrm{m^2}$$

- **Passo 2:** Extrair a raiz positiva.

$$d=\sqrt{1009}\,\mathrm{m}$$

$$d\approx31{,}76\,\mathrm{m}$$

**Resposta:** a travessia diagonal mede aproximadamente $$31{,}76\,\mathrm{m}$$.

### 2.2 A recíproca

A **recíproca** afirma: se o quadrado do maior lado iguala a soma dos quadrados dos outros, o triângulo é retângulo. Constrói-se um triângulo retângulo com os dois lados menores; Pitágoras dá a mesma terceira medida. Pelo caso LLL, ele é congruente ao triângulo original, que também possui ângulo reto.

Para 3, 4 e 6:

$$6^2=36$$

$$3^2+4^2=25$$

Como $$36\neq25$$, esse triângulo não é retângulo.

> ⚠️ **Atenção:**  
> Na recíproca, o lado testado isoladamente deve ser sempre o maior.

---

## 3. Relações métricas: projeções dos catetos sobre a hipotenusa

Uma escora perpendicular à hipotenusa separa o triângulo retângulo em três triângulos com a mesma forma.

### 3.1 Semelhança e quatro relações

Considere hipotenusa $$a$$, catetos $$b$$ e $$c$$, altura relativa $$h$$ e projeções $$m$$ e $$n$$, com $$m+n=a$$. Os dois triângulos menores são semelhantes ao original por AA.

Por exemplo, a proporção $$a/b=b/m$$ leva a $$b^2=am$$. Comparações análogas entre lados correspondentes produzem as outras relações; assim, nenhuma delas é uma regra isolada.

As proporções entre lados correspondentes geram:

$$b^2=am$$

$$c^2=an$$

$$h^2=mn$$

$$bc=ah$$

As três primeiras expressam médias geométricas:

$$b=\sqrt{am}$$

$$c=\sqrt{an}$$

$$h=\sqrt{mn}$$

Somar as duas relações dos catetos recupera Pitágoras, pois $$a(m+n)=a^2$$.

### 3.2 Um triângulo completo

**Projeções de uma cobertura**

A hipotenusa mede $$25\,\mathrm{cm}$$ e as projeções medem $$m=9\,\mathrm{cm}$$ e $$n=16\,\mathrm{cm}$$.

**Resolução:**

- **Passo 1:** Calcular o cateto ligado a $$m$$.

$$b^2=25\cdot9$$

$$b=15\,\mathrm{cm}$$

- **Passo 2:** Calcular o cateto ligado a $$n$$.

$$c^2=25\cdot16$$

$$c=20\,\mathrm{cm}$$

- **Passo 3:** Calcular a altura.

$$h^2=9\cdot16$$

$$h=12\,\mathrm{cm}$$

- **Passo 4:** Conferir a soma das projeções.

$$9+16=25\,\mathrm{cm}$$

**Resposta:** os catetos medem $$15\,\mathrm{cm}$$ e $$20\,\mathrm{cm}$$, e a altura mede $$12\,\mathrm{cm}$$.

> 🔢 **Padrão:**  
> Cada cateto é associado à projeção que ele produz sobre a hipotenusa.

---

## 4. Relações métricas: aplicações práticas

Num telhado, a altura útil depende dos dois caibros inclinados e da largura total apoiada.

### 4.1 Escolher pelos dados

Cada conjunto de medidas aponta para uma relação:

| Dados conhecidos | Relação adequada |
|---|---|
| $$a$$ e $$m$$ | $$b^2=am$$ |
| $$m$$ e $$n$$ | $$h^2=mn$$ |
| $$a$$, $$b$$ e $$c$$ | $$bc=ah$$ |

O erro mais frequente é cruzar $$b$$ com $$n$$. No desenho, a projeção correta fica sob o cateto correspondente.

### 4.2 Altura estrutural

**Caibros de um telhado**

Dois caibros perpendiculares medem $$6\,\mathrm{m}$$ e $$8\,\mathrm{m}$$; a viga oposta mede $$10\,\mathrm{m}$$. Determine a altura até essa viga e as projeções.

**Resolução:**

- **Passo 1:** Usar $$bc=ah$$.

$$6\cdot8=10h$$

$$h=4{,}8\,\mathrm{m}$$

- **Passo 2:** Associar o cateto de $$6\,\mathrm{m}$$ à sua projeção.

$$6^2=10m$$

$$m=3{,}6\,\mathrm{m}$$

- **Passo 3:** Calcular a outra projeção.

$$8^2=10n$$

$$n=6{,}4\,\mathrm{m}$$

**Resposta:** a altura mede $$4{,}8\,\mathrm{m}$$, e as projeções medem $$3{,}6\,\mathrm{m}$$ e $$6{,}4\,\mathrm{m}$$.

Para uma ceviana $$d$$ num triângulo qualquer, o **Teorema de Stewart**, publicado por Matthew Stewart em 1746, apresenta a generalização:

$$b^2m+c^2n-a(d^2+mn)=0$$

Aqui, ele apenas mostra que relações métricas também existem fora do caso retângulo.

> ⚠️ **Atenção:**  
> A altura relativa à hipotenusa é perpendicular a ela, enquanto a projeção está contida nela.
