# Operações — 9º Ano · Bloco 1

> **3º Bimestre — Equações do 2º grau e função quadrática (Parte 1)** · Bloco 1 (05/08–25/08)

**Capítulos deste bloco**

1. **Equações incompletas** (4 aulas)
2. **Fórmula de Bhaskara e relações entre raízes** (5 aulas)
3. **Fatoração algébrica** (3 aulas)

---

# BL1_Capítulo 1 — Equações incompletas

> Como resolver equações quadráticas incompletas?

---

## 1. Equações do tipo ax² = b

### 1.1 Retomada da forma geral

Uma equação do 2º grau tem a forma:

$$ax^2+bx+c=0$$

onde $$a$$, $$b$$ e $$c$$ são reais e $$a\neq0$$. Ela é **incompleta** quando $$b=0$$, $$c=0$$ ou ambos.

No tipo $$ax^2=b$$, dividimos por $$a$$ e extraímos a raiz com os dois sinais:

$$x^2=\frac{b}{a}$$

$$x=\pm\sqrt{\frac{b}{a}}$$

Essa escrita produz raízes reais quando $$\frac{b}{a}\geq0$$.

Para a área de $$144\,\mathrm{cm^2}$$:

$$l^2=144$$

$$l=\pm12$$

Como lado é uma medida positiva, temos $$l=12\,\mathrm{cm}$$.

### 1.2 Área e raiz

**Quadrado de área 50**

Um quadrado tem área de $$50\,\mathrm{cm^2}$$. Determine o lado.

**Resolução:**

- **Passo 1:** Modelar.

$$l^2=50$$

- **Passo 2:** Extrair as raízes.

$$l=\pm\sqrt{50}$$

$$l=\pm5\sqrt{2}$$

- **Passo 3:** Aplicar a restrição do contexto.

$$l=5\sqrt{2}$$

**Resposta:** o lado mede $$5\sqrt{2}\,\mathrm{cm}$$; a raiz negativa não representa comprimento.

> ⚠️ **Atenção:**  
> O sinal $$\pm$$ pertence à resolução algébrica; o contexto decide depois se alguma raiz deve ser descartada.

**Mahavira** (c. 800–c. 870) classificou equações quadráticas no *Ganita-sara-sangraha*.

---

## 2. Equações do tipo ax² + bx = 0

### 2.1 Fator comum e produto nulo

O tipo tem a estrutura:

$$ax^2+bx=0$$

Fatorando e anulando cada fator:

$$x(ax+b)=0$$

$$x=0$$

ou:

$$ax+b=0$$

$$x=-\frac{b}{a}$$

Dividir por $$x$$ é incorreto porque $$x$$ pode ser zero.

### 2.2 Duas raízes

**Fator comum preservado**

Resolva $$4x^2-12x=0$$.

**Resolução:**

- **Passo 1:** Fatorar.

$$4x(x-3)=0$$

- **Passo 2:** Anular o primeiro fator.

$$4x=0$$

$$x=0$$

- **Passo 3:** Anular o segundo fator.

$$x-3=0$$

$$x=3$$

**Resposta:** $$x=0$$ ou $$x=3$$.

> 🔢 **Padrão:**  
> No tipo $$ax^2+bx=0$$, zero é sempre uma das raízes.

---

## 3. Equações do tipo ax² + c = 0

### 3.1 Isolar e analisar

Para:

$$ax^2+c=0$$

temos:

$$x^2=-\frac{c}{a}$$

Se o lado direito for positivo, há duas raízes simétricas; se for zero, há uma raiz; se for negativo, não há raiz real. Isso ocorre porque o quadrado de todo número real é **não negativo**.

### 3.2 Caso sem raiz real

**Quadrado impossível nos reais**

Resolva $$2x^2+8=0$$ no conjunto dos reais.

**Resolução:**

- **Passo 1:** Isolar o termo quadrático.

$$2x^2=-8$$

- **Passo 2:** Dividir por 2.

$$x^2=-4$$

- **Passo 3:** Comparar com a propriedade dos quadrados reais: $$x^2\geq0$$.

**Resposta:** a equação não tem solução real.

No Ensino Médio, os números complexos ampliarão o conjunto em que esse tipo de raiz pode ser representado.

