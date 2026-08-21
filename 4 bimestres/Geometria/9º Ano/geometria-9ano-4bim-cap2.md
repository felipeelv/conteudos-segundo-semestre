# Capítulo 2 — Aplicações e problemas integrados

> Como um drone a 100 m de altura calcula em segundos a distância até uma torre, como uma cidade dimensiona uma cisterna para 50 famílias, e como os bombeiros estimam o volume de um edifício em chamas? Nenhum problema real se resolve com uma ferramenta só.

---

## 1. Aplicações da trigonometria

Um drone, o solo e o ponto observado formam um triângulo retângulo que transforma um ângulo em distâncias inacessíveis.

### 1.1 Modelagem pela figura

O procedimento trigonométrico separa quatro decisões:

- representar horizontais e verticais como catetos perpendiculares;
- identificar o ângulo conhecido;
- nomear cateto oposto, adjacente e hipotenusa;
- escolher seno, cosseno ou tangente conforme os lados envolvidos.

Ângulo de **elevação** parte da horizontal para cima; o de **depressão**, da horizontal para baixo. Largura de rio, altura de torre e navegação usam esse modelo.

O polímata **Al-Biruni (973–1048)** mediu o raio terrestre por um método trigonométrico baseado na altura de uma montanha e no ângulo de depressão do horizonte.

### 1.2 Drone e torre

**Distância observada por um drone**

Um drone está $$100\,\mathrm{m}$$ acima da base de uma torre e observa essa base sob ângulo de depressão de $$30^{\circ}$$.

**Resolução:**

- **Passo 1:** Usar a tangente para a distância horizontal $$x$$.

$$\mathrm{tg}\,30^{\circ}=\frac{100}{x}$$

$$\frac{\sqrt{3}}{3}=\frac{100}{x}$$

$$x=100\sqrt{3}\,\mathrm{m}$$

- **Passo 2:** Aplicar Pitágoras à linha de visão $$d$$.

$$d^2=100^2+(100\sqrt{3})^2$$

$$d^2=40\,000\,\mathrm{m^2}$$

$$d=200\,\mathrm{m}$$

**Resposta:** a distância horizontal é $$100\sqrt{3}\,\mathrm{m}$$, aproximadamente $$173{,}2\,\mathrm{m}$$, e a linha de visão mede $$200\,\mathrm{m}$$.

> 🔢 **Padrão:**  
> A razão trigonométrica é escolhida pelos lados conhecidos e procurados, não pela aparência do desenho.

---

## 2. Aplicações de áreas e volumes

Uma cisterna comunitária precisa armazenar água suficiente e caber no orçamento de impermeabilização.

### 2.1 Capacidade e atendimento

Prismas usam $$V=A_bh$$; cilindros usam $$V=\pi r^2h$$. O resultado cúbico converte-se por:

| Volume | Capacidade |
|---|---|
| $$1\,\mathrm{cm^3}$$ | $$1\,\mathrm{mL}$$ |
| $$1\,\mathrm{dm^3}$$ | $$1\,\mathrm{L}$$ |
| $$1\,\mathrm{m^3}$$ | $$1000\,\mathrm{L}$$ |

Dividir a capacidade pelo consumo diário indica por quanto tempo a reserva atende ao grupo.

O dimensionamento também separa volume geométrico e capacidade útil: reservatórios não devem operar até a borda. No orçamento, uma tampa acrescenta outra base à área; um tanque aberto usa apenas o fundo e as paredes. Assim, formato, segurança e material interferem na decisão.

### 2.2 Material e custo

**Cisterna de uma comunidade**

Uma cisterna aberta mede $$4\,\mathrm{m}$$ por $$2\,\mathrm{m}$$ por $$2{,}5\,\mathrm{m}$$. Cinquenta famílias consomem juntas $$20\,000\,\mathrm{L}$$ ao dia. A impermeabilização custa R$ 50,00 por metro quadrado.

**Resolução:**

- **Passo 1:** Calcular volume e capacidade.

$$V=4\cdot2\cdot2{,}5$$

$$V=20\,\mathrm{m^3}$$

$$20\,\mathrm{m^3}=20\,000\,\mathrm{L}$$

- **Passo 2:** Somar piso e quatro paredes.

$$A=4\cdot2+2\cdot4\cdot2{,}5+2\cdot2\cdot2{,}5$$

$$A=38\,\mathrm{m^2}$$

- **Passo 3:** Calcular o custo.

$$C=38\cdot50$$

$$C=\mathrm{R\$}\,1900{,}00$$

**Resposta:** a cisterna armazena $$20\,000\,\mathrm{L}$$, atende por 1 dia e custa R$ 1.900,00 para impermeabilizar internamente.

> ⚠️ **Atenção:**  
> Material de revestimento depende de área, enquanto água armazenada depende de volume.

---

## 3. Problemas geométricos integrados

Numa vistoria aérea, a vista superior fornece a base e o ângulo de observação relaciona alturas e distâncias.

### 3.1 Decompor antes de calcular

Um problema integrado deve ser separado em subproblemas:

- construir o triângulo retângulo da observação;
- escolher a razão trigonométrica;
- completar uma distância com Pitágoras;
- obter área na vista superior;
- usar essa base no volume espacial;
- verificar unidades e coerência de cada etapa.

Essa sequência liga o plano ao espaço sem misturar as grandezas.

### 3.2 Vistoria de um edifício

**Drone sobre um edifício**

Um drone voa a $$100\,\mathrm{m}$$ do solo. A distância horizontal até a borda do teto é $$60\,\mathrm{m}$$ e o ângulo de depressão é $$45^{\circ}$$. A planta do edifício mede $$30\,\mathrm{m}$$ por $$20\,\mathrm{m}$$.

**Resolução:**

- **Passo 1:** Usar a tangente para a diferença de alturas $$q$$.

$$\mathrm{tg}\,45^{\circ}=\frac{q}{60}$$

$$q=60\,\mathrm{m}$$

- **Passo 2:** Obter a altura do edifício.

$$h=100-60$$

$$h=40\,\mathrm{m}$$

- **Passo 3:** Calcular a linha de visão $$d$$ por Pitágoras.

$$d^2=60^2+60^2$$

$$d=60\sqrt{2}\,\mathrm{m}$$

- **Passo 4:** Calcular a base e o volume.

$$A_b=30\cdot20$$

$$A_b=600\,\mathrm{m^2}$$

$$V=600\cdot40$$

$$V=24\,000\,\mathrm{m^3}$$

**Resposta:** o edifício tem $$40\,\mathrm{m}$$ de altura, linha de visão de $$60\sqrt{2}\,\mathrm{m}$$ e volume modelado de $$24\,000\,\mathrm{m^3}$$.

> 🔢 **Padrão:**  
> Verificar cada subresultado evita que um erro trigonométrico contamine o cálculo espacial seguinte.
