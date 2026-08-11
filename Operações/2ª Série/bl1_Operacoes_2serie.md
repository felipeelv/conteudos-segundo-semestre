# Operações — 2ª Série · Bloco 1

> **3º Bimestre — Sistemas lineares e polinômios** · Bloco 1 (05/08–25/08)

**Capítulos deste bloco**

1. **Conceito e classificação de sistemas lineares** (3 aulas)
2. **Métodos de resolução: substituição, adição e escalonamento** (4 aulas)
3. **Determinantes, Cramer e discussão de sistemas** (5 aulas)

---

# BL1_Capítulo 1 — Conceito e classificação de sistemas lineares

> Como classificar um sistema pela quantidade de soluções?

---

## 1. Equações e sistemas lineares

### 1.1 Estrutura linear

Uma **equação linear** em $$n$$ incógnitas tem a forma

$$a_1x_1+a_2x_2+\timess+a_nx_n=b$$

onde $$a_i$$ são coeficientes reais, $$x_i$$ são incógnitas e $$b$$ é o termo independente. As incógnitas aparecem apenas na primeira potência e não são multiplicadas entre si.

Um **sistema linear** $$m\times n$$ reúne $$m$$ equações e $$n$$ incógnitas que devem ser satisfeitas simultaneamente. Sua forma matricial é

$$AX=B$$

onde $$A$$ é a matriz dos coeficientes, $$X$$ é a coluna das incógnitas e $$B$$ é a coluna dos termos independentes.

### 1.2 Tradução de uma situação

**Produção de dois itens**

Uma fábrica produz itens $$x$$ e $$y$$. O total é 50 e o item $$x$$ usa duas unidades de matéria-prima, contra uma de $$y$$, totalizando 70.

**Resolução:**

- **Passo 1:** Traduzir a quantidade total.

$$x+y=50$$

- **Passo 2:** Traduzir o consumo.

$$2x+y=70$$

- **Passo 3:** Reunir as condições.

$$\begin{cases}x+y=50\\2x+y=70\end{cases}$$

**Resposta:** A situação produz um sistema $$2\times2$$.

> 🔢 **Padrão:**  
> Incógnita ausente em uma equação ocupa sua coluna com coeficiente zero.

---

## 2. Solução e sistemas equivalentes

### 2.1 Solução ordenada

A **solução** de um sistema com $$n$$ incógnitas é a n-upla ordenada que satisfaz simultaneamente as $$m$$ equações. A ordem dos valores acompanha a ordem das incógnitas.

**Sistemas equivalentes** possuem exatamente o mesmo conjunto solução. Três transformações preservam essa equivalência:

- trocar duas equações de posição;
- multiplicar uma equação inteira por constante não nula;
- somar a uma equação um múltiplo de outra.

### 2.2 Verificação da solução

**Verificação de um terno**

Verifique $$(1,2,3)$$ em

$$\begin{cases}x+y+z=6\\2x-y+z=3\\x+2y-z=2\end{cases}$$

**Resolução:**

- **Passo 1:** Testar a primeira equação.

$$1+2+3=6$$

- **Passo 2:** Testar a segunda equação.

$$2\times1-2+3=3$$

- **Passo 3:** Testar a terceira equação.

$$1+2\times2-3=2$$

**Resposta:** Como as três igualdades são verdadeiras, $$(1,2,3)$$ é solução.

> ⚠️ **Atenção:**  
> Satisfazer apenas parte das equações não torna uma n-upla solução do sistema.

---

## 3. Classificação de sistemas

### 3.1 As três classes

A classificação usa três siglas:

| Classe | Significado | Quantidade de soluções |
|---|---|---:|
| SPD | possível e determinado | uma |
| SPI | possível e indeterminado | infinitas |
| SI | impossível | nenhuma |

Em um sistema quadrado, $$\det A\neq0$$ garante SPD. Quando $$\det A=0$$, o determinante sozinho apenas mostra que não há solução única; distinguir SPI de SI exige comparar as equações ou escalonar o sistema.

### 3.2 Critério e sistemas homogêneos

**Classificação imediata**

Classifique

$$\begin{cases}2x+3y=8\\x-y=-1\end{cases}$$

**Resolução:**

- **Passo 1:** Registrar a matriz dos coeficientes.

$$A=\begin{pmatrix}2&3\\1&-1\end{pmatrix}$$

- **Passo 2:** Calcular o determinante.

$$\det A=2\times(-1)-3\times1$$

$$\det A=-5$$

- **Passo 3:** Aplicar o critério suficiente: $$\det A\neq0$$.

**Resposta:** O sistema é SPD.

Um sistema **homogêneo**, com $$B=0$$, sempre tem a solução trivial. Se for quadrado e $$\det A=0$$, também possui soluções não triviais.

