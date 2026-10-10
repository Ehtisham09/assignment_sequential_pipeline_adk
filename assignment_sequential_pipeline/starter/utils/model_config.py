# =============================================================================
# FILE: utils/model_config.py
# PURPOSE:
#   One place that decides WHICH Gemini model every agent uses, and a small
#   pause between model calls so the free Gemini API tier (about 10 requests
#   per minute) does not return "429 RESOURCE_EXHAUSTED" errors.
#
#   Change the model without touching code by adding this to your .env file:
#       GEMINI_MODEL=gemini-3.1-flash-lite
# =============================================================================

import asyncio
import os

from dotenv import load_dotenv

# Make sure GOOGLE_API_KEY from .env is loaded, even under `adk web`.
load_dotenv()

# Default model. Alternatives if you hit quota limits: "gemini-3.1-flash-lite".
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

# Seconds to wait before every model call (free tier is ~10 requests/minute).
DELAY_SECONDS = float(os.getenv("GEMINI_DELAY_SECONDS", "6"))


async def rate_limit_pause(callback_context, llm_request):
    """before_model_callback: sleep briefly, then let the model call go ahead."""
    if DELAY_SECONDS > 0:
        await asyncio.sleep(DELAY_SECONDS)
    return None
