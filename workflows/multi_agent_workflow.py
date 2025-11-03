"""
Multi-agent workflow example demonstrating how to coordinate multiple agents.
This example shows how to use both math and string agents in a single workflow.
"""

import asyncio
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import tools to register them
import tools.math_tools
import tools.string_tools

from agents.math_agent import math_agent
from agents.string_agent import string_agent


async def multi_agent_workflow():
    """
    A workflow that demonstrates coordination between math and string agents.
    
    Scenario: Analyze a sentence and then perform calculations based on the analysis.
    """
    # Define our input
    sentence = "The quick brown fox jumps over the lazy dog"
    
    # Initialize memory log
    memory_log = []
    
    print("=== Multi-Agent Workflow Example ===")
    print(f"Input sentence: '{sentence}'")
    print()
    
    # Step 1: Use string agent to analyze the sentence
    print("Step 1: Analyzing sentence with string agent...")
    string_prompt = f"Analyze this sentence: '{sentence}'. Count the words and letters."
    
    string_result = await string_agent(string_prompt, memory_log)
    print(f"String agent result: {string_result}")
    print()
    
    # Step 2: Extract numeric results and use math agent
    print("Step 2: Using math agent to perform calculations...")
    
    # For demo purposes, let's assume we got word count and letter count
    # In a real scenario, you'd parse the string_result to extract these values
    math_prompt = "Calculate the following: take 9 words and 35 letters, then find the ratio of letters to words and multiply by 2"
    
    math_result = await math_agent(math_prompt, memory_log)
    print(f"Math agent result: {math_result}")
    print()
    
    # Step 3: Use string agent again to create a summary
    print("Step 3: Creating summary with string agent...")
    summary_prompt = f"Count the words in this summary: 'Analysis complete: processed sentence with multiple calculations'"
    
    summary_result = await string_agent(summary_prompt, memory_log)
    print(f"Summary result: {summary_result}")
    
    return {
        "original_sentence": sentence,
        "string_analysis": string_result,
        "math_calculations": math_result,
        "summary": summary_result
    }


async def sequential_agent_calls():
    """
    Another example showing sequential agent calls with data passing.
    """
    print("\n=== Sequential Agent Calls ===")
    
    memory_log = []
    
    # Math calculation first
    math_result = await math_agent("Calculate 15 + 25, then multiply by 3", memory_log)
    print(f"Math result: {math_result}")
    
    # Use the math result conceptually in string analysis
    string_result = await string_agent("Count words and letters in: 'We calculated one hundred twenty results'", memory_log)
    print(f"String result: {string_result}")
    
    return {"math": math_result, "string": string_result}


async def main():
    """
    Main function to run the multi-agent workflow examples.
    """
    # Run the main workflow
    workflow_result = await multi_agent_workflow()
    
    # Run sequential example
    sequential_result = await sequential_agent_calls()
    
    print("\n=== Final Results ===")
    print("Workflow result:", workflow_result)
    print("Sequential result:", sequential_result)


if __name__ == "__main__":
    asyncio.run(main())