import getpass
import sys
import inspect
import argparse

VALID_BROWSERS = ['chrome', 'firefox']
BAD_USERNAME_CHARS = '_!?@#~ '


def get_args_from_cmd_line() -> argparse.Namespace:
    parser = argparse.ArgumentParser("Download course materials from Canvas Online Learning Platform.")
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument(
        "-b",
        "--browser",
        help=f"Which browser is used for interacting with Canvas? Acceptable values include: {VALID_BROWSERS}",
        type=str,
        required=True
    )
    optional.add_argument(
                            "-gui",
                            "--use_gui",
                            help="Run with GUI? If this flag is omitted then headless is assumed",
                            action="store_true"
    )
    optional.add_argument(
                            "-up",
                            "--username_password",
                            help="Provide your Canvas login credentials on the command line. If not provided here, you"
                                 " will be prompted for them shortly. Ex: -cred jsmith32 pa$$word",
                            nargs=2,
                            type=str
    )
    optional.add_argument(
                            "-sch",
                            "--school",
                            help="School subdomain, default: asu",
                            default="asu",
                            type=str,
    )
    return parser.parse_args()


def add_user_pass_if_not_provided(args):
    if not args.username_password:
        print("Username and password were not provided earlier, please provide them now.")
        username = input("Canvas Username: ")
        password = getpass.getpass("Canvas Password: ")
        args.username_password = [username, password]


def validate_cmd_line_args(args):
    this_mod = sys.modules[__name__]
    validators = [func for name, func in inspect.getmembers(this_mod, inspect.isfunction) if name.endswith("is_valid")]
    for validator in validators:
        is_valid, reason = validator(args)
        if not is_valid:
            print(f'{reason}')
            sys.exit(1)


def browser_is_valid(args: argparse.Namespace) -> (bool, str):
    is_valid = args.browser.lower() in VALID_BROWSERS
    reason = '' if is_valid else f'{args.browser} is not a valid browser. You must provide one of: {VALID_BROWSERS}'
    return is_valid, reason


def username_is_valid(args: argparse.Namespace) -> (bool, str):
    is_valid = not any(ch in args.username_password[0] for ch in BAD_USERNAME_CHARS)
    reason = '' if is_valid else f'Username {args.username_password[0]} contains invalid characters'
    return is_valid, reason


def get_and_validate_args() -> argparse.Namespace:
    args = get_args_from_cmd_line()
    add_user_pass_if_not_provided(args)
    validate_cmd_line_args(args)
    return args


if __name__ == '__main__':
    get_and_validate_args()
