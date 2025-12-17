<h1>
    Caracteres especiais:
</h1>
<p>
    . = corresponde a qualquer caracter, exceto nova linha
    \d = corresponde a qualquer digito (0-9)
    \D = corresponde a qualquer caractere que não seja um dígito
    \w = corresponde a qualquer caractere alfanúmerico (letras, números e underline)
    \W = corresponde a qualquer caractere que não seja alfanúmerico
    \s = corresponde a qualquer espaço em branco (espaço, tabulações, etc.)
    \S = corresponde a qualquer caractere que não seja espaço em branco
</p>
<h1>
    Classes de caracteres:
</h1>
<p>
    [abc] = corresponde a qualquer caracter 'a', 'b' ou 'c'
    [^abc] = corresponde a qualquer caractere que não seja 'a', 'b' ou 'c'
    [a-z] = corresponde a qualquer caractere de 'a' a 'z' (minúsculas)
    [A-Z] = corresponde a qualquer caractere de 'A' a 'Z' (maiúsculas)
    [0-9] = corresponde a qualquer dígito (0-9)
    [a-zA-Z] = corresponde a qualquer letra, maiúscula ou minúscula
</p>
<h1>
    Quantificadores
</h1>
<p>
    * = 0 ou mais ocorrências do padrão anterior
    + = 1 ou mais ocorrências do padrão anterior
    ? = 0 ou 1 ocorrência do padrão anterior
    {n} = corresponde exatamente a n ocorrências do padrão anterior
    {n,} = corresponde a n ou mais ocorrências do padrão anterior
    {n,m} = corresponde entre n e m ocorrências do padrão anterior
</p>
<h1>
    Exemplo:
</h1>
<h2>
    Regex = \(\d{2}\)\s\d{4,5}-\d{4}
</h2>
<h2>
    Explicação:
</h2>
<p>
    - \(\d{2}\): Dois dígitos dentro de parênteses, como o código de área: (14)
    - \s: Um espaço.
    - \d{4,5}: Quatro ou cinco dígitos para o número do telefone: (14) 12345
    - -: O hífen literal: (14) 12345-
    - \d{4}: Quatro dígitos no final: (14) 12345-1234
</p>
<h2>
    Módulo "re"
</h2>
<p>
    usando com "import re"
</p>
<h2>
    Métodos:
</h2>
<p>
    - search
    - match
    - findall
    - sub
    - group
</p>