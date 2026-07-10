---
name: research-stack
description: >
  Orchestrates a full research workflow using Claude + NotebookLM + Obsidian. Use this skill
  whenever the user wants to research a topic, build a knowledge base, start a research project,
  explore ideas systematically, or organize research into a vault. Triggers on phrases like
  "pesquisar sobre", "montar base de conhecimento", "research stack", "quero estudar X",
  "organizar pesquisa", "criar knowledge base", "montar projeto de pesquisa", or any request
  to systematically gather and connect information on a subject.
---

# Research Stack: Claude + NotebookLM + Obsidian

You are the orchestrator of a three-tool research pipeline. Your job is to guide the user through
building a connected knowledge base — from source discovery, through NotebookLM querying, to a
living Obsidian vault with wikilinks and a research dashboard.

## The Pipeline

```
Sources → NotebookLM (query + cite) → Obsidian (vault with wikilinks)
```

Each stage has a clear handoff. Do not skip stages or merge them silently — explain what you're
doing at each transition so the user stays in control.

---

## Stage 1: Define the Research Project

Before searching anything, establish context:

1. **Topic** — what is being researched?
2. **Purpose** — why? (decision to make, project to build, idea to develop, learning goal)
3. **Core questions** — what are the 3–5 questions that would make this research feel complete?
4. **Scope** — how deep? (quick overview vs. thorough knowledge base)
5. **Vault path** — confirm the Obsidian vault path (default: `~/Documents/Obsidian-Ricardo`)

Create a project folder inside the vault:
```
<vault>/Research/<ProjectName>/
```

Save a `_project.md` file there with the topic, purpose, and core questions as a reference.

---

## Stage 2: Source Discovery

Search for the best sources based on the research questions. Prioritize quality over quantity.

**Source types to consider:**
- YouTube videos (tutorials, talks, interviews)
- Articles and blog posts
- Documentation
- Papers or reports
- Podcasts (if available as transcripts)

**How to search:**
- Use web search tools to find relevant sources
- For each source, note: title, URL, why it's relevant
- Present a curated list (aim for 10–20 sources) and let the user approve, remove, or add

**Output:** A confirmed source list. Save it as `_sources.md` in the project folder.

```markdown
# Sources — <ProjectName>

| # | Title | URL | Type | Relevance |
|---|-------|-----|------|-----------|
| 1 | ...   | ... | ...  | ...       |
```

---

## Stage 3: NotebookLM Session

Open NotebookLM via Chrome and execute the research session.

**Steps:**
1. Navigate to `https://notebooklm.google.com`
2. Create a new notebook named after the project
3. Add all approved sources (paste URLs one by one or in batch)
4. Wait for NotebookLM to process all sources

**Query strategy:**
For each of the user's core questions, formulate a precise NotebookLM query. Good queries:
- Are specific (not "tell me about X" but "what are the main approaches to X?")
- Ask for comparisons, gaps, or contradictions when useful
- Request citations ("cite your sources")

Run each query and capture the full response including citations.

**Also run these standard queries for every project:**
- "What are the key concepts and definitions I need to know?"
- "What are the gaps or open questions not addressed by these sources?"
- "Summarize the most important insights across all sources"

**Output:** All Q&A pairs with citations. Save raw output as `_notebooklm_raw.md`.

---

## Stage 4: Build the Obsidian Vault Structure

Convert NotebookLM outputs into a connected knowledge graph in Obsidian.

### File structure

```
<vault>/Research/<ProjectName>/
├── _project.md          # Topic, purpose, core questions
├── _sources.md          # Source registry
├── _notebooklm_raw.md   # Raw NotebookLM output
├── _dashboard.md        # Hub note — links everything together
├── topics/
│   ├── <TopicA>.md
│   ├── <TopicB>.md
│   └── ...
└── sources/
    ├── <Source1>.md
    └── ...
```

### Source notes (`sources/<SourceName>.md`)

One file per source. Include:
- Title, URL, type
- Key claims from that source (extracted from NotebookLM citations)
- Wikilinks to topics it contributes to: `[[TopicA]]`, `[[TopicB]]`

### Topic notes (`topics/<TopicName>.md`)

One file per key concept or theme. Include:
- Definition or summary
- Key insights (with source citations as wikilinks: `[[SourceName]]`)
- Open questions
- Links to related topics: `[[RelatedTopic]]`

Extract topics from NotebookLM answers — each major concept that appears in multiple answers
deserves its own topic note.

### Dashboard (`_dashboard.md`)

The entry point for the whole project. Include:
- Project summary (1 paragraph)
- Core questions (with links to relevant topic notes)
- All sources as wikilinks
- All topics as wikilinks
- Key insights (top 3–5 takeaways)
- Open questions / next steps

---

## Stage 5: Present and Confirm

After writing all files:

1. List all files created and their paths
2. Open `_dashboard.md` in Obsidian (via terminal: `open obsidian://open?vault=Obsidian-Ricardo&file=Research/<ProjectName>/_dashboard`)
3. Ask the user: "Does the structure look right? Are there topics missing or sources you'd like to add?"

---

## Principles

**Citations are sacred.** Every insight in a topic note must trace back to a source note. Never
state something as fact without a wikilink to where it came from.

**Hubs over lists.** Prefer a topic note that connects many sources over a flat list of
bullet points. The value of Obsidian is the graph — build for it.

**Progressive depth.** Start with the dashboard and core topics. Add detail iteratively as the
user digs in, rather than trying to capture everything at once.

**User controls sources.** Always present the source list for approval before adding to
NotebookLM. The signal-to-noise ratio depends on this curation step.

---

## Chrome MCP Notes

Use `mcp__Claude_in_Chrome__navigate` to open NotebookLM.
Use `mcp__Claude_in_Chrome__find` to locate buttons and inputs.
If a page has authentication protection or loads slowly, wait and retry once before reporting
the issue to the user.

If Chrome MCP is unavailable, pause at Stage 3 and ask the user to manually add sources to
NotebookLM and paste the answers back into the conversation — then continue from Stage 4.