**Eugène Rouché** (1832–1910) publicou em 1875 a base da classificação geral por postos, completada por Alfredo Capelli em 1892.

> ⚠️ **Atenção:**  
> Em sistemas gerais, $$\det A=0$$ não autoriza concluir SPI sem análise adicional.

---

# BL1_Capítulo 2 — Métodos de resolução: substituição, adição e escalonamento

> Como escolher e aplicar substituição, adição ou escalonamento?

---

## 1. Método da substituição

### 1.1 Fluxo do método

O **método da substituição** segue quatro ações:

- isolar uma incógnita;
- substituir a expressão na outra equação;
- resolver a equação resultante;
- voltar e calcular a variável restante.

### 1.2 Aplicação e verificação

**Sistema com variável de coeficiente 1**

Resolva

$$\begin{cases}2x+3y=8\\x-y=-1\end{cases}$$

**Resolução:**

- **Passo 1:** Isolar $$x$$ na segunda equação.

$$x=y-1$$

- **Passo 2:** Substituir na primeira.

$$2(y-1)+3y=8$$

$$2y-2+3y=8$$

$$5y=10$$

$$y=2$$

- **Passo 3:** Voltar à expressão isolada.

$$x=2-1$$

$$x=1$$

- **Passo 4:** Verificar na primeira equação original.

$$2\times1+3\times2=8$$

**Resposta:** A solução é $$(1,2)$$.

> ⚠️ **Atenção:**  
> A verificação final deve usar as equações originais, não apenas as transformadas.

---

## 2. Método da adição

### 2.1 Eliminação organizada

No **método da adição**, multiplicam-se equações inteiras por constantes para obter coeficientes opostos. Em seguida, somam-se os membros correspondentes.

### 2.2 Eliminação aplicada

**Eliminação de uma variável**

Resolva

$$\begin{cases}3x+2y=12\\2x-3y=-5\end{cases}$$

**Resolução:**

- **Passo 1:** Multiplicar a primeira equação por 3.

$$9x+6y=36$$

- **Passo 2:** Multiplicar a segunda por 2.

$$4x-6y=-10$$

- **Passo 3:** Somar as equações.

$$13x=26$$

$$x=2$$

- **Passo 4:** Substituir na primeira equação original.

$$3\times2+2y=12$$

$$2y=6$$

$$y=3$$

**Resposta:** A solução é $$(2,3)$$.

Escalonar é somar a uma equação um múltiplo de outra.

> ⚠️ **Atenção:**  
> Ao multiplicar uma equação, multiplique todos os termos, inclusive o membro direito.

---

## 3. Escalonamento: conceito

### 3.1 Operações e forma triangular

**Escalonar** é aplicar operações elementares até obter uma forma triangular. As operações permitidas são:

- trocar linhas;
- multiplicar uma linha por constante não nula;
- somar a uma linha um múltiplo de outra.

Na forma escalonada, cada linha começa depois da anterior; os primeiros coeficientes não nulos são os **pivôs**.

### 3.2 Aplicação e forma reduzida

**Primeira etapa de escalonamento**

Considere

$$\begin{cases}x+y=5\\2x-y=1\end{cases}$$

**Resolução:**

- **Passo 1:** Subtrair duas vezes a primeira equação da segunda.

$$-3y=-9$$

- **Passo 2:** Escrever o sistema triangular equivalente.

$$\begin{cases}x+y=5\\-3y=-9\end{cases}$$

**Resposta:** O sistema foi escalonado e a última equação já fornece $$y$$ diretamente.

**Wilhelm Jordan** (1842–1899) estendeu a eliminação de Gauss no *Handbuch der Vermessungskunde* (1873–1888). Na forma reduzida de Gauss-Jordan, também se anulam os coeficientes acima dos pivôs.

> 🔢 **Padrão:**  
> Cada pivô organiza a eliminação dos coeficientes abaixo dele.

---

## 4. Escalonamento: aplicação

### 4.1 Resolução completa

**Sistema de três incógnitas**

Resolva

$$\begin{cases}x+y+z=6\\2x-y+z=3\\x+2y-z=2\end{cases}$$

**Resolução:**

- **Passo 1:** Eliminar $$x$$ da segunda equação.

$$-3y-z=-9$$

- **Passo 2:** Eliminar $$x$$ da terceira equação.

$$y-2z=-4$$

- **Passo 3:** Eliminar $$y$$ da terceira equação transformada.

$$3(y-2z)+(-3y-z)=3\times(-4)+(-9)$$

$$-7z=-21$$

$$z=3$$

- **Passo 4:** Fazer a substituição reversa na segunda equação.

$$-3y-3=-9$$

$$-3y=-6$$

$$y=2$$

- **Passo 5:** Voltar à primeira equação.

$$x+2+3=6$$

$$x=1$$

**Resposta:** A solução é $$(1,2,3)$$.

