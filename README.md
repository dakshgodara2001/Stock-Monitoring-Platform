# Stock Monitoring Platform

The Stock Monitoring Platform is a real-time web application that allows users to monitor the latest stock prices from major companies.
It provides a user-friendly interface to select stocks and displays their current prices, previous close, open price, change, and volume.


https://github.com/dakshgodara2001/Stock-Monitoring-Platform/assets/52131905/d9d9f84b-1504-487e-96ae-e906967cbe96


## Features

- Real-time stock data: Get the latest stock prices from a wide selection of companies.
- Customizable dashboard: Select your preferred companies to view their stock prices.

## Setup and Installation

To set up the Stock Monitoring Platform on your local machine:

1. Clone the repository to your machine.
    ```
    git clone https://github.com/dakshgodara2001/stock-monitoring-platform.git
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
    DJANGO_SECRET_KEY='your_secret_key'
    ```

5. Set up the database.
    ```
    python manage.py migrate
    ```
    
6. Run the application.
    ```
    python manage.py runserver
    ```

The application will be available at `http://localhost:8000`.


7. Open another terminal or command prompt.


8. Start the Celery worker.
    ```
    celery -A stockmonitoring worker -l info

    ```

9. Open another terminal or command prompt.


10. Start the Celery beat:
    ```
    celery -A stockmonitoring beat -l info
    ```
    
The Celery worker and beat processes will now be running in the background, performing tasks and updating stock data at the scheduled intervals.


## About the API Used

The stock data is retrieved from the Alpha Vantage API. It provides access to real-time and historical stock market data, including stock quotes, intraday prices, and more. The API requires an API key for authentication, which needs to be obtained separately. The API key is stored in the `.env` file for security purposes.


## Design of the Application

The Stock Monitoring Platform follows a modern and user-friendly design. It includes the following key components:

- **Stock Picker**: Users can select stocks from a predefined list to monitor.
- **Real-time Updates**: Stock prices are updated in real-time using WebSocket communication.
- **Responsive Layout**: The application is designed to be responsive and accessible across different devices.
- **Interactive UI**: Users can view detailed information about each stock, including price, change, and volume.



## Back-End Code Documentation

The back-end code of this project is written in Python using the Django framework. Here's a brief overview of the main components:

- `models.py`: Contains the database models, including the `StockDetail` model for storing stock details and the association with users.

- `views.py`: Defines the views and API endpoints for handling user requests. It includes functions for stock tracking, authentication, and rendering HTML templates.

- `tasks.py`: Contains the Celery tasks for updating stock data asynchronously. It includes the `update_stock` task that retrieves stock quotes using the Alpha Vantage API.

- `consumers.py`: Defines the WebSocket consumer for real-time stock updates. It handles the WebSocket connections, subscribes to stock groups, and sends stock data to connected clients.

- `routing.py`: Configures the WebSocket routing for connecting to the WebSocket consumer.

- `asgi.py`: Configures ASGI settings for WebSocket communication.

- `celery.py`: Configures Celery settings for task scheduling and execution.

- `myfilters.py`: Contains custom template filters for extracting values from data dictionaries.



## Implementation Details

- The project uses Celery as a task queue and distributed task execution framework. Celery is integrated with Django using the `django-celery-beat` and `django-celery-results` packages.

- Redis is used as the broker and result backend for Celery. The `CELERY_BROKER_URL` setting is configured to use `redis://127.0.0.1:6379` as the Redis broker URL.

- Django Channels is used for WebSocket communication. The `CHANNEL_LAYERS` configuration in `settings.py` is set to use Redis as the backing store for Django Channels.


## Usage

Once the application is running:

1. Go to the main page.
2. Register if a new user otherwise Login.
3. Now go to StockPicker page.
4. Select your preferred stocks from the dropdown menu and submit.
5. The selected stocks will be displayed in a table and a scrolling ticker.


## Contact

If you have any questions or suggestions, please contact.
