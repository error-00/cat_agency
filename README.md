Here’s an updated version of the README that includes a section for the requirements.txt file:

# Mission and Target Management Application

This application is a RESTful API built with Django and Django REST Framework to manage missions and their associated targets.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/error-00/cat_agency.git
   cd cat_agency

2. **Create a virtual environment**:
   ```bash
    python -m venv venv

3. **Activate the virtual environment**:
	•	On Windows:
    ```bash
    venv\Scripts\activate
    
  •	On macOS/Linux:
    ```bash
    source venv/bin/activate

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt

5. **Set up the database**:
	•	Apply migrations:
    ```bash
    python manage.py migrate

5. **Run the application**:
    ```bash
    python manage.py runserver

  The application will be available at http://127.0.0.1:8000/.


## Usage

You can manage cats, missions and targets using the defined API endpoints. Use Postman or any API client to interact with the application.

API Endpoints

	•	GET /missions/ - List all missions
	•	POST /missions/create/ - Create a new mission
	•	GET /missions/{id}/ - Retrieve a specific mission
	•	PUT /missions/update/{id}/ - Update a specific mission
	•	DELETE /missions/delete/{id}/ - Delete a specific mission
	•	GET /cats/: Lists all cats.
	•	POST /cats/create/: Creates a new cat.
	•	GET /cats/{id}/: Retrieves a specific cat based on its ID.
	•	PUT /cats/update/{id}/: Updates the information of a specific cat.
	•	DELETE /cats/delete/{id}/: Deletes a specific cat by ID.



## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.
