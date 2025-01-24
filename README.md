# Mira Flows

A Python-based framework for creating and managing AI agent configurations using YAML-defined workflows.

## Features

- Create both elemental and compound AI agent flows
- Dynamic agent generation based on user requirements
- Support for multiple LLM providers (Anthropic, OpenAI, Meta)
- Built-in documentation dataset management
- Configurable workflow dependencies and parallel processing

## Installation

Requires Python 3.12 or higher.

```bash
git clone https://github.com/your-username/mira-flows.git
cd mira-flows
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the root directory
2. Add your Mira API key:

```env
MIRA_API_KEY=your_api_key_here
```

## Usage

### Creating a New Agent

```python
from mira_sdk import CompoundFlow, MiraClient

# Initialize client
client = MiraClient(config={"API_KEY": "your_api_key"})

# Create a new agent flow
flow = CompoundFlow(source="create-elemental-flow.yaml")
input_data = {
    "task": "Your task description",
    "requirements": "Your requirements",
    "preferences": "Your preferences"
}

# Test the flow
response = client.flow.test(flow, input_data)
```

### Creating Documentation Dataset

```python
python create_docs_dataset.py
```

## Project Structure

- `main.py` - Main application entry point
- `create_docs_dataset.py` - Documentation dataset creation utility
- `create-elemental-flow.yaml` - Template for elemental flow creation
- `create-compound-flow.yaml` - Experimental template for compound flow creation (see note below)
- `generated-example.yaml` - Example of a generated agent configuration

> **⚠️ Note:** The compound flow generator (`create-compound-flow.yaml`) is currently experimental and may produce configurations with dependency issues. It is recommended to carefully review and test any generated compound flows before deployment. For production use, prefer the elemental flow generator until the compound flow generator has been thoroughly tested.

## Flow Types

### Elemental Flow

Basic single-task flows with:

- Input validation
- LLM model configuration
- Prompt templates
- Output formatting

### Compound Flow

Multi-stage workflows supporting:

- Parallel processing
- Flow dependencies
- Multiple LLM interactions
- Dataset integration

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Author

- [Joy Mridha](https://github.com/Joy9001)
