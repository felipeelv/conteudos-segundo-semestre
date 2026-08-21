# Capítulo 2 — Aplicações integradas

> Avaliar um financiamento, interpretar um teste diagnóstico ou escolher onde guardar recursos exige mais de uma ferramenta. Como integrar dados, probabilidade e finanças com responsabilidade?

---

## 1. Interpretação de gráficos e tabelas

### 1.1 Descrever uma distribuição

Uma análise completa combina forma, centro, dispersão e contexto. Tabelas de frequência registram ocorrências; gráficos de barras comparam categorias; linhas mostram evolução temporal; setores representam partes de um total; histogramas agrupam medidas contínuas; box-plots resumem mediana, quartis e possíveis extremos.

Considere tempos hipotéticos, em minutos, de seis atendimentos:

$$
8,\ 9,\ 10,\ 10,\ 11,\ 30.
$$

**Resolução:**

- **Passo 1:** Calcular a média: $(8+9+10+10+11+30)/6=13$.
- **Passo 2:** Calcular a mediana: $(10+10)/2=10$.
- **Passo 3:** Calcular a amplitude: $30-8=22$.

**Resposta:** o valor 30 eleva a média para 13; a mediana 10 descreve melhor o centro dos demais atendimentos, e a amplitude 22 revela dispersão.

### 1.2 Criticar antes de decidir

Uma série temporal pode parecer disparar se o eixo começar perto do menor valor. Um recorte curto pode ocultar sazonalidade. Sem fonte, período, população e tamanho da amostra, o gráfico não sustenta generalização.

Correlação também não basta para afirmar causa. Duas variáveis podem responder a uma terceira, sofrer causalidade reversa ou coincidir. Cathy O’Neil mostrou como modelos opacos de crédito, contratação e avaliação podem amplificar desigualdades quando seus dados, objetivos e erros não são auditados.

Uma decisão baseada em dados deve registrar:

- o que foi medido e quem está representado;
- qual medida resume a distribuição;
- quais vieses e valores extremos existem;
- até onde a conclusão pode chegar.

> ⚠️ **Atenção:** a saída de um modelo é resultado de escolhas humanas, não verdade objetiva automática.

---

## 2. Probabilidade em situações reais

### 2.1 Mapa de modelos

| Estrutura | Modelo |
|---|---|
| resultados equiprováveis | $P(E)=n(E)/n(\Omega)$ |
| informação de que $B$ ocorreu | $P(A\mid B)=P(A\cap B)/P(B)$ |
| tentativas independentes | multiplicação das probabilidades |
| $k$ sucessos em $n$ tentativas | $P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$ |

As palavras “dado que”, “sem reposição”, “independente” e “exatamente $k$” indicam estruturas, mas as hipóteses devem ser confirmadas no contexto.

### 2.2 Um teste positivo

Considere um teste **hipotético**, não destinado a decisão médica: prevalência de 1%, sensibilidade de 90% e especificidade de 95%. Em 10.000 pessoas, espera-se que 100 tenham a condição; 90 delas testariam positivo. Entre 9.900 sem a condição, 5%, ou 495, teriam falso positivo.

**Resolução:**

- **Passo 1:** Contar positivos: $90+495=585$.
- **Passo 2:** Calcular a probabilidade condicional.

$$
P(condicao\mid positivo)=\frac{90}{585}\approx15{,}38\%
$$

**Resposta:** nesse cenário, um resultado positivo corresponde a cerca de 15,38% de probabilidade da condição, e não 90%. A prevalência baixa muda a interpretação.

O mesmo resultado decorre do teorema de Bayes:

$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.
$$

Em decisões financeiras, o **valor esperado** pondera cada resultado por sua probabilidade. Uma alternativa que paga R$ 100,00 com chance de 20% e zero nos demais casos tem valor esperado intuitivo de R$ 20,00. Isso não elimina risco nem garante receber a média. Sob incerteza, as probabilidades podem nem ser conhecidas.

> ⚠️ **Atenção:** decisões de saúde exigem interpretação profissional; o exemplo serve apenas para estudar probabilidade condicional.

---

## 3. Matemática financeira: aplicações integradas

### 3.1 Uma caixa de ferramentas

| Pergunta | Relação |
|---|---|
| valor após capitalização | $M=C(1+i)^n$ |
| equivalência anual e mensal | $1+i_a=(1+i_m)^{12}$ |
| valor futuro trazido ao presente | $VP=VF/(1+i)^n$ |
| valor criado por um projeto | $VPL=-I_0+\sum\dfrac{FC_k}{(1+r)^k}$ |

No sistema Price, as prestações são constantes e a amortização cresce ao longo do tempo. No SAC, a amortização é constante e as prestações diminuem. Comparar exige mesma taxa, prazo, entrada, encargos e total pago.

Um VPL positivo indica que, **dada a taxa de desconto adotada**, os fluxos futuros superam o investimento inicial. Ele não elimina incerteza nem transforma a taxa escolhida em fato.

### 3.2 Integração em uma decisão

Uma empresa avalia um equipamento de R$ 10.000,00. Um gráfico confiável de 24 meses indica economia média anual de R$ 6.000,00. A amostra também sugere 20% de chance de manutenção de R$ 2.000,00 por ano. O custo esperado anual é $0{,}20\cdot2000=400$, então o fluxo líquido esperado é R$ 5.600,00.

Com taxa hipotética de 10% ao ano e dois anos de uso:

**Resolução:**

- **Passo 1:** Trazer os fluxos ao presente.

$$
VPL=-10000+\frac{5600}{1{,}10}+\frac{5600}{(1{,}10)^2}
$$

- **Passo 2:** Calcular o resultado.

$$
VPL\approx-280{,}99
$$

**Resposta:** nas premissas adotadas, o VPL é negativo em cerca de R$ 281,00; o projeto não supera a taxa de comparação.

Para recursos financeiros, poupança, CDB e títulos públicos devem ser comparados por rentabilidade líquida, liquidez, prazo, risco, tributação e garantias aplicáveis — sem tratar taxa passada como promessa. Integrar significa verificar o gráfico, estimar a probabilidade e só então calcular a decisão financeira.

> 🔢 **Em resumo:** técnica, premissas transparentes e responsabilidade formam uma única decisão matemática.
