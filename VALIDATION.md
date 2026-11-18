# Validation - 2026-11-18

Environment: Python 3.12.3, FastMCP 4.2.1, MCP SDK 2.3.0.

- Offline pytest suite: **957 passed**, 17.25 seconds.
  Command: `.venv/bin/python -m pytest tests --ignore=tests/live -q`
- Suite includes in-memory MCP initialization/tool discovery for both supported
  protocol eras, authentication, strict write/token gates, read-only guard,
  batch gate, JSON-2 argument mapping and three new Odoo 20 transport tests.
- Black: 60 Python files unchanged.
- isort: passed.
- Ruff for modified transport and new tests: passed.
- `bash -n run-local.sh run-docker.sh`: passed.
- Full inherited Ruff/mypy backlog remains documented in CI as non-blocking.
- No Docker access, image build or container runtime validation performed.
- No live Odoo 20 API authentication, schema, business method or write test.
- No API key, database data or existing MCP registration was copied/changed.

The passing mocks validate the connector, not the live Odoo 20 server.
Live acceptance requires a separately provided External API key, explicit
selected target, identity/schema checks and a reviewed write/readback.
