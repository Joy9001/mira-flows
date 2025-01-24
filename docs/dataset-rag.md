# Core Concepts: Datasets and RAG

Step-by-step guide to installing and setting up Mira Flows SDK for your project

## Introduction

Datasets in Mira Flows support Retrieval-Augmented Generation (RAG) to enhance flows with specific knowledge. This capability allows flows to leverage custom knowledge bases for improved accuracy and contextual awareness in their responses. 🤖📈

## Dataset Attributes

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| Name | Unique identifier for dataset | Yes | "author/dataset_name" |
| Description | Purpose and content overview | Yes | "Optional description" |
| Source Type | Type of data being added | Yes | "url" or "file_path" |
| Source Path | Location of source data | Yes | "example.com" or "path/to/file" |
| Author | Creator's username | Yes | "your-username" |

## Supported File Formats

| Format | Description | Processing Method |
|--------|-------------|------------------|
| PDF (.pdf) | Document files | Text extraction from document |
| Markdown (.md) | Formatted text | Text extraction from document |
| URL | Web content | Web content scraping |
| CSV (.csv) | URL listings | URL extraction and content scraping |
| Text (.txt) | Plain text | Direct text extraction |

## Creating and Configuring Datasets

### Creating a Dataset

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
