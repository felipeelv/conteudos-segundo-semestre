# Geometria — 9º Ano · Bloco 2

> **3º Bimestre — Trigonometria e geometria espacial** · Bloco 2 (27/08–18/09)

**Capítulos deste bloco**

2. **Geometria espacial e representações** (3 aulas)

---

# BL2_Capítulo 1 — Geometria espacial e representações

> Como um manual plano representa um móvel tridimensional e como a mesma escala decimal mede de um vírus a uma distância astronômica?

---

## 1. Noções básicas de geometria espacial

As bordas e superfícies de uma sala permitem reconhecer retas e planos no espaço tridimensional.

### 1.1 Posições no espaço

Duas retas **coplanares** pertencem ao mesmo plano e podem ser paralelas ou concorrentes. Retas **reversas** não estão no mesmo plano e não se cruzam.

<!-- tikz:inicio fig-01-posicoes-entre-retas-no-espaco -->
![Comparação espacial entre retas paralelas, concorrentes e reversas com indicação dos planos que as contêm](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/9ano/geometria-espacial-e-representacoes/fig-01-posicoes-entre-retas-no-espaco.png)
<!-- tikz:fim fig-01-posicoes-entre-retas-no-espaco -->

Uma reta pode estar contida em um plano, ser paralela a ele ou atravessá-lo em um ponto, tornando-se secante.

<!-- tikz:inicio fig-02-posicoes-entre-reta-e-plano -->
![Reta contida em um plano, reta paralela ao plano e reta secante ao plano em um ponto](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/9ano/geometria-espacial-e-representacoes/fig-02-posicoes-entre-reta-e-plano.png)
<!-- tikz:fim fig-02-posicoes-entre-reta-e-plano -->

Dois planos podem ser paralelos, secantes ou coincidentes.

<!-- tikz:inicio fig-03-posicoes-entre-planos -->
![Comparação entre dois planos paralelos, secantes em uma reta e coincidentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/9ano/geometria-espacial-e-representacoes/fig-03-posicoes-entre-planos.png)
<!-- tikz:fim fig-03-posicoes-entre-planos -->

Um **poliedro** é limitado por polígonos. Seus elementos são vértices, arestas e faces.

<!-- tikz:inicio fig-04-elementos-de-um-poliedro -->
![Cubo com um vértice, uma aresta e uma face destacados e identificados](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/9ano/geometria-espacial-e-representacoes/fig-04-elementos-de-um-poliedro.png)
<!-- tikz:fim fig-04-elementos-de-um-poliedro -->

| Poliedro | Vértices $$V$$ | Arestas $$A$$ | Faces $$F$$ |
|---|---:|---:|---:|
| cubo | 8 | 12 | 6 |
| tetraedro | 4 | 6 | 4 |
| octaedro | 6 | 12 | 8 |

### 1.2 Verificação de Euler

Para poliedros sem furos, a contagem satisfaz:

$$V-A+F=2$$

**Bola de futebol geométrica**

Uma bola formada por 12 pentágonos e 20 hexágonos possui 60 vértices e 90 arestas.

**Resolução:**

- **Passo 1:** Contar as faces.

$$F=12+20$$

$$F=32$$

- **Passo 2:** Substituir na relação.

$$60-90+32=2$$

**Resposta:** a contagem verifica a relação de Euler, pois o resultado é 2.

> 🔢 **Padrão:**  
> Uma aresta é compartilhada por duas faces, mas deve ser contada apenas uma vez.

---

## 2. Vistas ortogonais e representações técnicas

Um manual de montagem mostra um móvel por diferentes direções para registrar dimensões que uma única imagem esconderia.

### 2.1 Três projeções coerentes

Uma **vista ortogonal** é obtida por linhas de projeção perpendiculares ao plano do desenho.

| Vista | Dimensões exibidas |
|---|---|
| frontal | largura e altura |
| lateral | profundidade e altura |
| superior | largura e profundidade |

<!-- tikz:inicio fig-05-objeto-e-tres-vistas-ortogonais -->
![Peça tridimensional ligada às vistas frontal, lateral e superior com dimensões compartilhadas](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/9ano/geometria-espacial-e-representacoes/fig-05-objeto-e-tres-vistas-ortogonais.png)
<!-- tikz:fim fig-05-objeto-e-tres-vistas-ortogonais -->

