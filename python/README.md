# Dicas de DEV para python

## PyEnv

Para gerenciar várias versões do python fácilmente

## Dependency Tree

Lista as dependência de um .env python em forma de árvore

### Listar a dependency tree

```
pipdeptree -fl
```

### Gerar o requirements.txt apenas com as dependências base

Windows - Powershell
```
pipdeptree --freeze  --warn silence |  Select-String -Pattern "^[\w0-9\-=.]+" > requirements.txt
```

Linux
```
pipdeptree --freeze  --warn silence | grep -P '^[\w0-9\-=.]+' > requirements.txt
```
pipdeptree --freeze  --warn silence |  Select-String -Pattern "^[\w0-9\-=.]+" > requirements.txt