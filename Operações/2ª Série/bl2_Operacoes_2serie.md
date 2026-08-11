# Operações — 2ª Série · Bloco 2

> **3º Bimestre — Sistemas lineares e polinômios** · Bloco 2 (27/08–18/09)

**Capítulos deste bloco**

4. **Conceitos fundamentais de polinômios** (6 aulas)
5. **Operações com polinômios** (4 aulas)
6. **Teoremas do resto e de D'Alembert** (2 aulas)

---

# BL2_Capítulo 1 — Conceitos fundamentais de polinômios

> O que define um polinômio e quando um valor é sua raiz?

---

## 1. Polinômio e função polinomial

### 1.1 Definição formal

Um **polinômio** real na variável $$x$$ tem a forma

$$P(x)=a_nx^n+a_{n-1}x^{n-1}+\timess+a_1x+a_0$$

onde os coeficientes $$a_k$$ são reais e os expoentes são inteiros não negativos.

A expressão formal registra termos e coeficientes. A **função polinomial** associada usa essa expressão como regra para relacionar cada $$x\in\mathbb{R}$$ ao valor $$P(x)$$.

### 1.2 Reconhecimento da estrutura

**Reconhecimento de uma expressão**

Analise $$P(x)=3x^4-2x+7$$.

**Resolução:**

- **Passo 1:** Verificar a quantidade de termos.

A soma possui três termos, portanto é finita.

- **Passo 2:** Verificar os expoentes: $$4,1,0$$.

- **Passo 3:** Verificar os coeficientes: $$3,-2,7\in\mathbb{R}$$.

**Resposta:** A expressão é um polinômio real em $$x$$.

**Jean le Rond d'Alembert** (1717–1783), coeditor da *Encyclopédie*, estudou equações polinomiais e formulou uma versão inicial do Teorema Fundamental da Álgebra.

> ⚠️ **Atenção:**  
> Expoente negativo, fracionário ou variável impede que a expressão seja um polinômio em $$x$$.

---

## 2. Grau e coeficientes

### 2.1 Elementos principais

Em um polinômio não nulo:

- o **grau** é o maior expoente com coeficiente não nulo;
- o **coeficiente líder** acompanha o termo de maior grau;
- o **termo independente** é $$a_0$$.

Alguns graus recebem nomes usuais:

| Grau | Nome |
|---:|---|
| 0 | constante não nulo |
| 1 | linear |
| 2 | quadrático |
| 3 | cúbico |

### 2.2 Leitura dos elementos

**Leitura dos elementos**

Analise $$P(x)=-2x^4+5x-7$$.

**Resolução:**

- **Passo 1:** Identificar o maior expoente: $$4$$.

- **Passo 2:** Ler o coeficiente desse termo.

$$a_4=-2$$

- **Passo 3:** Ler o termo sem variável.

$$a_0=-7$$

**Resposta:** O polinômio tem grau 4, coeficiente líder $$-2$$ e termo independente $$-7$$.

Os coeficientes das potências ausentes são zero; no exemplo, $$a_3=0$$ e $$a_2=0$$.

> 🔢 **Padrão:**  
> O grau depende do maior expoente com coeficiente não nulo, não da quantidade de termos escritos.

---

## 3. Valor numérico

### 3.1 Substituição organizada

O **valor numérico** $$P(a)$$ é obtido substituindo $$x$$ por $$a$$. Para reduzir erros:

- coloque entradas negativas entre parênteses;
- calcule potências antes de produtos;
- respeite os sinais de cada termo.

### 3.2 Avaliação em entrada negativa

**Valor em uma entrada negativa**

Calcule $$P(-2)$$ para $$P(x)=x^3-3x+1$$.

**Resolução:**

- **Passo 1:** Substituir a variável.

$$P(-2)=(-2)^3-3\times(-2)+1$$

- **Passo 2:** Calcular a potência.

$$P(-2)=-8-3\times(-2)+1$$

- **Passo 3:** Calcular o produto.

$$P(-2)=-8+6+1$$

- **Passo 4:** Somar.

$$P(-2)=-1$$

