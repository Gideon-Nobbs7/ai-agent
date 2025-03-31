# AI-Agent

Welcome to my ai-agent which interacts with a PostgreSQL database using **PydanticAI** and **OpenRouter** 

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Contributing](#contributing)

## Features
- Interact with your PostgreSQL database using natural language queries through Pydantic-AI and OpenRouter.
- Define custom tools using @agent.tool decorators to handle specific queries and tasks.

## Tech Stack
- **Programming Language**: Python
- **Framework**: PydanticAI

## Quick Start

Follow these steps to get started:

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/Gideon-Nobbs7/ai-agent
```

### 2. Set Up a Virtual Environment
Navigate to the project's root directory create a virtual environment respectively:
```bash
cd admin
python -m venv [environment_name]
```
Activate the virtual environment:
- On Windows:
  ```bash
  [environment_name]\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source [environment_name]/bin/activate
  ```
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Create .env file
Go to your project's root directory and create a .env file. Use the .env.example file as a reference for setting up your environment variables.

### 4. Initialize Your Database
Open your terminal and run the command below to create a products table and insert initial values into it:
```bash
python database.py
```

### 4. Use the AI-Agent
After creating your products table, you can interact with the AI agent by running:
```bash
python ai-agent.py
```
Enter prompts related to the product queries (eg.,
"What is the price of the Samsung phone?" or "What phone can I buy with a budget of 700?")


## Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Open a pull request with a detailed description of your changes.

---

Feel free to reach out if you have any questions or need further assistance.