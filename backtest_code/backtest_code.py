from .validator import CodeValidator
from .template_engine import TemplateEngine

class BacktestCompiler:
    def __init__(self):
        self.validator = CodeValidator()
        self.engine = TemplateEngine()

    def generate_dual_versions(self, strategy_code, stock_list):
        # 검증 및 전 종목 버전과 필터링 버전을 동시에 생성
        
        # 1. Security Validation
        is_valid, msg = self.validator.validate(strategy_code)
        if not is_valid:
            print(f"[ERROR] Security check failed: {msg}")
            return None, None, msg

        # 2. Dual-mode Template Rendering
        try:
            # 전 종목(2600개) 대상 코드 생성
            full_version = self.engine.render(strategy_code, stock_list, is_full_market=True)
            
            # 리포트 추천 종목 대상 코드 생성
            filtered_version = self.engine.render(strategy_code, stock_list, is_full_market=False)

            print("Dual versions generated successfully.")
            return full_version, filtered_version, "success"
            
        except Exception as e:
            print(f"[ERROR] Rendering failed: {e}")
            return None, None, str(e)