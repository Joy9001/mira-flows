# Core Concepts: Elemental Flows

Understanding the fundamental building blocks of Mira Flows

## Introduction

An Elemental Flow is a self-contained, autonomous unit designed to perform specific, unique actions. These flows serve as the foundational building blocks within the Mira Flows ecosystem, enabling precise and reliable AI-powered operations.

## Elemental Flow Attributes

### Version

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| version | Flow specification version using semantic versioning | Yes | "0.0.1" |

### Metadata

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| name | Unique identifier for the flow | Yes | "your-flow-name" |
| description | Explanation of flow's purpose | Yes | "A brief description of your flow" |
| author | Creator's username | Yes | "your-username" |
| tags | Keywords for categorization | No | [tag1, tag2, tag3] |
| private | Access control setting | Yes | false |

## Input Configuration

### Supported Input Types

| Type | Description |
|------|-------------|
| string | Text-based input values |

### Input Structure

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| inputs | Map of input parameters | Yes | Collection of input definitions |
| type | Data type of input (currently only string) | Yes | "string" |
| description | Purpose of the input | Yes | "Description of input1" |
| required | Whether input is mandatory | Yes | true or false |
| example | Sample input value | No | "Example value for input1" |

## Model Configuration

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| provider | AI service provider | Yes | "provider-name" |
| name | Specific model identifier | Yes | "model-name" |

## Dataset Configuration (Optional)

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| source | Reference to dataset | No | "author_name/dataset_name" |

## Prompt and Readme Configuration

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| prompt | Instructions for model behavior | Yes | "Generate a tweet on the given topic: " |
| readme | Usage documentation | Yes | Markdown-formatted guide |

## Basic Flow Structure

The official YAML structure for a basic Mira Flow:

```yaml
version: "your.version.here"

metadata:
  name: "your-flow-name"
  description: "A brief description of your flow"
  author: "your-username"
  tags: [tag1, tag2, tag3]
  private: false

inputs:
  input1:
    type: string
    description: "Description of input1"
    required: true
    example: "Example value for input1"
  input2:
    type: string
    description: "Description of input2"
    required: true
    example: "Example value for input2"

model:
  provider: "provider-name"
  name: "model-name"

prompt: |
  Your flow's primary instruction or role...
  You can use {input1} and {input2} placeholders to reference inputs.

readme: |
  Your flow's readme...
  You can use raw text or markdown here.
```

## RAG Integration 🔍

### Supported File Formats

| File Type | Processing Method |
|-----------|------------------|
| PDF (.pdf) | Text extraction from document |
| Markdown (.md) | Text extraction from document |
| URL | Web content scraping |
| CSV (.csv) | URL extraction and content scraping |
| Text (.txt) | Direct text extraction |
| Zip (.zip) | Processing of contained supported files |

### Creating a Dataset 🗃️

```python
from mira_sdk import MiraClient

client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})
# Create dataset
client.dataset.create("author/dataset_name", "Optional description")
```

### Adding Data Sources

```python
# Add URL to your dataset
client.dataset.add_source("author/dataset_name", url="example.com")

# Add file to your dataset
client.dataset.add_source("author/dataset_name", file_path="path/to/my/file.csv")
```

### Linking Dataset with Flow

Add the following configuration to your flow.yaml file:

```yaml
dataset:
  source: "author/dataset_name"
```

## Flow Structure with RAG

The official YAML structure for a flow with RAG capabilities:

```yaml
version: "your.version.here"

metadata:
  name: "your-flow-name"
  description: "A brief description of your flow"
  author: "your-username"
  tags: [tag1, tag2, tag3]
  private: false

inputs:
  input1:
    type: string
    description: "Description of input1"
    required: true
    example: "Example value for input1"

model:
  provider: "provider-name"
  name: "model-name"

dataset:
  source: "author_name/dataset_name"

prompt: |
  Your flow's primary instruction or role...
  You can use {input1} placeholders to reference inputs.

readme: |
  Your flow's readme...
  You can use raw text or markdown here.
