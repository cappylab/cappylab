# README Minimalist Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Cut `README.md` from ~20 content blocks to 5 sections, preserving the "Cappy" identity while removing redundant contribution visualizations, stats cards, decorative images, and typing SVGs.

**Architecture:** Pure content deletion from a single Markdown/HTML file (`README.md`). No code changes, no test changes, no asset file deletions. Each task is a small focused edit, committed separately so any change can be individually reverted. Validation is visual — after all tasks, render the README on GitHub and confirm structure.

**Tech Stack:** Markdown + HTML (inline). No runtime. No build step. Edits use the `Edit` tool with exact `old_string` / `new_string` matching.

**Spec:** `docs/superpowers/specs/2026-04-22-readme-minimalist-restructure-design.md`

**Notes for the implementing engineer:**
- Line numbers shift after each task. Use the exact HTML comment section markers (shown in each task) as anchors, not line numbers.
- Every task ends with a commit. This enables per-task revert if any single deletion is wrong.
- The `cat-waving.svg`, `cat-sleeping.svg`, and all `header-*.svg` files are kept on disk — we only stop referencing removed sections.
- Do NOT delete any files in `assets/`. Spec sub-project C may re-use them later.
- If in doubt whether a block is "decorative" vs "structural": `header-*.svg` = structural (section banner), everything else = decorative.

---

## File Structure

Files touched:
- **Modify:** `C:/Users/jeong/project/jhm1909/README.md`

