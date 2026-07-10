# Carousel Update

Safe, verified workflow for updating Elementor carousels via MCP. Prevents the carousel_items[] / elements[] desync bug and ensures credentials are valid before any write.

## Trigger

When the user asks to update, add, remove, or reorder slides in an Elementor carousel widget.

## Inputs

- **Page ID** — the Elementor page containing the carousel
- **Widget ID** — the specific carousel widget (if known; otherwise locate it)
- **Change description** — what to add/remove/reorder (slides, videos, logos, titles, etc.)

## Steps

### 1. Verify Application Passwords & MCP connectivity

Before any write operation:
1. Confirm the elementor-mcp server is connected (list tools or call a read-only endpoint)
2. If the connection fails or returns a nonce/auth error → **STOP** and tell the user to refresh Application Passwords or reconnect the MCP server
3. Do NOT fall back to REST API / curl workarounds — they cause persistence issues

### 2. Get current widget settings

1. Use `get-element-settings` (or equivalent MCP read tool) to fetch the full carousel widget data
2. Store the current state:
   - `elements[]` array (the container children)
   - `carousel_items[]` repeater array
   - Total slide count before changes
3. Report the current slide count and titles to the user for confirmation

### 3. Update widget — keep elements[] and carousel_items[] in sync

**Critical rule:** every entry in `carousel_items[]` must have a matching container in `elements[]`, and vice versa.

1. Build the updated `carousel_items[]` array with all required fields per slide (title, image, link, etc.)
2. Build the matching `elements[]` array with one container per slide
3. Verify both arrays have the **same length** before writing
4. Apply the update via elementor-mcp (never via REST API `_elementor_data`)
5. If the write fails with a nonce/auth error → go back to Step 1

### 4. Verify slide count and titles

After the write succeeds:
1. Re-fetch the widget settings using `get-element-settings`
2. Count slides in both `elements[]` and `carousel_items[]`
3. Confirm:
   - `elements[].length === carousel_items[].length === expected count`
   - Every slide has its expected title text set
4. If counts mismatch or titles are missing → fix immediately and re-verify
5. Report the verified counts and titles to the user

### 5. Save learnings

After a successful update (or after fixing a failure):
1. Invoke `/save-learnings` with:
   - What was changed (page, widget, slide count before/after)
   - Any issues encountered and how they were resolved
   - Any new failure patterns discovered
2. If a new desync pattern or MCP gotcha was found, note it for future skill updates

## Known failure modes

| Symptom | Cause | Fix |
|---|---|---|
| Fewer slides than expected | `carousel_items[]` and `elements[]` out of sync | Rebuild both arrays with matching lengths |
| Slides show but titles are blank | Title field not set per-slide in `carousel_items[]` | Set title for every repeater entry |
| Write returns 403 / nonce error | Expired Application Password or nonce | Refresh credentials, reconnect MCP |
| Changes don't persist after save | Used REST API instead of elementor-mcp | Always use MCP tools for writes |

## What NOT to do

- Never write `_elementor_data` via the WordPress REST API
- Never assume slide count is correct without re-fetching after the write
- Never skip the sync check between `elements[]` and `carousel_items[]`
- Never attempt curl/REST workarounds when MCP auth fails — fix the credentials instead