**Resposta:** O valor numérico é $$-1$$.

> ⚠️ **Atenção:**  
> Em $$(-2)^2$$ o resultado é positivo; em $$-2^2$$, a potência é calculada antes do sinal.

---

## 4. Raiz de um polinômio

### 4.1 Zero e grau

Um número $$a$$ é **raiz** de $$P$$ quando

$$P(a)=0$$

Para um polinômio não nulo de grau $$n$$, há no máximo $$n$$ raízes reais distintas. O Teorema Fundamental da Álgebra afirma, sem demonstração neste recorte, a existência de $$n$$ raízes complexas quando se contam as multiplicidades.

A raiz $$a$$ também se relaciona ao fator $$x-a$$, ideia que sustenta testes de divisibilidade.

### 4.2 Teste de raiz

**Teste direto de uma raiz**

Verifique se 2 é raiz de $$P(x)=x^3-6x^2+11x-6$$.

**Resolução:**

- **Passo 1:** Substituir $$x$$ por 2.

$$P(2)=2^3-6\times2^2+11\times2-6$$

- **Passo 2:** Calcular as potências.

$$P(2)=8-6\times4+22-6$$

- **Passo 3:** Calcular o produto.

$$P(2)=8-24+22-6$$

- **Passo 4:** Somar os termos.

$$P(2)=0$$

**Resposta:** O número 2 é uma raiz de $$P$$.

> 🔢 **Padrão:**  
> Toda raiz real produz um ponto $$(a,0)$$ no gráfico da função polinomial.

---

## 5. Polinômio nulo

### 5.1 Nulo e identicamente nulo

O **polinômio nulo** possui todos os coeficientes iguais a zero. A função associada é **identicamente nula**:

$$P(x)=0$$

para todo $$x\in\mathbb{R}$$. Sobre ℝ, as definições coincidem; seu grau não é definido.

### 5.2 Determinação dos coeficientes

**Coeficientes que anulam o polinômio**

Determine $$a$$, $$b$$ e $$c$$ para que

$$P(x)=(a-1)x^2+(b+2)x+c$$

seja nulo.

**Resolução:**

- **Passo 1:** Igualar o coeficiente quadrático a zero.

$$a-1=0$$

$$a=1$$

- **Passo 2:** Igualar o coeficiente linear a zero.

$$b+2=0$$

$$b=-2$$

- **Passo 3:** Igualar o termo independente a zero.

$$c=0$$

**Resposta:** O polinômio é nulo quando $$a=1$$, $$b=-2$$ e $$c=0$$.

> ⚠️ **Atenção:**  
> Ter uma raiz não torna um polinômio identicamente nulo; todos os coeficientes precisam ser zero.

---

## 6. Igualdade de polinômios

### 6.1 Identidade polinomial

Dois polinômios são **iguais** se, e somente se, possuem o mesmo coeficiente em cada potência de $$x$$. Esse princípio permite determinar parâmetros em identidades.

### 6.2 Comparação de coeficientes

**Coeficientes a determinar**

Encontre $$a$$ e $$b$$ para que

$$(a+1)x^2+(b-2)x+3=4x^2+x+3$$

para todo $$x$$ real.

**Resolução:**

- **Passo 1:** Comparar os coeficientes de $$x^2$$.

$$a+1=4$$

$$a=3$$

- **Passo 2:** Comparar os coeficientes de $$x$$.

$$b-2=1$$

$$b=3$$

- **Passo 3:** Conferir os termos independentes.

$$3=3$$

**Resposta:** A identidade vale para $$a=3$$ e $$b=3$$.

Termos ausentes devem ser escritos mentalmente com coeficiente zero antes da comparação.

Em decomposições ou ajustes de expressões, introduzem-se coeficientes desconhecidos e comparam-se as potências correspondentes pelo mesmo método.

> 🔢 **Padrão:**  
> Uma identidade polinomial transforma a igualdade de expressões em igualdades entre coeficientes.

---

# BL2_Capítulo 2 — Operações com polinômios

> Como operar e dividir polinômios com segurança?

---

## 1. Adição e subtração

