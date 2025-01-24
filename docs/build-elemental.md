# How To Guide: Build Elemental Flows

Learn how to build your own elemental flow using Mira Flows SDK

## Introduction

This guide explains how to create, test, and deploy elemental flows that implement focused, single-task processing. Elemental flows provide core functionality that can be used independently or as building blocks within compound flows. 🔄💡

## Development Lifecycle

Creating an elemental flow follows a systematic process:

1. **Configuration**: Define your elemental flow using YAML
2. **Testing**: Validate the flow's functionality
3. **Deployment**: Make your flow available
4. **Execution**: Run your flow in production
5. **Updates**: Iterate and improve

Let's explore each step in detail.

## Step 1: YAML Configuration

```yaml
# Version format ex. "0.0.1"
version: "your.version.here"                            # Flow specification version

# Basic metadata for the agent
metadata:
  name: "your-flow-name"                               # Unique identifier
  description: "A brief description of your flow"       # Flow purpose
  author: "your-username"                              # Must match your account username
  tags: [tag1, tag2, tag3, ...]                       # Keywords for categorization
  private: false                                       # Access control setting

# Define the input variables required
inputs:
  input1:                                              # First input parameter
    type: string                                       # Currently only String format
    description: "Description of input1"
    required: true
    example: "Example value for input1"
  input2:                                              # Second input parameter
    type: string
    description: "Description of input2"
    required: true
    example: "Example value for input2"

# LLM configuration
model:
  provider: "provider-name"                            # e.g., anthropic, openai, meta, etc.
  name: "model-name"                                   # Specific model identifier

# Dataset configuration (Optional)
dataset:
  source: "author_name/dataset_name"                   # Make sure this dataset exists

# Prompt template configuration
prompt: |
  Your flow's primary instruction or role...
  You can use {input1} and {input2} placeholders to reference inputs.

# ReadME configuration
readme: |
  Your flow's readme...
  You can use raw text or markdown here.
```

## Step 2: Testing

Test your elemental flow before deployment:

```python
from mira_sdk import MiraClient, Flow

client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})     # Initialize Mira Client

# Basic test
flow = Flow(source="/path/to/your.yaml")                    # Load flow configuration
input_dict = {"key": "value"}                               # Prepare test input
response = client.flow.test(flow, input_dict)               # Test flow
```

## Step 3: Deployment

Deploy your elemental flow to make it available:

```python
from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError

client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})     # Initialize client

flow = Flow(source="/path/to/your.yaml")                    # Load flow
try:
    client.flow.deploy(flow)                                # Deploy to platform
except FlowError as e:
    print(f"Error occurred: {str(e)}")                      # Handle deployment error
```

## Step 4: Execution

After deployment, execute your elemental flow:

```python
from mira_sdk import MiraClient, Flow

client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})     # Initialize client

version = "1.0.0"                                           # Optional specific version
input_data = {"key": "value"}                              # Execution input

# If no version is provided, it'll use the latest version by default
if version:
    flow_name = f"author/your-flow-name/{version}"
else:
    flow_name = "author/your-flow-name"

result = client.flow.execute(flow_name, input_data)         # Execute flow
print(result)
```

## Step 5: Updates

When you need to modify your elemental flow:

```python
from mira_sdk import Flow, MiraClient
from mira_sdk.exceptions import FlowError

client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})     # Initialize client

# Load existing flow
flow = client.flow.get("author/flow_name")                  # Get current version
flow.save("/path/to/flow.yaml")                            # Save for editing

# Deploy updated flow
try:
    client.flow.deploy(flow)                                # Deploy new version
except FlowError as e:
    print(f"Error occurred: {str(e)}")                      # Handle update error
```

**Note**: In case you forget to bump the flow version, it will get bumped by default every time you deploy the same flow.

By following these steps, you can create, test, deploy, and manage your own custom elemental flows on the Mira Flows platform. This process allows you to contribute to the Marketplace and continuously improve your flows over time. 🌟🔧
