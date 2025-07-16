Running Automated Tests for DynamiSpectra
=========================================

This guide explains how to run the automated tests of the DynamiSpectra package after cloning it from GitHub.

1. Clone the repository
-----------------------

Open your terminal (command prompt) and run:

.. code-block:: bash

    git clone https://github.com/Conradoou/DynamiSpectra.git

This will download the full project, including the test data.

2. Change to the project directory
----------------------------------

.. code-block:: bash

    cd DynamiSpectra

3. (Optional but recommended) Create and activate a virtual environment
-----------------------------------------------------------------------

- On Linux/macOS:

  .. code-block:: bash

      python3 -m venv venv
      source venv/bin/activate

- On Windows:

  .. code-block:: powershell

      python -m venv venv
      .\venv\Scripts\activate

4. Install required dependencies
--------------------------------

Install all required Python packages using:

.. code-block:: bash

    pip install -r requirements.txt

5. Install DynamiSpectra in editable mode
-----------------------------------------

This allows running the package locally with the latest changes:

.. code-block:: bash

    pip install -e .

6. Run the automated tests
--------------------------

Execute all tests with:

.. code-block:: bash

    pytest

To run a specific test file, for example the pressure analysis test:

.. code-block:: bash

    pytest tests/test_pressure.py

7. Check the test results
-------------------------

- If all tests pass, you will see output indicating no failures.
- If any test fails, pytest will display the error details for troubleshooting.

Notes
-----

- The test scripts use data files inside the `data/` folder, so keep this folder intact.
- Make sure you have `pytest` installed; it is included in `requirements.txt`.
- Inside the `tests/` folder, there is a subfolder named `Test results` that contains images of the expected output plots. You can visually compare these images with the plots generated during the test runs to confirm the results.
