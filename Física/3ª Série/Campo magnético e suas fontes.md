# BL1_Capítulo 1 — Campo magnético e suas fontes

> Abra a bússola do celular: a agulha aponta para o norte. Como ela "sabe"? E por que aponta para um norte que não é o do mapa — desviando cerca de 21° para oeste em São Paulo? O que é esse campo invisível, e por que a Terra inteira age como um ímã gigante?

---

## 1. Ímãs e campo magnético

Em 1600, **William Gilbert** (1544–1603) esculpiu uma esfera de magnetita — a *terrella* — e viu a agulha se comportar sobre ela como bússola no planeta. A conclusão do *De Magnete*: **a Terra é um grande ímã**.

### 1.1 Polos inseparáveis

Todo ímã tem **norte** e **sul**, e eles não se separam:

- cortado ao meio, surgem **dois ímãs completos**, cada um com os dois polos;
- a divisão se repete até a escala atômica com o mesmo resultado;
- nunca se observou um **monopolo magnético**.

Nisso o magnetismo difere da eletricidade, em que cargas positivas e negativas existem separadamente.

### 1.2 O vetor campo magnético

**Campo magnético** ($$\vec{B}$$) — grandeza vetorial atribuída a cada ponto do espaço, em **tesla (T)**. O gauss (G) ainda aparece em catálogos:

$$1\,\mathrm{T} = 10^{4}\,\mathrm{G}$$

| | Linhas de campo elétrico | Linhas de campo magnético |
|---|---|---|
| Começam e terminam | em cargas | **em lugar nenhum** |
| Forma | abertas | curvas **fechadas** |
| Dentro do ímã | — | continuam, do sul ao norte |

<!-- tikz:inicio fig-01-linhas-de-campo-do-ima -->
![Linhas fechadas de campo saindo do polo norte e retornando ao polo sul pelo interior do ímã](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/campo-magnetico-e-suas-fontes/fig-01-linhas-de-campo-do-ima.png)
<!-- tikz:fim fig-01-linhas-de-campo-do-ima -->

Linhas sem início nem fim traduzem geometricamente a inexistência de monopolos.

### 1.3 Ordens de grandeza

Referências para julgar qualquer valor de $$B$$:

| Fonte | Campo aproximado |
|---|---|
| Campo terrestre | 25–65 µT |
| Ímã de geladeira | 5 mT |
| Ímã de neodímio | 0,2–1,4 T |
| Aparelho de ressonância magnética | 1,5–3 T |

---

## 2. O campo magnético da Terra

A bússola nunca aponta para onde o mapa diz: em São Paulo o desvio chega a 21° para oeste.

### 2.1 A Terra como dipolo

O campo terrestre é um **dipolo magnético**, como um ímã em barra no interior do planeta:

- **inclinado ~11°** em relação ao eixo de rotação — daí a discrepância entre os dois nortes;
- 25 a 65 µT conforme a latitude; no Brasil ~23 µT, pela **Anomalia do Atlântico Sul**.

<!-- tikz:inicio fig-02-terra-como-dipolo-inclinado -->
![Eixo geográfico da Terra e eixo do dipolo magnético separados por cerca de onze graus](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/campo-magnetico-e-suas-fontes/fig-02-terra-como-dipolo-inclinado.png)
<!-- tikz:fim fig-02-terra-como-dipolo-inclinado -->

> 📏 **Medidas Impressionantes:**  
> A Anomalia do Atlântico Sul obriga satélites em órbita baixa a desligar instrumentos sensíveis ao cruzá-la, por causa da radiação que o campo enfraquecido deixa passar.

### 2.2 O detalhe que confunde

A ponta "norte" da bússola é atraída pelo norte geográfico — logo o que existe lá é, magneticamente, um **polo sul**. Nomenclatura histórica, que não muda.

### 2.3 Declinação e inclinação

| | Declinação | Inclinação |
|---|---|---|
| Ângulo entre | os dois nortes | campo e plano horizontal |
| Exemplo | 21° em São Paulo | ~0° no equador, ~90° nos polos |

<!-- tikz:inicio fig-03-declinacao-e-inclinacao -->
![Vista horizontal da declinação e vista vertical da inclinação do campo magnético](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/campo-magnetico-e-suas-fontes/fig-03-declinacao-e-inclinacao.png)
<!-- tikz:fim fig-03-declinacao-e-inclinacao -->

### 2.4 Shen Kuo e a primeira medida

Por volta de 1088, o chinês **Shen Kuo** (1031–1095) registrou que a agulha "aponta para o sul, mas com desvio para leste" — primeira descrição conhecida da declinação.

---

## 3. Campo de um fio retilíneo

Depois de 1820 ficou claro que corrente elétrica também produz campo. O caso mais simples é o fio reto e longo.

### 3.1 A expressão do campo

$$B_{fio} = \frac{\mu_0 \cdot I}{2\pi \cdot r}$$

- $$B$$ — campo (T) · $$I$$ — corrente (A) · $$r$$ — distância ao fio (m);
- $$\mu_0 = 4\pi \times 10^{-7}\,\mathrm{T \cdot m/A}$$ — permeabilidade magnética do vácuo.

Duas leituras: o campo é proporcional à corrente e **inversamente proporcional à distância** — dobrar $$r$$ reduz $$B$$ à metade.

### 3.2 Geometria e sentido

As linhas não apontam para o fio nem para longe dele: são **círculos concêntricos** em planos perpendiculares ao fio, por simetria cilíndrica.

**Regra da mão direita** — polegar no sentido da corrente convencional; os dedos, ao se curvarem, dão o sentido de $$\vec{B}$$.

