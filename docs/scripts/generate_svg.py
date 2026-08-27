#!/usr/bin/env python3
"""
Generate a clean, standalone SVG capability map diagram from the SATRE specification YAML.
"""

import argparse
from collections import OrderedDict
from pathlib import Path
import yaml
from typing import Any


def load_yaml(file_path: Path | str) -> dict[str, Any]:
    """Load a YAML specification file using PyYAML."""
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"YAML specification file not found at: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def parse_specification(
    spec_data: dict[str, Any],
) -> OrderedDict[str, OrderedDict[str, str]]:
    """
    Parse the specification YAML data and extract pillars and capabilities in order.

    Returns:
        OrderedDict mapping pillar names to an OrderedDict of {capability_index: capability_name}.
    """
    if "specification" not in spec_data or not isinstance(
        spec_data["specification"], list
    ):
        raise ValueError("YAML data must contain a 'specification' list.")

    pillars: OrderedDict[str, OrderedDict[str, str]] = OrderedDict()

    for item in spec_data["specification"]:
        pillar = item.get("pillar")
        capability = item.get("capability")
        cap_index = str(item.get("capability_index", "")).strip()

        if not pillar or not capability or not cap_index:
            continue

        if pillar not in pillars:
            pillars[pillar] = OrderedDict()

        if cap_index not in pillars[pillar]:
            pillars[pillar][cap_index] = capability

    # Sort capabilities inside each pillar by numeric capability index
    sorted_pillars: OrderedDict[str, OrderedDict[str, str]] = OrderedDict()
    for pillar_name, caps in pillars.items():
        sorted_caps = OrderedDict(
            sorted(
                caps.items(),
                key=lambda kv: [
                    int(part) for part in kv[0].split(".") if part.isdigit()
                ],
            )
        )
        sorted_pillars[pillar_name] = sorted_caps

    return sorted_pillars


def split_text_lines(text: str, max_chars_per_line: int = 26) -> list[str]:
    """Split text into balanced lines for card/pillar titles."""
    words = text.split()
    if not words:
        return []
    if len(text) <= max_chars_per_line:
        return [text]
    if len(words) == 1:
        return [words[0]]
    if len(words) == 2:
        return [words[0], words[1]]

    # Find split point closest to middle character count
    total_len = len(text)
    best_split = 1
    best_diff = 999
    curr_len = 0
    for i in range(len(words) - 1):
        curr_len += len(words[i]) + 1
        diff = abs((total_len - curr_len) - curr_len)
        if diff < best_diff:
            best_diff = diff
            best_split = i + 1

    return [" ".join(words[:best_split]), " ".join(words[best_split:])]


