import os
from backtest_code.backtest_code import BacktestCompiler
from backtest_code.execution_client import ExecutionClient

def run_poc():
    # 객체 초기화
    compiler = BacktestCompiler()
    client = ExecutionClient()

    # [입력 데이터] LLM으로부터 전달받았다고 가정
    user_logic = "if data['close'] > data['open']: self.buy()"
    report_universe = ['005930', '000660', '035420'] # 삼성전자, SK하이닉스, 네이버

    print("=== Quant-Agent PoC Pipeline Start ===")

    # 두가지 버전 코드 생성 (전 종목 버전 and 필터링 버전)
    full_code, filtered_code, status = compiler.generate_dual_versions(user_logic, report_universe)
    
    if status != "success":
        print(f"[ERROR] Compilation failed: {status}")
        return

    # 결과 저장 및 서버 전송 (전 종목 버전)
    with open("result_full_market.py", "w", encoding="utf-8") as f:
        f.write(full_code)
    print(" -> [OK] Full-market code saved.")
    client.request_execution(full_code, task_name="FULL_SCAN")

    # 결과 저장 및 서버 전송 (필터링 버전)
    with open("result_filtered_test.py", "w", encoding="utf-8") as f:
        f.write(filtered_code)
    print(" -> [OK] Filtered-universe code saved.")
    client.request_execution(filtered_code, task_name="FILTERED_BACKTEST")

    print("\n=== [DONE] All tasks completed successfully. ===")

if __name__ == "__main__":
    run_poc()