import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_text_file, check_html
from utils.model_config import MODEL, rate_limit_pause

qa_reviewer_agent = LlmAgent(
    name="qa_reviewer_agent",
    model=MODEL,
    instruction=load_instructions_file("agents/qa_reviewer/instructions.txt"),
    description=load_instructions_file("agents/qa_reviewer/description.txt"),
    tools=[write_text_file, check_html],
    output_key="qa_review_output",
    before_model_callback=rate_limit_pause,
)
