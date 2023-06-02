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
pip install pettingzoo[atari]
pip install "autorom[accept-rom-license]"
AutoROM
```

Run example:
```shell
python petting_zoo/env_interaction.py --category atari --env double_dunk_v3
```

### Butterfly

Ref: https://pettingzoo.farama.org/environments/butterfly/

Installation steps:
```shell
pip install pettingzoo[butterfly]
```

Run example:
```shell
python petting_zoo/env_interaction.py --category butterfly --env pistonball_v6
```