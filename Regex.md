<h1>O que é Regex?</h1>

<p>
    <strong>Regex (Expressões Regulares)</strong> é uma forma de descrever padrões de texto.
    Em vez de comparar texto letra por letra, você descreve regras que o texto deve seguir.
</p>

<p>
    Regex é usada para <strong>validar</strong>, <strong>buscar</strong>,
    <strong>extrair</strong> e <strong>substituir</strong> informações em strings.
</p>

<hr>

<h1>Caracteres Especiais</h1>

<p>
    Caracteres especiais representam conjuntos de caracteres e tornam a regex mais curta
    e poderosa.
</p>

<ul>
    <li><strong>.</strong> → qualquer caractere (exceto quebra de linha)</li>
    <li><strong>\d</strong> → qualquer dígito (0–9)</li>
    <li><strong>\D</strong> → qualquer caractere que não seja dígito</li>
    <li><strong>\w</strong> → letras, números e underline</li>
    <li><strong>\W</strong> → qualquer caractere não alfanumérico</li>
    <li><strong>\s</strong> → espaço em branco</li>
    <li><strong>\S</strong> → qualquer caractere que não seja espaço</li>
</ul>

<hr>

<h1>Classes de Caracteres</h1>

<p>
    Classes de caracteres permitem definir listas ou intervalos de caracteres aceitáveis
    em uma posição específica do texto.
</p>

<ul>
    <li><strong>[abc]</strong> → aceita a, b ou c</li>
    <li><strong>[^abc]</strong> → aceita qualquer caractere exceto a, b ou c</li>
    <li><strong>[a-z]</strong> → letras minúsculas</li>
    <li><strong>[A-Z]</strong> → letras maiúsculas</li>
    <li><strong>[0-9]</strong> → dígitos</li>
    <li><strong>[a-zA-Z]</strong> → qualquer letra</li>
</ul>

<hr>

<h1>Quantificadores</h1>

<p>
    Quantificadores definem quantas vezes o padrão anterior pode aparecer.
    São muito usados para validar tamanhos de campos.
</p>

<ul>
    <li><strong>*</strong> → zero ou mais vezes</li>
    <li><strong>+</strong> → uma ou mais vezes</li>
    <li><strong>?</strong> → zero ou uma vez</li>
    <li><strong>{n}</strong> → exatamente n vezes</li>
    <li><strong>{n,}</strong> → no mínimo n vezes</li>
    <li><strong>{n,m}</strong> → entre n e m vezes</li>
</ul>

<hr>

<h1>Âncoras</h1>

<p>
    Âncoras representam posições e garantem que a regex valide o início ou o fim da string.
</p>

<ul>
    <li><strong>^</strong> → início da string</li>
    <li><strong>$</strong> → final da string</li>
</ul>

<pre>^\d{3}$</pre>

<hr>

<h1>Grupos</h1>

<p>
    Grupos servem para organizar a regex e capturar partes específicas do texto,
    como DDD, números ou datas.
</p>

<ul>
    <li><strong>(...)</strong> → grupo capturante</li>
    <li><strong>(?:...)</strong> → grupo não capturante</li>
</ul>

<pre>(\d{2})\s(\d{4,5})-(\d{4})</pre>

<hr>

<h1>Alternância (OU lógico)</h1>

<p>
    A alternância permite aceitar uma opção ou outra, funcionando como um operador OR.
</p>

<pre>(cat|dog)</pre>

<hr>

<h1>Lookahead e Lookbehind</h1>

<p>
    Esses recursos validam o que vem antes ou depois sem incluir o texto no resultado.
    São considerados recursos avançados.
</p>

<h3>Lookahead positivo</h3>
<pre>\d+(?=kg)</pre>

<h3>Lookbehind positivo</h3>
<pre>(?<=R\$)\d+</pre>

<hr>

<h1>Escape de Caracteres Especiais</h1>

<p>
    Alguns caracteres possuem significado especial e precisam ser escapados para serem
    usados literalmente.
</p>

<pre>. ^ $ * + ? { } [ ] \ | ( )</pre>

<hr>

<h1>Regex em Python (módulo re)</h1>

<p>
    O módulo <code>re</code> é a implementação oficial de regex em Python.
</p>

<pre>import re</pre>

<h2>Métodos principais</h2>

<ul>
    <li><strong>search</strong> → procura em qualquer posição</li>
    <li><strong>match</strong> → verifica apenas o início</li>
    <li><strong>fullmatch</strong> → valida a string inteira</li>
    <li><strong>findall</strong> → retorna todas as ocorrências</li>
    <li><strong>sub</strong> → substitui padrões</li>
    <li><strong>group</strong> → acessa grupos capturados</li>
</ul>

<hr>

<h1>Exemplo Real em Python</h1>

<p>
    Exemplo de validação de telefone brasileiro usando regex.
</p>

<pre>
import re

padrao = r'\(\d{2}\)\s\d{4,5}-\d{4}'
telefone = '(14) 91234-5678'

if re.fullmatch(padrao, telefone):
    print('Telefone válido')
else:
    print('Telefone inválido')
</pre>