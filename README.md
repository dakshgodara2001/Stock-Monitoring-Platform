# Stock Monitoring Platform

The Stock Monitoring Platform is a real-time web application that allows users to monitor the latest stock prices from major companies.

## Features

- Real-time stock data: Get the latest stock prices from a wide selection of companies.
- Customizable dashboard: Select your preferred companies to view their stock prices.
- Stock ticker: View the latest stock prices in a scrolling ticker, just like in a stock exchange.

## Setup and Installation

To set up the Stock Monitoring Platform on your local machine:

1. Clone the repository to your machine.
    ```
    git clone https://github.com/yourusername/stock-monitoring-platform.git
    ```

2. Navigate to the project directory.
    ```
    cd stock-monitoring-platform
    ```

3. Install the necessary packages.
    ```
    pip install -r requirements.txt
    ```

4. Create a `.env` file at the project root and add your AlphaVantage API key:
    ```
    ALPHA_VANTAGE_API_KEY=your_api_key
    ```

5. Run the application.
    ```
    python manage.py runserver
    ```

The application will be available at `http://localhost:8000`.

## Usage

Once the application is running:

1. Go to the main page.
2. Select your preferred stocks from the dropdown menu and submit.
3. The selected stocks will be displayed in a table and a scrolling ticker.

## Contributing

We welcome contributions to the Stock Monitoring Platform! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or suggestions, please open an issue on GitHub.