### 1.1 Termos semelhantes

Na **adição**, agrupam-se coeficientes correspondentes. Na **subtração**, distribui-se primeiro o sinal negativo por todos os termos do segundo polinômio.

Organizar as expressões em grau decrescente e preencher mentalmente potências ausentes com coeficiente zero reduz erros. Cancelamentos podem fazer o grau do resultado ficar menor que o maior grau inicial.

### 1.2 Subtração termo a termo

**Diferença entre dois polinômios**

Calcule $$P(x)-Q(x)$$, sendo

$$P(x)=3x^2+2x-1$$

$$Q(x)=x^2-5x+4$$

**Resolução:**

- **Passo 1:** Distribuir o sinal da subtração.

$$P(x)-Q(x)=3x^2+2x-1-x^2+5x-4$$

- **Passo 2:** Agrupar termos semelhantes.

$$P(x)-Q(x)=(3x^2-x^2)+(2x+5x)+(-1-4)$$

- **Passo 3:** Operar os coeficientes.

$$P(x)-Q(x)=2x^2+7x-5$$

**Resposta:** A diferença é $$2x^2+7x-5$$.

> ⚠️ **Atenção:**  
> Na subtração, o sinal negativo altera todos os termos do polinômio subtraído.

---

## 2. Multiplicação

### 2.1 Distributiva e grau

O procedimento segue três ações:

- multiplicar coeficientes;
- somar expoentes de bases iguais;
- reunir termos semelhantes.

Para polinômios não nulos, o grau do produto é a soma dos graus. Produtos notáveis são casos particulares dessa distributiva.

### 2.2 Aplicação da distributiva

**Produto termo a termo**

Calcule $$(2x-3)(x^2+x+4)$$.

**Resolução:**

- **Passo 1:** Distribuir $$2x$$.

$$2x(x^2+x+4)=2x^3+2x^2+8x$$

- **Passo 2:** Distribuir $$-3$$.

$$-3(x^2+x+4)=-3x^2-3x-12$$

- **Passo 3:** Somar os resultados: $$2x^3+2x^2+8x-3x^2-3x-12$$.

- **Passo 4:** Reduzir termos semelhantes: $$2x^3-x^2+5x-12$$.

**Resposta:** O produto é $$2x^3-x^2+5x-12$$, de grau 3.

> 🔢 **Padrão:**  
> O grau do produto de polinômios não nulos é a soma dos graus dos fatores.

---

## 3. Divisão pelo método da chave

### 3.1 Divisão euclidiana

Para $$D(x)\neq0$$, existem quociente $$Q(x)$$ e resto $$R(x)$$ tais que

$$P(x)=D(x)Q(x)+R(x)$$

com $$R(x)=0$$ ou grau de $$R$$ menor que o grau de $$D$$. O método da chave funciona para qualquer divisor polinomial não nulo.

### 3.2 Algoritmo da chave

**Divisão exata pela chave**

Divida $$x^3-7x+6$$ por $$x-1$$.

**Resolução:**

- **Passo 1:** Ordenar e incluir a potência ausente.

$$P(x)=x^3+0x^2-7x+6$$

- **Passo 2:** Dividir os termos líderes.

$$\frac{x^3}{x}=x^2$$

$$x^2(x-1)=x^3-x^2$$

A subtração deixa $$x^2-7x+6$$.

- **Passo 3:** Repetir com o novo termo líder.

$$\frac{x^2}{x}=x$$

$$x(x-1)=x^2-x$$

A subtração deixa $$-6x+6$$.

- **Passo 4:** Obter o último termo.

$$\frac{-6x}{x}=-6$$

$$-6(x-1)=-6x+6$$

O resto é zero.

**Resposta:** O quociente é $$x^2+x-6$$ e o resto é 0.

> ⚠️ **Atenção:**  
> Ordene os polinômios e registre coeficiente zero nas potências ausentes antes da divisão.

---

## 4. Dispositivo de Briot–Ruffini

### 4.1 Procedimento sintético

