# Pyflask Todos
Todos application done using Python Flask with MongoDB

## Initial Setup

To install the Python packages specified in a `requirements.txt` file, you can use the `pip` package manager. The `requirements.txt` file typically lists all the dependencies and their versions that your Python project needs.

Here are the steps to install the requirements from a `requirements.txt` file:

1. **Navigate to your project directory:**

   Open a terminal or command prompt and navigate to the directory where your `requirements.txt` file is located.

2. **Activate a virtual environment (optional but recommended):**

   It's a good practice to create and activate a virtual environment to keep your project dependencies isolated. If you don't want to use a virtual environment, you can skip this step.

   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment
   # On Windows
   venv\Scripts\activate
   # On macOS and Linux
   source venv/bin/activate
   ```

3. **Install the requirements using pip:**

   Use `pip` to install the packages specified in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

   This command will read the `requirements.txt` file and install all the specified packages and their respective versions into your virtual environment.

4. **Verify the installation:**

   You can verify the installation by running:

   ```bash
   pip list
   ```

   This will display a list of installed packages, confirming that the packages from `requirements.txt` are installed.

5. **Deactivate the virtual environment (if used):**

   If you activated a virtual environment, you can deactivate it using the following command:

   ```bash
   deactivate
   ```

By following these steps, you will have successfully installed the Python packages specified in the `requirements.txt` file.

## Running the application

To run the application, run the command below in `pyflask-todos` folder.

```bash
 flask --app todoapp run --debug
```
