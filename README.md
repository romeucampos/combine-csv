# CSV Combiner with python

This Python script efficiently combines multiple CSV files into a single file using DuckDB, ensuring data consistency and allowing for the option to include distinct rows only.

## Prerequisites

- **Python 3**: Ensure Python 3 is installed on your system. This script has been tested with Python 3.10 and above. You can download Python from [python.org](https://www.python.org/downloads/).

## Getting Started

Follow these steps to get started with the CSV Combiner:

### 1. Clone the Repository

First, clone this repository to your local machine using Git. Open a terminal and run the following command:

```bash
git clone https://github.com/romeucampos/combine-csv.git
cd csv-combiner
```

### 2. Install Dependencies

The script requires DuckDB to run. You can install the required package using the provided `requirements.txt` file. In the project directory, execute:

```bash
pip install -r requirements.txt
```

This command installs all necessary Python packages listed in `requirements.txt`.

### 3. Running the Script

To run the script, use the following command in the terminal:

```bash
python combine_csv.py
```

Make sure to adjust the `path` variable inside `combine_csv.py` to point to the directory containing your CSV files. The script is configured to work across both Windows and Linux systems.

## Configuration

- **path**: Set to the directory where your CSV files are located.
- **extension**: Set to `"csv"` for CSV files or `"parquet"` for Parquet files.
- **distinct**: Use `"distinct"` to select unique rows only, or leave as `""` to include all rows.

## Output

The script combines all specified files into a single file named `combined_{extension}.{extension}`, located in the same directory as the input files.