import pytest
from backtest_code.validator import CodeValidator

@pytest.fixture
def validator():
    return CodeValidator()

def test_tc01_valid_strategy(validator):
    """[TC-01] 정상 전략 코드 검증"""
    code = "import pandas as pd\nprint(pd.__version__)"
    is_valid, msg = validator.validate(code)
    assert is_valid is True
    assert msg == "Valid"

def test_tc02_blocked_import(validator):
    """[TC-02] 미허용 모듈 차단"""
    code = "import os\nos.system('ls')"
    is_valid, msg = validator.validate(code)
    assert is_valid is False
    assert "Unauthorized module" in msg

def test_tc03_forbidden_function(validator):
    """[TC-03] 위험 함수 호출 차단"""
    code = "eval('1+1')"
    is_valid, msg = validator.validate(code)
    assert is_valid is False
    assert "Forbidden name" in msg

def test_tc04_attribute_access(validator):
    """[TC-04] 속성 우회 접근 차단"""
    code = "import pandas as pd\npd.os.system('rm -rf')"
    is_valid, msg = validator.validate(code)
    assert is_valid is False
    assert "Forbidden attribute" in msg

def test_tc05_syntax_error(validator):
    """[TC-05] 문법 오류 탐지"""
    code = "if x = 10:"
    is_valid, msg = validator.validate(code)
    assert is_valid is False
    assert "invalid syntax" in msg.lower()