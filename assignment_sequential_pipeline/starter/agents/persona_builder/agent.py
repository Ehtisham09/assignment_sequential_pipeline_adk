import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_text_file
from utils.model_config import MODEL, rate_limit_pause

persona_builder_agent = LlmAgent(
    name="persona_builder_agent",
    model=MODEL,
    instruction=load_instructions_file("agents/persona_builder/instructions.txt"),
    description=load_instructions_file("agents/persona_builder/description.txt"),
    tools=[write_text_file],
    output_key="personas_output",
    before_model_callback=rate_limit_pause,
)
