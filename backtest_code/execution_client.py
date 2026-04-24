import json

class ExecutionClient:
    def __init__(self, endpoint="http://localhost:8080/execute"):
        # 실제 서버 주소로 변경 예정
        # backtestAgent의 실행 엔드포인트를 기본값으로 설정
        self.endpoint = endpoint

    def request_execution(self, code: str, task_name: str = "backtest"):
        
        # 조립된 코드를 실행 서버(backtestAgent)로 전송
        
        print(f"Requesting execution to {self.endpoint}")
        
        payload = {
            "task": task_name,  # 전 종목 버전 or 필터링 버전 구분하는 태그
            "code": code    # TemplateEngine에서 생성된 전체 코드
        }

        try:
            # 데이터 서버에 전송
            # response = requests.post(self.endpoint, json=payload)
            print(f"Data packet for '{task_name}' is ready.")
            return {"status": "success", "msg": "Payload delivered"}
            
        except Exception as e:
            print(f"[ERROR] Connection failed: {e}")
            return {"status": "error", "msg": str(e)}