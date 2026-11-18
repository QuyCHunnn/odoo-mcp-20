# Odoo MCP 20

Repository: https://github.com/QuyCHunnn/odoo-mcp-20

Standalone MCP connector for Odoo 20, forked from the local Odoo 19 connector.
Uses External JSON-2 (`/json/2/<model>/<method>`), not native `/mcp` AI tools.
The connector preserves `execute_method`, `batch_execute`, `read_resource`,
strict confirmation tokens, read-only mode and HTTP authentication.

## Setup (Linux / WSL)

```bash
cd /home/quytrung22521557/odoo-mcp-20
uv venv --python 3.12
uv pip install --python .venv/bin/python -e '.[dev]'
cp .env.example .env
chmod 600 .env
# Edit .env with this target's URL, database, username and API key.
codex mcp add odoo20-custom -- /home/quytrung22521557/odoo-mcp-20/run-local.sh
```

Use an API key permitted for External API / RPC, not a key scoped only to native
MCP. Never copy credentials from the Odoo 19 deployment. JSON-2 availability
and permissions depend on your hosting / subscription and account permissions.

After restarting the MCP client, initialize and list tools. Read
`odoo://server/info`, confirm the selected database and Odoo version, then read
`odoo://model/res.partner/quick-schema` and try a small read. Do not test a write
until the identity is correct. Do not silently switch existing MCP connections.

## Behavior

- Odoo ACLs, record rules and private-method restrictions remain enforced.
- Technical models such as `ir.asset` and `ir.actions.client` are accessed via
  ordinary ORM permissions; native AI's model filter is not used by this API.
  Their availability on your actual Odoo 20 instance is not yet verified.
- `batch_execute(atomic=True)` stops on error; completed calls stay committed.
- Keep `MCP_SAFETY_MODE=strict`; replay confirmation tokens with identical calls.
- Optional HTTP transport requires MCP authentication; use the inherited docs.
- The Python import package remains `odoo_mcp`; use a separate venv from v19.

## Validation and migration boundaries

Offline regression and protocol tests are recorded in `VALIDATION.md`.
No live Odoo 20 acceptance or database writes have been performed.
Inherited model knowledge contains Odoo 19 examples. Treat it as reference only:
introspect actual Odoo 20 fields and methods before executing operations.
Do not interpret the target-version constant as evidence of live compatibility.

See `FORK.md` for provenance, `README.upstream.md` for inherited advanced options,
and the MIT `LICENSE` for the original copyright.

Official API documentation:
https://www.odoo.com/documentation/20.0/developer/reference/external_api.html
