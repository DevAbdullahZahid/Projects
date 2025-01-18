# Main script to initiate the orchestrator and run the workflow
from orchestrator.coordinator import Orchestrator

if __name__ == "__main__":
    # Sample client data for testing
    client_data = {
        "name": "TechCorp",
        "requirements": "Build an AI-powered analytics dashboard",
        "budget": "$50,000",
        "timeline": "6 months"
    }

    # Initializing the orchestrator and running the workflow
    orchestrator = Orchestrator()
    results = orchestrator.execute_workflow(client_data)

    # Printing the results
    for key, value in results.items():
        print(f"{key}: {value}")
