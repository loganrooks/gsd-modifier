"""Render and update the Project Uplift section in .planning/STATE.md."""

from __future__ import annotations

import pathlib
import re

from harness_modifier.uplift import output_policy as uplift_output_policy
from harness_modifier.uplift import state_section as uplift_state_section


def state_section_policy() -> dict:
    return uplift_state_section.load_state_section()


def output_policy() -> dict:
    return uplift_output_policy.load_output_policy()


def state_rel_path() -> str:
    return str(state_section_policy()["state_rel_path"])


def _ordered_selector_keys() -> list[str]:
    return list(state_section_policy()["ordered_selector_keys"])


def _selector_labels() -> dict[str, str]:
    return dict(state_section_policy()["selector_labels"])


def render_state_section(section_values: dict[str, str]) -> str:
    heading = str(output_policy()["state_heading"])
    selector_labels = _selector_labels()
    lines = [heading, ""]
    for selector_key in _ordered_selector_keys():
        if selector_key not in section_values:
            raise KeyError(f"missing state-section selector value: {selector_key}")
        lines.append(f"{selector_labels[selector_key]}: {section_values[selector_key]}")
    lines.append("")
    return "\n".join(lines)


def update_state_section_text(text: str, section_values: dict[str, str]) -> str:
    heading = str(output_policy()["state_heading"])
    section = render_state_section(section_values).rstrip()
    pattern = re.compile(rf"\n{re.escape(heading)}\n[\s\S]*?(?=\n## |\Z)")
    if pattern.search(text):
        return pattern.sub("\n" + section + "\n", text)

    for sibling_marker in state_section_policy()["sibling_markers"]:
        marker = "\n" + str(sibling_marker)
        if marker in text:
            return text.replace(marker, "\n" + section + "\n" + marker, 1)

    return text.rstrip() + "\n\n" + section


def write_state_section(repo_root: pathlib.Path, section_values: dict[str, str]) -> None:
    state_path = repo_root / state_rel_path()
    if not state_path.exists():
        return
    text = state_path.read_text(encoding="utf-8")
    state_path.write_text(update_state_section_text(text, section_values), encoding="utf-8")
