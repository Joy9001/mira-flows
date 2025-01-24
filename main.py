import os

from dotenv import load_dotenv
from mira_sdk import CompoundFlow, MiraClient
from mira_sdk.exceptions import FlowError

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

# Define the user input for the task, requirements, and preferences
# task = "Summarize news articles"
# requirements = "Fast processing, high accuracy, ability to handle multiple languages"
# preferences = (
#     "Focus on readability and concise summaries, avoid overly technical jargon"
# )

task = input("Enter the task for the new agent: ")
requirements = input("Enter the requirements for the agent (e.g., speed, accuracy): ")
preferences = input("Enter any preferences for the agent (optional): ")

# Prepare the input data dictionary based on user input
input_data = {
    "task": task,
    "requirements": requirements,
    "preferences": (preferences if preferences else ""),
}
print("Input data:", input_data)

# Load the compound flow that creates agents
flow = CompoundFlow(source="create-elemental-flow.yaml")

# Test and deploy the flow
try:
    # Test the flow with the input data
    response = client.flow.test(flow, input_data)
    print("Test response:\n\n", response["result"])

    # # Deploy the flow to the platform to create the agent
    # client.flow.deploy(flow)
    # print("Agent creation flow deployed successfully!")

    # # Execute the flow to generate the agent configuration
    # result = client.flow.execute("joy04/create-agent-flow", input_data)
    # print("Generated agent configuration:", result)

except FlowError as e:
    print(f"Error during execution: {str(e)}")
