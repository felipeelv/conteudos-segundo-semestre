# Capítulo 2 — Plano cartesiano

> No Batalha Naval, “B5” acerta um navio — e “5B” nem existe. Por que dois números em ordem localizam qualquer ponto de um plano infinito?

---

## 1. Sistema de coordenadas

Uma tela de jogo pode ser dividida por duas linhas numeradas que se cruzam e organizam todas as posições.

### 1.1 Eixos e origem

O **plano cartesiano** é formado por dois eixos numéricos perpendiculares e infinitos nas duas direções:

- eixo $$x$$ — horizontal, chamado eixo das abscissas;
- eixo $$y$$ — vertical, chamado eixo das ordenadas;
- origem $$O=(0,0)$$ — ponto de encontro dos eixos.

O filósofo e matemático **René Descartes (1596–1650)** uniu números e figuras em *La Géométrie* (1637). O nome “cartesiano” deriva de *Cartesius*, forma latina de seu sobrenome.

### 1.2 Quatro quadrantes

Os eixos dividem o plano em quatro regiões. A leitura começa no quadrante superior direito e segue no sentido anti-horário:

| Quadrante | Sinal de $$x$$ | Sinal de $$y$$ |
|---|---:|---:|
| I | positivo | positivo |
| II | negativo | positivo |
| III | negativo | negativo |
| IV | positivo | negativo |

**Localização de sensores**

Três sensores estão em $$A=(4,3)$$, $$B=(-2,5)$$ e $$C=(-3,-1)$$. Identifique seus quadrantes.

**Resolução:**

- **Passo 1:** Comparar os sinais de $$A$$ com a tabela: positivo e positivo.
- **Passo 2:** Comparar os sinais de $$B$$: negativo e positivo.
- **Passo 3:** Comparar os sinais de $$C$$: negativo e negativo.

**Resposta:** $$A$$ está no I quadrante, $$B$$ no II e $$C$$ no III; pontos sobre os eixos não pertencem a quadrante algum.

> ⚠️ **Atenção:**  
> O sinal de cada coordenada indica a direção a partir da origem, não o tamanho do ponto.

---

## 2. Localização de pontos

Num mapa quadriculado, trocar a caminhada horizontal pela vertical leva a outra posição.

### 2.1 A ordem das coordenadas

Um ponto é indicado pelo **par ordenado** $$(x,y)$$. A primeira coordenada é a abscissa; a segunda, a ordenada.

Para marcar $$P=(3,-2)$$, parte-se da origem:

- 3 unidades para a direita no eixo $$x$$;
- 2 unidades para baixo, paralelamente ao eixo $$y$$.

Assim, $$(3,-2)\neq(-2,3)$$. Pontos sobre os eixos têm uma coordenada nula: $$(x,0)$$ está no eixo $$x$$ e $$(0,y)$$ está no eixo $$y$$.

### 2.2 Figuras por vértices

Uma sequência de pares ordenados representa um polígono quando os pontos são ligados na ordem indicada. Lados horizontais têm a mesma ordenada; lados verticais têm a mesma abscissa.

**Planta de um canteiro**

Os vértices são $$A=(-2,1)$$, $$B=(3,1)$$, $$C=(3,4)$$ e $$D=(-2,4)$$. Identifique a figura.

**Resolução:**

- **Passo 1:** Os lados $$AB$$ e $$CD$$ são horizontais, pois conservam $$y$$.
- **Passo 2:** Os lados $$BC$$ e $$DA$$ são verticais, pois conservam $$x$$.
- **Passo 3:** Horizontais e verticais encontram-se perpendicularmente.

**Resposta:** os vértices formam um retângulo de comprimento 5 unidades e largura 3 unidades.

Um ponto dado no desenho é lido fazendo o caminho inverso: projeta-se primeiro no eixo $$x$$ e depois no eixo $$y$$.

> 🔢 **Padrão:**  
> Em $$(x,y)$$, o deslocamento horizontal sempre vem antes do vertical.

---

## 3. Distância entre pontos

Dois armários na mesma parede podem ser separados contando apenas quadrículas horizontais ou verticais.

### 3.1 Alinhamento horizontal e vertical

Se dois pontos têm a mesma ordenada, a distância é a diferença absoluta entre as abscissas:

$$d=|x_2-x_1|$$

Se têm a mesma abscissa, usa-se a diferença absoluta entre as ordenadas:

$$d=|y_2-y_1|$$

O **valor absoluto** transforma uma diferença negativa em medida positiva, pois distância não tem sentido contrário.

| Alinhamento | Coordenada igual | Coordenada comparada |
|---|---|---|
| horizontal | $$y$$ | $$x$$ |
| vertical | $$x$$ | $$y$$ |

### 3.2 Um trajeto em duas partes

Quando o deslocamento segue ruas horizontais e verticais, calcula-se cada trecho e depois somam-se as medidas. Esse trajeto não é uma diagonal.

**Rota de manutenção**

Um técnico sai de $$A=(-4,2)$$, vai horizontalmente até $$B=(3,2)$$ e depois verticalmente até $$C=(3,-3)$$. Calcule a rota.

**Resolução:**

- **Passo 1:** Calcular o trecho horizontal.

$$AB=|3-(-4)|$$

$$AB=7\,\mathrm{m}$$

- **Passo 2:** Calcular o trecho vertical.

$$BC=|-3-2|$$

$$BC=5\,\mathrm{m}$$

- **Passo 3:** Somar os dois trechos.

$$7+5=12\,\mathrm{m}$$

**Resposta:** a rota horizontal e vertical mede $$12\,\mathrm{m}$$.

> ⚠️ **Atenção:**  
> A ordem da subtração pode mudar, mas o valor absoluto mantém a mesma distância positiva.
