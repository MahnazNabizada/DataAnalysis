# Dash Basics — HTML Core Components

A beginner-friendly Dash application demonstrating the fundamentals of building interactive web applications with **Python, Dash, and Plotly**. This project focuses on Dash HTML components, application layout, and running a Dash development server locally.

## 📋 Project Overview

This project is part of a hands-on data visualization exercise and demonstrates how to:

- Create a Python virtual environment (`venv`)
- Install project dependencies from `requirements.txt`
- Configure the virtual environment as a Jupyter/VS Code kernel
- Build and run a Dash application
- Access the Dash application through a local browser URL
- Stop the Dash development server using `CTRL + C`

## 🛠️ Technologies

- **Python 3.14.5**
- **Dash**
- **Plotly**
- **Pandas**
- **Jupyter / IPython**
- **VS Code**
- **Git**

## 📁 Project Structure

```text
09-dash-basics-html-core-components/
│
├── .venv/
├── dash_interactivity.py
├── dash_interactivity_barplot.py
├── requirements.txt
└── README.md
```

> `.venv/` is a local virtual environment and should normally **not be committed to Git**.

---

## 🚀 Getting Started

### 1. Clone or open the project

Open the project folder in VS Code and open a terminal at the project root.

For example:

```powershell
cd "[Your_Work_Directory]\DataAnalysis\learning\courses\ibm\dataanalyst\08-data-visualization-with-python\activities\hands-on\10-dash-interactive-user-input-callbacks"
```

Confirm that the project files are present:

```powershell
dir
```

You should see files such as:

```text
dash_interactivity.py
dash_interactivity_barplot.py
requirements.txt
README.md
```

---

## 🐍 2. Create the Virtual Environment

Create a Python virtual environment named `.venv`:

```powershell
python -m venv .venv
```

If you have multiple Python versions installed and want to explicitly use Python 3.14:

```powershell
py -3.14 -m venv .venv
```

---

## ▶️ 3. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, your terminal should display:

```text
(.venv) PS [Your_Work_Directory]\...
```

This indicates that the virtual environment is active.

### Verify the Python version

```powershell
python --version
```

Expected output:

```text
Python 3.14.5
```

You can also verify which Python executable is being used:

```powershell
python -c "import sys; print(sys.executable)"
```

The path should point to:

```text
...\10-dash-interactive-user-input-callbacks\.venv\Scripts\python.exe
```

---

## 📦 4. Upgrade pip and Build Tools

With the virtual environment activated, upgrade the Python packaging tools:

```powershell
python -m pip install --upgrade pip setuptools wheel
```

Verify pip:

```powershell
python -m pip --version
```

---

## 📚 5. Install Project Requirements

Install all dependencies listed in `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
```

Using:

```powershell
python -m pip
```

instead of simply:

```powershell
pip
```

helps ensure that packages are installed into the currently active virtual environment.

### Verify Dash

```powershell
python -m pip show dash
```

You can also test the main packages:

```powershell
python -c "import dash, plotly, pandas; print('Dash, Plotly, and Pandas installed successfully.')"
```

---

# 🧠 6. Configure `.venv` as the VS Code/Jupyter Kernel

If you're working with Jupyter notebooks in VS Code, configure the project `.venv` as the notebook kernel.

### Step 1 — Install the IPython kernel

With `.venv` activated:

```powershell
python -m pip install ipykernel
```

### Step 2 — Open the notebook in VS Code

Open your `.ipynb` file.

At the top-right of the notebook, click the **Kernel / Python environment selector**.

### Step 3 — Select `.venv`

Choose the Python interpreter associated with:

```text
.venv\Scripts\python.exe
```

It should appear similar to:

```text
Python 3.14.5 ('.venv')
```

### Step 4 — Verify the kernel

Run the following notebook cell:

```python
import sys

print(sys.executable)
```

The output should point to:

```text
...\10-dash-interactive-user-input-callbacks\.venv\Scripts\python.exe
```

This confirms that your notebook is using the project's virtual environment.

---

# ▶️ 7. Run the Dash Application

Make sure the terminal is located in the project root and `.venv` is activated.

