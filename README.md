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

Follow these steps to set up your environment and prepare to run either the notebook or the script.

### 1. Clone the Repository
Download the project files to your computer:
```bash
git clone https://github.com/justinduckett/google-maps-geocoding-script.git
cd google-maps-geocoding-script
```
- **What this does**: This uses Git to copy the repository from GitHub to your local machine. You’ll need Git installed (download from [git-scm.com](https://git-scm.com/)).
- **If you don’t have Git**: Alternatively, click "Code" > "Download ZIP" on GitHub, then extract the ZIP file and navigate to the folder in a terminal or file explorer.

### 2. **Install Dependencies**:
   Install the required library using pip:
   ```bash
   pip install requests
   ```
   For the notebook, also install Jupyter:
   ```bash
   pip install notebook
   ```

### 3. Get a Google Maps API Key
- **Steps**:
  1. Go to [Google Cloud Console](https://console.cloud.google.com/).
  2. Create a project (or use an existing one).
  3. Enable the "Geocoding API" under APIs & Services > Library.
  4. Go to Credentials > Create Credentials > API Key.
  5. Copy the key (e.g., `xxxxxxxxxxxxxxxxx`) and keep it secure.
- **What this does**: The API key authenticates your requests to Google’s geocoding service.

### Summary
After these steps, you’ll have:
- The project files (`geocode_addresses.ipynb`, `geocode_addresses.py`).
- Python 3.x and `requests` installed.
- Jupyter (if using the notebook).
- An API key ready to use.

## Usage

### Option 1: Jupyter Notebook (`geocode_addresses.ipynb`)
1. **Prepare Your Input CSV**:
   - Create a CSV file (e.g., `addresses.csv`) with at least one column containing addresses.
   - Example:
     ```
     Address
     1600 Amphitheatre Parkway, Mountain View, CA
     1 Infinite Loop, Cupertino, CA
     ```
2. **Update the Notebook**:
   - Open it:
     ```bash
     jupyter notebook geocode_addresses.ipynb
     ```
   - Edit the last cell’s `input_file`, `output_file`, and `api_key` with your paths and key.
3. **Run**:
   - Click `Cell > Run All`. Output ends with:
     ```
     Geocoding complete. Results written to C:\path\to\your\output.csv
     ```

### Option 2: Python Script (`geocode_addresses.py`)
1. **Prepare Your Input CSV**:
   - Same as above.
2. **Update the Script**:
   - Edit `input_file`, `output_file`, and `api_key` in a text editor or IDE.
3. **Run**:
   - **Command Line**:
     ```bash
     python geocode_addresses.py
     ```
   - **VS Code**:
     - Open the folder, select Python interpreter, and click "Run."
   - Output:
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
- **API Key Security**: Don’t commit your API key. Use environment variables (e.g., `os.getenv("GOOGLE_API_KEY")`) for production.
- **Rate Limiting**: Uses `time.sleep(0.1)`—adjust if needed.
- **Error Handling**: Writes `None` for failed geocodes.

## Troubleshooting
- **API Errors**: Check API key and Geocoding API status in Google Cloud Console.
- **File Not Found**: Verify CSV path.
- **No Output**: Check terminal for errors.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with Python and the Google Maps Geocoding API.
- Created as a simple tool for geocoding address data.
