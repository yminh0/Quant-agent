# 🤖 Quant-Agent: LLM-based Algorithm Trading System

본 프로젝트는 LLM을 활용하여 투자 전략 수립부터 백테스트, 실행까지 자동화하는 알고리즘 트레이딩 플랫폼입니다.

> **현재 저장소 상태**: Backtest Compiler 파트 PoC 구현 

## Backtest code Compile 로직 PoC
### 🛠 핵심 기능 (Key Features)

1. **AST 기반 보안 검증 (Security)**
   - `validator.py`를 통해 파이썬 구문을 정적으로 분석합니다.
   - 화이트리스트 기반의 모듈 허용 및 위험 함수(`eval`, `os.system` 등)를 원천 차단합니다.

2. **듀얼 트랙 코드 생성 (Code Generation)**
   - LLM으로부터 전달받은 코드와 종목 리스트를 기반으로 동일한 로직을 사용하여 '시장 전체(Full-Market)'와 '필터링 종목(Filtered)' 두 가지 버전의 백테스트 코드를 생성합니다.
   - `template_engine.py`를 사용하여 구조화된 코드 조립을 보장합니다.

3. **에이전트 통신 (Integration)**
   - 생성된 코드를 JSON 패킷으로 구성하여 백테스트 실행 서버(`backtestAgent`)로 전송 요청을 수행합니다. -> **execution_client.py**

### 🚀 시작하기 (Getting Started)

#### 1. 환경 설정
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
```