### 4.2 Organização e classificação

O alinhamento das incógnitas em colunas evita misturar coeficientes. Na forma escalonada, uma linha $$0=0$$ indica informação redundante; uma linha $$0=k$$, com $$k\neq0$$, indica contradição.

> ⚠️ **Atenção:**  
> Substituição reversa começa na última equação não nula do sistema escalonado.

---

# BL1_Capítulo 3 — Determinantes, Cramer e discussão de sistemas

> Como resolver e classificar sistemas usando determinantes?

---

## 1. Determinantes aplicados a sistemas

### 1.1 Matrizes associadas

Para $$AX=B$$, a matriz $$A_i$$ é obtida substituindo em $$A$$ apenas a coluna da incógnita $$x_i$$ pela coluna $$B$$.

Se $$\det A\neq0$$, o sistema é SPD. Se $$\det A=0$$, não há solução única e será necessária outra análise.

### 1.2 Construção das matrizes substituídas

**Matrizes de um sistema**

Considere

$$\begin{cases}2x+3y=8\\x-y=-1\end{cases}$$

**Resolução:**

- **Passo 1:** Escrever a matriz dos coeficientes.

$$A=\begin{pmatrix}2&3\\1&-1\end{pmatrix}$$

- **Passo 2:** Substituir a coluna de $$x$$.

$$A_x=\begin{pmatrix}8&3\\-1&-1\end{pmatrix}$$

- **Passo 3:** Substituir a coluna de $$y$$.

$$A_y=\begin{pmatrix}2&8\\1&-1\end{pmatrix}$$

- **Passo 4:** Calcular o determinante principal.

$$\det A=2\times(-1)-3\times1$$

$$\det A=-5$$

**Resposta:** Como $$\det A\neq0$$, o sistema é SPD e suas matrizes associadas estão prontas para Cramer.

> ⚠️ **Atenção:**  
> Em $$A_i$$, somente a coluna da incógnita correspondente é substituída.

---

## 2. Regra de Cramer

### 2.1 Fórmula e validade

A **Regra de Cramer** estabelece, para um sistema quadrado com $$\det A\neq0$$,

$$x_i=\frac{\det A_i}{\det A}$$

onde $$A_i$$ substitui a coluna $$i$$ de $$A$$ pela coluna dos termos independentes.

A condição é indispensável: com $$\det A=0$$, a divisão não existe e o sistema não possui solução única.

### 2.2 Aplicação da fórmula

**Valores obtidos pelos determinantes**

Suponha $$\det A=-5$$, $$\det A_x=-5$$ e $$\det A_y=-10$$.

**Resolução:**

- **Passo 1:** Calcular $$x$$.

$$x=\frac{-5}{-5}$$

$$x=1$$

- **Passo 2:** Calcular $$y$$.

$$y=\frac{-10}{-5}$$

$$y=2$$

**Resposta:** A solução é $$(1,2)$$.

**Gabriel Cramer** (1704–1752) publicou a regra em 1750, no apêndice de sua obra sobre curvas algébricas. O método é elegante para sistemas pequenos, mas exige muitos determinantes em ordens elevadas.

> ⚠️ **Atenção:**  
> Cramer é válida somente quando $$\det A\neq0$$.

---

## 3. Cálculo de sistemas por Cramer

### 3.1 Sistema de ordem 2

**Duas incógnitas por Cramer**

Resolva

$$\begin{cases}2x+3y=8\\x-y=-1\end{cases}$$

**Resolução:**

- **Passo 1:** Calcular o determinante principal.

$$\det A=2\times(-1)-3\times1$$

$$\det A=-5$$

- **Passo 2:** Calcular o determinante de $$A_x$$.

$$\det A_x=8\times(-1)-3\times(-1)$$

$$\det A_x=-5$$

- **Passo 3:** Calcular o determinante de $$A_y$$.

$$\det A_y=2\times(-1)-8\times1$$

$$\det A_y=-10$$

- **Passo 4:** Aplicar Cramer.

$$x=\frac{-5}{-5}$$

$$x=1$$

$$y=\frac{-10}{-5}$$

$$y=2$$

- **Passo 5:** Verificar nas equações originais.

$$2\times1+3\times2=8$$

$$1-2=-1$$

**Resposta:** A solução é $$(1,2)$$ e satisfaz as duas equações.

### 3.2 Sistema de ordem 3

**Três incógnitas por Cramer**

Resolva

$$\begin{cases}x+y+z=6\\x-y+z=2\\x+y-z=0\end{cases}$$

**Resolução:**

- **Passo 1:** Calcular o determinante principal por expansão.

$$\det A=1(1-1)-1(-1-1)+1(1+1)$$

$$\det A=4$$

- **Passo 2:** Substituir a primeira coluna e calcular.

$$A_x=\begin{pmatrix}6&1&1\\2&-1&1\\0&1&-1\end{pmatrix}$$

