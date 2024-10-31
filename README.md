# Text Similarity Calculator

This Python script calculates the similarity between pairs of first names and last names from a CSV file. It uses the `difflib` library to compute the similarity ratio and flags pairs with an average similarity above a specified confidence score.

## Prerequisites

- Python 3.x
- `argparse` library (included in the Python standard library)
- `csv` library (included in the Python standard library)
- `difflib` library (included in the Python standard library)

## Installation

No additional packages are required for this script as it uses libraries included in the Python standard library.

## Usage

1. Prepare a CSV file with the following format:
    ```
    FirstName1,LastName1,FirstName2,LastName2
    สมพงษ์,สกุลดี,สมพง,สกุลด
    ประหยัดไท,สบายดี,ประหยัดไท,สบายดี
    ```

2. Run the script with the path to your CSV file as an argument:
    ```sh
    python text-similarity.py path/to/your/file.csv
    ```

## Example

Given a CSV file `names.csv` with the following content:
Running the script:
```sh
python text-similarity.py names.csv
```
```
John,Doe,Jon,Do,Y,85.00%
Jane,Smith,Janet,Smyth,N,65.00%
```
