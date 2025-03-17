# Geocoding Addresses with Google Maps API

This repository contains tools to geocode addresses from a CSV file using the Google Maps Geocoding API. Two versions are provided:
- **`geocode_addresses.ipynb`**: A Jupyter Notebook for interactive use, ideal for data exploration or demos.
- **`geocode_addresses.py`**: A standalone Python script for command-line or IDE execution, suitable for automation or production.

Both versions read a list of addresses, fetch latitude and longitude coordinates via the API, and write the results to a new CSV file.

## Features
- Takes a CSV file with addresses as input.
- Uses the Google Maps Geocoding API to fetch coordinates.
- Outputs a new CSV file with appended `Latitude` and `Longitude` columns.
- Includes basic rate limiting to avoid exceeding API quotas.

## Prerequisites
- **Python 3.x**: Ensure Python is installed on your system.
- **Google Maps API Key**: Obtain an API key from Google Cloud Platform with the Geocoding API enabled.
- **Dependencies**: Both files require:
  - `csv` (built-in)
  - `requests`
  - `time` (built-in)
- **For the Notebook**: Jupyter Notebook or JupyterLab installed.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/justinduckett/google-maps-geocoding-script.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   Install the required library using pip:
   ```bash
   pip install requests
   ```
   For the notebook, also install Jupyter:
   ```bash
   pip install notebook
   ```

## Usage

### Option 1: Jupyter Notebook (`geocode_addresses.ipynb`)
Best for interactive use or learning.

1. **Prepare Your Input CSV**:
   - Create a CSV file (e.g., `addresses.csv`) with at least one column containing addresses.
   - Example format:
     ```
     Address
     1600 Amphitheatre Parkway, Mountain View, CA
     1 Infinite Loop, Cupertino, CA
     ```

2. **Update the Notebook**:
   - Open the notebook in Jupyter:
     ```bash
     jupyter notebook geocode_addresses.ipynb
     ```
   - In the last code cell, modify:
     - `input_file`: Replace `C:\\Users\\fake_user\\python_files\\addresses.csv` with your input CSV path.
     - `output_file`: Replace `C:\\Users\\fake_user\\python_files\\addresses_geocoded.csv` with your output path.
     - `api_key`: Replace `'xxxxxxxxxxxxxxxxx'` with your Google Maps API key.

3. **Run the Notebook**:
   - Execute all cells (`Cell > Run All` or use the play button).
   - Output will appear below the cells, ending with a message like:
     ```
     Geocoding complete. Results written to C:\path\to\your\output.csv
     ```

### Option 2: Python Script (`geocode_addresses.py`)
Best for automation or running in a terminal/IDE.

1. **Prepare Your Input CSV**:
   - Same as above.

2. **Update the Script**:
   - Open `geocode_addresses.py` in a text editor or IDE (e.g., VS Code).
   - In the `if __name__ == "__main__":` block, modify:
     - `input_file`, `output_file`, and `api_key` as described above.

3. **Run the Script**:
   - **Via Command Line**:
     ```bash
     python geocode_addresses.py
     ```
   - **Via Visual Studio Code**:
     - Install VS Code and the Python extension.
     - Open the folder in VS Code (`File > Open Folder`).
     - Select your Python interpreter (`Ctrl+Shift+P` > "Python: Select Interpreter").
     - Click the "Run" button (green triangle) or right-click and select "Run Python File in Terminal."
   - Output will appear in the terminal, e.g.:
     ```
     Geocoding complete. Results written to C:\path\to\your\output.csv
     ```

## Example Output
Input (`addresses.csv`):
```
Address
1600 Amphitheatre Parkway, Mountain View, CA
```

Output (`addresses_geocoded.csv`):
```
Address,Latitude,Longitude
1600 Amphitheatre Parkway, Mountain View, CA,37.4224764,-122.0842499
```

## Notes
- **API Key Security**: Do not commit your API key to the repository. Consider using environment variables (e.g., `api_key = os.getenv("GOOGLE_API_KEY")`) and a `.env` file for production use.
- **Rate Limiting**: Both versions include a 0.1-second delay between API calls (`time.sleep(0.1)`). Adjust if needed based on your API quota.
- **Error Handling**: If an address fails to geocode, `None` is written for the coordinates.

## Troubleshooting
- **API Errors**: Verify your API key is valid and the Geocoding API is enabled in Google Cloud Console.
- **File Not Found**: Check your input file path.
- **No Output**: Ensure the script/notebook ran to completion and check for errors in the console/terminal.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with Python and the Google Maps Geocoding API.
- Created as a simple tool for geocoding address data.
