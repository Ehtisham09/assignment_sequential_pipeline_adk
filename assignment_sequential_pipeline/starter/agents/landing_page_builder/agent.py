import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_html_file, check_html
from utils.model_config import MODEL, rate_limit_pause

landing_page_builder_agent = LlmAgent(
    name="landing_page_builder_agent",
    model=MODEL,
    instruction=load_instructions_file("agents/landing_page_builder/instructions.txt"),
    description=load_instructions_file("agents/landing_page_builder/description.txt"),
    tools=[write_html_file, check_html],
    output_key="landing_page_output",
    before_model_callback=rate_limit_pause,
)
