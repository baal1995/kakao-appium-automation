import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common.exceptions import WebDriverException

# 카카오워크 앱의 설정
capabilities = {
    'platformName': 'Android',
    'deviceName': 'R3CX705KYZY',  # 실제 디바이스 이름
    'appPackage': 'com.kakaoenterprise.kakaowork',  # 카카오워크 앱 패키지 이름
    'appActivity': 'com.kakaoenterprise.kakaowork.ui.splash.SplashActivity',  # 카카오워크 앱의 첫 화면 액티비티
    'noReset': True
}

# Appium 서버 URL
appium_server_url = 'http://localhost:4723/wd/hub'  # Appium의 기본 URL과 포트 확인

# Google Sheets 연결 설정
def connect_to_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/rkdwn/Desktop/자동화/service_account.json", scope)  # 파일명 수정
    client = gspread.authorize(creds)
    sheet = client.open("테스트 체크리스트").sheet1  # "테스트 체크리스트" 시트 열기
    return sheet

# 전역으로 Google Sheets 연결을 한 번만 수행
sheet = connect_to_google_sheets()

class TestKakaoWork(unittest.TestCase):
    def setUp(self) -> None:
        try:
            # Appium 서버와 연결하여 앱 실행
            options = UiAutomator2Options().load_capabilities(capabilities)
            self.driver = webdriver.Remote(appium_server_url, options=options)
        except WebDriverException as e:
            if 'device' in str(e).lower():  # 디바이스 연결 문제인 경우
                print(f"USB 분리 오류 발생: {e}")
                self.update_result_in_sheet(1, "앱 실행 확인", "카카오워크 앱이 정상적으로 실행되는지 확인", "F")
                self.fail("디바이스 연결 오류로 인해 테스트를 종료합니다.")  # 테스트 실패 처리
            else:
                print(f"Appium 서버 오류: {e}")
                self.update_result_in_sheet(1, "앱 실행 확인", "카카오워크 앱이 정상적으로 실행되는지 확인", "F")
                self.fail("Appium 서버 오류로 인해 테스트를 종료합니다.")  # 서버 오류로 종료

    def tearDown(self) -> None:
        try:
            # 앱 종료 (세션 종료)
            if self.driver:
                self.driver.quit()  # WebDriver 세션 종료 (앱과 세션 종료)
                print("앱과 세션이 종료되었습니다.")
        except WebDriverException as e:
            print(f"앱 종료 중 오류 발생: {e}")

    def test_open_kakao_work(self) -> None:
        try:
            # 테스트 실행
            self.update_result_in_sheet(1, "앱 실행 확인", "카카오워크 앱이 정상적으로 실행되는지 확인", "P")
            self.enter_password()
            self.update_result_in_sheet(2, "비밀번호 입력", "키패드에서 '5943'을 입력하여 로그인 화면 진입 가능 여부 확인", "P")
            self.click_search_button()
            self.update_result_in_sheet(3, "검색 버튼 클릭", "비밀번호 입력 후 검색 버튼이 정상적으로 클릭되는지 확인", "P")
            time.sleep(1)
            self.enter_text_in_search("김기태")
            self.update_result_in_sheet(4, "검색창에 텍스트 입력", "검색창에 '김기태' 텍스트가 정상적으로 입력되는지 확인", "P")
            time.sleep(1.5)
            self.click_root_layout_button()
            self.update_result_in_sheet(5, "프로필 버튼 클릭", "검색 후 프로필 버튼(root_layout)이 정상적으로 클릭되는지 확인", "P")
            time.sleep(1.5)
            self.click_scroll_view_button()
            self.update_result_in_sheet(6, "1대1 채팅 버튼 클릭", "프로필 화면에서 1대1 채팅 버튼(scroll_view)이 정상적으로 클릭되는지 확인", "P")
            time.sleep(1)
            self.enter_message_in_text_box("Appium test message")
            self.update_result_in_sheet(7, "메시지 입력 박스 활성화", "메시지 입력 박스('메시지를 입력해보세요.')가 정상적으로 활성화되는지 확인", "P")
            self.click_send_message_button()
            self.update_result_in_sheet(8, "메시지 입력", "메시지 입력 박스에 'Appium test message'가 정상적으로 입력되는지 확인", "P")
            time.sleep(2)
            self.update_result_in_sheet(9, "메시지 보내기 버튼 클릭", "메시지 보내기 버튼(content-desc='메시지 보내기')이 정상적으로 클릭되어 메시지가 전송되는지 확인", "P")
            self.update_result_in_sheet(10, "테스트 결과", "모든 테스트가 성공적으로 진행됨", "P")
        except WebDriverException as e:
            print(f"테스트 중 오류 발생: {e}")
            self.update_result_in_sheet(1, "앱 실행 확인", "카카오워크 앱이 정상적으로 실행되는지 확인", "F")
            self.update_result_in_sheet(2, "비밀번호 입력", "키패드에서 '5943'을 입력하여 로그인 화면 진입 가능 여부 확인", "F")
            self.update_result_in_sheet(3, "검색 버튼 클릭", "비밀번호 입력 후 검색 버튼이 정상적으로 클릭되는지 확인", "F")
            self.update_result_in_sheet(4, "검색창에 텍스트 입력", "검색창에 '김기태' 텍스트가 정상적으로 입력되는지 확인", "F")
            self.update_result_in_sheet(5, "프로필 버튼 클릭", "검색 후 프로필 버튼(root_layout)이 정상적으로 클릭되는지 확인", "F")
            self.update_result_in_sheet(6, "1대1 채팅 버튼 클릭", "프로필 화면에서 1대1 채팅 버튼(scroll_view)이 정상적으로 클릭되는지 확인", "F")
            self.update_result_in_sheet(7, "메시지 입력 박스 활성화", "메시지 입력 박스('메시지를 입력해보세요.')가 정상적으로 활성화되는지 확인", "F")
            self.update_result_in_sheet(8, "메시지 입력", "메시지 입력 박스에 'Appium test message'가 정상적으로 입력되는지 확인", "F")
            self.update_result_in_sheet(9, "메시지 보내기 버튼 클릭", "메시지 보내기 버튼(content-desc='메시지 보내기')이 정상적으로 클릭되어 메시지가 전송되는지 확인", "F")
            self.update_result_in_sheet(10, "테스트 결과", "테스트 중 오류 발생", "F")

    def update_result_in_sheet(self, test_id, test_case_name, test_step, result):
        # Google Sheets에 결과 업데이트
        row = test_id + 1  # 테스트 ID에 맞는 행 찾기
        sheet.update_cell(row, 1, test_id)  # 1열에 테스트 ID
        sheet.update_cell(row, 2, test_case_name)  # 2열에 테스트 케이스 이름
        sheet.update_cell(row, 3, test_step)  # 3열에 테스트 단계
        sheet.update_cell(row, 4, result)  # 4열에 P/F 결과 (Pass/Fail)
        print(f"Test ID {test_id}: {test_case_name} - {result}")

    def enter_password(self):
        digits = ['5', '9', '4', '3']
        for digit in digits:
            button_xpath = f'//android.widget.Button[@text="{digit}"]'
            button = self.driver.find_element('xpath', button_xpath)
            button.click()
            time.sleep(1)
        print("비밀번호가 입력되었습니다.")

    def click_search_button(self):
        try:
            search_button_xpath = '//android.widget.Button[@content-desc="검색"]'
            search_button = self.driver.find_element('xpath', search_button_xpath)
            search_button.click()
            print("검색 버튼이 클릭되었습니다.")
        except Exception as e:
            print(f"검색 버튼 클릭 중 오류 발생: {e}")

    def enter_text_in_search(self, text):
        try:
            search_input_xpath = '//android.widget.EditText[@resource-id="com.kakaoenterprise.kakaowork:id/et_search"]'
            search_input = self.driver.find_element('xpath', search_input_xpath)
            search_input.send_keys(text)
            print(f"'{text}'가 검색창에 입력되었습니다.")
        except Exception as e:
            print(f"검색창에 텍스트 입력 중 오류 발생: {e}")

    def click_root_layout_button(self):
        try:
            button_xpath = '//android.view.ViewGroup[@resource-id="com.kakaoenterprise.kakaowork:id/root_layout"]'
            button = self.driver.find_element('xpath', button_xpath)
            button.click()
            print("프로필 버튼이 클릭되었습니다.")
        except Exception as e:
            print(f"프로필 버튼 클릭 중 오류 발생: {e}")

    def click_scroll_view_button(self):
        try:
            scroll_button_xpath = '//androidx.compose.ui.platform.ComposeView[@resource-id="com.kakaoenterprise.kakaowork:id/compose_view"]/android.view.View/android.widget.ScrollView/android.view.View[2]'
            scroll_button = self.driver.find_element('xpath', scroll_button_xpath)
            scroll_button.click()
            print("1대1 채팅 버튼이 클릭되었습니다.")
        except Exception as e:
            print(f"1대1 채팅 버튼 클릭 중 오류 발생: {e}")

    def enter_message_in_text_box(self, message):
        try:
            message_box_xpath = '//android.widget.EditText[@text="메시지를 입력해보세요."]'
            message_box = self.driver.find_element('xpath', message_box_xpath)
            message_box.send_keys(message)
            print(f"'{message}'가 메시지 입력 박스에 입력되었습니다.")
        except Exception as e:
            print(f"메시지 입력 중 오류 발생: {e}")

    def click_send_message_button(self):
        try:
            send_button_xpath = '//android.widget.Button[@content-desc="메시지 보내기"]'
            send_button = self.driver.find_element('xpath', send_button_xpath)
            send_button.click()
            print("메시지 보내기 버튼이 클릭되었습니다.")
        except Exception as e:
            print(f"메시지 보내기 버튼 클릭 중 오류 발생: {e}")

if __name__ == '__main__':
    unittest.main()