> ⚠️ **Atenção:**  
> “Sem solução real” é uma conclusão completa e não significa que a equação esteja mal formulada.

---

## 4. Decisão e fatoração

### 4.1 Fluxo de escolha

Três perguntas orientam a resolução:

- faltam $$b$$ e $$c$$? Divida por $$a$$ e obtenha zero;
- falta apenas $$b$$? Isole $$x^2$$ e use $$\pm$$;
- falta apenas $$c$$? Fatore $$x$$ e aplique o produto nulo.

Quando há diferença de quadrados, a fatoração oferece outro caminho econômico.

Os três tipos também podem ser lidos como produtos iguais a zero: fator comum, diferença de quadrados ou repetição do fator $$x$$.

### 4.2 Diferença de quadrados

**Equação resolvida por fatores**

Resolva $$x^2-9=0$$.

**Resolução:**

- **Passo 1:** Fatorar a diferença de quadrados.

$$(x+3)(x-3)=0$$

- **Passo 2:** Anular cada fator.

$$x+3=0$$

$$x=-3$$

$$x-3=0$$

$$x=3$$

**Resposta:** $$x=-3$$ ou $$x=3$$.

> 🔢 **Padrão:**  
> Casos incompletos têm métodos próprios mais curtos do que um procedimento geral.

---

# BL1_Capítulo 2 — Fórmula de Bhaskara e relações entre raízes

> Como resolver uma equação quadrática completa?

---

## 1. Dedução da fórmula

### 1.1 Completamento de quadrado

Partimos de $$ax^2+bx+c=0$$, onde $$a\neq0$$.

**Fórmula construída passo a passo**

**Resolução:**

- **Passo 1:** Dividir por $$a$$ e transpor o termo independente.

$$x^2+\frac{b}{a}x=-\frac{c}{a}$$

- **Passo 2:** Somar o quadrado necessário aos dois membros.

$$x^2+\frac{b}{a}x+\frac{b^2}{4a^2}=-\frac{c}{a}+\frac{b^2}{4a^2}$$

- **Passo 3:** Fatorar e reduzir o segundo membro.

$$\left(x+\frac{b}{2a}\right)^2=\frac{b^2-4ac}{4a^2}$$

- **Passo 4:** Multiplicar por $$4a^2$$.

$$(2ax+b)^2=b^2-4ac$$

- **Passo 5:** Extrair a raiz e isolar $$x$$.

$$2ax+b=\pm\sqrt{b^2-4ac}$$

$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

**Resposta:** definindo $$\Delta=b^2-4ac$$, obtemos $$x=\frac{-b\pm\sqrt{\Delta}}{2a}$$.

### 1.2 Cuidado com o módulo

Se a raiz do denominador for extraída separadamente, vale:

$$\sqrt{4a^2}=2|a|$$

e não $$2a$$ para todo real $$a$$. A passagem por $$(2ax+b)^2=\Delta$$ preserva os dois sinais e conduz corretamente à fórmula usual.

**Bhaskara II** (1114–c. 1185) difundiu a regra; “fórmula de Bhaskara” é uma denominação brasileira.

---

## 2. Discriminante

### 2.1 Três possibilidades

O **discriminante** é:

$$\Delta=b^2-4ac$$

onde $$a$$, $$b$$ e $$c$$ são os coeficientes. Seu sinal determina:

| Condição | Raízes reais |
|---|---:|
| $$\Delta>0$$ | duas distintas |
| $$\Delta=0$$ | uma dupla |
| $$\Delta<0$$ | nenhuma |

### 2.2 Atenção ao coeficiente negativo

**Quantidade de raízes prevista**

Analise $$x^2-5x+6=0$$.

**Resolução:**

- **Passo 1:** Identificar os coeficientes.

$$a=1$$

$$b=-5$$

$$c=6$$

- **Passo 2:** Calcular o discriminante.

$$\Delta=(-5)^2-4\times1\times6$$

$$\Delta=25-24$$

$$\Delta=1$$

**Resposta:** como $$\Delta>0$$, existem duas raízes reais distintas.

> ⚠️ **Atenção:**  
> O quadrado inclui o sinal: $$(-5)^2=25$$.

---

## 3. Equações completas

### 3.1 Fluxo de resolução

