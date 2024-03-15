"""
Hook configuration files for COSIPY.
"""

import argparse
import sys
from collections import namedtuple

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib  # backwards compatibility


def get_user_arguments() -> argparse.Namespace:
    """Parse user arguments when run as main.

    Optional switches:
        -h, --help              Show this help message and exit.

    Optional arguments:
        -c, --config <str>      Relative path to configuration file.
        -x, --constants <str>   Relative path to constants file.
        -s, --slurm <str>       Relative path to slurm configuration
                                file.

    Returns:
        Namespace of user arguments.
    """

    tagline = "Coupled snowpack and ice surface energy and mass balance model in Python."
    parser = argparse.ArgumentParser(prog="cosipy", description=tagline)

    # Optional arguments
    parser.add_argument(
        "-c",
        "--config",
        default="./config.toml",
        dest="config_path",
        type=str,
        metavar="<path>",
        required=False,
        help="relative path to configuration file",
    )

    parser.add_argument(
        "-x",
        "--constants",
        default="./constants.toml",
        dest="constants_path",
        type=str,
        metavar="<path>",
        required=False,
        help="relative path to constants file",
    )

    parser.add_argument(
        "-s",
        "--slurm",
        default="./slurm_config.toml",
        dest="slurm_path",
        type=str,
        metavar="<path>",
        required=False,
        help="relative path to Slurm configuration file",
    )

    arguments = parser.parse_args()

    return arguments


class TomlLoader(object):
    """Load and parse configuration files."""

    @staticmethod
    def get_raw_toml(file_path: str = "./config.toml") -> dict:
        """Open and load .toml configuration file.

        Args:
            file_path: Relative path to .toml configuration file.

        Returns:
            Loaded .toml data.
        """
        with open(file_path, "rb") as f:
            raw_config = tomllib.load(f)

        return raw_config

    @classmethod
    def set_config_values(cls, config_table: dict):
        """Overwrite attributes with configuration data.

        Args:
            config_table: Loaded .toml data.
        """
        for _, table in config_table.items():
            for k, v in table.items():
                setattr(cls, k, v)


class Config(TomlLoader):
    """Model configuration.

    Loads, parses, and sets model configuration for COSIPY from a valid
    .toml file.
    """

    def __init__(self):
        args = get_user_arguments()
        self.load(args.config_path)

    @classmethod
    def load(cls, path: str = "./config.toml"):
        raw_toml = cls.get_raw_toml(path)
        parsed_toml = cls.set_correct_config(raw_toml)
        cls.set_config_values(parsed_toml)

    @classmethod
    def set_correct_config(cls, config_table: dict) -> dict:
        """Adjust invalid or mutually exclusive configuration values.

        Args:
            config_table: Loaded .toml data.

        Returns:
            Adjusted .toml data.
        """
        # WRF Compatibility
        if config_table["DIMENSIONS"]["WRF"]:
            config_table["DIMENSIONS"]["northing"] = "south_north"
            config_table["DIMENSIONS"]["easting"] = "west_east"
        if config_table["DIMENSIONS"]["WRF_X_CSPY"]:
            config_table["FULL_FIELDS"]["full_field"] = True
        # TOML doesn't support null values
        if config_table["PARALLELIZATION"]["workers"] == 0:
            config_table["PARALLELIZATION"]["workers"] = None

        return config_table


class SlurmConfig(TomlLoader):
    """Slurm configuration.

    Loads, parses, and sets Slurm configuration for COSIPY from a valid
    .toml file.

    Attributes:
        account (str): Slurm account/group, equivalent to Slurm
            parameter `--account`.
        name (str): Equivalent to Slurm parameter `--job-name`.
        project (str): Project name.
        queue (str): Queue name.
        port (int): Network port number.
        cores (int): One grid point per core, do not change.
        nodes (str): Grid points submitted in one sbatch script.
        processes (int): Number of processes.
        memory (str): Memory per process.
        shebang (str): Shebang string.
        slurm_parameters (List[str]): Additional Slurm parameters.
    """

    def __init__(self):
        args = get_user_arguments()
        self.load(args.slurm_path)

    @classmethod
    def load(cls, path: str = "./slurm_config.toml"):
        raw_toml = cls.get_raw_toml(path)
        parsed_toml = cls.set_correct_config(raw_toml)
        cls.set_config_values(parsed_toml)

    @classmethod
    def set_correct_config(cls, config_table: dict) -> dict:
        """Adjust invalid or mutually exclusive configuration values.

        Args:
            config_table: Loaded .toml data.

        Returns:
            Adjusted .toml data.
        """
        if config_table["OVERRIDES"]["memory_per_process"]:
            memory = (
                config_table["OVERRIDES"]["memory_per_process"]
                * config_table["MEMORY"]["cores"]
            )
            config_table["MEMORY"]["memory"] = f"{memory}GB"

        return config_table


def main():
    args = get_user_arguments()
    Config.load(args.config_path)
    SlurmConfig.load(args.slurm_path)


if __name__ == "__main__":
    main()
else:
    main()
