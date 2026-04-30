# S&P 500 Trading Signals

Professional platform for S&P 500 market analysis and trading signal generation using machine learning.

## 🚀 Overview
This project provides tools to download S&P 500 historical data, process technical indicators, and generate trading signals using both statistical methods and machine learning models.

## 📂 Project Structure
- `data/`: Raw and processed market data.
- `notebooks/`: Jupyter Notebooks for exploration and model prototyping.
- `src/`: Core source code for data ingestion, feature engineering, and signal generation.
- `reports/`: Performance reports, plots, and analysis results.
- `requirements.txt`: Project dependencies.

## 🛠️ Installation

### Prerequisites
- Python 3.8+

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Ing-ManuelDiaz/sp500-trading-signals.git
   cd sp500-trading-signals
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Tech Stack
- **Data:** `yfinance`, `pandas`
- **Visualization:** `matplotlib`
- **Machine Learning:** `scikit-learn`
- **Environment:** `Jupyter Notebook`

## 📈 Usage
Run the data loader to fetch the latest S&P 500 data:
```bash
python src/data_loader.py
```
