# How To Guide: Build Compound Flows

Learn how to build your own compound flow using Mira Flows SDK

## Introduction

This guide explains how to create, test, and deploy compound flows that implement complex, multi-stage processing pipelines. Compound flows provide sophisticated capabilities for implementing business logic, custom processing stages, and integration with existing elemental flows. 🔄💡

## Development Lifecycle

Creating a compound flow follows a systematic process:

1. **Configuration**: Define your compound flow using YAML
2. **Testing**: Validate the entire processing pipeline
3. **Deployment**: Make your flow available
4. **Execution**: Run your multi-stage flow in production
5. **Updates**: Iterate and improve

> **Note**: Use OpenAI (gpt-4o) or Anthropic (claude-3.5-sonnet) models when building complex workflows to ensure optimal performance. [Checkout Available Models]

## Step 1: YAML Configuration

```yaml
# Flow specification version
version: "0.1.0"                                    # Flow specification version

metadata:
  flow_type: "compound"                             # Specifies this as a compound flow
  name: "your-flow-name"                            # Unique identifier
  description: "Describe what this compound flow accomplishes"
  author: "your-username"                           # Your Mira Flows username
  tags: [tag1, tag2, tag3]                         # Discovery keywords
  private: true                                     # Access control setting

inputs:
  prime_input_1:                                    # Primary input parameter
    type: string
    description: "What is this input used for"
    required: true
    example: "Example value"
  prime_input_2:                                    # Secondary input parameter
    type: string
    description: "Description of this input"
    required: false
    example: "Example"

workflow:

# Elemental Flow stage - starts immediately

  first_flow:                                       # First processing stage
    type: "elemental"
    flow_name: "john_doe/first_elemental_flow"
    inputs:
      abc: ${inputs.prime_input_1}
      xyz: ${inputs.prime_input_2}

# Custom processing stage - starts immediately (parallel to first_flow)

  second_flow:                                      # Parallel processing stage
    type: "custom"
    inputs:
      input1: ${inputs.prime_input_1}
    model:
      provider: "provider-name"                     # e.g., anthropic, openai, meta, etc.
      name: "model-name"                            # Specific model identifier
    prompt: |
      Your flow's primary instruction or role...
      You can use {input1} placeholders to reference inputs.

# Waits for both first_flow and second_flow to complete

  third_flow:
    type: "custom"
    depends_on: [first_flow, second_flow]  # Dependent on fist_flow and second_flow
    inputs:
      input1: ${first_flow.output} # uses output of first_flow as input
      input2: ${second_flow.output} # uses output of second_flow as input
    model:
      provider: "provider-name"
      name: "model-name"
    dataset:
      source: "author_name/dataset_name"
    prompt: |
      Your flow's primary instruction or role...
      You can use {input1} and {input2} placeholders to reference inputs.

output:
  value:                                           # Combine & customise outputs in order
    - ${first_flow.output}
    - ${second_flow.output}
    - ${third_flow.output}

readme: |
  This is a detailed explanation of what your flow does.

  ### Workflow Overview
  1. **First Flow**: Executes `john_doe/first_elemental_flow` with the provided inputs
  2. **Second Flow**: Runs in parallel with first flow
  3. **Third Flow**: Depends on both previous flows, executes after they complete

  ### Outputs
  - Combined outputs from all flows are returned in order
```

## Step 2: Testing

```python
from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError

client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})     # Initialize Mira Client
flow = CompoundFlow(source="/path/to/compound_flow.yaml")   # Load flow configuration

test_input = {                                              # Prepare test inputs
    "prime_input_1": "test data",
    "prime_input_2": "test parameters"
}

try:
    response = client.flow.test(flow, test_input)           # Test entire pipeline
    print("Test response:", response)
except FlowError as e:
    print("Test failed:", str(e))                           # Handle test failure
```

## Step 3: Deployment

```python
from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError

flow = CompoundFlow(source="/path/to/compound_flow.yaml")   # Load flow configuration

try:
    client.flow.deploy(flow)                               # Deploy to platform
    print("Compound flow deployed successfully!")          # Success message
except FlowError as e:
    print(f"Deployment error: {str(e)}")                   # Handle deployment error
```

## Step 4: Execution

```python
from mira_sdk import MiraClient
from mira_sdk.exceptions import FlowError

flow_name = "your-username/your-flow-name"                 # Flow identifier
input_data = {                                            # Execution inputs
    "prime_input_1": "production data",
    "prime_input_2": "production parameters"
}

try:
    result = client.flow.execute(flow_name, input_data)    # Execute workflow
    print("Execution result:", result)                     # Display result
except FlowError as e:
    print("Execution error:", str(e))                      # Handle execution error
```

## Step 5: Updates

```python
from mira_sdk import MiraClient
from mira_sdk.exceptions import FlowError

flow = client.flow.get("your-username/your-flow-name")     # Retrieve existing flow
flow.save("/path/to/compound_flow.yaml")                   # Save for editing

try:
    client.flow.deploy(flow)                               # Deploy updated version
    print("Updated flow deployed successfully!")           # Success message
except FlowError as e:
    print(f"Update error: {str(e)}")                       # Handle update error
```

**Note**: In case you forget to bump the flow version, it will get bumped by default every time you deploy the same flow.

By following these steps, you can create, test, deploy, and manage your own custom compound flows on the Mira Flows platform. 🌟🔧
