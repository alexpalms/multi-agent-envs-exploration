# Multi Agent Environments Tests
Tests with Multi Agent environments


## Petting Zoo

Ref: https://pettingzoo.farama.org/content/basic_usage/

### Atari

Refs:
  - https://pettingzoo.farama.org/environments/atari/
  - https://github.com/Farama-Foundation/AutoROM

Installation steps:
```shell
pip install petting-zoo[atari]
pip install "autorom[accept-rom-license]"
AutoROM
```

Run example:
```shell
python petting_zoo_atari/env_interaction.py --game double_dunk_v3
```