def generate_svg(
    pillars: OrderedDict[str, OrderedDict[str, str]],
    pillar_width: int = 280,
    card_width: int = 240,
    card_height: int = 52,
    pillar_gap: int = 16,
    card_gap: int = 10,
    margin_x: int = 20,
    margin_y: int = 20,
    header_height: int = 70,
    bottom_padding: int = 20,
    include_indices: bool = False,
) -> str:
    """Generate a clean SVG string for the SATRE capability map."""
    num_pillars = len(pillars)
    max_caps = max(len(caps) for caps in pillars.values()) if pillars else 0

    total_pillar_height = (
        header_height
        + (max_caps * card_height)
        + ((max_caps - 1) * card_gap if max_caps > 1 else 0)
        + bottom_padding
    )

    svg_width = (
        margin_x * 2 + num_pillars * pillar_width + (num_pillars - 1) * pillar_gap
    )
    svg_height = margin_y * 2 + total_pillar_height

    card_x_offset = (pillar_width - card_width) / 2

    svg_styles = {
        ".pillar-bg": "{ fill: #343131; stroke: #000000; stroke-width: 2px; rx: 12px; ry: 12px; }",
        # Override background or individual pillars by creating a selector ".pillar-bg-N"
        ".pillar-bg-5": "{ fill: #883131; stroke: #000000; stroke-width: 2px; rx: 12px; ry: 12px; }",
        ".pillar-title": "{ font-size: 16px; font-weight: bold; fill: #ffffff; text-anchor: middle; }",
        ".card-bg": "{ fill: #2980b9; stroke: #000000; stroke-width: 1.5px; rx: 8px; ry: 8px; }",
        ".card-text": "{ font-size: 13.5px; font-weight: bold; fill: #ffffff; text-anchor: middle; dominant-baseline: middle; }",
        ".card:hover .card-bg": "{ fill: #3498db; transition: fill 0.2s ease; }",
    }

    lines: list[str] = (
        [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}px" height="{svg_height}px" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif">',
            "  <defs>",
            "    <style>",
        ]
        + [f"{selector} {style}" for selector, style in svg_styles.items()]
        + [
            "    </style>",
            "  </defs>",
        ]
    )

    for p_idx, (pillar_name, capabilities) in enumerate(pillars.items(), 1):
        px = margin_x + (p_idx - 1) * (pillar_width + pillar_gap)
        py = margin_y

        pillar_bg_class = (
            f"pillar-bg-{p_idx}" if f".pillar-bg-{p_idx}" in svg_styles else "pillar-bg"
        )
        lines.append(f'  <g id="pillar-{p_idx}" class="pillar">')
        lines.append(
            f'    <rect class="{pillar_bg_class}" x="{px}" y="{py}" width="{pillar_width}" height="{total_pillar_height}" />'
        )

        # Pillar Title
        full_title = f"{p_idx}. {pillar_name}"
        title_lines = split_text_lines(full_title, max_chars_per_line=28)
        if len(title_lines) == 1:
            lines.append(
                f'    <text class="pillar-title" x="{px + pillar_width/2}" y="{py + 38}">{title_lines[0]}</text>'
            )
        else:
            lines.append(
                f'    <text class="pillar-title" x="{px + pillar_width/2}" y="{py + 28}">{title_lines[0]}</text>'
            )
            lines.append(
                f'    <text class="pillar-title" x="{px + pillar_width/2}" y="{py + 50}">{title_lines[1]}</text>'
            )

        # Capability Cards
        for c_idx, (cap_index, cap_name) in enumerate(capabilities.items()):
            cx = px + card_x_offset
            cy = py + header_height + c_idx * (card_height + card_gap)

            lines.append(f'    <g class="card" id="card-{p_idx}-{c_idx+1}">')
            lines.append(
                f'      <rect class="card-bg" x="{cx}" y="{cy}" width="{card_width}" height="{card_height}" />'
            )

            label = f"{cap_index} {cap_name}" if include_indices else cap_name
            text_lines = split_text_lines(label, max_chars_per_line=20)

            if len(text_lines) == 1:
                lines.append(
                    f'      <text class="card-text" x="{cx + card_width/2}" y="{cy + card_height/2}">{text_lines[0]}</text>'
                )
            else:
                lines.append(
                    f'      <text class="card-text" x="{cx + card_width/2}" y="{cy + card_height/2 - 9}">{text_lines[0]}</text>'
                )
                lines.append(
                    f'      <text class="card-text" x="{cx + card_width/2}" y="{cy + card_height/2 + 9}">{text_lines[1]}</text>'
                )

            lines.append("    </g>")

        lines.append("  </g>")

    lines.append("</svg>")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a standalone SVG capability map diagram directly from the SATRE specification YAML."
    )
    parser.add_argument(
        "--input-file",
        "-i",
        default="source/spec/specification.yaml",
        help="Path to specification.yaml",
    )
    parser.add_argument(
        "--output-file",
        "-o",
        default="images/generated/pillars.svg",
        help="Path to save SVG output file",
    )
    parser.add_argument(
        "--include-indices",
        action="store_true",
        help="Include capability indices (e.g. 1.1) on card labels.",
    )

    args = parser.parse_args()

    spec_data = load_yaml(args.input_file)
    pillars = parse_specification(spec_data)
    svg_content = generate_svg(
        pillars=pillars,
        include_indices=args.include_indices,
        card_gap=10,
        header_height=70,
    )

    if args.output_file:
        output_path = Path(args.output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(svg_content + "\n")
        print(f"Generated SVG capability map written to: {output_path}")
    else:
        print(svg_content)


if __name__ == "__main__":
    main()
