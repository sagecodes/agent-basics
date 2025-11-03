"""
Simple workflow example demonstrating how to call an agent.
This example shows how to interact with the math agent to solve a basic problem.
"""

import asyncio
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import tools to register them
import tools.math_tools  # This registers the tools

from agents.math_agent import math_agent


async def simple_math_workflow():
    """
    A simple workflow that demonstrates calling the math agent with a basic math problem.
    """
    # Define a math problem
    problem = "Calculate 5 + 3, then multiply the result by 2"
    
    # Initialize empty memory log for this example
    memory_log = []
    
    print(f"Problem: {problem}")
    print("Calling math agent...")
    
    # Call the math agent
    result = await math_agent(problem, memory_log)
    
    print(f"Agent response: {result}")
    
    return result


async def main():
    """
    Main function to run the simple workflow example.
    """
    print("=== Simple Agent Call Workflow ===")
    await simple_math_workflow()


if __name__ == "__main__":
    asyncio.run(main())