Cada dimensão aparece em duas vistas. Essa repetição permite conferir a coerência e reconstruir mentalmente o objeto. A **perspectiva cavaleira**, por sua vez, reúne três dimensões em um desenho com arestas inclinadas para sugerir profundidade.

O matemático e engenheiro francês **Gaspard Monge** (1746–1818) sistematizou a geometria descritiva, base das projeções usadas em desenho técnico.

### 2.2 Leitura de uma peça

**Bloco retangular**

Uma peça mede $$8\,\mathrm{cm}$$ de largura, $$5\,\mathrm{cm}$$ de profundidade e $$3\,\mathrm{cm}$$ de altura.

**Resolução:**

- **Passo 1:** Combinar largura e altura na vista frontal.

$$8\,\mathrm{cm}\times3\,\mathrm{cm}$$

- **Passo 2:** Combinar profundidade e altura na lateral.

$$5\,\mathrm{cm}\times3\,\mathrm{cm}$$

- **Passo 3:** Combinar largura e profundidade na superior.

$$8\,\mathrm{cm}\times5\,\mathrm{cm}$$

**Resposta:** as vistas são retângulos de $$8\times3$$, $$5\times3$$ e $$8\times5$$ centímetros, respectivamente.

Linhas contínuas representam arestas visíveis; tracejadas indicam arestas escondidas.

<!-- tikz:inicio fig-06-perspectiva-e-arestas-ocultas -->
![Peça em perspectiva cavaleira com arestas visíveis contínuas e arestas escondidas tracejadas](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/9ano/geometria-espacial-e-representacoes/fig-06-perspectiva-e-arestas-ocultas.png)
<!-- tikz:fim fig-06-perspectiva-e-arestas-ocultas -->

> ⚠️ **Atenção:**  
> Girar o objeto sem registrar a direção observada pode trocar largura por profundidade.

---

## 3. Sistema de medidas

O tamanho de um vírus e a capacidade de um celular parecem incomparáveis, mas ambos são escritos com potências de dez.

### 3.1 Múltiplos e submúltiplos

O Sistema Internacional organiza prefixos decimais:

| Prefixo | Símbolo | Fator |
|---|---:|---:|
| tera | T | $$10^{12}$$ |
| giga | G | $$10^9$$ |
| mega | M | $$10^6$$ |
| quilo | k | $$10^3$$ |
| mili | m | $$10^{-3}$$ |
| micro | $$\mu$$ | $$10^{-6}$$ |
| nano | n | $$10^{-9}$$ |

Assim, $$120\,\mathrm{nm}=1{,}2\cdot10^{-7}\,\mathrm{m}$$. Em escala astronômica, uma unidade astronômica vale aproximadamente $$1{,}496\cdot10^{11}\,\mathrm{m}$$ e um ano-luz, $$9{,}461\cdot10^{15}\,\mathrm{m}$$.

### 3.2 Armazenamento digital

Um byte reúne 8 bits. No padrão decimal, $$1\,\mathrm{GB}=10^9\,\mathrm{bytes}$$.

Os mesmos prefixos formam quilobyte, megabyte, gigabyte e terabyte. Por exemplo, $$256\,\mathrm{GB}=2{,}56\cdot10^{11}\,\mathrm{bytes}$$, o que evidencia sua ordem de grandeza.

**Fotos em um celular**

Um aparelho possui $$256\,\mathrm{GB}$$ e cada foto ocupa, em média, $$5\,\mathrm{MB}$$.

**Resolução:**

- **Passo 1:** Converter gigabytes em megabytes.

$$256\,\mathrm{GB}=256\,000\,\mathrm{MB}$$

- **Passo 2:** Dividir a capacidade pelo tamanho de uma foto.

$$\frac{256\,000}{5}=51\,200$$

**Resposta:** desconsiderando o sistema e outros arquivos, cabem aproximadamente 51.200 fotos.

> 🔢 **Padrão:**  
> A ordem de grandeza indica a potência de dez predominante em uma medida.
