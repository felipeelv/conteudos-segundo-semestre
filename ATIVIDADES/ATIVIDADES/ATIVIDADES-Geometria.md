# Atividades — Geometria

> 6º ao 9º ano EF · 1ª e 2ª séries EM · 12 capítulos · 3º bimestre
> Rubricas: `../METODOLOGIA/04-RUBRICAS.md` · códigos de tipo: `../METODOLOGIA/03-REPERTORIO.md` · metodologia completa: `../METODOLOGIA/00-LEIA-ME.md`

---

## Diagnóstico rápido

Geometria é a disciplina do bimestre em que a lista de exercícios é **menos** justificável, por uma razão estrutural: cada subseção do capítulo termina em um exemplo resolvido com `Passo 1 / Passo 2 / Passo 3` e `Resposta`. Um exercício com a mesma estrutura do exemplo mede a capacidade de copiar o modelo da página anterior.

O segundo problema é que **todas as figuras vêm prontas** (imagens TikZ hospedadas no repositório). O aluno nunca constrói. Em Geometria, isso é grave: van Hiele (1986) situa a passagem do reconhecimento visual para a descrição de propriedades e daí para a dedução informal justamente na atividade de construir e conferir.

O repertório, então, se organiza em quatro tipos:

- **CONS** — construção com compasso, régua, malha, recorte e planificação. É o tipo dominante. A propriedade se mostra construindo.
- **MOD** — problema com decisão: qual embalagem gasta menos material, qual formato cerca mais área, quanto piso comprar contando a perda. Modelagem no sentido de Blum & Leiss (2007).
- **ERR** — análise de resolução errada. A Geometria escolar tem erros altamente previsíveis (usar o lado oblíquo como altura, converter m² como se fosse m, trocar cateto oposto e adjacente ao mudar o ângulo). Cury (2007) mostra que analisar o erro alheio é mais diagnóstico que evitar o próprio.
- **EX** — mantido, mas reduzido a **um bloco por capítulo**, sempre com um item que exija escolher a expressão ou justificar o procedimento.

Carga: 2 capítulos por ano/série, com 3 seções cada. As atividades são curtas e encadeadas.

---

# 6º Ano

## Bloco 1 · Capítulo 1 — Quadriláteros e circunferência

**Conteúdo:** elementos, ângulos e famílias de quadriláteros · inclusão de classes (a placa quadrada é quadrado, retângulo, losango e paralelogramo) · Adrien-Marie Legendre (1752–1833) · lados e ângulos do paralelogramo · diagonais · circunferência e círculo, linha e região · a razão constante entre comprimento e diâmetro.

### Atividade principal — A árvore das famílias
**Tipo:** CONS · **Tempo:** 1 aula · **Formato:** duplas

**Objetivo:** a inclusão de classes é o ponto mais difícil do capítulo e o mais mal avaliado por exercício. "Todo quadrado é retângulo" soa falso para o aluno de 6º ano, e a única forma de convencê-lo é fazê-lo classificar peças físicas por propriedade.

**Materiais:** 8 quadriláteros recortados em papel-cartão (quadrado, retângulo não quadrado, losango não quadrado, paralelogramo comum, trapézio isósceles, trapézio retângulo, trapézio escaleno, quadrilátero irregular), régua e esquadro.

**Comando para o aluno:**
> "**(a)** Meçam os lados, os ângulos e as diagonais das 8 peças e registrem numa tabela.
> **(b)** Desenhem numa folha grande três regiões encaixadas, uma dentro da outra, e coloquem cada peça na região certa: **quadriláteros** ⊃ **paralelogramos** ⊃ ... vocês decidem as regiões internas.
> **(c)** Respondam com as peças na mão, não de memória:
> - Todo quadrado é retângulo? Mostrem com as medidas.
> - Todo retângulo é quadrado? Mostrem a peça que responde.
> - Existe peça que é losango e retângulo ao mesmo tempo? Qual?
> **(d)** Escrevam a **propriedade mínima** que uma peça precisa ter para entrar em cada região que vocês desenharam."

**Rubrica:** R2 adaptada — *conceitos presentes* (3) passa a ser peças corretamente medidas; *ligações nomeadas* (4) passa a ser a propriedade mínima do item (d); *hierarquia* (2) é o encaixe correto das regiões; legibilidade (1). Encaixe correto com item (d) em branco tem no máximo 6.

### Complementares
- **CONS · 30 min ·** Descobrir π: medir com fita o contorno e o diâmetro de cinco objetos redondos (lata, tampa, moeda, prato, cesto), calcular a razão contorno÷diâmetro em cada caso e comparar os cinco resultados. Responder: por que os cinco valores são parecidos e não iguais? — *Rubrica R1, com os 3 pontos de registro medindo a tabela de medições.*
- **ERR · 20 min ·** Cinco afirmações para julgar como verdadeiras ou falsas, com **contraexemplo desenhado** quando falsas: "todo losango é quadrado"; "todo quadrado é losango"; "as diagonais de todo paralelogramo são iguais"; "as diagonais de todo paralelogramo se cortam ao meio"; "circunferência e círculo são a mesma coisa". — *Rubrica R11.*

---

## Bloco 2 · Capítulo 1 — Área de figuras planas

**Conteúdo:** área não é perímetro · área do retângulo e do quadrado · área do paralelogramo · área do triângulo · área do trapézio · malha e decomposição · comparação de áreas.

### Atividade principal — Vinte centímetros de barbante
**Tipo:** MOD · **Tempo:** 1 aula · **Formato:** duplas

**Objetivo:** o capítulo abre com "área não é perímetro" e prova isso com um exemplo. Esta atividade transforma a frase em descoberta: mesmo perímetro, áreas muito diferentes.

**Materiais:** barbante de 20 cm por dupla, malha quadriculada de 1 cm.

