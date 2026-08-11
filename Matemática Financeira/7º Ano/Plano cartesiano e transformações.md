# BL2_Capítulo 1 — Plano cartesiano e transformações

> No Tetris, cada peça pode ser deslocada, girada ou espelhada — e continua sendo a mesma peça. Como descrever cada um desses movimentos usando só as coordenadas dos vértices?

---

## 1. Sistema de coordenadas cartesianas

Um ponto no mapa digital precisa de duas informações para indicar uma posição.

### 1.1 Eixos, origem e quadrantes

O plano cartesiano possui dois eixos perpendiculares:

- eixo horizontal: abscissas, representadas por $$x$$;
- eixo vertical: ordenadas, representadas por $$y$$;
- encontro dos eixos: origem $$O(0,0)$$.

Os sinais identificam os quatro quadrantes:

| Quadrante | Sinal de $$x$$ | Sinal de $$y$$ |
|---|---:|---:|
| I | + | + |
| II | − | + |
| III | − | − |
| IV | + | − |

Em *La Géométrie*, de 1637, **René Descartes** relacionou álgebra e geometria por coordenadas. “Cartesiano” deriva de *Cartesius*, forma latina de seu nome; a história da mosca no teto é apenas uma lenda pedagógica.

### 1.2 Pares ordenados

Um ponto é escrito como $$P(x,y)$$: primeiro vem a posição horizontal; depois, a vertical.

$$P(2,3) \neq P(3,2)$$

**Localização de seis pontos**

Considere $$A(3,2)$$, $$B(-2,4)$$, $$C(-3,-1)$$, $$D(4,-2)$$, $$E(0,3)$$ e $$F(-2,0)$$.

**Resolução:**

- **Passo 1:** Comparar os sinais das coordenadas.

| Ponto | Localização |
|---|---|
| $$A(3,2)$$ | quadrante I |
| $$B(-2,4)$$ | quadrante II |
| $$C(-3,-1)$$ | quadrante III |
| $$D(4,-2)$$ | quadrante IV |
| $$E(0,3)$$ | eixo $$y$$ |
| $$F(-2,0)$$ | eixo $$x$$ |

**Resposta:** pontos com uma coordenada zero ficam sobre um eixo e não pertencem a quadrante algum.

Latitude e longitude também formam um par de localização usado pelo GPS, embora a Terra exija um modelo esférico, não um plano.

> ⚠️ **Atenção:**
>
> Trocar a ordem das coordenadas geralmente muda a posição do ponto.

---

## 2. Multiplicação e simetrias

Um zoom pode aumentar uma figura mantendo seus ângulos e suas proporções.

### 2.1 Multiplicar coordenadas

Com fator inteiro $$k$$, a transformação é:

$$T_k: P(x,y) \to P'(kx,ky)$$

Nessa regra, $$P$$ é o ponto inicial, $$P'$$ o transformado e $$k$$ o fator inteiro.

- se $$|k|>1$$, há ampliação;
- se $$k=-1$$, há reflexão pela origem;
- se $$k< -1$$, ampliação e reflexão ocorrem juntas.

No recorte com inteiros, uma redução é descrita como o caminho inverso: dividir as coordenadas ampliadas pelo mesmo inteiro.

**Ampliação de um triângulo**

Considere $$A(1,1)$$, $$B(3,1)$$ e $$C(1,2)$$, com $$k=2$$.

**Resolução:**

- **Passo 1:** Multiplicar cada coordenada por 2.

$$A'(2,2)$$

$$B'(6,2)$$

$$C'(2,4)$$

- **Passo 2:** Conferir a transformação inversa.

$$A'(2,2) \to A(1,1)$$

**Resposta:** as distâncias à origem dobram na ampliação; dividi-las por 2 recupera o triângulo inicial.

### 2.2 Simetrias

As três simetrias deste recorte possuem regras diferentes:

| Referência | Transformação |
|---|---|
| Eixo $$x$$ | $$(x,y) \to (x,-y)$$ |
| Eixo $$y$$ | $$(x,y) \to (-x,y)$$ |
| Origem | $$(x,y) \to (-x,-y)$$ |

Para $$P(3,-2)$$, os resultados são $$P_x'(3,2)$$, $$P_y'(-3,-2)$$ e $$P_O'(-3,2)$$.

A reflexão nos eixos é **axial**; pela origem, é **central**. Em um polígono, a mesma regra deve ser aplicada a todos os vértices.

> 🔢 **Padrão:**
>
> Na reflexão por um eixo, somente a coordenada perpendicular a esse eixo troca de sinal.

---

## 3. Translação, rotação e reflexão

Uma peça pode mudar de lugar sem mudar o comprimento de nenhum lado.

### 3.1 Regras de movimento

A **translação** desloca cada ponto pela mesma quantidade:

$$P(x,y) \to P'(x+a,y+b)$$

Nessa expressão, $$a$$ é o deslocamento horizontal e $$b$$, o vertical.

Duas rotações em torno da origem possuem regras diretas:

| Movimento | Transformação |
|---|---|
| 90° anti-horária | $$(x,y) \to (-y,x)$$ |
| 180° | $$(x,y) \to (-x,-y)$$ |

A rotação de 180° coincide com a simetria pela origem. A reflexão retoma as regras dos eixos vistas anteriormente.

**Movimentos de um ponto**

Considere $$P(2,1)$$.

**Resolução:**

- **Passo 1:** Transladar 3 unidades à direita e 2 para baixo.

$$P'(2+3,1-2)=P'(5,-1)$$

- **Passo 2:** Girar o ponto inicial 90° no sentido anti-horário.

$$P''(-1,2)$$

- **Passo 3:** Girar o ponto inicial 180°.

$$P'''(-2,-1)$$

**Resposta:** cada movimento produz coordenadas diferentes, mas segue uma regra aplicável a todos os vértices da peça.

### 3.2 Transformações isométricas

Translação, rotação e reflexão são **isometrias**: preservam comprimentos, ângulos e forma.

Elas aparecem em:

- padrões da Alhambra e obras de M. C. Escher;
- simetria de borboletas e cristais;
- movimentos de peças em jogos digitais.

Um software de geometria dinâmica, como o GeoGebra, representa o ponto e atualiza suas coordenadas quando a transformação é aplicada.

> ⚠️ **Atenção:**
>
> Ampliação e redução preservam a forma, mas não são isometrias porque alteram as distâncias.
