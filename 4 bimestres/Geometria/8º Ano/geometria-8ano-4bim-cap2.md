# Capítulo 2 — Plano cartesiano

> Refletir uma figura exigia régua e compasso. Agora, uma regra de duas letras resolve: trocar o sinal de y. O que acontece quando a geometria vira álgebra?

---

## 1. Plano cartesiano: aprofundamento e figuras

Uma planta digital registra cada canto como um par ordenado e transforma o desenho em dados precisos.

### 1.1 Sistema consolidado

No par ordenado $$(x,y)$$, $$x$$ é a abscissa e $$y$$, a ordenada. Os sinais identificam quadrantes:

| Região | Condição |
|---|---|
| I | $$x>0$$ e $$y>0$$ |
| II | $$x<0$$ e $$y>0$$ |
| III | $$x<0$$ e $$y<0$$ |
| IV | $$x>0$$ e $$y<0$$ |

Na origem, $$x=y=0$$. Sobre o eixo $$x$$, $$y=0$$; sobre o eixo $$y$$, $$x=0$$.

A matemática italiana **Maria Gaetana Agnesi (1718–1799)** publicou *Instituzioni analitiche* em 1748, obra que articulou linguagem algébrica e representação geométrica.

### 1.2 Polígonos e medidas

Vértices ligados em sequência determinam a figura. Para lados horizontais e verticais, o comprimento é obtido pela diferença absoluta da coordenada que varia.

**Terreno em coordenadas**

Considere $$A=(-3,-1)$$, $$B=(2,-1)$$, $$C=(2,3)$$ e $$D=(-3,3)$$.

**Resolução:**

- **Passo 1:** Calcular os lados horizontais.

$$AB=|2-(-3)|$$

$$AB=5\,\mathrm{m}$$

- **Passo 2:** Calcular os lados verticais.

$$BC=|3-(-1)|$$

$$BC=4\,\mathrm{m}$$

- **Passo 3:** Calcular o perímetro.

$$P=2\cdot(5+4)$$

$$P=18\,\mathrm{m}$$

**Resposta:** os pontos formam um retângulo de lados $$5\,\mathrm{m}$$ e $$4\,\mathrm{m}$$, com perímetro de $$18\,\mathrm{m}$$.

> ⚠️ **Atenção:**  
> Lados inclinados não podem ser medidos apenas pela diferença de uma coordenada.

---

## 2. Transformações no plano cartesiano

Uma animação move todos os vértices por regras coordenadas, sem redesenhar cada segmento manualmente.

### 2.1 Regras algébricas

Cada isometria associa o ponto original à sua imagem:

| Transformação | Regra |
|---|---|
| translação por $$(a,b)$$ | $$(x,y)\mapsto(x+a,y+b)$$ |
| reflexão no eixo $$x$$ | $$(x,y)\mapsto(x,-y)$$ |
| reflexão no eixo $$y$$ | $$(x,y)\mapsto(-x,y)$$ |
| reflexão na origem | $$(x,y)\mapsto(-x,-y)$$ |
| rotação de $$90^{\circ}$$ anti-horária | $$(x,y)\mapsto(-y,x)$$ |

Refletir na origem equivale a girar $$180^{\circ}$$. Translações e rotações preservam orientação; reflexões nos eixos a invertem.

Na reflexão pelo eixo $$x$$, a distância vertical ao eixo permanece e troca de lado; por isso somente $$y$$ muda de sinal. Na rotação anti-horária de $$90^{\circ}$$, a direção horizontal torna-se vertical: as coordenadas trocam de posição e a antiga ordenada recebe sinal oposto.

### 2.2 Imagem de uma figura

**Triângulo em animação**

O triângulo tem $$A=(1,1)$$, $$B=(3,1)$$ e $$C=(1,2)$$. Translade-o pelo vetor $$(2,-1)$$ e determine também a rotação de $$90^{\circ}$$ anti-horária do original.

**Resolução:**

- **Passo 1:** Somar o vetor a $$A$$.

$$A'=(1+2,1-1)$$

$$A'=(3,0)$$

- **Passo 2:** Aplicar a mesma regra a $$B$$.

$$B'=(3+2,1-1)$$

$$B'=(5,0)$$

- **Passo 3:** Aplicar a regra a $$C$$.

$$C'=(1+2,2-1)$$

$$C'=(3,1)$$

- **Passo 4:** Aplicar $$(x,y)\mapsto(-y,x)$$ aos três vértices originais.

$$A''=(-1,1)$$

$$B''=(-1,3)$$

$$C''=(-2,1)$$

**Resposta:** a translação produz $$A'=(3,0)$$, $$B'=(5,0)$$ e $$C'=(3,1)$$; a rotação produz $$A''=(-1,1)$$, $$B''=(-1,3)$$ e $$C''=(-2,1)$$, preservando comprimentos e ângulos.

> 🔢 **Padrão:**  
> Uma transformação de figura inteira aplica exatamente a mesma regra a todos os vértices.

---

## 3. Problemas geométricos integrados

Uma reforma combina a planta cartesiana, a área do piso, o comprimento do rodapé e a mudança de posição do cômodo.

### 3.1 Quatro etapas de Pólya

Em *How to Solve It* (1945), **George Pólya (1887–1985)** organizou um método de resolução:

- **entender** — separar dados, incógnitas e restrições;
- **planejar** — escolher propriedades e fórmulas;
- **executar** — calcular com unidades coerentes;
- **revisar** — conferir se o resultado responde à situação.

Esse método impede que uma única fórmula seja aplicada a um problema que exige ferramentas diferentes.

### 3.2 Planta de um cômodo

**Reforma de uma sala**

Os vértices da sala são $$A=(0,0)$$, $$B=(5,0)$$, $$C=(5,4)$$ e $$D=(0,4)$$, em metros. A planta será deslocada pelo vetor $$(2,-1)$$.

**Resolução:**

- **Passo 1:** Identificar o retângulo e calcular o piso.

$$A=5\cdot4$$

$$A=20\,\mathrm{m^2}$$

- **Passo 2:** Calcular o rodapé pelo perímetro.

$$P=2\cdot(5+4)$$

$$P=18\,\mathrm{m}$$

- **Passo 3:** Somar o vetor aos vértices.

$$A'=(2,-1),\ B'=(7,-1),\ C'=(7,3),\ D'=(2,3)$$

**Resposta:** a sala exige $$20\,\mathrm{m^2}$$ de piso e $$18\,\mathrm{m}$$ de rodapé; a translação muda as coordenadas, mas preserva essas medidas.

> ⚠️ **Atenção:**  
> Área e perímetro respondem a necessidades diferentes, embora sejam calculados sobre a mesma planta.
