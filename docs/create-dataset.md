# How To Guide: Implement RAG Capabilities

Learn how to enhance your flows with Retrieval-Augmented Generation (RAG) using Mira Flows SDK

## Understanding RAG Implementation

Retrieval-Augmented Generation (RAG) enhances your flows with specific domain knowledge. The implementation process involves three main stages:

1. 🗂️ **Create a Dataset**: Establish a knowledge base that contains specialized information your flow will reference during execution.
2. ➕ **Add Data Sources**: Populate your dataset with relevant information from various supported sources.
3. 🔗 **Link Dataset to Flow**: Connect the dataset to your flow, enabling it to leverage this information during processing.

## Step 1: Creating Your Dataset

Begin by establishing your knowledge base:

```python
from mira_sdk import MiraClient

client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})        # Initialize client

# Create a new dataset
client.dataset.create(
    "author/dataset_name",                                     # Unique identifier
    "Description of your knowledge base"                       # Dataset purpose
)
```

## Step 2: Adding Data Sources

Populate your dataset with information from various supported formats:

```python
# Add a PDF document as data source
client.dataset.add_source("author/dataset_name", file_path="document.pdf")

# Add a URL as data source
client.dataset.add_source("author/dataset_name", url="https://example.com/data")

# Add multiple URL sources via a CSV file
client.dataset.add_source("author/dataset_name", file_path="sources.csv")
```

## Step 3: Linking Dataset to Flow

Connect your dataset to an existing flow by modifying its configuration:

```yaml
# Additional flow configuration with RAG
dataset:
  source: "author/dataset_name"         # Link to your dataset

# Rest of your flow configuration remains unchanged
```
