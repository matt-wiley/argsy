from email.policy import default
import sys 
from argsy import Argsy


CLI_ARGS=dict(
        program=dict(
            name="argsy_test",
            description="cli_args_for_argsy_test"
        )
    )


def test_parses_program_level_option_arg_with_input_value():
    test_args_input=CLI_ARGS
    test_args_input.get("program")["args"] = dict(
                thing=dict(
                    cmd_type="option",
                    flags="-t|--thing",
                    help="Does a thing."
                )
            )
    argsy_parser=Argsy(config_dict=CLI_ARGS)

    parsed_args = argsy_parser.parse_args(['-t','t_value'],print_result=True)

    assert parsed_args.get('cmd') is None
    assert parsed_args.get('args').get('thing') == 't_value'


def test_parses_program_level_option_arg_with_default_value():
    test_args_input=CLI_ARGS
    test_args_input.get("program")["args"] = dict(
                thing=dict(
                    cmd_type="option",
                    flags="-t|--thing",
                    help="Does a thing.",
                    default="louise"
                )
            )
    argsy_parser=Argsy(config_dict=CLI_ARGS)

    parsed_args = argsy_parser.parse_args([],print_result=True)

    assert parsed_args.get('cmd') is None
    assert parsed_args.get('args').get('thing') == 'louise'

def test_parses_program_level_position_arg_with_input_value():
    test_args_input=CLI_ARGS
    test_args_input.get("program")["args"] = dict(
                thing=dict(
                    cmd_type="position",
                    help="Does a thing."
                )
            )
    argsy_parser=Argsy(config_dict=CLI_ARGS)

    parsed_args = argsy_parser.parse_args(['position_value'],print_result=True)

    assert parsed_args.get('cmd') is None
    assert parsed_args.get('args').get('thing') == 'position_value'

def test_parses_program_level_option_arg_with_store_true_action():
    test_args_input=CLI_ARGS
    test_args_input.get("program")["args"] = dict(
                thing=dict(
                    cmd_type="option",
                    flags="-t|--thing",
                    help="Does a thing.",
                    action="store_true"
                )
            )
    argsy_parser=Argsy(config_dict=CLI_ARGS)

    parsed_args = argsy_parser.parse_args(['-t'],print_result=True)

    assert parsed_args.get('cmd') is None
    assert parsed_args.get('args').get('thing') == True

def test_parses_multiple_program_level_args():
    test_args_input=CLI_ARGS
    test_args_input.get("program")["args"] = dict(
                thing_a=dict(
                    cmd_type="position",
                    help="Does thing A."
                ),
                thing_b=dict(
                    cmd_type="option",
                    flags="-b|--thing-b",
                    help="Does thing B."
                ),
                thing_c=dict(
                    cmd_type="option",
                    flags="-c|--thing-c",
                    help="Does thing C.",
                    action="store_true"
                ),
                thing_d=dict(
                    cmd_type="option",
                    flags="-d|--thing-d",
                    help="Does thing D.",
                    default="d_value"
                )
            )
    argsy_parser=Argsy(config_dict=CLI_ARGS)

    parsed_args = argsy_parser.parse_args(['a_value','-b','b_value','-c'],print_result=True)

    assert parsed_args.get('cmd') is None
    assert parsed_args.get('args').get('thing_a') == 'a_value'
    assert parsed_args.get('args').get('thing_b') == 'b_value'
    assert parsed_args.get('args').get('thing_c') == True
    assert parsed_args.get('args').get('thing_d') == 'd_value'