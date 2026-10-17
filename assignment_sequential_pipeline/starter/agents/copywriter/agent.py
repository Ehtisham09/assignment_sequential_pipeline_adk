import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_text_file, count_words
from utils.model_config import MODEL, rate_limit_pause

copywriter_agent = LlmAgent(
    name="copywriter_agent",
    model=MODEL,
    instruction=load_instructions_file("agents/copywriter/instructions.txt"),
    description=load_instructions_file("agents/copywriter/description.txt"),
    tools=[write_text_file, count_words],
    output_key="marketing_copy_output",
    before_model_callback=rate_limit_pause,
)
