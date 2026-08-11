# BL2_Capítulo 1 — Gráficos estatísticos

> Em 1854, um médico marcou num mapa de Londres um ponto para cada morte por cólera — e os pontos cercavam uma única bomba d'água. Como um gráfico bem escolhido pode revelar o que nenhuma tabela mostra (e até salvar vidas)?

---

## 1. Tipos de gráficos estatísticos

O mesmo conjunto pode destacar comparação, evolução, proporção ou localização.

### 1.1 Quatro representações

Cada gráfico responde melhor a um tipo de pergunta:

| Tipo | Uso principal |
|---|---|
| Barras horizontais | comparar categorias com nomes longos |
| Colunas verticais | comparar categorias ou poucos períodos |
| Linhas | acompanhar evolução no tempo |
| Setores | mostrar partes de um total de 100% |

Nos setores, cada 1% corresponde a:

$$1\% = 3{,}6^{\circ}$$

**Transporte de uma turma hipotética**

Considere ônibus 50%, caminhada 30% e bicicleta 20%.

**Resolução:**

- **Passo 1:** Multiplicar cada percentual por $$3{,}6^{\circ}$$.

$$50 \cdot 3{,}6^{\circ}=180^{\circ}$$

$$30 \cdot 3{,}6^{\circ}=108^{\circ}$$

$$20 \cdot 3{,}6^{\circ}=72^{\circ}$$

- **Passo 2:** Conferir a volta completa.

$$180^{\circ}+108^{\circ}+72^{\circ}=360^{\circ}$$

**Resposta:** ônibus ocupa metade do círculo; caminhada e bicicleta completam os outros 180°.

### 1.2 Elementos e mapas-gráficos

Uma representação verificável contém:

- título informativo;
- eixos com unidade e escala;
- legenda, quando necessária;
- fonte e data.

Em 1854, o médico **John Snow** marcou mortes por cólera num mapa do Soho, em Londres. A concentração próxima à bomba de Broad Street fortaleceu a hipótese de contaminação da água e ajudou a justificar a retirada de sua alavanca.

Esse **mapa-gráfico** relaciona dados e localização. Painéis da pandemia de 2020 retomaram o princípio ao distribuir casos no território e no tempo.

> ⚠️ **Atenção:**
>
> Sem fonte e data, o leitor não consegue conferir de onde vieram os dados nem a qual período pertencem.

---

## 2. Escolha adequada de gráficos

Um gráfico bonito pode ser inadequado para a pergunta que deveria responder.

### 2.1 Pergunta e variável

A decisão começa pelo objetivo da pesquisa:

| Pergunta | Tipo de dado | Gráfico adequado |
|---|---|---|
| Qual categoria é maior? | categorias sem ordem | barras ou colunas |
| Como o valor mudou? | sequência temporal | linhas |
| Como o total se divide? | poucas partes de 100% | setores |

Em *Sémiologie Graphique*, de 1967, **Jacques Bertin** sistematizou variáveis visuais como posição, tamanho e cor. Posição favorece comparação precisa; tamanho mostra quantidade; cor separa grupos quando usada com contraste legível.

### 2.2 Avaliar a escolha

**Três pesquisas hipotéticas**

Escolha a representação mais adequada para dez sabores, vendas mensais e divisão de um orçamento em cinco partes.

**Resolução:**

- **Passo 1:** Identificar o que será comparado.

| Situação | Escolha | Motivo |
|---|---|---|
| Dez sabores | barras | setores ficariam numerosos e difíceis de comparar |
| Vendas por mês | linhas | os pontos possuem ordem temporal |
| Cinco partes do orçamento | setores | as categorias completam 100% |

- **Passo 2:** Rejeitar tipos que criam relações inexistentes.

Uma linha entre sabores sugeriria continuidade e ordem, embora as categorias sejam independentes.

**Resposta:** adequação depende da estrutura dos dados, não do efeito visual preferido.

Um gráfico de setores funciona melhor com poucas categorias. Com dez fatias parecidas, diferenças pequenas ficam difíceis de perceber; barras permitem comparar comprimentos numa mesma escala.

> 🔢 **Padrão:**
>
> Comparação pede posição ou comprimento; evolução pede sequência; parte de um todo pede proporção completa.

---

## 3. Construção e interpretação

Antes do gráfico, uma tabela organiza os valores que serão representados.

### 3.1 Da tabela à planilha

Considere dados hipotéticos de empréstimos mensais de uma biblioteca escolar:

| Mês | Livros emprestados |
|---|---:|
| Maio | 120 |
| Junho | 135 |
| Julho | 150 |

**Gráfico de evolução mensal**

**Resolução:**

- **Passo 1:** Registrar meses na primeira coluna e quantidades na segunda.
- **Passo 2:** Selecionar a tabela e inserir um gráfico de linhas.
- **Passo 3:** Usar o título “Livros emprestados — maio a julho”, eixo vertical iniciado em zero, unidade “livros” e fonte “exemplo didático hipotético, 2026”.
- **Passo 4:** Calcular a variação do primeiro ao último mês.

$$\frac{150-120}{120}\cdot100=25\%$$

**Resposta:** os empréstimos cresceram 25% entre maio e julho; a tabela preserva os valores e a linha evidencia a tendência de alta.

### 3.2 Leitura crítica

Um roteiro reduz conclusões apressadas:

1. ler título, fonte e data;
2. conferir unidade e escala;
3. verificar se o tipo combina com os dados;
4. identificar tendência e exceções;
5. limitar a conclusão à amostra e ao período.

Distorções frequentes incluem:

- eixo cortado, que exagera diferenças;
- eixo invertido, que troca a direção visual;
- efeito 3D, que altera a percepção das áreas;
- comparação de grupos, períodos ou unidades incompatíveis.

No exemplo, iniciar o eixo em 115 faria o crescimento parecer muito maior, embora os valores continuassem 120, 135 e 150.

O artigo 27 do Código do CONAR exige apresentação verdadeira e proíbe informação visual capaz de levar o consumidor ao engano. A lista oficial de casos de 2025 inclui representações julgadas sob o critério de veracidade, mas não sustenta uma contagem específica de “gráficos enganosos”.

> ⚠️ **Atenção:**
>
> O gráfico permite afirmar o que ocorreu no conjunto observado, não o que necessariamente ocorre fora dele.