**Comando para o aluno:**
> "Com o barbante de 20 cm formem, sobre a malha, **todos** os retângulos possíveis de lados inteiros. Preencham a tabela:
> | Base (cm) | Altura (cm) | Perímetro (cm) | Área (cm²) |
> |---|---|---|---|
>
> **(a)** Quantos retângulos diferentes vocês encontraram?
> **(b)** O perímetro mudou de um para outro?
> **(c)** Qual deles tem a **maior** área? Qual tem a menor?
> **(d)** Construam um gráfico de barras com a área de cada retângulo. O que o gráfico mostra?
> **(e)** Se o barbante pudesse formar qualquer figura, e não só retângulos, qual formato daria a maior área possível com 20 cm de contorno? Testem com o barbante e digam o que vocês observaram."

**Rubrica:** R12, com ajuste — o item (e) vale 2 dos 10 pontos e não exige a resposta exata: exige que a dupla teste e descreva. Os 3 pontos de *interpretação no contexto* estão em (c) e (d).

### Complementares
- **EX · 35 min ·** Seis áreas para calcular: retângulo, quadrado, paralelogramo (com altura dada e lado oblíquo como distrator), triângulo, trapézio e uma figura na malha. Dois dos seis exigem conversão de unidade. Um item pede que o aluno **escreva qual expressão escolheu e por quê**. — *Rubrica R1.*
- **CONS · 25 min ·** Uma figura irregular na malha quadriculada. Calcular sua área por **duas** decomposições diferentes (por exemplo: dividindo em retângulo + triângulos; e completando um retângulo maior e subtraindo). Comparar os dois resultados e explicar por que precisam coincidir. — *Rubrica R1, com os 3 pontos de registro medindo as duas estratégias desenhadas.*

---

## Atividade integradora — 6º ano
### A reforma da nossa sala
**Tipo:** MOD · **Tempo:** 2 aulas · **Formato:** grupos de 4

**Comando para o aluno:**
> "Vamos orçar a reforma da sala.
> **1.** Meçam o piso e as quatro paredes e desenhem a planta na malha, com escala indicada.
> **2.** Calculem a área do piso e a área total a pintar — descontando portas e janelas, que também devem ser medidas.
> **3.** Uma lata de tinta cobre 40 m². Quantas latas? Sobra tinta? Quanto?
> **4.** O piso é vendido em caixas de 2 m². Quantas caixas, considerando **10% de perda** no corte?
> **5.** Calculem o perímetro do rodapé.
> **6.** Uma frase final: qual medida vocês tiveram mais dificuldade de obter, e o que fizeram para resolver?"

**Rubrica:** R12. O item 4 sem a perda de 10% perde 2 pontos; o item 2 sem descontar portas e janelas perde 2.

---

# 7º Ano

## Bloco 1 · Capítulo 1 — Circunferência e círculo

**Conteúdo:** circunferência como lugar geométrico dos pontos a distância *r* de um centro · o compasso materializa a definição · posições de um ponto · posições de uma reta (secante, tangente, externa) · comprimento da circunferência e o número π como constante irracional · as duas formas da fórmula.

### Atividade principal — Cinco construções com compasso
**Tipo:** CONS · **Tempo:** 2 aulas · **Formato:** individual

**Objetivo:** "lugar geométrico" é a ideia mais poderosa e mais abstrata do capítulo. Ela só se sustenta se o aluno usar o compasso como o instrumento que **materializa a condição**, e não como um desenhador de bolinhas.

**Comando para o aluno:**
> "Faça as cinco construções abaixo. Ao lado de cada uma, escreva em uma frase **qual condição** os pontos que você traçou cumprem.
> **1.** Uma circunferência de raio 4 cm. Marque três pontos sobre ela, um interno e um externo, e verifique cada classificação com o compasso.
> **2.** Uma reta **secante** a essa circunferência. Quantos pontos em comum?
> **3.** Uma reta **tangente** a ela. Meça o ângulo entre essa reta e o raio no ponto de contato. Qual valor você encontrou?
> **4.** Duas circunferências **tangentes externamente**, e depois duas **secantes**. Compare a distância entre os centros com a soma dos raios em cada caso.
> **5.** Uma circunferência que passe por **três** pontos dados que você mesmo marcou. Descreva como conseguiu — e responda: e se os três pontos estivessem alinhados?"

**Rubrica:** R1, com ajuste — as frases de condição valem 4 dos 10 pontos (substituindo o critério de resposta correta). A construção 5 vale 2 e a pergunta final dela, 1. Cinco construções perfeitas sem as frases têm no máximo 5.

### Complementares
- **INV · 30 min ·** π com erro medido: medir contorno e diâmetro de oito objetos redondos, calcular a razão em cada, calcular a média das oito e o erro percentual em relação a 3,14159. Responder: a média ficou mais perto do valor real que a maioria das medições isoladas? Por quê? — *Rubrica R8.*
- **EX · 30 min ·** Cinco itens sobre comprimento: dados *r*, calcular *C*; dado *d*, calcular *C*; dado *C*, achar *r*; quantas voltas uma roda dá em 100 m; e um item que peça para explicar por que as duas formas da fórmula (*C* = 2π*r* e *C* = π*d*) são a mesma. — *Rubrica R1.*

---

## Bloco 2 · Capítulo 1 — Área e perímetro

**Conteúdo:** dimensões diferentes de área e de perímetro · conversões e expressões · área de quadriláteros · área de triângulos · área do círculo pela transformação em quase-retângulo · figuras compostas e equivalência.

### Atividade principal — Cercar a horta com o que temos
**Tipo:** MOD · **Tempo:** 2 aulas · **Formato:** duplas

**Objetivo:** decidir o formato a partir de uma restrição é o que separa modelagem de exercício. E aqui o resultado é contraintuitivo: o círculo ganha.

