import pytest
import yaml
from pathlib import Path

@pytest.fixture
def load_automation():
    """Загружает YAML-файл с автоматизациями."""
    file_path = Path("automations") / "light_on.yaml"
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def test_light_automation_structure(load_automation):
    """Проверяет структуру автоматизации."""
    assert isinstance(load_automation, list)
    automation = load_automation[0]
    assert "alias" in automation
    assert "trigger" in automation
    assert "condition" in automation or "action" in automation
