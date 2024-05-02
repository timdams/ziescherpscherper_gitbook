```shell
    "git.openRepositoryInParentFolders": "never",
        "command-runner.terminal.name": "runCommand",
        "command-runner.terminal.autoClear": true,
        "command-runner.terminal.autoFocus": true,
        "command-runner.commands": 
        {
            "build pandoc preview": "pandoc metadata.yaml ${file} -o temp.pdf --resource-path=assets --template templates\\tempeisvogel.latex --number-sections --from markdown --listings --variable toc-own-page=true --variable book=true --top-level-division=chapter  --filter pandoc-latex-environment --self-contained --verbose ; code temp.pdf",
            "echo workspaceFolder": "echo ${workspaceFolder}",
            "echo file": "echo ${file}"
        }
```