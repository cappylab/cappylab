# README Minimalist Restructure — Design

**Date:** 2026-04-22
**Scope:** Sub-project A of larger "upgrade & improve" initiative (A: layout cleanup, B: new sections, C: visual polish, D: technical reliability). This spec covers A only.
**Target file:** `README.md`

## Goal

Reduce visual redundancy in the profile README while preserving the "Cappy" identity. Target ~5 top-level content sections instead of the current ~20 blocks. Keep the personality; cut the repetition.

## Current problems

The current README has four overlapping contribution visualizations (Streak, Activity Graph, Snake, 3D), two overlapping stats blocks (GitHub Stats + Top Languages AND a 4-card Metrics block), two typing SVGs (header + footer), and ~7 decorative cat images interspersed between sections. Many of these elements convey the same information in different visual forms, creating noise without adding signal.

## New structure

The restructured README has 5 content sections plus a thin header/footer:

### 1. Header
- Capsule-render wave banner with text "Welcome to Cappy's Universe"
- One typing SVG showing rotating taglines
- **Remove:** random dev quote block, the four profile/follower/stars/repos badges (redundant with Stats section below)

### 2. About Me
- `header-about.svg` title banner
- `cat-waving.svg` (signature cat #1) placed inline with the about block
- JavaScript-style code block with `cappy = { ... }` object (keep current content)
- Email badge "Let's Talk"
- **Remove:** standalone `cat-waving.svg` row below the code block (moved inline above)

### 3. Tech Stack
- `header-tech.svg` title banner
- Keep existing 5-row table (Languages / Frontend / Backend / DevOps / Tools) — already compact, no changes

### 4. Stats & Activity
This is the consolidated "numbers and contributions" block, replacing 4 separate sections in the current README.
- `header-stats.svg` title banner
- GitHub Stats card + Top Languages card (side-by-side, as today)
- `header-3d.svg` title banner
- 3D Contribution Graph (`./profile-3d-contrib/profile-night-green.svg`) — the signature contribution viz
- **Remove:** Streak Stats, Snake Graph section, Activity Graph section, Trophies section, the 4-card Metrics block, all decorative cat rows between these stats sections

### 5. Connect
- `header-connect.svg` title banner
- Three badges: Gmail, GitHub, Portfolio
- Tagline line: "Open to collaboration on Go backend, distributed systems, and developer tooling"
- `cat-sleeping.svg` (signature cat #2) on a single line above footer — only decorative cat retained in the tail of the document
- **Remove:** `cat-tower.svg`, `potted-plant.svg` from this row (keep just `cat-sleeping.svg`)

### Footer
- Single capsule-render wave banner with text "See you around!"
- **Remove:** footer typing SVG (redundant with header typing SVG)

## What gets removed in total

| Element | Reason |
|---|---|
| Random dev quote | Decorative, no real info |
| Profile views / Followers / Stars / Repos badges (4x) | Redundant with Stats section |
| Streak Stats | Replaced by 3D graph as single contribution viz |
| Snake Graph section + header | Replaced by 3D |
| Activity Graph section + header | Replaced by 3D |
| Trophies section + header + cat-chasing-butterfly | Show-off, doesn't fit minimalist direction |
| Metrics 4-card block + header | Redundant with GitHub Stats + Top Languages |
| Footer typing SVG | Redundant with header |
| `cat-playing-yarn.svg`, `flower-patch.svg`, `cat-eating.svg` row | Decorative between sections |
| `vine.svg`, `cat-sitting-tree.svg`, `bush.svg` row | Decorative |
| `cat-chasing-butterfly.svg` | Part of removed trophies section |
| `cat-tower.svg`, `potted-plant.svg` in connect row | Decorative, keeping only cat-sleeping |

SVG asset files themselves are NOT deleted from the `assets/` folder — only their references removed from `README.md`. This preserves reversibility.

## What stays

- Capsule-render wave banners (header + footer)
- One typing SVG (header only)
- About Me code block + email badge
- Tech Stack table
- GitHub Stats + Top Languages cards
- 3D Contribution Graph
- Connect badges (Gmail + GitHub + Portfolio)
- Title banner SVGs: `header-about`, `header-tech`, `header-stats`, `header-3d`, `header-connect` (these have structural function — they delineate sections, not decorative)
- `cat-waving.svg` (inline with About Me)
- `cat-sleeping.svg` (above footer)

## Section count comparison

| | Before | After |
|---|---|---|
| Top-level content sections | ~11 | 5 |
| Decorative image rows | 4 rows (~10 images) | 0 rows |
| Inline decorative cats | 0 | 2 |
| Contribution visualizations | 4 | 1 |
| Stats cards blocks | 2 | 1 |
| Typing SVGs | 2 | 1 |

## Non-goals

- Changing the visual theme (tokyonight colors stay)
- Changing SVG assets themselves (that's sub-project C)
- Adding new sections like pinned projects, Spotify, WakaTime (that's sub-project B)
- Fixing external image service reliability, alt-text, or load performance (that's sub-project D)
- Rewriting the `cappy = { ... }` code block content (content stays; only its surrounding layout changes)

## Implementation approach

Single-file edit to `README.md`. No code, no new files, no deletions from `assets/`. The restructure is a series of HTML/Markdown deletions and one cat image relocation (cat-waving into the About block).

Validation: after edits, render the README on GitHub (either push to a branch or preview locally) and visually confirm the 5-section structure. Because this is a profile README with many externally-hosted images, automated tests are not applicable — visual review is the validation step.

## Success criteria

- README has exactly 5 content sections between header and footer
- Exactly 1 contribution visualization (3D graph)
- Exactly 1 stats block (GitHub Stats + Top Languages)
- Exactly 1 typing SVG (in header)
- Exactly 2 decorative cats (`cat-waving` in About, `cat-sleeping` above footer)
- No duplicate information across sections
- The "Cappy" identity (cat theme, tokyonight palette, personality in About block) is preserved
- All SVG assets in `assets/` remain on disk (unreferenced ones stay for future use)