**Comando para o aluno:**
> "A escola tem **40 metros** de tela e quer cercar a maior horta possível.
> **(a)** Calculem a área obtida com cada formato abaixo, usando os 40 m inteiros de contorno:
> - quadrado
> - retângulo 15 m × 5 m
> - retângulo 12 m × 8 m
> - triângulo equilátero
> - círculo
> **(b)** Organizem os cinco resultados em ordem crescente de área. Qual formato aproveita melhor a tela?
> **(c)** Entre os três retângulos (incluindo o quadrado), qual é o padrão? Enunciem-no em uma frase.
> **(d)** O círculo ganhou. Mas a horta precisa de canteiros retos para o plantio. Proponham um formato de compromisso e calculem a área dele.
> **(e)** Convertam a área vencedora para cm² e para hectares. Uma das duas conversões costuma dar errado — expliquem qual e por quê."

**Rubrica:** R12, com ajuste — o item (e) vale 2 dos 10 pontos e é o teste dimensional. O item (d) vale 2 e aceita qualquer solução defensável, desde que a área esteja calculada corretamente.

### Complementares
- **ERR · 25 min ·** "Um estudante escreveu: *'A sala tem 3 m por 4 m, então tem 12 m² = 1 200 cm².'* Localize o erro, explique por que a conversão de área não é igual à de comprimento, e apresente o valor correto. Depois, faça o mesmo com: *'um terreno de 2 km² tem 2 000 m².'*" — *Rubrica R11.*
- **CONS · 30 min ·** Do círculo ao quase-retângulo: recortar um círculo de raio 6 cm em 12 setores iguais, reorganizá-los alternadamente formando uma figura próxima de um retângulo, colar e medir a base e a altura da figura obtida. Responder: a base ficou próxima de quê? A altura ficou próxima de quê? Como isso justifica *A* = π*r*²? — *Rubrica R4.*

---

## Atividade integradora — 7º ano
### A praça da escola
**Tipo:** MOD + CONS · **Tempo:** 2 aulas · **Formato:** grupos de 4

**Comando para o aluno:**
> "Projetem uma praça de **20 m × 15 m** contendo obrigatoriamente: um canteiro circular, um deque retangular, um caminho e um espaço triangular.
> **1.** Desenhem a planta na malha, com escala indicada. O canteiro circular precisa ser traçado com compasso.
> **2.** Calculem a área de cada elemento e a área livre restante.
> **3.** Calculem o perímetro do canteiro circular (é o comprimento da guia de concreto) e o do deque.
> **4.** O caminho tem 1,2 m de largura e liga dois cantos opostos. Calculem sua área.
> **5.** A grama custa por m² e a guia de concreto por metro linear. Com preços que vocês definirem, apresentem o orçamento total.
> **6.** Uma frase: em qual elemento vocês usaram área e em qual usaram perímetro? Por que não se pode trocar um pelo outro no orçamento?"

**Rubrica:** R12 (70%) + R10 para a planta (30%). O item 6 é obrigatório: sem ele, a nota máxima é 7.

---

# 8º Ano

## Bloco 1 · Capítulo 1 — Transformações geométricas

**Conteúdo:** transformação geométrica e isometria (preserva comprimentos, ângulos e áreas) · translação e vetor · procedimento de construção · reflexão pelo eixo · rotação pelo centro · composição de transformações e ordem das operações · tesselações.

### Atividade principal — Uma tesselação e sua receita
**Tipo:** CONS · **Tempo:** 2 aulas · **Formato:** duplas

**Objetivo:** tesselação é o único conteúdo do capítulo que exige compor transformações. E a **receita** — a descrição exata dos parâmetros — é o que revela se o aluno sabe o que cada transformação faz.

**Materiais:** malha quadriculada, régua, transferidor, papel-manteiga para conferir sobreposição.

**Comando para o aluno:**
> "**(a)** Criem um módulo (uma figura de 4 a 6 lados) sobre a malha.
> **(b)** Cubram uma área de no mínimo 12 cm × 12 cm repetindo o módulo, **sem sobreposição e sem falha**, usando ao menos **duas** transformações diferentes.
> **(c)** Escrevam a **receita** da tesselação: liste, em ordem, cada transformação aplicada, com os parâmetros completos — para translação, o vetor (quantos quadrados para o lado e quantos para cima); para reflexão, qual é o eixo; para rotação, qual é o centro e qual é o ângulo.
> **(d)** Verifiquem com o papel-manteiga que a figura não mudou de tamanho em nenhuma repetição. Por que ela não muda? Usem a palavra **isometria** na resposta.
> **(e)** Troquem a receita com outra dupla. Cada dupla tem de reproduzir a tesselação da outra **apenas pela receita**, sem ver o desenho. Se não conseguirem, a receita está incompleta — anotem o que faltava."

**Rubrica:** R10, com ajuste — o item (e) é o teste da atividade e vale 3 dos 10 pontos. Uma tesselação bonita com receita que a outra dupla não conseguiu reproduzir perde esses 3 pontos, porque a descrição — não o desenho — é o objeto avaliado.

### Complementares
- **EX · 30 min ·** Aplicar as três transformações a um mesmo triângulo de lados 3, 4 e 5 sobre a malha, com parâmetros dados. Medir os lados e os ângulos da imagem em cada caso e preencher a tabela de verificação de isometria. Um item pede a coordenada exata de um vértice após cada transformação. — *Rubrica R1.*
- **ERR · 25 min ·** "Um estudante afirmou: *'Como as duas são isometrias, aplicar uma reflexão e depois uma rotação dá o mesmo resultado que aplicar a rotação e depois a reflexão.'* Teste a afirmação na malha com uma figura assimétrica e os parâmetros que você escolher. Depois explique por que a afirmação é falsa e por que o fato de as duas serem isometrias não garante o que ele concluiu." — *Rubrica R11.*

