import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_text_file, calculate_pricing
from utils.bedrock_llm import BedrockLlm  # noqa: F401 - registers bedrock/... model

product_strategist_agent = LlmAgent(
    name="product_strategist_agent",
    model="bedrock/amazon.nova-lite-v1:0",
    instruction=load_instructions_file("agents/product_strategist/instructions.txt"),
    description=load_instructions_file("agents/product_strategist/description.txt"),
    tools=[calculate_pricing, write_text_file],
    output_key="product_strategy_output",
)