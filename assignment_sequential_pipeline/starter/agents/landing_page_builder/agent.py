import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_html_file
from utils.bedrock_llm import BedrockLlm  # noqa: F401 - registers bedrock/... model

landing_page_builder_agent = LlmAgent(
    name="landing_page_builder_agent",
    model="bedrock/amazon.nova-lite-v1:0",
    instruction=load_instructions_file("agents/landing_page_builder/instructions.txt"),
    description=load_instructions_file("agents/landing_page_builder/description.txt"),
    tools=[write_html_file],
    output_key="landing_page_output",
)