<!-- tikz:inicio fig-04-campo-ao-redor-do-fio -->
![Fio com corrente e linhas circulares de campo orientadas pela regra da mão direita](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/campo-magnetico-e-suas-fontes/fig-04-campo-ao-redor-do-fio.png)
<!-- tikz:fim fig-04-campo-ao-redor-do-fio -->

📝 **Fio com 10 A, a 5 cm dele**

$$B = \frac{4\pi \times 10^{-7} \cdot 10}{2\pi \cdot 0{,}05} = 4 \times 10^{-5}\,\mathrm{T} = 40\,\mathrm{\mu T}$$

Mesma ordem do campo terrestre — daí a bússola perto de um fio com corrente sair do rumo.

---

## 4. Espira e solenoide

O fio reto produz campo espalhado. Enrolá-lo faz as contribuições de cada trecho se somarem na mesma região.

### 4.1 Espira circular

$$B_{centro} = \frac{\mu_0 \cdot I}{2R}$$

- **inversamente proporcional ao raio** — espiras menores concentram mais campo;
- o campo no centro é **perpendicular ao plano** da espira;
- a espira se comporta como um pequeno ímã, com face norte e face sul.

<!-- tikz:inicio fig-05-campo-da-espira -->
![Espira com corrente e vetor campo perpendicular ao plano no centro](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/campo-magnetico-e-suas-fontes/fig-05-campo-da-espira.png)
<!-- tikz:fim fig-05-campo-da-espira -->

📝 **Espira de 5 cm de raio com 2 A**

$$B_{centro} = \frac{4\pi \times 10^{-7} \cdot 2}{2 \cdot 0{,}05} \approx 2{,}5 \times 10^{-5}\,\mathrm{T}$$

### 4.2 Solenoide

**Solenoide** — fio enrolado em espiras justapostas ao longo de um cilindro.

$$B_{sol} = \mu_0 \cdot n \cdot I$$

- $$n = N/L$$ — espiras por metro · $$N$$ — total de espiras · $$L$$ — comprimento (m).

No modelo ideal (solenoide infinitamente longo):

- campo interno **uniforme** — mesma intensidade, direção e sentido;
- campo externo praticamente **nulo**;
- o **raio não aparece** na expressão: não importa a espessura nem a posição interna.

<!-- tikz:inicio fig-06-campo-do-solenoide -->
![Solenoide com linhas internas paralelas e campo externo semelhante ao de um ímã](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/campo-magnetico-e-suas-fontes/fig-06-campo-do-solenoide.png)
<!-- tikz:fim fig-06-campo-do-solenoide -->

> ⏸️ **Pare e Pense:**  
> Para dobrar o campo interno de um solenoide, você poderia dobrar a corrente. Que outra alteração produziria o mesmo efeito?

Suas linhas de campo são idênticas às de um ímã em barra: é o modelo idealizado de qualquer **eletroímã**.

---

## 5. Corrente elétrica como fonte de campo

Por dois séculos, eletricidade e magnetismo foram estudados como fenômenos independentes. Uma aula em Copenhagen desfez isso.

### 5.1 A experiência de Oersted

Em **21 de abril de 1820**, o dinamarquês **Hans Christian Ørsted** (1777–1851) fechou o circuito de uma pilha diante de uma bússola. A agulha girou — e não foi atraída para o fio: posicionou-se **perpendicularmente** a ele, indicando campo em círculos ao redor do condutor.

<!-- tikz:inicio fig-07-experiencia-de-oersted -->
![Fio ligado a uma pilha desviando a agulha de uma bússola próxima](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/campo-magnetico-e-suas-fontes/fig-07-experiencia-de-oersted.png)
<!-- tikz:fim fig-07-experiencia-de-oersted -->

### 5.2 O que a agulha provou

- **corrente elétrica produz campo magnético**;
- os dois fenômenos são manifestações de uma mesma coisa — a primeira unificação experimental;
- o magnetismo dos ímãs passou a ser entendido como correntes microscópicas na matéria.

> 💡 **Você sabia?**  
> Em poucos meses após a notícia de 1820, Ampère formulou a descrição matemática do fenômeno — uma das reações mais rápidas da história da Física a um resultado experimental.

Se corrente gera campo, é possível **ligar, desligar e regular** um campo magnético — impossível com ímã permanente. Daí nasceram o eletroímã, o motor elétrico e o telégrafo.

---

## 6. Eletroímãs e aplicações

O guindaste de ferro-velho levanta uma tonelada de sucata e a solta no ponto exato — nenhum ímã permanente faria isso.

### 6.1 Como funciona

**Eletroímã** — solenoide com **núcleo ferromagnético** (em geral ferro doce) no interior.

Três fatores aumentam a intensidade: mais espiras por metro, mais corrente, núcleo de material adequado.

| | Ímã permanente | Eletroímã |
|---|---|---|
| Campo | fixo | ligado, desligado e regulado |
| Ao cortar a corrente | — | o campo praticamente desaparece |

### 6.2 Onde aparecem

| Aplicação | Como usa o eletroímã |
|---|---|
| **Ressonância magnética** | bobinas supercondutoras geram 1,5 a 3 T |
| **Relés e travas** | um eletroímã move um contato; a fechadura abre pelo interfone |
| **Tarja magnética** | informações gravadas como regiões magnetizadas |

> ⚡ **Física no Dia a Dia:**  
> Guardar o cartão de tarja junto a um ímã de bolsa pode apagar os dados gravados — a magnetização das regiões é reescrita.

### 6.3 O polo que se move

O polo norte magnético **se desloca cerca de 50 km por ano** em direção à Sibéria, com deriva acelerando desde o século passado.

Por isso o **World Magnetic Model** (NOAA) é atualizado a cada cinco anos. Sem essa correção, a bússola do celular acumularia erro — ela aponta para um norte que se move.
