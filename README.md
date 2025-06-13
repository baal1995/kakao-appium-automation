# kakao-appium-automation
카카오 워크 및 카카오뱅크 앱 자동화 테스트 프로젝트

# 카카오워크 앱 Appium 자동화 테스트

카카오워크 Android 앱을 대상으로 Appium을 활용한 자동화 테스트를 구현한 프로젝트입니다.  
ADB를 이용한 터치 기반 제어와 WebView 대응, Google Spreadsheet 연동까지 포함된 실전 테스트입니다.

## ✅ 주요 기능
- Appium을 활용한 실제 디바이스 자동화 테스트
- 로그인 키패드 터치 자동화 (`5943`)
- WebView 요소 대응 (XPath 직접 사용)
- Google Sheets 연동: 테스트 결과 자동 기록
- 예외처리 포함한 안정적인 테스트 흐름

## 🧪 테스트 시나리오
1. 앱 실행 확인
2. 비밀번호 입력 (****)
3. 검색 버튼 클릭
4. 검색창 텍스트 입력 ("사원")
5. 프로필(root_layout) 클릭
6. 1:1 채팅 버튼 클릭
7. 메시지 입력 박스 활성화
8. 메시지 입력 ("Appium test message")
9. 메시지 전송
10. 테스트 결과 기록

## ⚙️ 사용 기술
- Python 3.x
- Appium-Python-Client
- gspread, oauth2client
- Google Sheets API
- Android 디바이스 + ADB

## 🗂️ 프로젝트 구조
kakao-appium-automation/
├── run_kakaowork_test.py
├── requirements.txt
├── credentials/
│ └── service_account.json (업로드 금지, .gitignore 처리)
├── docs/
│ └── test_scenarios.md
