# VaxuraUniProt: Organism Proteins Cellular Location Extractor

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python 3.8](https://img.shields.io/badge/Python-3.8-blue.svg) ![License MIT](https://img.shields.io/badge/license-MIT-green)

This repository contains a Python script based on the work of the [VaxuraUniProt](https://github.com/ahorazahedi/VaxuraUniProt) project. It connects to UniProtKB, retrieves reviewed proteins information for a specific organism, extracts their cellular location, and saves the data in a CSV file.

## Table of Contents
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Prerequisites](#prerequisites)
- [Installing](#installing)
- [Running the tests](#running-the-tests)
- [Built With](#built-with)
- [Contributing](#contributing)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

You can Use DownloaderUniprot.ipynb to Use This code on Google Colab For Faster Network Connection Dont Forget To Connect Google Drive To colab First
### Prerequisites

Ensure that you have the following installed on your local machine:

```
Python 3.8 or later
pip (Python Package Installer)
```

### Installing

Clone the repo to your local machine:

```bash
git clone https://github.com/ahorazahedi/VaxuraUniProt.git
```

Go to the project directory:

```bash
cd VaxuraUniProt
```

Install the necessary packages:

```bash
pip install biopython
```

## Usage

To run the script, you can use the command below.Update Organisms.txt Based on its Default Format And Get Results in Download Folder It Also Zip When all jobs are Done To Make its Transfer Easily

```bash
python Downloader.py
```

This will create a CSV file named `uniprot_<organism>_proteins.csv` in the current directory.

## Running the tests

(Add information about how to run tests if available)

## Built With

- [Python 3.8](https://www.python.org/)
- [Biopython](https://biopython.org/)
- [UniProt API](https://www.uniprot.org/help/api)

## Contributing

Please read [CONTRIBUTING.md](https://github.com/ahorazahedi/VaxuraUniProt/blob/main/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/ahorazahedi/VaxuraUniProt/tags).

## Authors

- **Ahora Zahedi** - *Initial work* - [Your GitHub Username](https://github.com/ahorazahedi)

See also the list of [contributors](https://github.com/ahorazahedi/VaxuraUniProt/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/ahorazahedi/VaxuraUniProt