No **dispositivo de Briot–Ruffini**, use $$a$$ do divisor $$x-a$$. Baixe, multiplique e some: o último resultado é o resto; os demais formam o quociente.

### 4.2 Aplicação do dispositivo

**Divisão sintética**

Divida $$2x^3-3x^2+5$$ por $$x-2$$.

**Resolução:**

- **Passo 1:** Registrar os coeficientes, incluindo o termo ausente: $$2,-3,0,5$$.

- **Passo 2:** Baixar o primeiro coeficiente e multiplicar por 2.

$$2\times2=4$$

- **Passo 3:** Somar à coluna seguinte.

$$-3+4=1$$

- **Passo 4:** Repetir as operações.

$$1\times2=2$$

$$0+2=2$$

$$2\times2=4$$

$$5+4=9$$

- **Passo 5:** Interpretar os coeficientes finais.

$$Q(x)=2x^2+x+2$$

$$R=9$$

**Resposta:** O quociente é $$2x^2+x+2$$ e o resto é 9.

**Paolo Ruffini** (1765–1822) desenvolveu o dispositivo como forma econômica de dividir por fatores lineares.

> 🔢 **Padrão:**  
> No divisor $$x-a$$, o número usado no dispositivo é $$a$$ com o sinal já invertido em relação ao termo escrito.

---

# BL2_Capítulo 3 — Teoremas do resto e de D'Alembert

> Como encontrar restos e fatores sem fazer toda a divisão?

---

## 1. Teorema do resto

### 1.1 Enunciado e demonstração

O **Teorema do Resto** afirma: na divisão de $$P(x)$$ por $$x-a$$, o resto é

$$R=P(a)$$

Pela divisão euclidiana,

$$P(x)=(x-a)Q(x)+R$$

Substituindo $$x=a$$:

$$P(a)=(a-a)Q(a)+R$$

$$P(a)=0\times Q(a)+R$$

$$P(a)=R$$

### 1.2 Cálculo direto do resto

**Resto sem divisão completa**

Determine o resto da divisão de $$P(x)=x^3-4x+1$$ por $$x-2$$.

**Resolução:**

- **Passo 1:** Identificar o valor de $$a$$.

$$a=2$$

- **Passo 2:** Calcular $$P(2)$$.

$$P(2)=2^3-4\times2+1$$

$$P(2)=8-8+1$$

$$P(2)=1$$

**Resposta:** O resto é 1.

**Étienne Bézout** (1730–1783), autor da *Théorie générale des équations algébriques* (1779), é associado na tradição escolar ao pequeno teorema que relaciona esse resto a $$P(a)$$.

> 🔢 **Padrão:**  
> Dividir por $$x-a$$ transforma o cálculo do resto na avaliação de $$P(a)$$.

---

## 2. Teorema de D'Alembert

### 2.1 Equivalência

O **Teorema de D'Alembert** estabelece

$$x-a\ \text{divide}\ P(x)\Longleftrightarrow P(a)=0$$

Se $$x-a$$ divide $$P$$, o resto é zero; pelo Teorema do Resto, $$P(a)=0$$. Reciprocamente, se $$P(a)=0$$, o resto da divisão por $$x-a$$ é zero, logo a divisão é exata.

### 2.2 Teste de divisibilidade

**Teste de divisibilidade por uma raiz**

Verifique se $$x-2$$ divide $$P(x)=x^3-6x^2+11x-6$$.

**Resolução:**

- **Passo 1:** Avaliar o polinômio em 2.

$$P(2)=2^3-6\times2^2+11\times2-6$$

- **Passo 2:** Calcular as potências.

$$P(2)=8-6\times4+22-6$$

- **Passo 3:** Calcular o produto.

$$P(2)=8-24+22-6$$

- **Passo 4:** Somar.

$$P(2)=0$$

**Resposta:** Como $$P(2)=0$$, o número 2 é raiz e $$x-2$$ divide $$P(x)$$ exatamente.

A equivalência testa raízes sem efetuar a divisão.

> ⚠️ **Atenção:**  
> Para divisor $$x+3$$, escreva $$x-(-3)$$ e avalie o polinômio em $$-3$$.
