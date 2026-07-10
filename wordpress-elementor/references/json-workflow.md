# Legacy JSON Workflow (no MCP)

Use this only when the elementor-mcp is not connected. When MCP is available, prefer native MCP tools.

---

## Export from Editor (browser console)

With Elementor Editor open, run in DevTools console:

```javascript
var data = JSON.stringify(elementor.elements.toJSON(), null, 2);
var blob = new Blob([data], {type: 'application/json'});
var url = URL.createObjectURL(blob);
var a = document.createElement('a');
a.href = url;
a.download = 'elementor-export.json';
document.body.appendChild(a);
a.click();
document.body.removeChild(a);
URL.revokeObjectURL(url);
```

---

## Import Wrapper (required)

Elementor rejects raw arrays. Wrap before importing:

```python
import json

with open('elementor-export.json') as f:
    elements = json.load(f)

template = {
    "version": "0.4",
    "title": "Template Name",
    "type": "container",
    "content": elements,
    "page_settings": {}
}

with open('elementor-import.json', 'w', encoding='utf-8') as f:
    json.dump(template, f, ensure_ascii=False, separators=(',', ':'))
```

---

## Strip Empty Fields (reduce payload ~40%)

```python
def deep_strip(obj):
    if isinstance(obj, list):
        return [deep_strip(v) for v in obj]
    if isinstance(obj, dict):
        r = {}
        for k, v in obj.items():
            sv = deep_strip(v)
            if sv is None or sv == '': continue
            if isinstance(sv, list) and len(sv) == 0: continue
            if isinstance(sv, dict) and len(sv) == 0: continue
            r[k] = sv
        return r if r else None
    return obj
```

---

## Known Issues

- **Cloudflare WAF**: blocks JSON containing `<script>` inline. Never include JS in the JSON — add it separately via HTML widget after import
- **nginx 413**: if upload fails, `client_max_body_size` may be too low. Apply `deep_strip()` first; if still failing, ask client to increase server limit
- **Inject without saving** (for testing only): `elementor.elements.reset([obj]); elementor.saver.setFlagEditorChange(true)`
