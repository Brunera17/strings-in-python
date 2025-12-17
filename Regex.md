
<h1>Caracteres Especiais</h1>
<ul>
    <li><strong>.</strong> = qualquer caractere, exceto nova linha</li>
    <li><strong>\d</strong> = qualquer dígito (0–9)</li>
    <li><strong>\D</strong> = qualquer caractere que não seja dígito</li>
    <li><strong>\w</strong> = caractere alfanumérico (letras, números e _)</li>
    <li><strong>\W</strong> = caractere não alfanumérico</li>
    <li><strong>\s</strong> = espaço em branco</li>
    <li><strong>\S</strong> = não espaço em branco</li>
</ul>

<h1>Classes de Caracteres</h1>
<ul>
    <li><strong>[abc]</strong> = a, b ou c</li>
    <li><strong>[^abc]</strong> = qualquer caractere exceto a, b ou c</li>
    <li><strong>[a-z]</strong> = letras minúsculas</li>
    <li><strong>[A-Z]</strong> = letras maiúsculas</li>
    <li><strong>[0-9]</strong> = dígitos</li>
    <li><strong>[a-zA-Z]</strong> = qualquer letra</li>
</ul>

<h1>Quantificadores</h1>
<ul>
    <li><strong>*</strong> = 0 ou mais</li>
    <li><strong>+</strong> = 1 ou mais</li>
    <li><strong>?</strong> = 0 ou 1</li>
    <li><strong>{n}</strong> = exatamente n</li>
    <li><strong>{n,}</strong> = n ou mais</li>
    <li><strong>{n,m}</strong> = entre n e m</li>
</ul>

<h1>Âncoras</h1>
<ul>
    <li><strong>^</strong> = início da string</li>
    <li><strong>$</strong> = final da string</li>
</ul>

<pre>^\d{3}$</pre>

<h1>Grupos</h1>
<ul>
    <li><strong>(...)</strong> = grupo capturante</li>
    <li><strong>(?:...)</strong> = grupo não capturante</li>
</ul>

<pre>(\d{2})\s(\d{4,5})-(\d{4})</pre>

<h1>Alternância (OU lógico)</h1>
<pre>(cat|dog)</pre>

<h1>Lookahead e Lookbehind</h1>

<h2>Lookahead positivo</h2>
<pre>\d+(?=kg)</pre>

<h2>Lookbehind positivo</h2>
<pre>(?<=R\$)\d+</pre>

<h1>Escape de Caracteres Especiais</h1>
<p>Precisam de barra invertida (<code>\</code>):</p>
<pre>. ^ $ * + ? { } [ ] \ | ( )</pre>

<h1>Exemplo Completo</h1>

<h2>Regex</h2>
<pre>\(\d{2}\)\s\d{4,5}-\d{4}</pre>

<h2>Explicação</h2>
<ul>
    <li><strong>\(\d{2}\)</strong> → DDD entre parênteses</li>
    <li><strong>\s</strong> → espaço</li>
    <li><strong>\d{4,5}</strong> → número inicial</li>
    <li><strong>-</strong> → hífen</li>
    <li><strong>\d{4}</strong> → número final</li>
</ul>

<h1>Módulo <code>re</code> (Python)</h1>

<pre>import re</pre>

<h2>Métodos</h2>
<ul>
    <li><strong>re.search</strong> → procura em qualquer parte</li>
    <li><strong>re.match</strong> → início da string</li>
    <li><strong>re.fullmatch</strong> → string inteira</li>
    <li><strong>re.findall</strong> → retorna todas as ocorrências</li>
    <li><strong>re.sub</strong> → substituição</li>
    <li><strong>group()</strong> → acessa grupos capturados</li>
</ul>

<h1>Flags</h1>
<ul>
    <li><strong>re.IGNORECASE</strong> → ignora maiúsculas/minúsculas</li>
    <li><strong>re.MULTILINE</strong> → ^ e $ por linha</li>
    <li><strong>re.DOTALL</strong> → . aceita quebra de linha</li>
    <li><strong>re.VERBOSE</strong> → regex comentada</li>
</ul>

<h1>Exemplo Real em Python</h1>

<pre>
import re

padrao = r'\(\d{2}\)\s\d{4,5}-\d{4}'
telefone = '(14) 91234-5678'

if re.fullmatch(padrao, telefone):
    print('Telefone válido')
else:
    print('Telefone inválido')
</pre>