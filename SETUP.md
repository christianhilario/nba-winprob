# Setup (both of us)

## 1. Create the GitHub repo (Chris does this once)
1. Unzip this folder, `cd nba-winprob`.
2. On GitHub: **New repository** → name `nba-winprob` → private → **don't** add README/.gitignore (we already have them).
3. Push:
   ```bash
   git init
   git add .
   git commit -m "Initial scaffold"
   git branch -M main
   git remote add origin https://github.com/<your-username>/nba-winprob.git
   git push -u origin main
   ```
4. Repo → **Settings → Collaborators → Add people** → David's GitHub username.
5. (Optional) **Settings → Branches → Add rule** for `main`: require a pull request before merging. Matches our "review each other's code" promise.

## 2. David clones
```bash
git clone https://github.com/<chris-username>/nba-winprob.git
cd nba-winprob
```

## 3. Python env (both)
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
pytest -q                         # tests should run (most skip until code exists)
```

## 4. Daily git workflow
```bash
git checkout main && git pull
git checkout -b chris/clean-pipeline      # or david/lstm, etc.
# ...work...
git add -p && git commit -m "Align events with game clock"
git push -u origin chris/clean-pipeline
```
Then open a PR on GitHub, the other person reviews + merges. Small PRs > giant ones.

**Data is not in git.** Each of us runs the download script locally, or one person downloads and shares `data/processed/*.parquet` via Google Drive.

## 5. Claude Code
1. Install (needs Node 18+): `npm install -g @anthropic-ai/claude-code`
2. From the repo root: `claude`
3. It auto-reads `CLAUDE.md`, so it already knows the project, who owns what, and the tutor-not-ghostwriter rule. No need to run `/init`.
4. Project slash commands (in `.claude/commands/`):
   - `/explain-error` — paste a traceback, get a Socratic explanation
   - `/review` — reviews your current diff for bugs + leakage
   - `/leak-check` — audits a file for train/test leakage
5. `.claude/settings.json` pre-approves safe commands (pytest, git status/diff) and blocks reading huge raw data files.

Commit `.claude/` and `CLAUDE.md` so we share the same setup. Personal tweaks go in `.claude/settings.local.json` (gitignored).