---

## Bloco 2 · Capítulo 1 — Áreas de figuras planas

**Conteúdo:** escolha da expressão para cada quadrilátero · aplicação em terreno (lote trapezoidal) · área do triângulo como metade do paralelogramo · medida de cobertura (telhado) · composição e decomposição de figuras · área, rendimento e perda.

### Atividade principal — Orçamento com perda
**Tipo:** MOD · **Tempo:** 2 aulas · **Formato:** duplas

**Objetivo:** o capítulo tem uma subseção chamada "área, rendimento e perda" e a resolve em um exemplo. Esta atividade a converte em decisão: comprar a mais é desperdício, comprar a menos para a obra.

**Insumo:** a planta de um telhado composto por duas faces trapezoidais e duas triangulares, com todas as medidas indicadas. Rendimento da telha: 12 telhas por m². Perda estimada em cortes: 8%. A telha é vendida em pacotes de 25.

**Comando para o aluno:**
> "**(a)** Calculem a área de cada uma das quatro faces, indicando **qual expressão** vocês escolheram e por quê. Cuidado: em uma delas há uma medida que não serve para o cálculo.
> **(b)** Calculem a área total do telhado.
> **(c)** Calculem o número de telhas necessárias sem perda.
> **(d)** Acrescentem os 8% de perda e digam quantos pacotes de 25 devem ser comprados.
> **(e)** Quantas telhas sobram? Isso é problema? Justifiquem.
> **(f)** Um pedreiro diz: 'compra 10% a mais e não erra'. Calculem quanto isso custaria a mais e digam em que situação o conselho dele se justifica."

**Rubrica:** R12, com ajuste — o distrator do item (a) (a medida que não serve, tipicamente o lado oblíquo oferecido como se fosse altura) vale 2 dos 10 pontos. O item (d) sem arredondar **para cima** ao número inteiro de pacotes perde 2 pontos: uma obra não compra 7,4 pacotes.

### Complementares
- **ERR · 25 min ·** Uma resolução completa e errada, fornecida pelo professor, em que a área de um paralelogramo foi calculada multiplicando os dois **lados** em vez de base × altura. Localizar o passo, explicar por que é erro (com desenho mostrando a diferença entre lado oblíquo e altura), refazer, e escrever a regra geral de cuidado. — *Rubrica R11.*
- **EX · 30 min ·** Seis áreas: dois quadriláteros, dois triângulos, uma figura composta por decomposição e uma por complementação e subtração. Em cada item, escrever a expressão escolhida antes de calcular. Um item traz duas figuras diferentes de mesma área — pedir que verifiquem. — *Rubrica R1.*

---

## Atividade integradora — 8º ano
### Piso padronizado, orçamento real
**Tipo:** CONS + MOD · **Tempo:** 2 aulas · **Formato:** grupos de 4

**Comando para o aluno:**
> "**Parte 1 — projeto.** Criem um padrão de piso por tesselação, usando ao menos duas transformações, e escrevam a receita completa. O módulo é uma peça que existirá de fato.
> **Parte 2 — orçamento.** Um espaço real da escola (corredor, sala ou quadra) será revestido com esse padrão. Meçam o espaço, desenhem a planta com escala, calculem a área, o número de módulos e acrescentem a perda de corte que vocês estimarem — justificando a porcentagem escolhida pelo formato do módulo.
> **Parte 3 — comparação.** Um módulo quadrado gera menos perda que um módulo hexagonal ou triangular. Calculem a perda dos **dois** casos no seu espaço e digam quanto o padrão mais interessante custa a mais.
> **Parte 4 — recomendação.** Uma página: qual dos dois vocês recomendam à escola, com a diferença de custo e a razão."

**Rubrica:** R10 para o padrão e a planta (40%) + R12 para o orçamento e a comparação (60%). A Parte 3 sem os dois cálculos limita a nota a 6.

---

# 9º Ano

## Bloco 1 · Capítulo 1 — Trigonometria no triângulo retângulo

**Conteúdo:** os lados em relação ao ângulo · semelhança pelo caso AA e independência das razões em relação ao tamanho · seno, cosseno e tangente · tg θ = sen θ / cos θ · Hiparco de Niceia (c. 190–c. 120 a.C.) · valores notáveis de 30°, 45° e 60° e os dois triângulos de origem · relação fundamental sen²θ + cos²θ = 1 · sen θ = cos(90° − θ) · ângulos de elevação e de depressão · resolução de triângulos.

### Atividade principal — Medir a altura da escola sem subir nela
**Tipo:** INV + MOD · **Tempo:** 2 aulas · **Formato:** grupos de 4

**Objetivo:** é a atividade que a pergunta de abertura do capítulo promete e que o capítulo não entrega. Construir o instrumento e obter um número com erro é o que fixa a ideia de que a razão trigonométrica não depende do tamanho do triângulo.

**Materiais:** transferidor de 180°, canudo ou tubo de caneta, linha, peso pequeno (porca, borracha), fita adesiva, trena ou fita métrica.