Files NOT touched (important):
- `assets/cats/*.svg` — all kept
- `assets/plants/*.svg` — all kept
- `profile-3d-contrib/profile-night-green.svg` — kept, still referenced
- Any workflow or CI config — out of scope (that's sub-project D)

---

## Task 1: Remove random dev quote

**Files:**
- Modify: `README.md` (the `<p align="center">` block containing the `quotes-github-readme.vercel.app` image, which sits immediately after the typing SVG block and before the `PROFILE VIEWS` section comment)

- [ ] **Step 1: Locate the block**

Look for this exact block in `README.md`:

```html
<p align="center">
  <img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight" alt="Random Dev Quote" />
</p>

```

Note: the trailing blank line is part of the block to remove. It sits between the typing SVG paragraph and the `<!-- PROFILE VIEWS -->` comment.

- [ ] **Step 2: Delete the block**

Use the Edit tool with:

`old_string`:
```
<p align="center">
  <img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight" alt="Random Dev Quote" />
</p>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░ PROFILE VIEWS ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

`new_string`:
```
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░ PROFILE VIEWS ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

- [ ] **Step 3: Verify the block is gone**

Run: `grep -c "quotes-github-readme" README.md`
Expected: `0`

- [ ] **Step 4: Commit**

```bash
git add README.md
git commit -m "refactor(readme): remove random dev quote (decorative, no info)"
```

---

## Task 2: Remove the 4-badge profile/follower/stars/repos block

**Files:**
- Modify: `README.md` (the `PROFILE VIEWS` section and its four-badge `<p align="center">` block)

Rationale: these badges (profile views, followers, stars, public repos) all show numeric metrics that overlap with the GitHub Stats card. Removing them cleans the header and avoids duplicating information.

- [ ] **Step 1: Locate the block**

The block spans from the `PROFILE VIEWS` section comment through the trailing `<br/>` before the `ABOUT ME` section.

- [ ] **Step 2: Delete the block**

Use the Edit tool with:

`old_string`:
```
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░ PROFILE VIEWS ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<p align="center">
  <a href="https://github.com/jhm1909">
    <img src="https://komarev.com/ghpvc/?username=jhm1909&style=for-the-badge&color=00d4ff&label=PROFILE+VIEWS" alt="Profile Views" />
  </a>
  <a href="https://github.com/jhm1909?tab=followers">
    <img src="https://img.shields.io/github/followers/jhm1909?style=for-the-badge&color=bb86fc&labelColor=0d1117&label=Followers" alt="Followers" />
  </a>
  <a href="https://github.com/jhm1909?tab=repositories">
    <img src="https://img.shields.io/github/stars/jhm1909?style=for-the-badge&color=ff6b6b&labelColor=0d1117&label=Stars" alt="Stars" />
  </a>
  <a href="https://github.com/jhm1909?tab=repositories">
    <img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=f1e05a&labelColor=0d1117&label=Public+Repos&query=%24.public_repos&url=https%3A%2F%2Fapi.github.com%2Fusers%2Fjhm1909" alt="Public Repos" />
  </a>
</p>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░░ ABOUT ME ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

`new_string`:
```
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░░ ABOUT ME ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

- [ ] **Step 3: Verify the block is gone**

Run: `grep -c "komarev.com/ghpvc" README.md`
Expected: `0`

Run: `grep -c "PROFILE VIEWS" README.md`
Expected: `0`

- [ ] **Step 4: Commit**

```bash
git add README.md
git commit -m "refactor(readme): remove 4-badge header block (redundant with stats)"
```

---

## Task 3: Relocate cat-waving inline within About (above code block)

**Files:**
- Modify: `README.md` (move the `cat-waving.svg` paragraph from after the email badge to between the `header-about.svg` banner and the code block table)

Rationale: the spec's success criteria require exactly 2 decorative cats: `cat-waving` in About and `cat-sleeping` above footer. This task relocates `cat-waving.svg` from a standalone row at the end of the About section to an inline position between the About section banner and the code block. This keeps the signature cat but ties it visually into the About flow.

This task does **two edits** in one commit: one insertion, one deletion.

- [ ] **Step 1: Insert cat-waving paragraph between header-about banner and code block**

Use the Edit tool with:

`old_string`:
```
<p align="center">
  <img src="./assets/cats/header-about.svg" width="700" alt="About Me" />
</p>

<table align="center">
```

`new_string`:
```
<p align="center">
  <img src="./assets/cats/header-about.svg" width="700" alt="About Me" />
</p>

<p align="center">
  <img src="./assets/cats/cat-waving.svg" width="160" alt="Cat Waving" />
</p>

<table align="center">
```

Note: the `width="160"` is slightly smaller than the original `width="180"` to make the cat feel like a companion to the About banner rather than a second focal point.

- [ ] **Step 2: Remove the old standalone cat-waving row**

Use the Edit tool with:

`old_string`:
```
<p align="center">
  <img src="./assets/cats/cat-waving.svg" width="180" alt="Cat Waving" />
</p>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░ TECH STACK ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

`new_string`:
```
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░ TECH STACK ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

- [ ] **Step 3: Verify cat-waving appears exactly once, in the new position**

Run: `grep -c "cat-waving" README.md`
Expected: `1`

Run: `grep -B2 -A2 "cat-waving" README.md`
Expected: the match shows cat-waving between the `header-about.svg` line and the `<table align="center">` line.

Run: `grep -c 'width="180" alt="Cat Waving"' README.md`
Expected: `0` (the old 180-wide version is gone)

- [ ] **Step 4: Commit**

```bash
git add README.md
git commit -m "refactor(readme): move cat-waving inline above About code block"
```

---

## Task 4: Remove Streak Stats section

**Files:**
- Modify: `README.md` (the `STREAK STATS` block between GitHub Stats table and the cat-yarn decorative row)

Rationale: Streak is one of four contribution visualizations in the current README. The spec keeps only the 3D Contribution Graph as the signature viz.

- [ ] **Step 1: Locate the block**

The streak block is delimited by its comment (different comment style than major section headers — uses a single-line divider).

- [ ] **Step 2: Delete the block**

Use the Edit tool with:

`old_string`:
```
<!-- ═══════════════════════════════════════════ STREAK STATS ═══════════ -->

<p align="center">
  <a href="https://github.com/jhm1909">
    <img src="https://streak-stats.demolab.com?user=jhm1909&theme=tokyonight&hide_border=true&background=0d1117&ring=00d4ff&fire=ff6b6b&currStreakLabel=00d4ff&sideLabels=bb86fc&currStreakNum=c9d1d9&sideNums=c9d1d9&dates=8b949e&date_format=j%20M%5B%20Y%5D" alt="GitHub Streak" />
  </a>
</p>

<br/>

```

`new_string`: (empty string — delete the block and the trailing blank line)
```

```

Note: the `new_string` is a single blank line. This collapses the gap where the block used to be into one blank line, preserving readability in the file.

- [ ] **Step 3: Verify**

Run: `grep -c "streak-stats.demolab" README.md`
Expected: `0`

- [ ] **Step 4: Commit**

```bash
git add README.md
git commit -m "refactor(readme): remove streak stats (3D graph is the signature viz)"
```

---

## Task 5: Remove decorative cat-yarn/flower/cat-eating row

**Files:**
- Modify: `README.md` (the `<p align="center">` row with three SVGs that sits after the stats block and before the `TROPHIES` section)

- [ ] **Step 1: Delete the block**

Use the Edit tool with:

`old_string`:
```
<p align="center">
  <img src="./assets/cats/cat-playing-yarn.svg" height="140" alt="Cat Playing Yarn" />
  <img src="./assets/plants/flower-patch.svg" height="140" alt="Flower Patch" />
  <img src="./assets/cats/cat-eating.svg" height="140" alt="Cat Eating" />
</p>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░ TROPHIES ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

`new_string`:
```
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░ TROPHIES ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

- [ ] **Step 2: Verify**

Run: `grep -c "cat-playing-yarn" README.md`
Expected: `0`

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "refactor(readme): remove decorative cat-yarn/flower/cat-eating row"
```

---

## Task 6: Remove Trophies section + cat-chasing-butterfly row

**Files:**
- Modify: `README.md` (the entire `TROPHIES` section including its header banner, trophy image, and the decorative cat-chasing-butterfly row that follows)

- [ ] **Step 1: Delete the block**

Use the Edit tool with:

`old_string`:
```
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░ TROPHIES ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<p align="center">
  <img src="./assets/cats/header-trophies.svg" width="700" alt="GitHub Trophies" />
</p>

<p align="center">
  <a href="https://github.com/ryo-ma/github-profile-trophy">
    <img src="https://github-trophies.vercel.app/?username=jhm1909&theme=tokyonight&no-frame=true&no-bg=true&column=4&row=2&margin-w=15&margin-h=15&rank=SECRET,SSS,SS,S,AAA,AA,A,B,C&v=2" alt="GitHub Trophies" />
  </a>
</p>

<br/>

<p align="center">
  <img src="./assets/cats/cat-chasing-butterfly.svg" width="220" alt="Cat Chasing Butterfly" />
</p>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░ ACTIVITY GRAPH ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

`new_string`:
```
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░ ACTIVITY GRAPH ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

- [ ] **Step 2: Verify**

Run: `grep -c "github-trophies" README.md`
Expected: `0`

Run: `grep -c "cat-chasing-butterfly" README.md`
Expected: `0`

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "refactor(readme): remove trophies section (show-off, not minimalist)"
```

---

## Task 7: Remove Activity Graph section + plant/tree decorative row

**Files:**
- Modify: `README.md` (the `ACTIVITY GRAPH` section including the graph itself and the `vine/cat-sitting-tree/bush` decorative row that follows)

- [ ] **Step 1: Delete the block**

Use the Edit tool with:

`old_string`:
```
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░ ACTIVITY GRAPH ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<p align="center">
  <img src="./assets/cats/header-activity.svg" width="700" alt="Contribution Activity" />
</p>

<p align="center">
  <a href="https://github.com/jhm1909">
    <img src="https://github-readme-activity-graph.vercel.app/graph?username=jhm1909&bg_color=0d1117&color=00d4ff&line=bb86fc&point=ff6b6b&area=true&area_color=00d4ff&hide_border=true&custom_title=Cappy's%20Contribution%20Activity%20%E2%80%94%20Last%2031%20Days&radius=8" alt="Activity Graph" />
  </a>
</p>

<br/>

<p align="center">
  <img src="./assets/plants/vine.svg" height="140" alt="Vine" />
  <img src="./assets/cats/cat-sitting-tree.svg" height="140" alt="Cat Sitting in Tree" />
  <img src="./assets/plants/bush.svg" height="140" alt="Bush" />
</p>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░ SNAKE GRAPH ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

`new_string`:
```
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░ SNAKE GRAPH ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

- [ ] **Step 2: Verify**

Run: `grep -c "activity-graph.vercel" README.md`
Expected: `0`

Run: `grep -c "ACTIVITY GRAPH" README.md`
Expected: `0`

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "refactor(readme): remove activity graph section (3D is the signature viz)"
```

---

## Task 8: Remove Snake Graph section

**Files:**
- Modify: `README.md` (the entire `SNAKE GRAPH` section including the `<picture>` element with dark/light variants)

- [ ] **Step 1: Delete the block**

Use the Edit tool with:

`old_string`:
```
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░ SNAKE GRAPH ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<p align="center">
  <img src="./assets/cats/header-snake.svg" width="700" alt="Contribution Snake" />
</p>

<p align="center">
  <a href="https://github.com/jhm1909">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jhm1909/jhm1909/output/github-snake-dark.svg" />
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/jhm1909/jhm1909/output/github-snake.svg" />
      <img alt="GitHub Contribution Snake" src="https://raw.githubusercontent.com/jhm1909/jhm1909/output/github-snake-dark.svg" />
    </picture>
  </a>
</p>


<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░ 3D CONTRIBUTION ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

`new_string`:
```
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░ 3D CONTRIBUTION ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

Note: there are two consecutive blank lines between the closing `</p>` and the next section comment in the current file. Both are included in the `old_string` above.

- [ ] **Step 2: Verify**

Run: `grep -c "github-snake" README.md`
Expected: `0`

Run: `grep -c "SNAKE GRAPH" README.md`
Expected: `0`

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "refactor(readme): remove snake graph section (3D is the signature viz)"
```

---

## Task 9: Remove Metrics section (4-card block)

**Files:**
- Modify: `README.md` (the entire `METRICS` section, which includes `header-metrics.svg`, the profile-details card, and the 2x2 table of 4 summary cards)

Rationale: the 4-card Metrics block (profile-details, repos-per-language, most-commit-language, stats, productive-time) covers the same information as GitHub Stats + Top Languages already shown above. Removing it eliminates the last major redundancy.

- [ ] **Step 1: Delete the block**

Use the Edit tool with:

`old_string`:
```
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░ METRICS ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<p align="center">
  <img src="./assets/cats/header-metrics.svg" width="700" alt="Detailed Metrics" />
</p>

<p align="center">
  <a href="https://github.com/jhm1909">
    <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=jhm1909&theme=tokyonight" alt="Profile Details" />
  </a>
</p>

<table align="center">
  <tr>
    <td>
      <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=jhm1909&theme=tokyonight" alt="Repos per Language" />
    </td>
    <td>
      <img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=jhm1909&theme=tokyonight" alt="Most Commit Language" />
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=jhm1909&theme=tokyonight" alt="Stats" />
    </td>
    <td>
      <img src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=jhm1909&theme=tokyonight&utcOffset=9" alt="Productive Time" />
    </td>
  </tr>
</table>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░ CONNECT ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

`new_string`:
```
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░ CONNECT ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
```

- [ ] **Step 2: Verify**

Run: `grep -c "github-profile-summary-cards" README.md`
Expected: `0`

Run: `grep -c "header-metrics" README.md`
Expected: `0`

Run: `grep -c "METRICS" README.md`
Expected: `0`

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "refactor(readme): remove 4-card metrics block (redundant with stats)"
```

---

## Task 10: Simplify Connect cat row (keep only cat-sleeping)

**Files:**
- Modify: `README.md` (the three-image row at the end of the Connect section)

Rationale: the spec keeps exactly 2 decorative cats in the final README (`cat-waving` inline in About — placed there by Task 3 — and `cat-sleeping` above the footer). This task drops `cat-tower.svg` and `potted-plant.svg`, leaving `cat-sleeping.svg` as the only image in the pre-footer row.

- [ ] **Step 1: Replace the three-image row with single cat-sleeping**

Use the Edit tool with:

`old_string`:
```
<p align="center">
  <img src="./assets/cats/cat-tower.svg" height="160" alt="Cat Tower" />
  <img src="./assets/plants/potted-plant.svg" height="160" alt="Potted Plant" />
  <img src="./assets/cats/cat-sleeping.svg" height="160" alt="Cat Sleeping" />
</p>
```

`new_string`:
```
<p align="center">
  <img src="./assets/cats/cat-sleeping.svg" height="160" alt="Cat Sleeping" />
</p>
```

- [ ] **Step 2: Verify**

Run: `grep -c "cat-tower" README.md`
Expected: `0`

Run: `grep -c "potted-plant" README.md`
Expected: `0`

Run: `grep -c "cat-sleeping" README.md`
Expected: `1`

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "refactor(readme): connect row keeps only cat-sleeping (signature cat)"
```

---

## Task 11: Remove footer typing SVG

**Files:**
- Modify: `README.md` (the footer `<p align="center">` containing the `readme-typing-svg.demolab.com` image, which sits between the final `<br/>` and the closing capsule wave)

Rationale: the typing SVG in the footer is visually very similar to the one in the header and repeats "Thanks for visiting" / "Have a purrfect day". Removing it makes the footer a single clean wave banner.

- [ ] **Step 1: Delete the block**

Use the Edit tool with:

`old_string`:
```
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=16&duration=4000&pause=1000&color=BB86FC&center=true&vCenter=true&width=600&height=40&lines=Thanks+for+visiting!+%F0%9F%90%B1;Have+a+purrfect+day!;Let's+build+something+amazing+together" alt="Thanks Typing" />
</p>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:bb86fc,50:6366f1,100:00d4ff&height=150&section=footer&text=See%20you%20around!&fontSize=20&fontColor=ffffff&fontAlignY=70&animation=fadeIn" />
```

`new_string`:
```
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:bb86fc,50:6366f1,100:00d4ff&height=150&section=footer&text=See%20you%20around!&fontSize=20&fontColor=ffffff&fontAlignY=70&animation=fadeIn" />
```

- [ ] **Step 2: Verify**

Run: `grep -c "readme-typing-svg.demolab" README.md`
Expected: `1`

(Exactly one typing SVG remains — the one in the header.)

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "refactor(readme): remove footer typing SVG (redundant with header)"
```

---

## Task 12: Final verification and push

**Files:**
- Read-only: `README.md`, git log

- [ ] **Step 1: Verify final structure counts**

Run: `grep -c '^<!-- ═══════════════════════════════════════════════════════════════════════ -->$' README.md`

This counts the top-and-bottom rules of the major section headers. Each major section header uses 2 such lines (top + bottom), plus one extra pair wrapping the HEADER comment at the very top. The 5 content sections (ABOUT ME, TECH STACK, GITHUB STATS, 3D CONTRIBUTION, CONNECT) + HEADER + TYPING SVG + FOOTER = 8 sections × 2 = 16 rule lines.

Expected: `16`

If the count does not match, list the sections:

Run: `grep -E 'ABOUT|TECH|STATS|3D|CONNECT|FOOTER|HEADER|TYPING' README.md | grep '░'`
Expected exactly these 8 lines (order matters):
```
<!-- ░░░░░░░░░░░░░░░░░░░░░░░░ HEADER ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░░ TYPING SVG ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░░ ABOUT ME ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░ TECH STACK ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ░░░░░░░░░░░░░░░░░░░░ GITHUB STATS ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ░░░░░░░░░░░░░░░░░░ 3D CONTRIBUTION ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░ CONNECT ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
<!-- ░░░░░░░░░░░░░░░░░░░░░░ FOOTER ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ -->
```

- [ ] **Step 2: Verify no stray references to removed assets**

Run: `grep -E "streak-stats|github-snake|activity-graph|trophies|github-profile-summary-cards|cat-playing-yarn|cat-chasing-butterfly|cat-sitting-tree|cat-tower|flower-patch|vine.svg|bush.svg|potted-plant|Random Dev Quote|komarev" README.md`
Expected: no output (empty)

If anything prints, re-check which task missed it.

- [ ] **Step 3: Verify kept assets still referenced**

Run: `grep -c "profile-3d-contrib/profile-night-green.svg" README.md`
Expected: `1`

Run: `grep -c "github-readme-stats-sigma-five" README.md`
Expected: `2` (GitHub Stats card + Top Languages card)

Run: `grep -c "cat-waving" README.md`
Expected: `1`

Run: `grep -c "cat-sleeping" README.md`
Expected: `1`

- [ ] **Step 4: Visual render check**

Push the branch (if working in a branch) or confirm the commits are on `main`:

```bash
git log --oneline -15
```

Expected: 11 refactor commits from this plan, plus the earlier `docs(spec)` commit, plus any prior history. Latest commit should be Task 11's footer typing SVG removal.

Then open `https://github.com/jhm1909` and visually confirm:
- Header wave + one typing SVG
- About code block (no dev quote, no 4-badge row above)
- Tech stack table unchanged
- GitHub Stats + Top Languages cards
- 3D Contribution Graph
- No trophies, no snake, no activity graph, no metrics cards, no streak
- Connect section with Gmail + GitHub + Portfolio badges
- One cat (`cat-sleeping`) above footer
- Footer wave only (no thanks typing SVG)

Because GitHub rendering can differ slightly from local, rely on the live render as the final acceptance check.

- [ ] **Step 5: Summary commit (optional)**

If all 11 prior tasks committed cleanly, no summary commit is needed. If any task was rebased or squashed, ensure the final `git log` reflects the intended history.

---

## Rollback

Each task is a separate commit. To revert a single change (e.g., you decide to put trophies back), run:

```bash
git revert <commit-sha>
```

To revert the whole restructure:

```bash
git revert <task-1-sha>..<task-11-sha>
```

The spec document (`docs/superpowers/specs/2026-04-22-readme-minimalist-restructure-design.md`) stays in the repo either way — it remains a useful record of the decision.
