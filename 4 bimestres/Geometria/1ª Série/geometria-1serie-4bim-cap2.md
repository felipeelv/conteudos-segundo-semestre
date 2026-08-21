# Capítulo 2 — Trigonometria: do triângulo retângulo ao triângulo qualquer

> Como o IBGE mapeia 8,5 milhões de km² do Brasil sem visitar cada ponto? E como o Pão de Açúcar, com 396 m, foi medido em 1817 — sem GPS, drone ou laser?

---

## 1. Razões trigonométricas: seno, cosseno e tangente

Rampas de tamanhos diferentes conservam a inclinação quando os triângulos retângulos apresentam o mesmo ângulo agudo.

### 1.1 Lados em relação ao ângulo

Para um ângulo agudo $$\theta$$, a hipotenusa é oposta ao ângulo reto. Os catetos recebem nomes relativos:

- **oposto** — não toca $$\theta$$;
- **adjacente** — forma $$\theta$$ com a hipotenusa.

As razões são:

$$\mathrm{sen}\,\theta=\frac{\mathrm{cateto\ oposto}}{\mathrm{hipotenusa}}$$

$$\cos\theta=\frac{\mathrm{cateto\ adjacente}}{\mathrm{hipotenusa}}$$

$$\mathrm{tg}\,\theta=\frac{\mathrm{cateto\ oposto}}{\mathrm{cateto\ adjacente}}$$

### 1.2 Por que são constantes

Triângulos retângulos com o mesmo ângulo $$\theta$$ são semelhantes por AA. Seus lados correspondentes podem aumentar, mas as divisões entre eles permanecem iguais; portanto, cada razão depende apenas do ângulo.

**Rampa de seção 5-12-13**

Num triângulo retângulo, em relação a $$\theta$$, o cateto oposto mede $$5\,\mathrm{m}$$, o adjacente $$12\,\mathrm{m}$$ e a hipotenusa $$13\,\mathrm{m}$$.

**Resolução:**

- **Passo 1:** Calcular o seno.

$$\mathrm{sen}\,\theta=\frac{5}{13}$$

- **Passo 2:** Calcular o cosseno.

$$\cos\theta=\frac{12}{13}$$

- **Passo 3:** Calcular a tangente.

$$\mathrm{tg}\,\theta=\frac{5}{12}$$

**Resposta:** as razões são $$5/13$$, $$12/13$$ e $$5/12$$, respectivamente, e não possuem unidade.

Os dois ângulos agudos são complementares; assim, $$\mathrm{sen}\,\theta=\cos(90^{\circ}-\theta)$$.

> ⚠️ **Atenção:**  
> Ao trocar o ângulo de referência, os catetos oposto e adjacente trocam de função.

---

## 2. Relação fundamental e identidade da tangente

Num triângulo de hipotenusa unitária, as medidas dos catetos coincidem com seno e cosseno do ângulo escolhido.

### 2.1 Pitágoras normalizado

Se os catetos são $$b$$ e $$c$$ e a hipotenusa é $$a$$, Pitágoras fornece:

$$b^2+c^2=a^2$$

Dividindo todos os termos por $$a^2$$:

$$\frac{b^2}{a^2}+\frac{c^2}{a^2}=1$$

Como as frações são os quadrados das razões, resulta:

$$\mathrm{sen}^2\theta+\cos^2\theta=1$$

Logo, $$\cos^2\theta=1-\mathrm{sen}^2\theta$$. A notação $$\mathrm{sen}^2\theta$$ significa $$(\mathrm{sen}\,\theta)^2$$.

Para ângulos agudos, seno e cosseno são positivos. Por isso, ao extrair a raiz de uma forma derivada, escolhe-se o valor positivo: $$\cos\theta=\sqrt{1-\mathrm{sen}^2\theta}$$ ou $$\mathrm{sen}\,\theta=\sqrt{1-\cos^2\theta}$$.

### 2.2 Tangente por quociente

Dividir seno por cosseno cancela a hipotenusa:

$$\frac{\mathrm{sen}\,\theta}{\cos\theta}=\frac{b/a}{c/a}$$

$$\mathrm{tg}\,\theta=\frac{\mathrm{sen}\,\theta}{\cos\theta}$$

**Razões a partir do seno**

Para um ângulo agudo, $$\mathrm{sen}\,\theta=3/5$$. Determine cosseno e tangente.

**Resolução:**

- **Passo 1:** Usar a relação fundamental.

$$\cos^2\theta=1-\left(\frac{3}{5}\right)^2$$

$$\cos^2\theta=\frac{16}{25}$$

- **Passo 2:** Tomar a raiz positiva, pois o ângulo é agudo.

$$\cos\theta=\frac{4}{5}$$

- **Passo 3:** Calcular a tangente.

