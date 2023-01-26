# About

I don't always use VSCode. But when I do, I use Ultisnips.

This script allows you to write all of your snippets in vims Ultisnips format,
and convert the whole batch to json format for use in vscode.

# Installation

`pip install git+https://github.com/hrnggg/ultisnips-vscode.git`

# Usage

- Create a config file at any directory.
- Add the paths to your snippets folders. 
- On a mac this file might contain:

``` json
{
    "ultisnips-snippets":  "~/.vim/UltiSnips/",
    "vscode-snippets": "~/Library/Application Support/Code/User/snippets/"
}
```

- On linux this file might contain:


``` json
{
    "ultisnips-snippets":  "~/.config/nvim/UltiSnips",
    "vscode-snippets": "~/.config/Code/User/snippets/"
}
```

- Run the command `ultisnips2vscode </path/to/config>` to synchronize your snippets. This will
  output something like:

``` 
sh.snippets                    -->        shellscript.json
python.snippets                -->        python.json
all.snippets                   -->        global.code-snippets
texmath.snippets               -->        doconce.json
doconce.snippets               -->        doconce.json
gitcommit.snippets             -->        git-commit.json
zsh.snippets                   -->        shellscript.json
json.snippets                  -->        json.json
html.snippets                  -->        html.json
c.snippets                     -->        c.json
texmath.snippets               -->        latex.json
tex.snippets                   -->        latex.json
texmath.snippets               -->        markdown.json
markdown.snippets              -->        markdown.json
```
