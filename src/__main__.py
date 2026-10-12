from .io_utils import load_csv_to_dataframe
from .schemas import PathConfig


def main():
    config = PathConfig()
    config.ensure_directories()

    file_path = config.input_dir / "creditcard.csv"

    df = load_csv_to_dataframe(file_path)


if __name__ == "__main__":
    main()