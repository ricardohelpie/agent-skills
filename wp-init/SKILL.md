---
name: wp-init
description: Initializes a WordPress/Elementor project in Claude Code. Creates CLAUDE.md with project context, .mcp.json with Basic Auth credentials, and documents WP Application Password. Run at the start of any new WP client project.
metadata:
  author: Ricardo
  version: "1.0.0"
  domain: wordpress
  triggers: wp-init, new WordPress project, init WP, setup WordPress MCP
  role: setup
  scope: project-init
  output-format: files
---

# WP Init

Sets up a WordPress/Elementor project with MCP connection, credentials, and CLAUDE.md documentation — mirroring the Cosmetique setup pattern.

## Steps

When run, execute in this exact order:

### 1. Explore codebase
- Check current directory for existing `CLAUDE.md`, `.mcp.json`, and any project files
- Identify the project name (from folder name or ask the user)
- Ask for: WP site URL, WP admin username, and Application Password (if not already provided)

### 2. Create or update CLAUDE.md
Create `CLAUDE.md` in the project root with:

```markdown
# CLAUDE.md — [Project Name]

## WordPress Credentials

- **Site URL:** https://example.com
- **Admin user:** admin_username
- **Application Password:** xxxx xxxx xxxx xxxx xxxx xxxx
- **REST API base:** https://example.com/wp-json/wp/v2

## MCP Servers

- `elementor-mcp` — Elementor widget editing via MCP
- `wordpress` — WordPress REST API via MCP

> MCP configured in `.mcp.json`. Restart Claude Code after any MCP config change.

## Project Notes

[Add project-specific notes here]
```

### 3. Create .mcp.json
Create `.mcp.json` at the project root with Basic Auth:

```json
{
  "mcpServers": {
    "elementor-mcp": {
      "command": "npx",
      "args": ["elementor-mcp"],
      "env": {
        "WP_URL": "https://example.com",
        "WP_USERNAME": "admin_username",
        "WP_APP_PASSWORD": "xxxx xxxx xxxx xxxx xxxx xxxx"
      }
    },
    "wordpress": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-wordpress"],
      "env": {
        "WORDPRESS_SITE_URL": "https://example.com",
        "WORDPRESS_USERNAME": "admin_username",
        "WORDPRESS_PASSWORD": "xxxx xxxx xxxx xxxx xxxx xxxx"
      }
    }
  }
}
```

Replace placeholders with actual values provided by the user.

### 4. Confirm and prompt restart
After creating both files:
1. Show a summary of what was created
2. Remind the user: **"Restart Claude Code from the project folder so MCP servers load correctly."**
3. Do NOT proceed with any WordPress/Elementor work until restart is confirmed

## Constraints

- NEVER store credentials anywhere other than `CLAUDE.md` and `.mcp.json` in the project root
- NEVER commit `.mcp.json` to git — remind the user to add it to `.gitignore`
- Always use Basic Auth (Application Password), not OAuth, unless the user explicitly requests OAuth
- If Application Password is not yet created, guide the user: WP Admin → Users → Profile → Application Passwords
