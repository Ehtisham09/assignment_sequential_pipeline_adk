# =============================================================================
# FILE: file_writer_tool.py
# PURPOSE:
#   Tools the pipeline agents use to save their work to the output/ folder.
#   `write_text_file` is complete and shows the pattern. You must finish
#   `write_html_file` and add at least ONE custom (non file-writer) tool.
# =============================================================================

import datetime
from pathlib import Path


# -----------------------------------------------------------------------------
# TOOL FUNCTION: write_text_file  (COMPLETE – use this as your reference)
# -----------------------------------------------------------------------------
def write_text_file(content: str, file_label: str) -> dict:
    """
    Writes a markdown document to a timestamped .md file in the output folder.

    Args:
        content (str): The full markdown document to save.
        file_label (str): Short snake_case label for the file name,
                          e.g. "market_research", "personas", "qa_review".

    Returns:
        dict: A dictionary containing the status and generated filename.
    """

    # Get the current date and time, format it as YYMMDD_HHMMSS.
    # Example: "250611_142317"
    timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")

    # Keep the label safe for file names (letters, numbers, underscores only).
    safe_label = "".join(c if c.isalnum() or c == "_" else "_" for c in file_label.lower())

    # Example: "output/250611_142317_market_research.md"
    filename = f"output/{timestamp}_{safe_label}.md"

    # Ensure the "output" directory exists.
    Path("output").mkdir(exist_ok=True)

    try:
        Path(filename).write_text(content, encoding="utf-8")
        return {
            "status": "success",
            "file": filename,
            "message": f"{safe_label} saved successfully."
        }

    except Exception as e:
        return {
            "status": "error",
            "file": filename,
            "message": f"Error: {str(e)}"
        }


# -----------------------------------------------------------------------------
# TOOL FUNCTION: write_html_file
# -----------------------------------------------------------------------------
def write_html_file(content: str) -> dict:
    """
    Writes a complete HTML page to a timestamped .html file in the output folder.

    Args:
        content (str): Full HTML document (including <!DOCTYPE html>) as a string.

    Returns:
        dict: A dictionary containing the status and generated filename.
    """

    timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = f"output/{timestamp}_landing_page.html"

    Path("output").mkdir(exist_ok=True)

    try:
        Path(filename).write_text(content, encoding="utf-8")
        return {
            "status": "success",
            "file": filename,
            "message": "landing_page saved successfully."
        }

    except Exception as e:
        return {
            "status": "error",
            "file": filename,
            "message": f"Error: {str(e)}"
        }


# -----------------------------------------------------------------------------
# CUSTOM TOOL 1: calculate_pricing  (used by product_strategist_agent)
# -----------------------------------------------------------------------------
def calculate_pricing(cost_per_user: float, margin_percent: float) -> dict:
    """
    Calculates a monthly subscription price from the cost to serve one user
    and a target profit margin, and suggests prices for three pricing tiers.

    Args:
        cost_per_user (float): Estimated monthly cost to serve one user, in USD.
        margin_percent (float): Target profit margin as a percentage (e.g. 60 for 60%).

    Returns:
        dict: Status, the base price, and suggested prices for the Free, Pro and Team tiers.
    """

    if cost_per_user < 0:
        return {"status": "error", "message": "cost_per_user must not be negative."}
    if not 0 <= margin_percent < 100:
        return {"status": "error", "message": "margin_percent must be at least 0 and less than 100."}

    # Price such that (price - cost) / price = margin  ->  price = cost / (1 - margin)
    base_price = cost_per_user / (1 - margin_percent / 100)

    return {
        "status": "success",
        "cost_per_user": round(cost_per_user, 2),
        "margin_percent": margin_percent,
        "base_price": round(base_price, 2),
        "suggested_tiers": {
            "free": 0.0,
            "pro": round(base_price, 2),
            "team": round(base_price * 2.5, 2),
        },
        "message": "Use these numbers as a starting point for the three pricing tiers.",
    }


# -----------------------------------------------------------------------------
# CUSTOM TOOL 2: count_words  (used by copywriter_agent)
# -----------------------------------------------------------------------------
def count_words(text: str) -> dict:
    """
    Counts the number of words in a piece of text. Use it to check length
    limits such as 'tagline max 8 words' or 'blurb max 30 words'.

    Args:
        text (str): The text to count words in.

    Returns:
        dict: Status and the word count.
    """

    words = text.split()
    return {"status": "success", "word_count": len(words)}


# -----------------------------------------------------------------------------
# CUSTOM TOOL 3: check_html  (used by landing_page_builder_agent and qa_reviewer_agent)
# -----------------------------------------------------------------------------
def check_html(html: str) -> dict:
    """
    Checks that an HTML landing page contains the required basic parts:
    doctype, title, viewport meta tag, inline style, and the main sections
    (hero, features, pricing, faq, cta, footer).

    Args:
        html (str): The full HTML document to check.

    Returns:
        dict: Status, a list of passed checks, and a list of missing items.
    """

    lower = html.lower()
    required = {
        "doctype": "<!doctype html>",
        "title tag": "<title>",
        "viewport meta": 'name="viewport"',
        "inline style": "<style",
        "hero section": "hero",
        "features section": "features",
        "pricing section": "pricing",
        "faq section": "faq",
        "cta section": "cta",
        "footer": "<footer",
    }
    passed = [name for name, marker in required.items() if marker in lower]
    missing = [name for name, marker in required.items() if marker not in lower]

    return {
        "status": "success" if not missing else "incomplete",
        "passed": passed,
        "missing": missing,
        "message": "HTML looks complete." if not missing else f"Missing: {', '.join(missing)}",
    }
