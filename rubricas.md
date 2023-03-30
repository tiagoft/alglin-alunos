# Rubricas - AlgLin


## Argumentação

| Nível | Descrição |
| --- | --- |
| F | A argumentação apresentada não é clara o suficiente para permitir a reprodução do código computacional a partir dela por não existir ou por não citar ou descrever corretamente os elementos corretos que aparecem no código, ou é uma argumentação que se baseia unicamente na reprodução do código computacional, ou é uma argumentação factualmente incorreta ou que justifica um código factualmente incorreto. |
| E | A argumentação apresentada não é clara o suficiente para permitir a reprodução do código computacional a partir dela por não existir ou por não explicitar a relevância dos elementos que aparecem no código, ou é uma argumentação que se baseia unicamente em comentar o código computacional. |
| D | A argumentação apresentada não é clara o suficiente para permitir a reprodução do código computacional a partir dela por não apresentar uma articulação entre os elementos matemáticos semelhante à que aparece no código ou omitir passagens que não são triviais mas são necessárias para a compreensão da solução. |
| C | A argumentação apresentada permite a reprodução do código computacional, embora haja pequenos erros pontuais em aspectos que não são relevantes para a solução (exemplo: dizer que o algoritmo aplicado foi inventado em 1963 quando essa data não é correta). |
| B | A argumentação apresentada permite a reprodução do código computacional mas cita fatos que, embora corretos, são irrelevantes para o funcionamento (exemplo: dizer que o algoritmo aplicado foi inventado em 1963 quando, de fato, foi, embora essa data seja irrelevante para o código computacional).
| A | A argumentação está correta, completa e objetiva. As justificativas matemáticas são apresentadas de forma clara e organizada, sem erros ou equívocos, e correspondem imediatamente ao código apresentado. A solução apresentada é bem justificada e explica de forma completa o raciocínio por trás da resposta.


## Código computacional

| Rubrica | Descrição |
| --- | --- |
| F | O programa não funciona, não roda, ou resolve um problema diferente do proposto. |
| E | O programa apresenta problemas de implementação, como erros de lógica, que levam a resultados incorretos ou incompletos. |
| D | O programa apresenta uma solução algoritmica que não usa sua correspondência matemática ou não usa pacotes adequados em situações que esse uso seria muito simples (por exemplo: implementando uma multiplicação matricial com laços *for* aninhados, ao invés de usar a multiplicação matricial do Numpy). |
| C | O programa implementa corretamente uma solução matemáticamente correta e usa pacotes nas situações comuns, mas tem problemas de clareza como variáveis e funções com nomes que não correspondem ao seu conteudo/funcionalidade (ex: `var_1` ou `a1, a2, a3, a4`), ou deixar de usar ou comentar de forma lacônica o uso de construções da linguagem muito diferentes das que vimos em aula (ex: ao usar funções que nunca foram usadas em aula, ou pacotes que nunca foram usados, precisamos de um comentário como "a função X recebe A e retorna B, e por isso ela faz o papel da transformação T que foi discutida na argumentação"). |
| B | O programa implementa corretamente uma solução matemáticamente correta, com nomes de funções e variáveis auto-explicativos, está corretamente comentada, mas deixou de apagar instruções "print" que foram usadas para debug ou deixou de comentar corretamente o código ou deixou elementos que não deveriam estar em produção como nome da equipe, frases de efeito, ou outras questões de organização. |
| A | O programa implementa uma solução matemática correta e completa, com nomes de funções e variáveis que são auto-explicativos, e, sempre que possível, coincidem com os nomes usados na argumentação, e comentários detalhados que ligam o algoritmo mostrado a sua argumentação. |


## Exemplo

**Pergunta**

Um pote com 3kg de cobre e 5kg de platina custa R$1000. Um pote com 2kg de cobre e 7kg de platina custa R$800. Usando uma formulação matricial, descubra: qual é o preço do cobre e qual é o preço da platina?

**Solução (argumentação)**

Podemos equacionar o problema como:
$$
\begin{aligned}
3C + 5P &= 1000 \\
2C + 7P &= 800,
\end{aligned}
$$
onde $C$ é o preço do cobre e $P$ é o preço da platina.

Podemos re-escrever a equação na forma matricial:

$$
\begin{bmatrix}
3 & 5 \\
2 & 7
\end{bmatrix}
\begin{bmatrix}
C \\ P
\end{bmatrix}
=
\begin{bmatrix}
1000 \\ 800
\end{bmatrix}
$$

Isolando $[C P]^T$:

$$
\begin{bmatrix}
3 & 5 \\
2 & 7
\end{bmatrix}^{-1}
\begin{bmatrix}
3 & 5 \\
2 & 7
\end{bmatrix}
\begin{bmatrix}
C \\ P
\end{bmatrix}
=
\begin{bmatrix}
C \\ P
\end{bmatrix}
=
\begin{bmatrix}
3 & 5 \\
2 & 7
\end{bmatrix}^{-1}
\begin{bmatrix}
1000 \\ 800
\end{bmatrix}
$$

**Solução (código)**

    import numpy as np

    A = np.array( [ [3, 5], [2, 7]])
    precos_potes = np.array( [ [1000], [800]])
    precos_metais = np.linalg.inv(A) @ precos_potes

    print("Preços dos metais:")
    print("Cobre: R$", precos_metais[0])
    print("Platina: R$", precos_metais[1])
    
**Exemplo de argumentação ruim (não explica a relevância dos elementos - E)**


$$
\begin{aligned}
3A + 5B &= 1000 \\
2A + 7B &= 800,
\end{aligned}
$$

logo:

A @ X = y,

X = np.linalg.inv(A) @ y

**Exemplo de argumentação ruim (não articula os elementos, então não explica como chegou até este ponto - D)**

Do enunciado:

$$
\begin{bmatrix}
C \\ P
\end{bmatrix}
=
\begin{bmatrix}
3 & 5 \\
2 & 7
\end{bmatrix}^{-1}
\begin{bmatrix}
1000 \\ 800
\end{bmatrix}
$$


**Exemplo de implementação computacional ruim (não tem correspondência com a argumentação)**

    import numpy as np
    import pandas as pd

    A1 = np.array( [ [3, 5] ])
    A2 = np.array( [ [2, 7] ])
    A = np.vstack ((A1, A2))
    B = np.array( [ [10], [8]]) * 100
    C = np.linalg.inv(A) @ B
    print(C)

**Exemplo de implementação computacional ruim (factualmente errada)**

    import numpy as np

    A = np.array( [ [3, 2], [5, 7]])
    B = np.array( [ [800], [1000]])
    C = np.linalg.inv(A) @ B
    print(C)

