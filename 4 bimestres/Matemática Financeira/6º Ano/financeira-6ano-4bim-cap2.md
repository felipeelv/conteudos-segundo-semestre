# Capítulo 2 — Gráficos e probabilidade

> Na propaganda, a barra do produto X parece 5 vezes maior que a do concorrente — mas os números são 80 × 76. Como um gráfico faz uma diferença pequena parecer enorme sem mentir nos números?

---

## 1. Gráfico de setores e leitura crítica

Um gráfico de setores divide o círculo inteiro, $$360^{\circ}$$, conforme a participação de cada categoria.

### 1.1 Das porcentagens às fatias

Cada setor representa parte do total, e todas as fatias precisam somar 100%.

Nos casos mais simples, a relação entre porcentagem e ângulo é direta:

| Porcentagem | Parte do círculo | Ângulo |
|---:|---:|---:|
| 25% | um quarto | $$90^{\circ}$$ |
| 50% | metade | $$180^{\circ}$$ |
| 75% | três quartos | $$270^{\circ}$$ |
| 100% | inteiro | $$360^{\circ}$$ |

Suponha uma pesquisa hipotética com 40 respostas: 20 escolheram caminhada, 10 bicicleta e 10 jogos.

| Preferência | Frequência | Porcentagem | Ângulo |
|---|---:|---:|---:|
| caminhada | 20 | 50% | $$180^{\circ}$$ |
| bicicleta | 10 | 25% | $$90^{\circ}$$ |
| jogos | 10 | 25% | $$90^{\circ}$$ |

O semicírculo da caminhada mostra metade das escolhas. As duas outras categorias ocupam quartos iguais.

### 1.2 Como a forma visual pode enganar

O jornalista americano **Darrell Huff** catalogou truques de representação em *How to Lie with Statistics*, de 1954.

Três distorções continuam frequentes:

- **eixo cortado** — iniciar uma escala em 75 faz 80 parecer muito maior que 76;
- **efeito 3D** — perspectiva faz a fatia da frente parecer maior;
- **tipo inadequado** — setores não servem quando as categorias não formam um único total.

No caso 80 × 76, a diferença é de quatro unidades:

$$80-76=4$$

Comparada ao valor 76, ela representa aproximadamente:

$$\frac{4}{76}\cdot100\approx5{,}26\%$$

Uma barra cinco vezes mais alta produz impressão incompatível com essa diferença. Um roteiro de leitura reduz o risco: conferir título, fonte, escala, tipo, tendência e conclusão.

> ⚠️ **Atenção:**  
> Números corretos não tornam honesto um gráfico cuja escala distorce a comparação.

---

## 2. Probabilidade

Uma urna hipotética contém cinco fichas azuis, três verdes e duas amarelas, todas com a mesma chance de sorteio.

### 2.1 Casos favoráveis e possíveis

Quando os resultados são igualmente prováveis, usa-se:

$$P(E)=\frac{n(E)}{n(\Omega)}$$

Os elementos da expressão são:

- $$E$$ — evento observado;
- $$n(E)$$ — quantidade de casos favoráveis;
- $$\Omega$$ — espaço amostral;
- $$n(\Omega)$$ — quantidade total de resultados possíveis.

**Sorteio de uma ficha azul**

**Resolução:**

- **Passo 1:** Contar as dez fichas possíveis.

$$n(\Omega)=5+3+2=10$$

- **Passo 2:** Contar as cinco fichas azuis favoráveis.

$$n(E)=5$$

- **Passo 3:** Calcular e interpretar a probabilidade.

$$P(E)=\frac{5}{10}=\frac{1}{2}=0{,}5=50\%$$

**Resposta:** a chance de azul é 50%; em cada sorteio, metade dos resultados possíveis favorece o evento.

Uma probabilidade $$P=0{,}75$$ indica 75 chances favoráveis em cada 100 casos comparáveis. Já $$P=\frac{1}{100}$$ indica um caso favorável em 100 e, portanto, um evento bem menos provável.

### 2.2 Uma tentativa e muitas repetições

Em dez lançamentos de moeda, obter sete caras não é impossível. Em muitas repetições, a proporção de caras tende a se aproximar de 50%.

Jakob Bernoulli estudou essa regularidade no livro *Ars Conjectandi*, publicado em 1713. Isso não significa que a moeda “compensa” imediatamente uma sequência: cada novo lançamento continua com as mesmas duas possibilidades.

> 🔢 **Padrão:**  
> Probabilidade descreve uma tendência do processo, não uma promessa sobre a próxima tentativa.

---

## 3. Fluxogramas

Um fluxograma registra a ordem de um processo e mostra caminhos diferentes quando existe uma decisão.

### 3.1 Quatro símbolos básicos

Cada forma cumpre uma função:

| Forma | Função | Exemplo de texto |
|---|---|---|
| oval | início ou fim | “início” |
| retângulo | ação | “registrar nome” |
| losango | decisão | “há vaga?” |
| seta | direção do fluxo | liga uma etapa à seguinte |

Um processo bem definido possui um início, um fim e duas saídas identificadas em cada decisão: “sim” e “não”.

### 3.2 Leitura de uma triagem

O esquema textual representa um fluxo simplificado de atendimento:

```text
[Início]
    ↓
<Há dor no peito?>
   ├─ sim → [Encaminhar para emergência] → [Fim]
   └─ não → [Seguir a avaliação] → [Fim]
```

O losango não executa uma ação: ele separa os caminhos. Os retângulos registram o que acontece em cada resposta.

O engenheiro americano **Frank Gilbreth** apresentou gráficos de processo à Sociedade Americana de Engenheiros Mecânicos em 1921. O recurso foi adotado em administração, computação e saúde porque torna sequências e decisões visíveis.

Uma rotina cotidiana segue a mesma lógica: começa, realiza ações, verifica uma condição e termina. Se chover, escolher capa; se não, seguir sem ela. Escrever todas as saídas impede que o processo pare num caminho sem conclusão.

> ⚠️ **Atenção:**  
> Toda decisão do fluxograma precisa nomear as saídas e conduzir a uma próxima etapa.
