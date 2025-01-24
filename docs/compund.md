# Core Concepts: Compound Flows

Step-by-step guide to installing and setting up Mira Flows SDK for your project

## Introduction

A Compound Flow is an advanced flow type designed for complex, multi-stage processing pipelines. Unlike Elemental Flows which perform single, focused tasks, Compound Flows can create sophisticated decision trees, implement custom processing logic, and orchestrate multiple processing stages. 🎯

## Compound Flow Attributes

### Version ⚡

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| version | Flow specification version using semantic versioning | Yes | "0.1.0" |

### Metadata

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| flow_type | Type of flow (must be "compound") | Yes | "compound" |
| name | Unique identifier for the flow | Yes | "your-flow-name" |
| description | Explanation of flow's purpose | Yes | "A brief description" |
| author | Creator's username | Yes | "your-username" |
| tags | Keywords for categorization | No | [tag1, tag2, tag3] |
| private | Access control setting | Yes | false |

### Input Configuration

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| inputs | Map of input parameters | Yes | Collection of input definitions |
| type | Data type of input (currently only string) | Yes | "string" |
| description | Purpose of the input | Yes | "Description of input1" |
| required | Whether input is mandatory | Yes | true or false |
| example | Sample input value | No | "Example value for input1" |

## Workflow Configuration

Each Compound Flow must define a workflow consisting of multiple processing stages. There are two types of workflow stages:

### Elemental Stage Configuration

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| type | Must be "elemental" | Yes | "elemental" |
| flow_name | Reference to existing Elemental Flow | Yes | "author/flow-name" |
| inputs | Mapping to flow inputs | Yes | Input mapping object |
| depends_on | List of dependent stages | No | ["stage1", "stage2"] |

### Custom Stage Configuration

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| type | Must be "custom" | Yes | "custom" |
| model | LLM configuration | Yes | Model settings object |
| prompt | Processing instructions | Yes | Template with placeholders |
| inputs | Stage input parameters | Yes | Input mapping object |
| dataset | RAG dataset configuration | No | "author_name/dataset_name" |
| depends_on | List of dependent stages | No | ["stage1", "stage2"] |

### Dependency Configuration

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| depends_on | List of stages that must complete before execution | No | ["stage1", "stage2"] |

### Execution Behavior

- Stages without depends_on can execute in parallel
- Stages with depends_on will wait for specified stages to complete
- Multiple stages can depend on the same previous stage

### Output Configuration

| Component | Description | Required | Example |
|-----------|-------------|-----------|----------|
| output.value | List of stage outputs to combine | Yes | [${stage1.outputs}, ${stage2.outputs}] |

## Basic Flow Structure

```yaml
# Flow specification version
version: "0.1.0"

# Flow metadata and configuration
metadata:
  flow_type: "compound"
  name: "your-flow-name"
  description: "Describe what this compound flow accomplishes"
  author: "your-username"
  tags: [tag1, tag2, tag3]
  private: true

# Primary input definitions
inputs:
  prime_input_1:
    type: string
    description: "What this input is used for"
    required: true
    example: "Example value"
  prime_input_2:
    type: string
    description: "Description of this input"
    required: false
    example: "Example"

# Workflow definition
workflow:

# Elemental Flow stage - starts immediately
  first_flow:
    type: "elemental"
    flow_name: "john_doe/first_elemental_flow"
    inputs:
      abc: ${inputs.prime_input_1}
      xyz: ${inputs.prime_input_2}

# Custom processing stage - starts immediately (parallel to first_flow)
  second_flow:
    type: "custom"
    inputs:
      input1: ${inputs.input_name}
    model:
      provider: "provider-name"
      name: "model-name"
    prompt: |
      Your flow's primary instruction or role...
      You can use {input1} placeholders to reference inputs.

# Waits for both first_flow and second_flow to complete
  third_flow:
    type: "custom"
    depends_on: [first_flow, second_flow]
    inputs:
      input1: ${first_flow.output}
      input2: ${second_flow.output}
    model:
      provider: "provider-name"
      name: "model-name"
    dataset:
      source: "author_name/dataset_name"
    prompt: |
      Your flow's primary instruction or role...
      You can use {input1} and {input2} placeholders to reference inputs.

# Output configuration
output:
  value:
    - ${first_flow.output}
    - ${second_flow.output}
    - ${third_flow.output}

# Flow documentation
readme: |
  This is a detailed explanation of what your flow does.

### Workflow Overview

  1. **First Flow**: Executes `john_doe/first_elemental_flow` with the provided inputs.
  2. **Second Flow**: Runs in parallel with first flow
  3. **Third Flow**: Depends on both previous flows, executes after they complete

### Outputs

- Combined outputs from all flows are returned in order.

## Implementation Structure 🛠️
Compound Flows can either define custom processing logic within their workflow or integrate existing Elemental Flows, providing maximum flexibility for solving complex challenges. The workflow allows for:

- Advanced Decision Making with conditional processing paths 🧠
- Custom Processing stages with direct model and prompt configurations ⚙️
- Integration of existing Elemental Flows for reusability 🔄
- Parallel execution of independent stages ⚡
- Sequential execution through depends_on configurations 🔗
- Flexible input/output mapping between stages 🔀
