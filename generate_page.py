import markdown
import codecs
import re


with codecs.open('README.md', mode='r', encoding='utf-8') as file:
    readme_content = file.read()

# Replace triple backticks with <pre><code> tags
html_content = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', readme_content, flags=re.DOTALL)


def remove_code_language(html_content, language):
    pattern = fr'<pre><code>{language}'
    return re.sub(pattern, r'<pre><code>', html_content, flags=re.DOTALL)


# Define the list of languages to remove
languages = ['batch', 'bash', 'powershell']


# Remove the specified language texts from <pre><code> blocks
for language in languages:
    html_content = remove_code_language(html_content, language)


# Convert Markdown to HTML
html_content = markdown.markdown(html_content)

# Remove indentation from HTML
html_content = re.sub(r'\n\s+', '\n', html_content)


# Generate the index.html file
with codecs.open('index.html', mode='w', encoding='utf-8') as file:
    file.write(f'''<!DOCTYPE html>
<html>
<head>
    <title>Equivalent commands</title>
    <link rel="stylesheet" href="https://unpkg.com/2077-css/minified/main.min.css">
    <link rel="stylesheet" href="style.css">
</head>

<body>
<div id="content">
    {html_content}
</div>

<footer>
<p>nil+ .656e646f726d69</p>
</footer>
</body>
</html>''')