$$\mathrm{tg}\,\theta=\frac{3/5}{4/5}$$

$$\mathrm{tg}\,\theta=\frac{3}{4}$$

**Resposta:** o cosseno é $$4/5$$ e a tangente é $$3/4$$.

> 🔢 **Padrão:**  
> A relação fundamental permite obter uma das duas razões quando a outra e o quadrante geométrico são conhecidos.

---

## 3. Ângulos notáveis

Os esquadros de desenho usam $$30^{\circ}$$, $$45^{\circ}$$ e $$60^{\circ}$$ porque suas razões têm valores exatos.

### 3.1 Origem geométrica

Uma altura num triângulo equilátero de lado 2 forma dois triângulos com hipotenusa 2, cateto 1 e cateto $$\sqrt{3}$$. Deles surgem os valores de $$30^{\circ}$$ e $$60^{\circ}$$.

Pitágoras justifica a altura:

$$h^2=2^2-1^2$$

$$h=\sqrt{3}$$

Um quadrado de lado 1 cortado pela diagonal produz um triângulo retângulo isósceles com hipotenusa $$\sqrt{2}$$, origem dos valores de $$45^{\circ}$$.

Nesse caso, dividir cateto 1 por hipotenusa $$\sqrt{2}$$ e racionalizar fornece $$\sqrt{2}/2$$. Assim, a tabela pode ser reconstruída pelas duas figuras, sem depender apenas de memorização.

A racionalização preserva o valor exato sem recorrer a aproximação decimal.

### 3.2 Tabela exata

| $$\theta$$ | $$\mathrm{sen}\,\theta$$ | $$\cos\theta$$ | $$\mathrm{tg}\,\theta$$ |
|---|---|---|---|
| $$30^{\circ}$$ | $$\frac{1}{2}$$ | $$\frac{\sqrt{3}}{2}$$ | $$\frac{\sqrt{3}}{3}$$ |
| $$45^{\circ}$$ | $$\frac{\sqrt{2}}{2}$$ | $$\frac{\sqrt{2}}{2}$$ | $$1$$ |
| $$60^{\circ}$$ | $$\frac{\sqrt{3}}{2}$$ | $$\frac{1}{2}$$ | $$\sqrt{3}$$ |

Pares complementares trocam seno e cosseno; em $$45^{\circ}$$, eles coincidem.

**Verificação para 30 graus**

Confirme a relação fundamental com os valores exatos de $$30^{\circ}$$.

**Resolução:**

- **Passo 1:** Elevar seno e cosseno ao quadrado.

$$\mathrm{sen}^2 30^{\circ}=\frac{1}{4}$$

$$\cos^2 30^{\circ}=\frac{3}{4}$$

- **Passo 2:** Somar.

$$\frac{1}{4}+\frac{3}{4}=1$$

**Resposta:** os valores de $$30^{\circ}$$ satisfazem $$\mathrm{sen}^2\theta+\cos^2\theta=1$$.

> 🔢 **Padrão:**  
> Nos pares $$30^{\circ}$$ e $$60^{\circ}$$, seno e cosseno aparecem em ordem invertida.

---

## 4. Aplicações das razões trigonométricas

Um teodolito mede um ângulo a partir da horizontal e converte a observação em altura, largura ou distância.

### 4.1 Medição indireta e triangulação

O ângulo de **elevação** aponta da horizontal para cima; o de **depressão**, para baixo. Depois de modelar um triângulo retângulo, escolhe-se a razão pelos lados disponíveis.

Em 1533, **Gemma Frisius (1508–1555)** sistematizou a triangulação cartográfica: uma base conhecida e ângulos medidos determinam novas distâncias. O princípio sustenta redes geodésicas usadas em mapeamento territorial.

No Brasil, medições históricas do Pão de Açúcar e levantamentos do IBGE aplicam essa lógica. Rampas também relacionam desnível e avanço horizontal; inclinação de 8,33% corresponde aproximadamente a $$\mathrm{tg}\,\theta=0{,}0833$$.

### 4.2 Altura inacessível

**Torre observada do solo**

Um ponto está a $$100\sqrt{3}\,\mathrm{m}$$ da base de uma torre. O ângulo de elevação até o topo é $$30^{\circ}$$.

**Resolução:**

- **Passo 1:** Relacionar altura e distância pela tangente.

$$\mathrm{tg}\,30^{\circ}=\frac{h}{100\sqrt{3}}$$

- **Passo 2:** Substituir o valor notável.

$$\frac{\sqrt{3}}{3}=\frac{h}{100\sqrt{3}}$$

- **Passo 3:** Isolar a altura.

$$h=100\,\mathrm{m}$$

**Resposta:** a torre mede $$100\,\mathrm{m}$$ acima do nível do observador.

