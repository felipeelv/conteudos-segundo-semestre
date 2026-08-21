# Capítulo 3 — Transformações geométricas

> O logo da Mercedes-Benz fica idêntico quando girado 120°; os anéis olímpicos, quando refletidos no eixo vertical. Que movimentos deixam uma figura invariante — e o que exatamente cada movimento preserva?

---

## 1. Transformações: translação e reflexão

Mover uma escultura pelo salão e observá-la num espelho alteram sua posição de maneiras geometricamente diferentes.

### 1.1 Isometria e translação

**Transformação geométrica** associa cada ponto de um objeto a um ponto da imagem. **Isometria** preserva distâncias e, portanto, mantém forma, tamanho e ângulos.

Na translação, todos os pontos percorrem o mesmo vetor $$\vec{v}$$, definido por:

- direção;
- sentido;
- módulo.

O objeto muda de posição e preserva a orientação: a ordem espacial dos vértices não se inverte.

### 1.2 Reflexão num plano

Na reflexão espacial, um plano funciona como espelho. Cada segmento entre ponto e imagem é perpendicular ao plano, que o corta ao meio.

| Propriedade | Translação | Reflexão |
|---|---|---|
| distâncias | preserva | preserva |
| ângulos | preserva | preserva |
| orientação | preserva | inverte |

Mãos direita e esquerda têm a mesma forma e medidas, mas orientações opostas; uma não coincide com a outra apenas por deslocamento.

**Escultura deslocada e refletida**

Uma escultura possui arestas de $$2\,\mathrm{m}$$, $$3\,\mathrm{m}$$ e $$4\,\mathrm{m}$$. Ela é transladada $$5\,\mathrm{m}$$ ao norte e depois refletida num plano vertical.

**Resolução:**

- **Passo 1:** A translação aplica o mesmo vetor a todos os vértices.
- **Passo 2:** A reflexão conserva cada distância ao criar a imagem oposta.
- **Passo 3:** Registrar o que muda: posição nas duas etapas e orientação apenas na reflexão.

**Resposta:** a imagem final continua com arestas de $$2\,\mathrm{m}$$, $$3\,\mathrm{m}$$ e $$4\,\mathrm{m}$$, mas apresenta orientação invertida.

> 🔢 **Padrão:**  
> Toda isometria preserva medidas; apenas algumas preservam também a orientação.

---

## 2. Transformações: rotação

Uma hélice gira ao redor de um eixo fixo e retorna à mesma aparência após certos ângulos.

### 2.1 Eixo, ângulo e simetria

Uma **rotação espacial** é determinada por eixo, ângulo $$\theta$$ e sentido. Ela preserva:

- distâncias;
- ângulos;
- forma e tamanho;
- orientação.

Um objeto tem simetria de rotação quando algum giro menor que $$360^{\circ}$$ o leva à mesma posição aparente. Uma estrela de três pontas igualmente espaçadas coincide consigo após $$120^{\circ}$$ e $$240^{\circ}$$.

**Sophus Lie (1842–1899)** sistematizou transformações contínuas, como rotações por qualquer ângulo, em sua *Teoria dos Grupos de Transformação* (1888–1893).

### 2.2 Rotação que gera sólidos

| Figura plana | Eixo de giro | Sólido gerado |
|---|---|---|
| retângulo | um lado | cilindro |
| triângulo retângulo | um cateto | cone |
| semicírculo | diâmetro | esfera |

**Rotor de três pás**

Três pás idênticas estão igualmente espaçadas em torno do eixo. Determine o menor giro de simetria e o próximo giro equivalente.

**Resolução:**

- **Passo 1:** Dividir a volta pelo número de pás.

$$\theta=\frac{360^{\circ}}{3}$$

$$\theta=120^{\circ}$$

- **Passo 2:** Somar mais um intervalo.

$$120^{\circ}+120^{\circ}=240^{\circ}$$

**Resposta:** os giros não nulos menores que uma volta que preservam a aparência são $$120^{\circ}$$ e $$240^{\circ}$$.

> ⚠️ **Atenção:**  
> O eixo permanece fixo; os demais pontos descrevem circunferências em planos perpendiculares a ele.

---

## 3. Homotetia

Uma miniatura preserva ângulos e proporções do original, mas altera todas as distâncias por um mesmo fator.

### 3.1 Centro e razão

Na **homotetia** de centro $$O$$ e razão $$k$$, os pontos satisfazem:

$$\overrightarrow{OP'}=k\cdot\overrightarrow{OP}$$

| Razão | Efeito |
|---|---|
| $$k>1$$ | ampliação |
| $$0<k<1$$ | redução |
| $$k<0$$ | imagem no lado oposto de $$O$$ |

A homotetia preserva ângulos, paralelismo e proporções, mas multiplica distâncias por $$|k|$$. Portanto, não é isometria quando $$|k|\neq1$$.

### 3.2 Invariantes comparados

| Transformação | Distância | Ângulo | Orientação | Tamanho |
|---|---|---|---|---|
| translação | preserva | preserva | preserva | preserva |
| reflexão | preserva | preserva | inverte | preserva |
| rotação | preserva | preserva | preserva | preserva |
| homotetia | altera | preserva | depende de $$k$$ | altera |

**Miniatura invertida**

Um ponto de uma escultura está a $$8\,\mathrm{m}$$ do centro. Aplica-se $$k=-1/2$$.

**Resolução:**

- **Passo 1:** Calcular a nova distância.

$$OP'=\left|-\frac{1}{2}\right|\cdot8$$

$$OP'=4\,\mathrm{m}$$

- **Passo 2:** Interpretar o sinal: a imagem fica no lado oposto do centro.
- **Passo 3:** Calcular os fatores dimensionais.

$$k^2=\frac{1}{4}$$

$$|k|^3=\frac{1}{8}$$

**Resposta:** a imagem fica a $$4\,\mathrm{m}$$ no lado oposto; áreas ficam em $$1/4$$ e volumes em $$1/8$$ dos originais.

> 🔢 **Padrão:**  
> A homotetia preserva a forma e gera sólidos semelhantes, mas somente razões de módulo 1 preservam o tamanho.
