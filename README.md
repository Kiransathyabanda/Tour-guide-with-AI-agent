# Tour Guide AI

This project is an AI-powered tour guide application using CrewAI that helps identify famous tourist places and create detailed travel plans. This application leverages OpenAI's large language model (LLM) to retrieve tourist information and plan trips from Nagpur to Manali.

## Features

- **Identify Tourist Places**: Retrieve information on famous tourist places from the specified location.
- **Plan Itinerary**: Create a detailed travel plan including timing, places to visit, distance, and transportation routes.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/tour-guide-ai.git
    cd tour-guide-ai
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Environment Variables**:
    ```sh
    export OPENAI_API_BASE='https://api.groq.com/openai/v1'
    export OPENAI_MODEL_NAME='llama3-70b-8192'
    export OPENAI_API_KEY='your-api-key'
    ```

## Usage

1. **Run the script**:
    ```sh
    python main.py
    ```

2. **View the output**:
    - The output will provide a list of famous tourist places and a detailed travel plan from Nagpur to Manali.

## Files

- `main.py`: Main script to run the AI agents and tasks.
- `requirements.txt`: List of Python dependencies.
- `README.md`: This readme file.

## Dependencies

- crewai

## Credits

- Developed by [kiransathyabanda].

## License

This project is licensed under the [MIT License](LICENSE).
