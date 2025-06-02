# Mange cows

Que tal ver vacas falantes em seu terminal? O comando `cowsay` ou `cowthink` transformará texto em vacas felizes no formato ASCII, com balões de fala ou de pensamento. Se você não gosta de vacas, outras artes ASCII estão disponíveis para substituí-la por outras criaturas (Tux, o demônio do BSD, dragões e uma gama de animais, de um peru a um elefante em uma cobra). 

Para listar os formatos disponíveis, execute o comando:

- `cowsay -l`

Este comando gerará a seguinte saída:

```
Cow files in /usr/share/cowsay/cows:
apt bud-frogs bunny calvin cheese cock cower daemon default dragon
dragon-and-cow duck elephant elephant-in-snake eyes flaming-sheep fox
ghostbusters gnu hellokitty kangaroo kiss koala kosh luke-koala
mech-and-cow milk moofasa moose pony pony-smaller ren sheep skeleton
snowman stegosaurus stimpy suse three-eyes turkey turtle tux unipony
unipony-smaller vader vader-koala www
```

Para colocar um balão com uma mensagem para seu personagem escolhido, execute:

- `cowsay -f FORMATO "MENSAGEM"`

Substitua *FORMATO* por um dos formatos listados anteriormente e substitua *"MENSAGEM"* por uma mensagem qualquer. Lembre-se das aspas duplas.


```{toctree}
---
maxdepth: 1
caption: Formas disponíveis
glob: 
---

formas/*
```
