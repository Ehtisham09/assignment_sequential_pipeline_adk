# Instructor Notes (do not distribute)

## What to hand out
Give students `ASSIGNMENT.md` and the `starter/` folder. Keep this file for yourself.
Fill in the blanks in `ASSIGNMENT.md` first: weight, release date, due date, and the approval date for own-idea projects.

## What the starter gives vs. what students build
| Given | Students build |
|---|---|
| Agent 1 (`market_researcher`) complete: code, description, full prompt | Agents 2–6: tool imports, `output_key`, full `instructions.txt` |
| `write_text_file` tool | `write_html_file` + at least one custom tool |
| Root `SequentialAgent` with agent 1 wired in | Wiring agents 2–6 in order |
| Runner that prints events + a state summary | Updating `FINAL_AGENT_NAME` |
| `check_pipeline.py` contract checker | README, two runs, reflection |

The `description.txt` files are pre-filled so every student starts from the same idea of what each agent does. Students write the prompts.

## Grading workflow (~10 min per submission)
1. `cd starter && uv sync && uv run check_pipeline.py`: covers most of "Pipeline architecture" and "State passing" automatically.
2. Open the two `output/*_landing_page.html` files in a browser (Final artifacts).
3. Read the `qa_review` files. Did they catch a real cross-agent issue? (QA reviewer)
4. Skim 2 of the 5 `instructions.txt` files for the ROLE/INPUTS/TASK/OUTPUT/RULES/TOOL structure (Instruction quality).
5. Read the README and reflection.

## Common problems you'll see
- **`state['key']` in prompts** (copied from the class examples, which have this in their INPUTS lines). It does nothing; only `{key}` is substituted. The checker flags it.
- **Empty `output_key` values**: Nova Lite calls the tool and then replies "File saved." That reply is what gets stored in state, so the next agent gets nothing. The fix is the "return the SAME full document" line in TOOL USAGE.
- **Prices or names drift** between strategist → copy → page. That is good material for the QA agent and the reflection.
- **HTML truncated** on long pages with Nova Lite. Suggest fewer sections or `amazon.nova-pro-v1:0` for agent 5 only.

## Possible follow-up assignment
Turn agents 5 + 6 into a `LoopAgent` (page builder ↔ reviewer until score ≥ 8). This is already listed as bonus marks.