**Comando para o aluno:**
> "**Etapa 1 — construir o clinômetro.** Colem o canudo na borda reta do transferidor e amarrem a linha com o peso no centro dele. Ao olhar pelo canudo, a linha marca no transferidor um ângulo — o **complemento** do ângulo de elevação. Registrem como vocês converteram a leitura no ângulo de elevação.
> **Etapa 2 — medir.** Escolham um alvo alto (prédio, poste, mastro, árvore). Meçam:
> - a distância horizontal do observador até a base do alvo;
> - o ângulo de elevação até o topo;
> - a altura dos olhos do observador em relação ao chão.
>
> **Etapa 3 — calcular.** Usem a tangente para achar a altura acima da linha do olhar e **somem a altura dos olhos**. Mostrem todos os passos.
> **Etapa 4 — repetir.** Refaçam a medição de uma **segunda distância**, bem diferente da primeira.
> **Etapa 5 — relatório.**
> **(a)** As duas medições deram o mesmo valor? Qual a diferença entre elas, em metros e em porcentagem?
> **(b)** Em teoria deveriam dar o mesmo resultado. Por quê? A resposta tem de usar semelhança de triângulos.
> **(c)** Citem três fontes de erro do procedimento e digam se cada uma tende a **aumentar** ou a **diminuir** a altura calculada.
> **(d)** Por que somar a altura dos olhos é indispensável? O que aconteceria se vocês esquecessem?"

**Rubrica:** R8, com ajuste — o item (b) vale 3 dos 10 pontos: é onde a semelhança AA justifica a constância da razão. O item (c) exige a **direção** do erro, não só o nome. Grupo que obtenha dois valores idênticos deve ser questionado sobre a precisão do transferidor.

### Complementares
- **EX · 35 min ·** Seis triângulos retângulos a resolver: três com valores notáveis (30°, 45°, 60°) e três com razões dadas em tabela. Dois itens usam a relação fundamental para achar o cosseno a partir do seno. Um item final: dado que sen 40° ≈ 0,643, obter cos 50° sem calculadora e justificar. — *Rubrica R1.*
- **ERR · 25 min ·** "Num triângulo retângulo em *A*, um estudante calculou sen *B* = 3/5 e depois, ao mudar o ângulo de referência para *C*, manteve sen *C* = 3/5. Localize o erro, explique-o com a definição de cateto oposto e adjacente, e calcule os valores corretos das três razões para *B* e para *C*. Depois responda: qual relação existe entre sen *B* e cos *C*, e por quê?" — *Rubrica R11.*

---

## Bloco 2 · Capítulo 1 — Geometria espacial e representações

**Conteúdo:** posições relativas de pontos, retas e planos no espaço · relação de Euler (V − A + F = 2) · vistas ortogonais e três projeções coerentes · leitura de peça · sistema de medidas, múltiplos e submúltiplos · armazenamento digital.

### Atividade principal — Da peça às vistas, e das vistas à peça
**Tipo:** CONS · **Tempo:** 2 aulas · **Formato:** duplas

**Objetivo:** vista ortogonal se avalia nos **dois sentidos**. Desenhar as vistas de uma peça que se vê é bem mais fácil do que reconstruir a peça a partir das vistas — e é o segundo caso que revela a leitura espacial.

**Materiais:** 12 a 15 cubinhos por dupla (dado, açúcar em cubo, peças de encaixe ou cubos de papel).

**Comando para o aluno:**
> "**Parte 1 — da peça às vistas.** Montem uma peça com 8 a 12 cubinhos, com pelo menos um degrau e um recuo. Desenhem em malha as três vistas ortogonais: frontal, superior e lateral, com as medidas em unidades de cubo.
> **Parte 2 — a troca.** Entreguem **apenas as três vistas** a outra dupla, que deve remontar a peça sem ver a original. Registrem: a peça remontada ficou igual? Se não, qual vista estava ambígua?
> **Parte 3 — a ambiguidade.** É possível que duas peças diferentes tenham as mesmas três vistas. Construam um exemplo e mostrem as vistas idênticas. Depois digam qual **quarta** informação resolveria a ambiguidade.
> **Parte 4 — Euler.** Escolham um poliedro (prisma, pirâmide ou um sólido de faces planas que vocês montem), contem vértices, arestas e faces e verifiquem V − A + F. Anotem o resultado."

**Rubrica:** R10, com ajuste — a Parte 3 vale 3 dos 10 pontos e é a mais alta da atividade: encontrar duas peças com as mesmas vistas exige compreender o que a projeção descarta. A Parte 2 vale 3, com a nota atribuída pelo resultado da remontagem alheia.

### Complementares
- **EX · 25 min ·** Verificar a relação de Euler em cinco poliedros com V, A e F dados; em um sexto item, os dados não fecham em 2 — pedir que digam se o erro está na contagem ou se o sólido não pode existir, e por quê. — *Rubrica R1, com o sexto item valendo 3 dos 10 pontos.*
- **MOD · 30 min ·** Armazenamento digital: uma foto do celular do aluno tem tamanho X. Calcular quantas fotos cabem em 64 GB; quanto ocupa um vídeo de 3 minutos gravado por ele; e o total de espaço que a turma de 30 alunos gastaria para guardar 200 fotos cada. Todas as passagens entre KB, MB, GB e TB devem estar registradas. Encerrar com: por que 1 GB não são exatamente 1 000 MB nos sistemas de computação? — *Rubrica R12.*

---

## Atividade integradora — 9º ano
### Levantamento da escola
**Tipo:** INV + CONS · **Tempo:** 3 aulas · **Formato:** grupos de 4

**Comando para o aluno:**
> "O grupo entrega um dossiê técnico de um espaço da escola:
> **1. Alturas por trigonometria** — três alturas medidas com o clinômetro (prédio, poste, árvore), cada uma com duas medições independentes, o ângulo registrado, o cálculo completo e o erro entre as duas medições.
> **2. Planta em escala** — planta baixa do espaço, com escala declarada e medidas reais indicadas.
> **3. Vistas ortogonais** — as três vistas de **um** elemento construído do espaço (escada, mureta, canteiro elevado, guarita).
> **4. Conversões** — todas as medidas apresentadas em metros e em centímetros, e as áreas em m² e em cm², com as conversões demonstradas.
> **5. Nota técnica** — uma página: qual das três alturas do item 1 vocês consideram a mais confiável, e por quê. Fatores possíveis: distância medida, terreno inclinado, dificuldade de ver o topo, precisão do transferidor."