$$\det A_x=6(1-1)-1(-2-0)+1(2-0)$$

$$\det A_x=4$$

- **Passo 3:** Substituir a segunda coluna e calcular.

$$A_y=\begin{pmatrix}1&6&1\\1&2&1\\1&0&-1\end{pmatrix}$$

$$\det A_y=1(-2-0)-6(-1-1)+1(0-2)$$

$$\det A_y=8$$

- **Passo 4:** Substituir a terceira coluna e calcular.

$$A_z=\begin{pmatrix}1&1&6\\1&-1&2\\1&1&0\end{pmatrix}$$

$$\det A_z=1(0-2)-1(0-2)+6(1+1)$$

$$\det A_z=12$$

- **Passo 5:** Calcular as incógnitas.

$$x=\frac{4}{4}$$

$$x=1$$

$$y=\frac{8}{4}$$

$$y=2$$

$$z=\frac{12}{4}$$

$$z=3$$

**Resposta:** A solução é $$(1,2,3)$$.

Para ordens maiores, o escalonamento costuma exigir menos operações.

> 🔢 **Padrão:**  
> Um sistema de ordem $$n$$ exige $$n+1$$ determinantes na aplicação direta de Cramer.

---

## 4. Discussão de sistemas

### 4.1 Critérios seguros

Para sistemas quadrados:

- $$\det A\neq0$$ garante SPD;
- $$\det A=0$$ e algum $$\det A_i\neq0$$ garantem SI;
- $$\det A=0$$ e todos os $$\det A_i=0$$ não bastam, em geral, para concluir SPI.

No último caso, o escalonamento ou a comparação de postos decide corretamente, sobretudo em ordem 3 ou maior.

### 4.2 Discussão com parâmetro

**Sistema com parâmetro**

Discuta

$$\begin{cases}mx+y=1\\x+my=1\end{cases}$$

**Resolução:**

- **Passo 1:** Calcular o determinante principal.

$$\det A=m\times m-1\times1$$

$$\det A=m^2-1$$

- **Passo 2:** Identificar os valores que garantem SPD: $$m^2-1\neq0$$; $$m\neq-1\ \text{e}\ m\neq1$$.

- **Passo 3:** Analisar $$m=1$$.

$$\begin{cases}x+y=1\\x+y=1\end{cases}$$

As equações coincidem, portanto há infinitas soluções.

- **Passo 4:** Analisar $$m=-1$$.

$$\begin{cases}-x+y=1\\x-y=1\end{cases}$$

Multiplicar a segunda equação por $$-1$$ produz

$$-x+y=-1$$

que contradiz a primeira.

**Resposta:** O sistema é SPD para $$m\neq-1$$ e $$m\neq1$$, SPI para $$m=1$$ e SI para $$m=-1$$.

> ⚠️ **Atenção:**  
> Determinantes substituídos todos nulos não substituem a análise de posto em sistemas gerais.

---

## 5. Teorema de Rouché–Capelli

### 5.1 Postos das matrizes

O **posto** é o número de linhas não nulas após o escalonamento. O Teorema de Rouché–Capelli afirma:

$$\mathrm{posto}(A)=\mathrm{posto}([A|B])$$

se, e somente se, o sistema é compatível. Sendo $$n$$ o número de incógnitas:

| Condição | Classe |
|---|---|
| $$\mathrm{posto}(A)=\mathrm{posto}([A|B])=n$$ | SPD |
| $$\mathrm{posto}(A)=\mathrm{posto}([A|B])<n$$ | SPI |
| $$\mathrm{posto}(A)<\mathrm{posto}([A|B])$$ | SI |

### 5.2 Classificação pelo escalonamento

**Classificação por posto**

Classifique

$$\begin{cases}x+y+z=3\\2x+2y+2z=6\end{cases}$$

**Resolução:**

- **Passo 1:** Escrever a matriz ampliada.

$$[A|B]=\begin{pmatrix}1&1&1&3\\2&2&2&6\end{pmatrix}$$

- **Passo 2:** Subtrair duas vezes a primeira linha da segunda: $$\begin{pmatrix}1&1&1&3\\0&0&0&0\end{pmatrix}$$.

- **Passo 3:** Comparar os postos com o número de incógnitas.

$$\mathrm{posto}(A)=1$$

$$\mathrm{posto}([A|B])=1$$

$$n=3$$

**Resposta:** O sistema é SPI, pois os postos são iguais e menores que o número de incógnitas.

As três ações formam um fluxo único:

- classificar pela comparação dos postos;
- resolver por um método equivalente adequado;
- discutir parâmetros repetindo a classificação nos casos críticos.

> 🔢 **Padrão:**  
> Igualdade dos postos garante compatibilidade; compará-los com $$n$$ decide entre SPD e SPI.
