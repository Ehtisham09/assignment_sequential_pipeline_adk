import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_text_file, calculate_pricing
from utils.model_config import MODEL, rate_limit_pause

product_strategist_agent = LlmAgent(
    name="product_strategist_agent",
    model=MODEL,
    instruction=load_instructions_file("agents/product_strategist/instructions.txt"),
    description=load_instructions_file("agents/product_strategist/description.txt"),
    tools=[write_text_file, calculate_pricing],
    output_key="product_strategy_output",
    before_model_callback=rate_limit_pause,
)