Quatro etapas evitam erros:

- escrever a equação na forma geral;
- identificar $$a$$, $$b$$ e $$c$$ com os sinais;
- calcular $$\Delta$$;
- aplicar a fórmula e simplificar cada raiz.

### 3.2 Aplicação completa

**Dimensões de um terreno**

Um terreno retangular tem $$600\,\mathrm{m^2}$$, e o comprimento excede a largura em $$10\,\mathrm{m}$$. Chamando a largura de $$x$$, temos $$x^2+10x-600=0$$.

**Resolução:**

- **Passo 1:** Identificar os coeficientes.

$$a=1$$

$$b=10$$

$$c=-600$$

- **Passo 2:** Calcular $$\Delta$$.

$$\Delta=10^2-4\times1\times(-600)$$

$$\Delta=100+2400$$

$$\Delta=2500$$

- **Passo 3:** Aplicar a fórmula.

$$x=\frac{-10\pm\sqrt{2500}}{2\times1}$$

$$x=\frac{-10\pm50}{2}$$

- **Passo 4:** Separar as raízes.

$$x_1=\frac{-10+50}{2}$$

$$x_1=20$$

$$x_2=\frac{-10-50}{2}$$

$$x_2=-30$$

- **Passo 5:** Verificar a raiz válida no contexto.

$$20\times30=600$$

$$30-20=10$$

**Resposta:** a largura é $$20\,\mathrm{m}$$ e o comprimento, $$30\,\mathrm{m}$$; a raiz $$-30$$ não representa uma medida.

> ⚠️ **Atenção:**  
> A fórmula começa com $$-b$$ e seu denominador completo é $$2a$$.

---

## 4. Soma das raízes

### 4.1 Dedução

Somando as duas expressões da fórmula:

$$x_1+x_2=\frac{-b+\sqrt{\Delta}}{2a}+\frac{-b-\sqrt{\Delta}}{2a}$$

$$x_1+x_2=\frac{-2b}{2a}$$

$$x_1+x_2=-\frac{b}{a}$$

Definimos $$S=x_1+x_2$$. Os radicais se cancelam e o sinal de $$b$$ aparece invertido.

### 4.2 Verificação estrutural

**Soma sem Bhaskara**

Determine a soma das raízes de $$2x^2-6x-8=0$$.

**Resolução:**

- **Passo 1:** Identificar $$a$$ e $$b$$.

$$a=2$$

$$b=-6$$

- **Passo 2:** Aplicar a relação.

$$S=-\frac{-6}{2}$$

$$S=3$$

**Resposta:** a soma das raízes é 3.

> 🔢 **Padrão:**  
> A soma das raízes é $$-\frac{b}{a}$$, com o sinal de $$b$$ invertido.

---

## 5. Produto e composição

### 5.1 Dedução do produto

Multiplicando as raízes conjugadas:

$$x_1x_2=\frac{(-b+\sqrt{\Delta})(-b-\sqrt{\Delta})}{4a^2}$$

$$x_1x_2=\frac{b^2-\Delta}{4a^2}$$

$$x_1x_2=\frac{4ac}{4a^2}$$

$$x_1x_2=\frac{c}{a}$$

Definimos $$P=x_1x_2$$. Com raízes conhecidas, uma equação mônica pode ser composta por:

$$x^2-Sx+P=0$$

### 5.2 Caminho inverso

**Equação de raízes 3 e 5**

**Resolução:**

- **Passo 1:** Calcular a soma.

$$S=3+5$$

$$S=8$$

- **Passo 2:** Calcular o produto.

$$P=3\times5$$

$$P=15$$

- **Passo 3:** Compor a equação.

$$x^2-8x+15=0$$

**Resposta:** uma equação com essas raízes é $$x^2-8x+15=0$$.

> ⚠️ **Atenção:**  
> Na composição, a soma entra com sinal trocado e o produto mantém seu sinal.

---

# BL1_Capítulo 3 — Fatoração algébrica

> Quando a fatoração resolve uma equação quadrática?

---

## 1. Fator comum e diferença de quadrados

### 1.1 Fator comum

O fator comum reúne o maior divisor compartilhado pelos coeficientes e a menor potência comum da variável:

$$6x^2+9x=3x(2x+3)$$

