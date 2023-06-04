# BBB23 Twitter Data Processing

This repository contains a script for processing Twitter data related to the BBB23 Final. The script separates the tweets by participant and generates graphics based on the tweet data.

## Authors
- Anderson Sprenger
- Gabriel Souza
- Vinicius Dias

## Getting Started
To use this script, follow the instructions below:

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Obtain the `coleta_bbb_pt_new.json` file containing the Twitter data for the BBB23 Final.
4. Place the `coleta_bbb_pt_new.json` file in the root directory of the repository.
5. Run the script using a Python interpreter.

## Prerequisites
- Python 3.x
- JSON library

## Usage
1. Execute the script by running `python process_tweets.py`.
2. The script will read the `coleta_bbb_pt_new.json` file and process the Twitter data.
3. The tweets will be separated and saved into individual files based on the participants' names.
4. The generated files will be stored in the `participantes` directory.
5. Each file will contain the tweets corresponding to a specific participant.
6. The file names will match the participants' names.

## Notes
- Ensure that the `coleta_bbb_pt_new.json` file is present in the root directory before running the script.
- The generated files in the `participantes` directory will be overwritten each time the script is executed.
- The script uses the JSON library to load and save data in the JSON format.

Feel free to explore and modify the script to suit your specific needs. If you have any questions or encounter any issues, please contact us via email: anderson.sprenger@edu.pucrs.br.

Happy processing!