**Rubrica:** R8 para o item 1 (40%) + R10 para os itens 2 e 3 (40%) + R1 para o item 4 (20%). O item 5 é eliminatório para a faixa superior: dossiê sem análise de confiabilidade tem no máximo 7.

---

# 1ª Série

## Bloco 1 · Capítulo 1 — Circunferência

**Conteúdo:** circunferência e círculo · critério algébrico de posição de ponto · posições relativas de reta e circunferência · posições de duas circunferências · ângulo central e ângulo inscrito · a relação 2:1 e por que surge a metade · ângulo de segmento (corda e tangente) · ângulos excêntricos interior e exterior · potência de ponto e o produto constante.

### Atividade principal — Descobrir a relação 2:1 e depois prová-la
**Tipo:** CONS · **Tempo:** 2 aulas · **Formato:** duplas

**Objetivo:** este é o ponto do bimestre em que o aluno passa da constatação para a dedução — a transição de nível de van Hiele. A atividade tem as duas metades explicitamente separadas.

**Comando para o aluno:**
> "**Parte 1 — conjecturar (medindo).**
> Tracem uma circunferência de raio 5 cm e marquem um arco AB. Marquem **quatro** pontos distintos P₁, P₂, P₃, P₄ sobre o arco maior. Tracem os quatro ângulos inscritos A P B e o ângulo central A O B.
> Preencham a tabela: medida de cada ângulo inscrito · medida do ângulo central · razão entre eles.
> **(a)** O que vocês observam sobre os quatro ângulos inscritos?
> **(b)** Qual é a razão entre o central e cada inscrito? Ela se mantém?
> **(c)** Enunciem a conjectura em uma frase.
>
> **Parte 2 — provar (raciocinando).**
> Agora o caso particular em que o ponto P está posicionado de modo que o segmento PO passe pelo centro e o lado PB seja um diâmetro.
> **(d)** O triângulo AOP tem dois lados que são raios. Que tipo de triângulo é? O que isso diz sobre seus ângulos da base?
> **(e)** Chamem o ângulo inscrito em P de α. Escrevam os outros dois ângulos do triângulo AOP em função de α.
> **(f)** O ângulo central AOB é o **suplementar** de um dos ângulos que vocês escreveram. Concluam o valor de AOB em função de α.
> **(g)** Escrevam a demonstração completa deste caso em três passos numerados.
> **(h)** Vocês provaram um caso particular. Em três linhas: por que isso ainda não é a prova geral, e o que faltaria?"

**Rubrica:** R4, com ajuste — a Parte 1 vale 3 dos 10 pontos (as medições e a conjectura); o item (g) vale 4; o item (h) vale 2; organização, 1. Aluno que meça corretamente e não conclua a Parte 2 tem no máximo 4: a atividade avalia a passagem da medição para o argumento.

### Complementares
- **EX · 35 min ·** Seis ângulos a determinar numa mesma figura de circunferência com cordas e secantes: dois centrais, dois inscritos, um de segmento, um excêntrico interior e um exterior. Em cada item, indicar **qual relação** foi usada. Um item final pede a determinação de um arco a partir de dois ângulos dados. — *Rubrica R1.*
- **MOD · 30 min ·** Potência de ponto aplicada: um observador está num ponto P externo a uma pista circular e traça duas visadas que cortam a pista. Dadas três das quatro distâncias, calcular a quarta. Em seguida, o mesmo problema com uma visada tangente, usando PT² = PA · PB. Encerrar com uma frase: por que o produto é o mesmo para qualquer par de secantes traçadas de P? — *Rubrica R12.*

---

## Bloco 2 · Capítulo 1 — Áreas de figuras planas

**Conteúdo:** princípios fundamentais de área · pontos de uma rede · área do paralelogramo por recomposição · altura perpendicular · área do triângulo · caso equilátero · área do losango pelas diagonais · área do trapézio por duplicação · polígonos regulares e a passagem para o círculo · faixa circular.

### Atividade principal — Três demonstrações com tesoura
**Tipo:** CONS · **Tempo:** 2 aulas · **Formato:** duplas

**Objetivo:** o capítulo apresenta as fórmulas de área acompanhadas de justificativa (recomposição, duplicação, diagonais). Ler a justificativa é diferente de produzi-la. A tesoura força a produção.

**Materiais:** papel-cartão, tesoura, régua, cola.

**Comando para o aluno:**
> "Para cada uma das três fórmulas abaixo, vocês vão **(i)** recortar, **(ii)** recompor e **(iii)** escrever o argumento em três passos numerados.
>
> **1. Paralelogramo → retângulo (recomposição).** Recortem um paralelogramo, corte-o por uma altura, translade a parte cortada e forme um retângulo. Escrevam: por que a área não mudou? Que medida do retângulo corresponde à base do paralelogramo? E à altura? Conclusão.
> **2. Trapézio → paralelogramo (duplicação).** Recortem dois trapézios idênticos, gire um deles 180° e junte-os. Que figura resultou? Qual é a base dela em função de *B* e *b*? Por que a fórmula do trapézio tem uma divisão por 2?
> **3. Losango → retângulo (diagonais).** Recortem um losango, corte-o pelas duas diagonais e reorganize as quatro partes em um retângulo. Quais são as dimensões desse retângulo em função de *D* e *d*? Conclusão.
>
> Ao final, uma questão comum às três:
> **(a)** As três demonstrações usam o mesmo princípio. Qual? Enunciem-no.
> **(b)** Esse princípio funcionaria para provar a fórmula da área do **círculo**? Justifiquem em quatro linhas."

