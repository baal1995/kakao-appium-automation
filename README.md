# kakao-appium-automation

**카카오워크 및 카카오뱅크 앱 Appium 자동화 테스트 프로젝트**

Android 앱을 대상으로 Appium을 활용해 실제 업무 시나리오 기반 자동화를 구현했습니다.  
비정형 ADB 좌표 터치, WebView 대응, Google Sheets 결과 기록, 안정적인 예외 처리 등을 포함합니다.

[📥 영상 다운로드 (Google Drive)](https://drive.google.com/your-shared-video-link)

---

## ✅ 주요 기능

- Appium 기반 실제 디바이스 자동화
- WebView 및 특수 요소 대응 (XPath 활용)
- ADB 좌표 기반 강제 터치로 비표준 버튼 제어
- Google Sheets 연동 결과 기록 (카카오워크용)
- `unittest` 기반 구조화된 테스트 설계

---

## 🧪 테스트 시나리오 구성

### ▶ 카카오워크 (`/kakaowork/run_kakaowork_test.py`)
- 앱 실행 확인
- 비밀번호 키패드 자동 입력
- 검색 버튼 클릭
- 사용자 이름 입력
- 사용자 프로필 클릭
- 1:1 채팅 진입
- 메시지 입력 및 전송
- Google Sheets에 각 단계 결과 자동 기록

### ▶ 카카오뱅크 (`/kakao_bank/run_kakaobank_test.py`)
- 지문 인증 (사용자 수동 처리 대기)
- 카드 상태 확인 버튼 클릭
- 체크카드 신청 (좌표 기반 ADB 강제 클릭)
- 약관 전체 동의
- 스크롤 다운 및 다음 단계 이동
- 확인 버튼 2회 클릭

---

## ⚙️ 기술 스택

- Python 3.x
- Appium-Python-Client
- Selenium (WebDriverWait + expected_conditions)
- gspread / oauth2client (Google Sheets API)
- Android 디바이스 + ADB

---

## 📂 프로젝트 구조

```plaintext
kakao-appium-automation/
├── README.md
├── requirements.txt
├── .gitignore
├── kakaowork/
│   └── run_kakaowork_test.py
├── kakao_bank/
│   └── run_kakaobank_test.py
├── credentials/
│   └── service_account.json (※ 업로드 금지)
```

---

## 📊 Google Sheets 연동 (카카오워크)

Google Cloud Platform에서 발급받은 `service_account.json` 키 파일이 필요합니다.  
`credentials/` 폴더에 파일을 위치시키고 `.gitignore`로 제외합니다.

---

## 🚀 실행 방법

```bash
pip install -r requirements.txt
python kakaowork/run_kakaowork_test.py
python kakao_bank/run_kakaobank_test.py
```
