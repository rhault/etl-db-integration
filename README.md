# PDF Data Extraction for Power BI

## Description
This project aims to solve an ETL (Extract, Transform, Load) problem for a Power BI dashboard. The data is in a poorly formatted PDF, making direct extraction difficult. After testing AI-based solutions without success, I developed a Python script to extract, process, and save the data into a CSV file that can be imported into Power BI.

## Technologies Used
- Python 3.x
- [PyPDF2](https://pypdf2.readthedocs.io/) for text extraction from PDFs
- Regular expressions (regex) for data standardization
- CSV for storing extracted data
- Power BI for data visualization

## Installation and Usage
### 1. Clone the Repository
```sh
 git clone https://github.com/rhault/etl-db-integration.git
 cd etl-db-integration
```

### 2. Install Dependencies
Ensure Python is installed, then install the necessary dependencies:
```sh
pip install PyPDF2
```

### 4. Run the Script
```sh
python main.py
```
This will generate a CSV file (e.g., `JANUARY2025.csv`) with the extracted and processed data.

## Project Structure
```
/
|-- main.py        # Main script for data extraction and processing
|-- JANUARY2025.pdf  # Source PDF file (example)
|-- header.csv       # File containing the column headers for the final CSV
```

## Code Explanation
The script follows these steps:
1. **Text Extraction**: Uses `PyPDF2` to extract text from each page of the PDF.
2. **Text Processing**: Applies regex to identify relevant patterns such as product codes, dates, and document numbers.
3. **Data Structuring**: Organizes the information in a structured format, separating client and product names.
4. **CSV Export**: Writes the structured data into a CSV file ready for Power BI import.

## License
This project is licensed under the [MIT License](LICENSE).