**Rubrica:** R4, com ajuste — os três argumentos em passos valem 6 dos 10 pontos (2 cada); o item (a) vale 2; o item (b) vale 2. Recortes corretos com argumento ausente ou apenas descritivo ("virou um retângulo") pontuam metade em cada demonstração.

### Complementares
- **MOD · 30 min ·** Um polígono irregular desenhado sobre malha com todos os vértices em pontos da rede. Calcular a área por **três** caminhos: (i) decomposição em triângulos e retângulos; (ii) complementação em um retângulo maior e subtração; (iii) contagem de pontos internos e de borda pela relação da rede. Comparar os três resultados e explicar qual foi o mais rápido e qual o mais seguro. — *Rubrica R12.*
- **EX · 30 min ·** Cinco itens: área de triângulo equilátero de lado dado; área de losango a partir das diagonais; área de trapézio; área de faixa circular entre dois raios; e área de hexágono regular por decomposição em triângulos equiláteros. Cada item exige a expressão escrita antes do cálculo. — *Rubrica R1.*

---

## Atividade integradora — 1ª série
### O vitral
**Tipo:** CONS + MOD · **Tempo:** 3 aulas · **Formato:** duplas

**Comando para o aluno:**
> "Projetem um vitral circular de 60 cm de raio, dividido em regiões coloridas.
> **1. Construção.** O desenho é feito com compasso e régua. Ele contém obrigatoriamente: uma faixa circular externa, um polígono regular inscrito, ao menos dois triângulos, um losango e um trapézio.
> **2. Ângulos.** Identifiquem no desenho um ângulo central, um ângulo inscrito e um ângulo de segmento, com suas medidas calculadas — não medidas com transferidor.
> **3. Áreas por cor.** Calculem a área de cada região colorida e verifiquem que a soma de todas é igual à área do círculo. A diferença aceitável é de 2%; se for maior, encontrem o erro.
> **4. Chumbo.** Calculem o comprimento total das linhas de chumbo entre as regiões — isto é, a soma dos contornos internos.
> **5. Orçamento.** Com preços por m² de vidro colorido e por metro de chumbo definidos por vocês, apresentem o custo.
> **6. Nota.** Meia página: qual foi a área mais difícil de calcular, e que estratégia resolveu?"

**Rubrica:** R10 para a construção (30%) + R1 para os ângulos calculados (20%) + R12 para as áreas e o orçamento (50%). O item 3 é o teste de consistência: se a soma não fecha e a dupla não localiza o erro, perde 3 pontos.

---

# 2ª Série

## Bloco 1 · Capítulo 1 — Cilindros

**Conteúdo:** duas construções equivalentes do cilindro · elementos (base, geratriz, eixo, altura) · cilindro reto × oblíquo · cilindro equilátero · área lateral pelo desenrolamento · área total · volume como base × altura · secção meridiana e secção transversal.

### Atividade principal — A lata que gasta menos alumínio
**Tipo:** MOD · **Tempo:** 2 aulas · **Formato:** duplas

**Objetivo:** é o problema de otimização real da indústria de embalagens e usa **todas** as fórmulas do capítulo em uma única decisão. O aluno descobre que volume fixo admite infinitas latas, e que só uma gasta o mínimo.

**Comando para o aluno:**
> "Uma fábrica precisa de latas cilíndricas de **1 litro** (1 000 cm³).
> **(a)** Mostrem que existem infinitas latas de 1 L, escrevendo *h* em função de *r*.
> **(b)** Preencham a tabela para *r* = 3, 4, 5, 5,42, 6, 7 e 8 cm: altura correspondente, área lateral, área das duas bases e **área total**.
> **(c)** Construam o gráfico da área total em função de *r*. O gráfico tem mínimo? Onde?
> **(d)** Para o *r* que minimiza a área total, calculem a razão *h* / (2*r*). O que vocês encontraram? Comparem com a definição de **cilindro equilátero** do capítulo.
> **(e)** Meçam uma lata de refrigerante real (raio e altura) e calculem a razão *h* / (2*r*) dela. Ela é a lata ótima? Se não, proponham **duas** razões — fora da Geometria — para a indústria não usar a forma ótima.
> **(f)** Calculem quanto material se economizaria, em percentual, ao trocar a lata real pela lata ótima de mesmo volume."

**Rubrica:** R12, com ajuste — o item (d) vale 3 dos 10 pontos: reconhecer que o mínimo cai exatamente no cilindro equilátero é o achado da atividade. O item (e) vale 2 e aceita qualquer par de razões defensáveis (empilhamento, encaixe na mão, tradição de mercado, rótulo, transporte).

### Complementares
- **CONS · 30 min ·** Planificar e montar um cilindro de raio 4 cm e altura 10 cm em papel-cartão. Antes de colar, medir a base do retângulo lateral e comparar com 2π*r* calculado. Responder: por quantos milímetros a medição diferiu do cálculo, e por quê? Em seguida, cortar o cilindro montado por uma secção meridiana e por uma transversal, e desenhar a figura obtida em cada corte. — *Rubrica R1.*
- **EX · 35 min ·** Seis itens: área lateral e total dado *r* e *h*; volume; raio a partir do volume e da altura; identificar um cilindro equilátero a partir das medidas; capacidade de um reservatório em litros; e a área do rótulo que envolve uma lata com 1 cm de sobreposição na emenda. — *Rubrica R1.*

---

## Bloco 2 · Capítulo 1 — Cones

**Conteúdo:** duas descrições equivalentes do cone · relação fundamental *g*² = *h*² + *r*² · eixo e secção meridiana · cone reto × oblíquo · cone equilátero · área lateral por planificação · área total · volume como um terço do cilindro · tronco de cone.

### Atividade principal — Um terço, verificado com areia
**Tipo:** INV + CONS · **Tempo:** 2 aulas · **Formato:** grupos de 4

