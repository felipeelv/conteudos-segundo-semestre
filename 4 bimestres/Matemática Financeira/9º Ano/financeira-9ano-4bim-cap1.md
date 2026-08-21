# Capítulo 1 — Medidas estatísticas

> Nove pessoas recebem R$ 2.000,00 e uma recebe R$ 100.000,00. A média é R$ 11.800,00, valor que ninguém recebe. Qual medida descreve melhor o salário típico?

---

## 1. Medidas de tendência central e de dispersão

### 1.1 Centro de um conjunto de dados

A **média** distribui igualmente o total entre as observações; a **mediana** ocupa o centro do rol ordenado; a **moda** é o valor mais frequente. Um conjunto pode ter uma moda, duas modas ou nenhuma.

Para os dez salários da abertura:

**Resolução:**

- **Passo 1:** Calcular a média.

$$
\bar{x}=\frac{9\cdot2\,000+100\,000}{10}=11\,800
$$

- **Passo 2:** Como há dez valores, calcular a mediana pela média entre o quinto e o sexto, ambos iguais a 2.000.

$$
Md=\frac{2\,000+2\,000}{2}=2\,000
$$

- **Passo 3:** Identificar a moda: $Mo=2\,000$.

**Resposta:** média de R$ 11.800,00 e mediana e moda de R$ 2.000,00; estas duas descrevem melhor o salário típico.

Na média ponderada, cada valor tem um peso. Uma prova 8 com peso 3 e um trabalho 6 com peso 1 produzem:

$$
\bar{x}_{p}=\frac{8\cdot3+6\cdot1}{3+1}=7{,}5
$$

Adolphe Quetelet estudou populações por valores médios no século XIX. Seu “homem médio” marcou a estatística social, mas um valor central nunca descreve sozinho toda a diversidade.

### 1.2 Dispersão

A **amplitude** mede a distância entre extremos: $A=x_{max}-x_{min}$. Os conjuntos $5,6,7,8,9$ e $1,7,7,7,13$ têm média 7, mas amplitudes 4 e 12. O segundo é mais disperso.

O **desvio padrão populacional** $\sigma$ também indica espalhamento: quanto maior, mais distantes os dados tendem a estar da média. Sua fórmula pode ser reconhecida como referência,

$$
\sigma=\sqrt{\frac{\sum(x_i-\bar{x})^2}{n}},
$$

mas aqui importa interpretar, não calculá-la. Em distribuições aproximadamente simétricas, média, mediana e moda costumam ficar próximas.

> 🔢 **Em resumo:** centro e dispersão respondem a perguntas diferentes e devem ser lidos em conjunto.

---

## 2. Escolha da medida adequada; construção de gráficos

### 2.1 A medida responde ao formato dos dados

A **média** aproveita todos os valores e descreve bem distribuições aproximadamente simétricas. A **mediana** resiste a valores extremos, por isso é mais representativa em distribuições assimétricas, como os salários da abertura. Para categorias sem ordem numérica, como forma de pagamento mais usada, a **moda** é a medida possível.

Um valor extremo, ou **outlier**, desloca a média. Compare:

| Dados | Média | Mediana |
|---|---:|---:|
| 2, 2, 2, 2, 2 | 2 | 2 |
| 2, 2, 2, 2, 100 | 21,6 | 2 |

Acrescentar 100 altera muito a média, mas não a mediana. Essa resistência é chamada **robustez**. John Tukey, criador do box-plot, defendia observar a distribuição antes de escolher um cálculo.

### 2.2 Representação honesta

Um gráfico deve tornar visível a medida discutida. Uma linha horizontal pode marcar a média em um gráfico de pontos. Um box-plot pode mostrar intuitivamente a mediana e a posição dos dados, sem exigir aqui o cálculo formal de quartis.

| Elemento | Verificação |
|---|---|
| eixos | unidade e escala estão claras? |
| dados | fonte e período foram informados? |
| destaque | a medida central está identificada? |
| forma | o gráfico corresponde ao tipo de variável? |

Edward Tufte tornou-se referência em visualização por defender clareza e evitar elementos que competem com os dados. Uma representação honesta permite comparar valores sem exagerar diferenças.

Em uma planilha, `=MÉDIA(A1:A5)` calcula a média, `=MEDIANA(A1:A5)` encontra a mediana e `=MÁXIMO(A1:A5)-MÍNIMO(A1:A5)` calcula a amplitude. As funções automatizam operações, mas a escolha da medida continua dependendo da distribuição e da pergunta.

Para os salários da abertura, a mediana de R$ 2.000,00 é a melhor descrição do valor típico; a média de R$ 11.800,00 continua válida, porém responde à divisão igual do total. Informar ambas evita que uma medida verdadeira produza uma impressão enganosa.

> ⚠️ **Atenção:** nenhum cálculo substitui a leitura do formato e do contexto dos dados.
