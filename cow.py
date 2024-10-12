import cowsay
import sys
import argparse

def greet(name: str) -> None:
    """
    Print a greeting using the cowsay trex.

    Args:
        name (str): The name to greet.
    """
    cowsay.trex(f"Hello, {name}!")

def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments with the name.
    """
    parser = argparse.ArgumentParser(
        description="Greet the user with a T-Rex."
    )
    parser.add_argument(
        "name",
        type=str,
        help="Name of the person to greet."
    )
    return parser.parse_args()

def main() -> None:
    """
    Main function to run the script.
    """
    args = parse_args()
    greet(args.name)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
