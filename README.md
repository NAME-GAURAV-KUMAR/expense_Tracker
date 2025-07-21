# Expense Tracker

A simple web-based Expense Tracker application built with Flask (Python), HTML, CSS, and JavaScript. This application allows users to add, view, and delete expenses, and keeps track of their remaining balance.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Database Configuration](#database-configuration)
- [Styling](#styling)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Add Expenses**: Easily add new expenses with a title, amount, and date.
- **View Expenses**: See a list of all recorded expenses.
- **Delete Expenses**: Remove unwanted expenses from the list.
- **Track Balance**: Displays the initial balance and dynamically updates the remaining balance after adding or deleting expenses.
- **Responsive Design**: The application is styled to be user-friendly on various screen sizes.

## Project Structure

The project follows a standard Flask application structure:
EXPENSE TRACKER/
├── static/
│   ├── script.js
│   └── style.css
├── templates/
│   └── index.html
└── app.py
- `app.py`: The main Flask application file, handling routes, database interactions, and API endpoints.
- `templates/index.html`: The main HTML file for the user interface.
- `static/script.js`: Contains the JavaScript code for frontend functionality (adding, deleting, and displaying expenses, updating balance).
- `static/style.css`: Contains the CSS for styling the application.

## Technologies Used

-   **Backend**: Python (Flask)
-   **Frontend**:
    -   HTML5
    -   CSS3
    -   JavaScript
-   **Database**: MySQL (using `mysql.connector`)

## Setup and Installation

Follow these steps to get the project up and running on your local machine:

1.  **Clone the Repository (if applicable)**:
    ```bash
    git clone <repository_url>
    cd Expense-Tracker # or whatever your project directory is named
    ```

2.  **Create a Virtual Environment**:
    It's recommended to use a virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**:
    -   **On Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    -   **On macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies**:
    Install the required Python packages using pip.
    ```bash
    pip install Flask mysql-connector-python
    ```

5.  **Database Setup**:
    This application uses MySQL. You need to have a MySQL server running.

    -   **Create a Database**: Open your MySQL client (e.g., MySQL Workbench, command line) and create a database named `org`.
        ```sql
        CREATE DATABASE org;
        ```
    -   **Configure Database Credentials**: In `app.py`, update the `get_db_connection` function with your MySQL credentials:
        ```python
        def get_db_connection():
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Saurav00@', # <--- CHANGE THIS TO YOUR MYSQL PASSWORD
                database='org'
            )
            return conn
        ```
    -   The `init_db()` function in `app.py` will automatically create the `expenses` table when the application starts if it doesn't already exist.

## Usage

1.  **Run the Flask Application**:
    Navigate to the project's root directory (where `app.py` is located) in your terminal and run:
    ```bash
    python app.py
    ```
    You should see output similar to this, indicating the server is running:
    ```
     * Serving Flask app 'app'
     * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)
    Press CTRL+C to quit
    ```

2.  **Access the Application**:
    Open your web browser and go to the URL displayed in the terminal (e.g., `http://127.0.0.1:5000/`).

3.  **Interact with the Expense Tracker**:
    -   Use the form to add new expenses.
    -   View your expenses in the list below the form.
    -   Click the "Delete" button next to an expense to remove it.
    -   The "Remaining Balance" will update automatically.

## Database Configuration

The `app.py` file connects to a MySQL database. Ensure your MySQL server is running and you have configured the database name (`org`) and user credentials (`root`, `Saurav00@`) correctly in the `get_db_connection()` function.

The `expenses` table will be created automatically upon the first run of the application if it doesn't exist, with the following schema:

```sql
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    amount FLOAT NOT NULL,
    date DATE NOT NULL
);
Styling
The style.css file provides a modern and clean design for the application, featuring:

Deep blue background for the body.

Light blue-white main container with rounded corners and subtle shadows.

Gradient blue "Balance" section for prominence.

Clean form styling with focus effects.

Expenses displayed as "cards" within a table structure, optimized for readability.

Accent pink/red for the "Add Expense" button and expense amounts.

API Endpoints
The Flask application exposes the following API endpoints:

GET /api/expenses: Retrieves all expenses from the database.

POST /api/expenses: Adds a new expense to the database.

Request Body (JSON): {"title": "Expense Title", "amount": 50.00, "date": "YYYY-MM-DD"}

DELETE /api/expenses/<int:id>: Deletes an expense by its ID.

GET /api/balance: Calculates and returns the remaining balance.

Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature/your-feature-name).

Open a Pull Request.

License
This project is open source and available under the MIT License.
