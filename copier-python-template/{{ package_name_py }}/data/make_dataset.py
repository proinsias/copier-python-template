"""Turn raw data into a cleaned, analysis-ready dataset."""

import logging
from pathlib import Path

import click
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath: str, output_filepath: str) -> None:
    """Run data processing scripts.

    Turns raw data from (../raw) into cleaned data ready to be analyzed
    (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info(
        "making final data set at %s from raw data from %s",
        output_filepath,
        input_filepath,
    )


if __name__ == "__main__":
    LOG_FMT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