Run:

```powershell
python dash_basics.py
```

You can also run the file using VS Code's **Run Python File** button.

> **Note:** When running a Python file directly, use `python dash_interactivity.py` or `python dash_interactivity_barplot.py`.
>
> If using the module syntax, use `python -m dash_interactivity` or `python -m dash_interactivity_barplot` — **do not include `.py`**.

Correct:

```powershell
python dash_interactivity.py
or
python dash_interactivity_barplot.py
```

or:

```powershell
python -m dash_interactivity
or
python -m dash_interactivity_barplot
```

Incorrect:

```powershell
python -m dash_interactivity.py
or
python -m dash_interactivity_barplot.py
```

---

# 🌐 8. Open the Dash Application

After starting the application, the terminal should display a local address similar to:

```text
Dash is running on http://127.0.0.1:8050/
```

or:

```text
Dash is running on http://localhost:8050/
```

Open the displayed address in your web browser.

For example:

```text
http://127.0.0.1:8050/
```

The Dash application should now be displayed in the browser.

### 🔗 Live Local Link

The application is running locally on your computer. The link is therefore only accessible while the Dash server is running:

```text
http://127.0.0.1:8050/
```

> This is **not a publicly accessible internet URL**. It is a local development server.

---

# ⛔ 9. Stop the Dash Application

To stop the running Dash development server, return to the terminal where the application is running and press:

```text
CTRL + C
```

On Windows:

```text
Ctrl + C
```

You should see the application stop and return to the PowerShell prompt:

```text
(.venv) PS [Your_Work_Directory]\...\10-dash-interactive-user-input-callbacks>
```

The local Dash URL will no longer be available after the server is stopped.

---

# 🔄 10. Run the Application Again

To restart the application:

```powershell
python dash_basics.py
```

Then open:

```text
http://127.0.0.1:8050/
```

in your browser again.

---

# 🧹 11. Deactivate the Virtual Environment

When you're finished working on the project:

```powershell
deactivate
```

The `(.venv)` prefix should disappear from your terminal.

For example:

Before:

```text
(.venv) PS [Your_Work_Directory]\...
```

After:

```text
PS [Your_Work_Directory]\...
```

---

# 📌 Useful Commands

| Task                   | Command                                         |
| ---------------------- | ----------------------------------------------- |
| Create venv            | `python -m venv .venv`                          |
| Activate venv          | `.\.venv\Scripts\Activate.ps1`                  |
| Check Python           | `python --version`                              |
| Check Python path      | `python -c "import sys; print(sys.executable)"` |
| Upgrade pip            | `python -m pip install --upgrade pip`           |
| Install requirements   | `python -m pip install -r requirements.txt`     |
| Install Jupyter kernel | `python -m pip install ipykernel`               |
| Check Dash             | `python -m pip show dash`                       |
| Run Dash app           | `python dash_basics.py`                         |
| Run as module          | `python -m dash_basics`                         |
| Stop Dash              | `CTRL + C`                                      |
| Deactivate venv        | `deactivate`                                    |

---

# 🐛 Troubleshooting

## `python -m dash_basics.py` produces an error

Use:

```powershell
python dash_basics.py
```

With `-m`, the `.py` extension must be omitted:

```powershell
python -m dash_basics
```

---

## `dash` cannot be imported

If you receive:

```text
ModuleNotFoundError: No module named 'dash'
```

make sure `.venv` is activated:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then install the requirements:

```powershell
python -m pip install -r requirements.txt
```

---

## The browser cannot connect to `localhost:8050`

Make sure the Dash application is still running in the terminal.

If the server was stopped with:

```text
CTRL + C
```

restart it:

```powershell
python dash_basics.py
```

Then visit:

```text
http://127.0.0.1:8050/
```

---

## Check installed packages

To see all packages installed in the active virtual environment:

```powershell
python -m pip list
```

To create/update the requirements file from the current environment:

```powershell
python -m pip freeze > requirements.txt
```

---

## 📄 License

This project is intended for educational and learning purposes as part of Python, Data Analysis, Data Visualization, and Dash development practice.
