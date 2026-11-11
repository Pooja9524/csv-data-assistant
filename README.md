# CSV Data Assistant

Point it at a CSV file and get a plain-English explanation of the dataset:
columns, data types, missing values, averages, and most common values.

Python reads **every row** and calculates the exact statistics. A Groq-hosted
LLM then explains those statistics in plain English. The model never sees the raw
rows and does no calculations, so the numbers are exact for any file size.

## How it works
```
CSV file --> profiler.py --> exact statistics --> explainer.py --> Groq LLM --> explanation
            (reads all rows)   (counts, averages,    (builds a short    (writes it in
                                missing values)        text summary)      plain English)
```

## Setup
Requires Python 3.9 or newer and a free Groq API key from https://console.groq.com.

1. Download the project (green **Code** button, then **Download ZIP**) and unzip it.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
   On Mac or Linux, use `source .venv/bin/activate` instead.
4. Install the libraries:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Create a file named `.env` in the project folder with:
   ```
   GROQ_API_KEY=your_key_here
   GROQ_MODEL=openai/gpt-oss-20b
   ```

## Run it in the terminal
With the virtual environment active (the prompt starts with `(.venv)`), run:
```bash
python main.py sample.csv
```
Use any CSV file name in place of `sample.csv`. The program reads the file,
prints the explanation, and exits. It is a one-shot command, not an interactive chat.

If you forget the file name, it shows how to use it:
```
Usage: python main.py yourfile.csv
```

Example output:
```
Reading sample.csv ...

The dataset contains 8 rows of sales data.
The region column has 4 distinct values, with South appearing 3 times, North 2 times, and West 2 times.
Quantity has one missing value, an average of 7.14, a minimum of 2, and a maximum of 20.
...
```

## Test on a large file
```bash
python big_csv.py          # creates big.csv with 100,000 rows
python profiler.py big.csv # exact statistics for all rows
python main.py big.csv     # full explanation
```

## Files
- `groq_client.py` - sends a request to the Groq API and returns the reply
- `profiler.py` - reads the CSV one row at a time and calculates the statistics
- `explainer.py` - turns the statistics into text and asks the model to explain them
- `main.py` - command-line entry point
- `big_csv.py` - generates a 100,000-row test file
- `sample.csv` - small example file

## Built with
Plain Python (standard library only: `csv`, `collections`), the `groq` SDK, and
`python-dotenv`. No pandas or other frameworks.

## Notes and limitations
- The model name is set in `.env` (`GROQ_MODEL`). It currently runs on a Groq-hosted
  model (`openai/gpt-oss-20b`). It can be switched to a Llama model if your Groq
  account has access to one.
- Never commit your `.env` file. It contains your API key.
- Date columns are treated as text, so no date range or trend is calculated.
- Only the most common values per text column are reported.
- The explanation wording comes from the LLM and can vary between runs, but the
  numbers come from Python.
