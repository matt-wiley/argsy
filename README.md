# argsy 

Tiny wrapper for Python's `argparse` package with YAML-based cli configuration.

## Overview

The `argsy` package aims to make CLI argument configuration and parsing declarative and simple, while still leveraging Python's `argparse` package to handle the parsing details and user help messaging.

Configuration supports declarative configuration of:

1. top-level position args, options / flags
2. a single tier of subcommands
3. position args, options / flags for each subcommand
4. support for setting default values for options / flags
5. partial `nvars` support for capturing multiple input values
6. support for the `action` directive (for things like toggling booleans)

## Getting Started

### Install `argsy`

```sh
pip install argsy>=1.0.0
```

### Define your program structure

CLI arguments are define as either:

1. a YAML file or string, or
2. a Python `dict` object

#### YAML file
```yaml
#
# my_cli_args.yml
# 
program:
  name: my_program
  descripton: "About what my_program does."
  args:
    option1:
      cmd_type: option
      flags: '-o|--option1'
      help: "Short text about the option."
      required: true
```

```python
#
# my_program.py
# 
from argsy import Argsy

argsy_parser = Argsy(config_file_name="my_cli_args.yml")
parsed_args = argsy_parser.parse_args(sys.argv[1:])

# User runs: 
#     my_program -o USER_PROVIDED_OPTION_VALUE
# 
# Resulting 'parsed_args':
# {
#   'cmd': None, 
#   'args': {
#     'option1': USER_PROVIDED_OPTION_VALUE
#   }
# }
```


#### YAML String
```python
#
# my_program.py
# 
from argsy import Argsy

CLI_ARGS = """
program:
  name: my_program
  descripton: "About what my_program does."
  args:
    option1:
      cmd_type: option
      flags: '-o|--option1'
      help: "Short text about the option."
      required: true
"""

argsy_parser = Argsy(config_str=CLI_ARGS)
parsed_args = argsy_parser.parse_args(sys.argv[1:])

# User runs: 
#     my_program -o USER_PROVIDED_OPTION_VALUE
# 
# Resulting 'parsed_args':
# {
#   'cmd': None, 
#   'args': {
#     'option1': USER_PROVIDED_OPTION_VALUE
#   }
# }
```



#### Python Dictionary

```python
#
# my_program.py
# 
from argsy import Argsy

CLI_ARGS = dict(
    program=dict(
        name='my_program',
        description='About what my_program does.',
        args=dict(
            option1=dict(
                cmd_type='option',
                flags='-o|--option1',
                help='Short text about the option.',
                required=True
            )
        )
    )
)

argsy_parser = Argsy(config_dict=CLI_ARGS)
parsed_args = argsy_parser.parse_args(sys.argv[1:])

# User runs: 
#     my_program -o USER_PROVIDED_OPTION_VALUE
# 
# Resulting 'parsed_args':
# {
#   'cmd': None, 
#   'args': {
#     'option1': USER_PROVIDED_OPTION_VALUE
#   }
# }
```
