# Capítulo 9 — Problemas de lógica e tomada de decisão

> Como pistas que não dão a resposta diretamente podem determinar uma única solução?

---

## 1. Organizar várias condições em tabela

Ana, Beto e Caio moram em casas azul, verde e amarela. Beto mora na verde; Ana não mora na azul; Caio não mora na amarela.

```text
Pista 1 confirma Beto–verde.
Pista 2 exclui Ana–azul.
Pista 3 exclui Caio–amarela.
```

### 1.1 Todas as combinações antes da decisão

A tabela de dupla entrada mostra cada pessoa contra cada cor. Marcamos `não` quando uma pista exclui e `sim` quando confirma.

| Pessoa | azul | verde | amarela |
|---|---|---|---|
| Ana | não | não | sim |
| Beto | não | sim | não |
| Caio | sim | não | não |

Os outros “não” aparecem porque cada cor pertence a uma pessoa.

### 1.2 Ler a solução organizada

**Exemplo resolvido — Casas coloridas**

Beto ocupa a verde. Restam azul e amarela; Ana não pode usar azul, então fica com amarela. Caio fica com azul.

**Resposta:** Ana mora na casa amarela, Beto na verde e Caio na azul.

> 🔢 **Padrão:**  
> Cada pista vira uma marca verificável na tabela.

---

## 2. Eliminar até restar uma resposta

Lia, Nuno e Ravi escolheram xadrez, desenho e música. Ravi escolheu música; Nuno não escolheu xadrez; Lia não escolheu desenho.

```text
mais fechada: Ravi = música
depois: Nuno ≠ xadrez
por fim: Lia ≠ desenho
```

### 2.1 Uma eliminação abre a seguinte

Começamos pela pista que confirma uma combinação inteira. Essa marca elimina a mesma opção para as outras pessoas.

| Pessoa | xadrez | desenho | música |
|---|---|---|---|
| Lia | sim | não | não |
| Nuno | não | sim | não |
| Ravi | não | não | sim |

### 2.2 Fechar e conferir o caso

**Exemplo resolvido — Oficinas**

Ravi ocupa música. Lia e Nuno ficam com xadrez e desenho; como Nuno não escolheu xadrez, ele fica com desenho e Lia com xadrez.

**Resposta:** Lia escolheu xadrez, Nuno desenho e Ravi música. As três pistas permanecem verdadeiras.

> ⚠️ **Atenção:**  
> A resposta só fecha depois de ser conferida em todas as pistas.

---

## 3. Decidir comparando o mesmo critério

Um pacote de internet A oferece 10 GB por R$ 30,00. O pacote B oferece 15 GB por R$ 42,00. A decisão busca 30 GB pelo menor preço.

```text
A: 10 GB → para 30 GB, usar 3 pacotes
B: 15 GB → para 30 GB, usar 2 pacotes
```

### 3.1 Igualar o ponto de comparação

Antes da conta, escolhemos o critério: mesma quantidade de dados. Comparar apenas os preços anunciados favoreceria o pacote menor sem mostrar o custo de 30 GB.

- Opção A: três grupos de 10 GB.
- Opção B: dois grupos de 15 GB.
- A escolha vem dos dois totais calculados.

### 3.2 Calcular as duas opções

**Exemplo resolvido — Pacotes para 30 GB**

$$
\begin{aligned}
3\times\text{R\$ 30,00}&=\text{R\$ 90,00}\\
2\times\text{R\$ 42,00}&=\text{R\$ 84,00}\\
\text{R\$ 90,00}-\text{R\$ 84,00}&=\text{R\$ 6,00}
\end{aligned}
$$

**Resposta:** para 30 GB, o pacote B custa R$ 6,00 menos e compensa pelo critério escolhido.

> 🔢 **Padrão:**  
> Compare opções no mesmo critério antes de decidir.
