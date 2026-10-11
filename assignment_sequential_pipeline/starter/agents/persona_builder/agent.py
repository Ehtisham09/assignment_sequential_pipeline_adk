import os
import sys
from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils.file_loader import load_instructions_file
from tools.file_writer_tool import write_text_file
from utils.bedrock_llm import BedrockLlm  # noqa: F401 - registers bedrock/... model

persona_builder_agent = LlmAgent(
    name="persona_builder_agent",
    model="bedrock/amazon.nova-lite-v1:0",
    instruction=load_instructions_file("agents/persona_builder/instructions.txt"),
    description=load_instructions_file("agents/persona_builder/description.txt"),
    tools=[write_text_file],
    output_key="personas_output",
)