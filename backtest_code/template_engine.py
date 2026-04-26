class TemplateEngine:
    def render(self, strategy_code: str, stock_list: list, is_full_market: bool = False):
        # 버전 2가지 구분
        if is_full_market:
            # 종목 필터링 없이 전체 시장 대상으로 백테스트
            # DB에서 전체 종목 리스트를 가져오는 코드로 대체 예정
            universe_setup = "TARGET_UNIVERSE = fetch_all_market_stocks()"
        else:
            # 종목 필터링 사용
            universe_setup = f"TARGET_UNIVERSE = {stock_list}"

        # LLM이 생성한 전략 코드에서 불필요한 공백 제거 및 들여쓰기 조정
        # 모든 줄바꿈마다 공백 8칸을 강제로 집어넣어 for 문 안에 들어가도록 함
        indented_code = strategy_code.strip().replace('\n', '\n        ')

        return f"""     
        # 예시)
import pandas as pd
from market_data import fetch_all_market_stocks # 전 종목 데이터를 가져왔다고 가정

# --- 유니버스 설정 ---
{universe_setup}

# 백테스트를 돌린다면 이런 식으로
def run_backtest():
    for stock in TARGET_UNIVERSE:
        print(f"[*] 분석 중: {{stock}}")
        
        # --- LLM이 생성한 전략 주입 ---
        {indented_code}

if __name__ == "__main__":
    run_backtest()
""".strip() # 불필요한 공백 제거