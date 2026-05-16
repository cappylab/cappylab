#!/usr/bin/env python3
"""Generate a local WakaTime stats card for the profile README."""

from __future__ import annotations

import argparse
import html
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path


API_URL = "https://wakatime.com/api/v1/users/{username}/stats/last_7_days"
DEFAULT_COLORS = [
    "#00d4ff",
    "#bb86fc",
    "#ff6b6b",
    "#3cec76",
    "#f7c843",
    "#36e3ff",
    "#fd1464",
    "#8b949e",
]


def fetch_stats(username: str) -> dict:
    req = urllib.request.Request(
        API_URL.format(username=urllib.parse.quote(username)),
        headers={"User-Agent": "cappylab-readme-wakatime-card/1.0"},
    )

    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"WakaTime API returned HTTP {exc.code}: {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach WakaTime API: {exc.reason}") from exc


def language_rows(data: dict, limit: int) -> list[dict]:
    rows = data.get("languages") or []
    if not rows:
        return []

    return rows[:limit]


def render_svg(data: dict, username: str, limit: int) -> str:
    rows = language_rows(data, limit)
    visible_total = data.get("is_coding_activity_visible")
    range_label = data.get("human_readable_range") or "last week"
    subtitle = f"WakaTime language usage - {range_label}"
    footer = "Total coding time is private; public language split shown."
    if visible_total and data.get("human_readable_total"):
        footer = f"Total: {data['human_readable_total']}"

    width = 720
    row_height = 29
    top = 74
    bar_x = 190
    bar_width = 440
    height = top + max(len(rows), 1) * row_height + 54

    parts = [
        f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">',
        "<style>",
        ".title{font:600 22px 'Segoe UI',Ubuntu,Sans-Serif;fill:#00d4ff}",
        ".sub{font:500 13px 'Segoe UI',Ubuntu,Sans-Serif;fill:#8b949e}",
        ".label{font:600 13px 'Segoe UI',Ubuntu,Sans-Serif;fill:#c9d1d9}",
        ".pct{font:600 12px 'Segoe UI',Ubuntu,Sans-Serif;fill:#8b949e}",
        ".foot{font:500 12px 'Segoe UI',Ubuntu,Sans-Serif;fill:#8b949e}",
        "</style>",
        '<rect x="0.5" y="0.5" width="719" height="{height_minus_one}" rx="10" fill="#0d1117" stroke="#30363d"/>'.format(
            height_minus_one=height - 1
        ),
        '<text x="28" y="38" class="title">Weekly Coding Stats</text>',
        f'<text x="28" y="59" class="sub">{html.escape(subtitle)}</text>',
    ]

    if not rows:
        parts.extend(
            [
                '<text x="28" y="96" class="label">No public WakaTime language data available.</text>',
                f'<text x="28" y="{height - 24}" class="foot">{html.escape(footer)}</text>',
                "</svg>",
            ]
        )
        return "\n".join(parts) + "\n"

    for index, row in enumerate(rows):
        y = top + index * row_height
        name = html.escape(str(row.get("name", "Unknown")))
        percent = float(row.get("percent") or 0)
        percent_label = f"{percent:.2f}".rstrip("0").rstrip(".")
        color = DEFAULT_COLORS[index % len(DEFAULT_COLORS)]
        fill_width = max(2, min(bar_width, round(bar_width * percent / 100, 2)))

        parts.extend(
            [
                f'<text x="28" y="{y + 14}" class="label">{name}</text>',
                f'<rect x="{bar_x}" y="{y + 3}" width="{bar_width}" height="12" rx="6" fill="#21262d"/>',
                f'<rect x="{bar_x}" y="{y + 3}" width="{fill_width}" height="12" rx="6" fill="{color}"/>',
                f'<text x="{bar_x + bar_width + 18}" y="{y + 14}" class="pct">{percent_label}%</text>',
            ]
        )

    parts.extend(
        [
            f'<text x="28" y="{height - 24}" class="foot">{html.escape(footer)}</text>',
            "</svg>",
        ]
    )
    return "\n".join(parts) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", default="cappy")
    parser.add_argument("--output", default="assets/wakatime-stats.svg")
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()

    payload = fetch_stats(args.username)
    data = payload.get("data")
    if not isinstance(data, dict):
        raise RuntimeError("WakaTime API response did not contain a data object")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_svg(data, args.username, args.limit), encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
