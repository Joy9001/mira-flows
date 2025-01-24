import os
from pathlib import Path

from dotenv import load_dotenv
from mira_sdk import MiraClient

# Load environment variables
load_dotenv()

# Initialize Mira Client
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

# Dataset configuration
DATASET_NAME = "joy04/mira-docs"
DATASET_DESCRIPTION = (
    "Documentation files for Mira Flows containing guides and examples"
)
DOCS_PATH = Path("docs")


def create_docs_dataset():
    # Create the dataset
    client.dataset.create(DATASET_NAME, DATASET_DESCRIPTION)

    # Add all MD files from the docs directory
    for md_file in DOCS_PATH.glob("*.md"):
        print(f"Adding {md_file} to dataset...")
        client.dataset.add_source(DATASET_NAME, file_path=str(md_file))


if __name__ == "__main__":
    try:
        create_docs_dataset()
        print(f"Successfully created dataset: {DATASET_NAME}")
    except Exception as e:
        print(f"Error creating dataset: {str(e)}")