Essa escrita permite aplicar o produto nulo quando a expressão está igualada a zero.

### 1.2 Diferença de quadrados

A identidade é:

$$a^2-b^2=(a+b)(a-b)$$

Ela exige dois quadrados separados por subtração. Para números reais, lembre:

$$\sqrt{x^2}=|x|$$

Assim, por exemplo:

$$\sqrt{4a^2}=2|a|$$

**Diferença reconhecida**

Fatore $$x^2-16$$.

**Resolução:**

- **Passo 1:** Identificar os quadrados.

$$x^2=(x)^2$$

$$16=4^2$$

- **Passo 2:** Aplicar a identidade.

$$x^2-16=(x+4)(x-4)$$

**Resposta:** a forma fatorada é $$(x+4)(x-4)$$.

> ⚠️ **Atenção:**  
> A soma $$a^2+b^2$$ não se fatora dessa maneira sobre os números reais.

**Girolamo Cardano** (1501–1576) usou fatorações sistematicamente no *Ars Magna* (1545) para reduzir equações a casos resolvíveis.

---

## 2. Trinômios

### 2.1 Trinômio quadrado perfeito

As identidades fundamentais são:

$$(a+b)^2=a^2+2ab+b^2$$

$$(a-b)^2=a^2-2ab+b^2$$

Para reconhecer um **trinômio quadrado perfeito**, verificamos se o termo central é duas vezes o produto das bases dos quadrados extremos.

**Quadrado de uma soma**

Fatore $$x^2+6x+9$$.

**Resolução:**

- **Passo 1:** Identificar as bases algébricas dos quadrados extremos.

$$x^2=(x)^2$$

$$9=3^2$$

- **Passo 2:** Conferir o termo central algebricamente.

$$2\times x\times3=6x$$

- **Passo 3:** Escrever o quadrado.

$$x^2+6x+9=(x+3)^2$$

**Resposta:** a forma fatorada é $$(x+3)^2$$.

A raiz principal satisfaz $$\sqrt{x^2}=|x|$$; no reconhecimento da identidade, porém, usamos a base algébrica $$x$$ cujo quadrado é $$x^2$$.

### 2.2 Trinômio pelas raízes

Se a equação tem raízes reais $$x_1$$ e $$x_2$$, então:

$$ax^2+bx+c=a(x-x_1)(x-x_2)$$

onde $$a\neq0$$. O sinal das raízes aparece invertido dentro dos fatores.

**Trinômio pelas raízes**

Fatore $$x^2-5x+6$$.

**Resolução:**

- **Passo 1:** Calcular o discriminante.

$$\Delta=(-5)^2-4\times1\times6$$

$$\Delta=1$$

- **Passo 2:** Calcular as raízes.

$$x=\frac{5\pm\sqrt{1}}{2}$$

$$x_1=3$$

$$x_2=2$$

- **Passo 3:** Escrever a forma fatorada.

$$x^2-5x+6=(x-3)(x-2)$$

**Resposta:** a forma fatorada é $$(x-3)(x-2)$$.

> ⚠️ **Atenção:**  
> $$(a+b)^2$$ contém o termo $$2ab$$; não é igual a $$a^2+b^2$$.

---

## 3. Fatoração na resolução

### 3.1 Fatorar e anular

O princípio do produto nulo fornece:

$$(x-r_1)(x-r_2)=0$$

$$x=r_1\text{ ou }x=r_2$$

onde $$r_1$$ e $$r_2$$ são as raízes. Fatoração é preferível quando há fator comum, diferença de quadrados ou trinômio quadrado perfeito; sem padrão visível, a fórmula geral é mais segura.

### 3.2 Atalho conferido

**Raízes de uma diferença**

Resolva $$x^2-16=0$$.

**Resolução:**

- **Passo 1:** Fatorar.

$$(x+4)(x-4)=0$$

- **Passo 2:** Anular o primeiro fator.

$$x+4=0$$

$$x=-4$$

- **Passo 3:** Anular o segundo fator.

$$x-4=0$$

$$x=4$$

**Resposta:** $$x=-4$$ ou $$x=4$$.

> 🔢 **Padrão:**  
> A fatoração é um atalho quando a estrutura é reconhecível e também uma forma de verificar raízes obtidas por outro método.