Num telhado com caibro de $$4\,\mathrm{m}$$ a $$30^{\circ}$$, as componentes são $$4\cdot\mathrm{sen}\,30^{\circ}=2\,\mathrm{m}$$ na vertical e $$4\cdot\cos30^{\circ}=2\sqrt{3}\,\mathrm{m}$$ na horizontal.

> ⚠️ **Atenção:**  
> Elevação e depressão são medidas a partir da horizontal, nunca da vertical.

---

## 5. Lei dos senos

Uma rota triangular sem ângulo reto ainda pode ser determinada quando se conhece um lado e ângulos suficientes.

### 5.1 Enunciado e origem

Num triângulo qualquer, lados minúsculos ficam opostos aos ângulos maiúsculos correspondentes:

$$\frac{a}{\mathrm{sen}\,A}=\frac{b}{\mathrm{sen}\,B}=\frac{c}{\mathrm{sen}\,C}=2R$$

onde $$R$$ é o raio da circunferência circunscrita.

Para justificar, considere a corda de comprimento $$a$$. Um ângulo inscrito $$A$$ que enxerga essa corda mede metade do ângulo central correspondente. Ao formar um triângulo retângulo com raio $$R$$, obtém-se:

$$a=2R\cdot\mathrm{sen}\,A$$

O mesmo raciocínio vale para as outras cordas. Em triângulo obtusângulo, usa-se pontualmente $$\mathrm{sen}(180^{\circ}-x)=\mathrm{sen}\,x$$.

### 5.2 Aplicação de navegação

A lei é adequada para AAL ou quando são conhecidos dois lados e o ângulo oposto a um deles.

**Trecho entre duas boias**

Num triângulo de navegação, $$A=45^{\circ}$$, $$B=60^{\circ}$$ e o lado oposto a $$A$$ mede $$10\,\mathrm{km}$$. Determine $$b$$.

**Resolução:**

- **Passo 1:** Montar a proporção correspondente.

$$\frac{10}{\mathrm{sen}\,45^{\circ}}=\frac{b}{\mathrm{sen}\,60^{\circ}}$$

- **Passo 2:** Substituir valores notáveis.

$$b=10\cdot\frac{\sqrt{3}/2}{\sqrt{2}/2}$$

- **Passo 3:** Simplificar.

$$b=5\sqrt{6}\,\mathrm{km}$$

$$b\approx12{,}25\,\mathrm{km}$$

**Resposta:** o trecho mede $$5\sqrt{6}\,\mathrm{km}$$, aproximadamente $$12{,}25\,\mathrm{km}$$.

> 🔢 **Padrão:**  
> Na Lei dos Senos, cada lado deve permanecer emparelhado com seu ângulo oposto.

---

## 6. Lei dos cossenos

Um levantamento com dois lados e o ângulo entre eles exige uma relação que generaliza Pitágoras.

### 6.1 Projeção e enunciado

Traçar a altura a partir de um vértice separa o triângulo em dois triângulos retângulos. Se a projeção de $$c$$ sobre $$b$$ mede $$c\cos A$$, Pitágoras aplicado às partes produz:

$$a^2=b^2+c^2-2bc\cos A$$

As formas análogas surgem por troca cíclica das letras. Se $$A=90^{\circ}$$, então $$\cos90^{\circ}=0$$ e a expressão torna-se Pitágoras.

Para ângulo obtuso, $$\cos(180^{\circ}-x)=-\cos x$$; o termo subtraído torna-se positivo, coerente com o lado oposto maior.

### 6.2 Escolha e aplicação

| Dados | Relação preferencial |
|---|---|
| LAL ou LLL | Lei dos Cossenos |
| AAL ou LLA | Lei dos Senos |

**Distância em um terreno**

Dois lados de um terreno medem $$7\,\mathrm{m}$$ e $$5\,\mathrm{m}$$, com ângulo de $$60^{\circ}$$ entre eles.

**Resolução:**

- **Passo 1:** Aplicar a Lei dos Cossenos.

$$a^2=7^2+5^2-2\cdot7\cdot5\cdot\cos60^{\circ}$$

- **Passo 2:** Substituir o cosseno.

$$a^2=49+25-70\cdot\frac{1}{2}$$

$$a^2=39\,\mathrm{m^2}$$

- **Passo 3:** Extrair a raiz positiva.

$$a=\sqrt{39}\,\mathrm{m}$$

$$a\approx6{,}24\,\mathrm{m}$$

**Resposta:** o terceiro lado mede $$\sqrt{39}\,\mathrm{m}$$, aproximadamente $$6{,}24\,\mathrm{m}$$.

> ⚠️ **Atenção:**  
> Na configuração LAL, o ângulo usado deve ser exatamente o compreendido entre os dois lados conhecidos.