**Objetivo:** *V* = (1/3)·π*r*²*h* é a fórmula do bimestre que o aluno aceita sem entender de onde vem o 1/3. Encher três cones em um cilindro resolve isso em cinco minutos e não sai da memória.

**Materiais:** papel-cartão, tesoura, fita, areia fina, arroz ou sal, régua, compasso.

**Comando para o aluno:**
> "**Etapa 1 — construir.** Construam, em papel-cartão:
> - um **cone** de raio de base 5 cm e altura 12 cm, a partir do setor circular planificado;
> - um **cilindro** de mesmo raio de base (5 cm) e mesma altura (12 cm).
>
> Para planificar o cone: calculem primeiro a geratriz *g* pela relação fundamental; o setor tem raio *g*, e o comprimento do arco do setor tem de ser igual ao comprimento da circunferência da base. Mostrem esse cálculo.
> **Etapa 2 — verificar.** Encham o cone de areia e transfiram para o cilindro. Repitam. Quantos cones cheios são necessários para encher o cilindro?
> **Etapa 3 — calcular.** Calculem o volume dos dois sólidos pelas fórmulas e a razão entre eles. Confere com o que vocês observaram?
> **Etapa 4 — relatório.**
> **(a)** Qual foi a geratriz calculada? E o ângulo do setor planificado? Mostrem as duas contas.
> **(b)** Quantos cones couberam de fato? Se não foi exatamente 3, digam qual a diferença percentual e a que atribuem.
> **(c)** Calculem a área lateral e a área total do cone.
> **(d)** Cortem o cone por uma **secção meridiana** e desenhem a figura obtida, com as medidas. Em que caso essa secção é um triângulo equilátero? Verifiquem se o seu cone é equilátero.
> **(e)** Cortem o cone paralelamente à base, na metade da altura, e retirem a ponta. Sobrou um **tronco de cone**. Meçam os dois raios e a altura dele e calculem seu volume. Comparem com metade do volume do cone original: são iguais? Expliquem."

**Rubrica:** R8, com ajuste — o item (e) vale 3 dos 10 pontos e é a questão mais reveladora do capítulo: cortar na metade da altura **não** dá metade do volume, e explicar por quê exige entender a variação cúbica. Grupo que responda "sim, são iguais" perde os 3 pontos integralmente.

### Complementares
- **EX · 35 min ·** Seis itens: geratriz a partir de *h* e *r*; altura a partir de *g* e *r*; área lateral; área total; volume; e reconhecimento de cone equilátero a partir de duas medidas. Um sétimo item pede o volume de um tronco de cone com os dois raios e a altura dados. — *Rubrica R1.*
- **MOD · 30 min ·** Um balde doméstico real (tronco de cone) é medido pelo aluno: raio maior, raio menor e altura. Calcular a capacidade em litros e comparar com a capacidade impressa no balde, se houver. Depois responder: o balde é mais bem aproximado por um tronco de cone ou por um cilindro de raio médio? Calcular as duas aproximações e dizer qual erra menos. — *Rubrica R12.*

---

## Atividade integradora — 2ª série
### Três embalagens para o mesmo produto
**Tipo:** MOD · **Tempo:** 3 aulas · **Formato:** grupos de 4

**Comando para o aluno:**
> "Um produto líquido de **500 mL** será embalado. O grupo compara **três** propostas de embalagem de mesmo volume:
> **A** — cilindro · **B** — cone · **C** — tronco de cone
>
> Para cada proposta:
> **1.** Escolham as dimensões e mostrem que o volume é de 500 mL.
> **2.** Calculem a área total de material necessária.
> **3.** Construam a embalagem em papel-cartão a partir da planificação, com o cálculo da planificação registrado.
> **4.** Meçam a altura ocupada e a área da base — que é a área de prateleira que a embalagem consome.
>
> **Comparação e recomendação (2 páginas):**
> **(a)** Tabela final com volume, área de material, altura e área de base das três.
> **(b)** Qual gasta menos material? Qual ocupa menos prateleira? São a mesma?
> **(c)** Qual das três é impossível de apoiar em pé sem suporte, e o que isso implica no custo?
> **(d)** Recomendação final ao fabricante, com **dois** critérios explicitados e a admissão do que se perde ao escolher.
> **(e)** Se o pedido fosse 1 000 mL em vez de 500 mL, a área de material dobraria? Calculem para a proposta A e expliquem o resultado."

**Rubrica:** R12 (60%) + R10 para as três planificações construídas (40%). O item (e) vale 2 dos pontos de R12 e é o teste da relação entre variação linear, quadrática e cúbica — o conceito que atravessa os dois capítulos da 2ª série.

---

## Balanço da distribuição

| Tipo | 6º | 7º | 8º | 9º | 1ª | 2ª |
|---|---|---|---|---|---|---|
| CONS — construção, recorte, planificação | 3 | 3 | 2 | 2 | 3 | 2 |
| MOD — modelagem com decisão | 2 | 2 | 3 | 1 | 2 | 3 |
| ERR — análise de erro | 1 | 1 | 2 | 1 | 0 | 0 |
| EX — exercício | 1 | 1 | 2 | 2 | 2 | 2 |
| INV — investigação com medição | 1 | 1 | 0 | 2 | 0 | 1 |

O exercício está presente em todos os anos, sempre com um item que exige justificar a escolha da expressão ou explicar por que o procedimento funciona. Nunca é a atividade principal: em Geometria, a resolução do tipo `Passo 1 / Passo 2 / Passo 3` já está impressa na página, e repeti-la avalia leitura, não geometria.

A análise de erro desaparece na 1ª e na 2ª série porque ali o instrumento equivalente é mais forte: pedir a **demonstração** (relação 2:1, três recomposições, verificação do 1/3) põe o aluno na posição de justificar, que é o que a análise de erro simula nos anos anteriores.
