"""Offline checks of Odoo 20 external transport; no database is contacted."""

from unittest.mock import Mock

import pytest

from odoo_mcp.odoo_client import OdooClient


def client():
    return OdooClient("https://odoo20.example.test", "demo20", "admin", api_key="test-only")


def test_technical_model_uses_json2_and_database_header():
    c = client()
    response = Mock(status_code=200)
    response.json.return_value = [{"name": "3D Map"}]
    c._post_with_rate_limit_retry = Mock(return_value=response)
    assert c._execute("ir.actions.client", "search_read", domain=[], fields=["name"]) == [{"name": "3D Map"}]
    args, kwargs = c._post_with_rate_limit_retry.call_args
    assert args[0] == "https://odoo20.example.test/json/2/ir.actions.client/search_read"
    assert args[1] == {"domain": [], "fields": ["name"]}
    assert kwargs["retry_allowed"] is True
    assert c.session.headers["X-Odoo-Database"] == "demo20"
    assert c.session.headers["Authorization"] == "Bearer test-only"


def test_asset_create_has_no_automatic_retry():
    c = client()
    response = Mock(status_code=200)
    response.json.return_value = [42]
    c._post_with_rate_limit_retry = Mock(return_value=response)
    assert c._execute("ir.asset", "create", vals_list=[{"name": "map3d"}]) == [42]
    assert c._post_with_rate_limit_retry.call_args.kwargs["retry_allowed"] is False


def test_unauthorized_explains_native_mcp_key_scope():
    c = client()
    response = Mock(
        status_code=401, reason="Unauthorized", url="https://odoo20.example.test/json/2/ir.asset/search_read"
    )
    response.json.return_value = {"message": "Invalid API key"}
    c._post_with_rate_limit_retry = Mock(return_value=response)
    with pytest.raises(ValueError, match="native MCP-only key"):
        c._execute("ir.asset", "search_read", domain=[])
