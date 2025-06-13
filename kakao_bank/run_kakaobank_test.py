import unittest
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class KakaobankAutomation(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "R3CX705KYZY"  # 실제 디바이스 ID
        options.app_package = "com.kakaobank.channel"
        options.app_activity = ".presentation.view.activity.StartActivity"
        options.no_reset = True
        options.disable_window_animation = True

        # Appium 서버 연결
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

    def test_click_card_application_button(self):
        print("지문 인증을 완료해주세요 (10초 대기)")
        time.sleep(10)  # 사용자가 직접 지문 인증할 시간을 줌

        try:
            # 'cardStateButton' 버튼 클릭
            button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@resource-id='com.kakaobank.channel:id/cardStateButton']"))
            )
            button.click()
            print("첫 번째 버튼 클릭 완료!")

            # 새로운 화면이 로딩될 시간을 고려하여 대기
            time.sleep(7)  

            # 🔹 체크카드 신청 버튼 강제 클릭 (ADB tap)
            x, y = 246, 2270  # 강제 클릭 좌표
            self.driver.execute_script("mobile: shell", {
                "command": "input",
                "args": ["tap", str(x), str(y)]
            })
            print(f"체크카드 신청 버튼 ADB 강제 클릭 완료! (좌표: {x}, {y})")

            # 🔹 약관 동의 버튼 클릭
            time.sleep(3)
            print("필수 약관 및 안내사항 전체 동의 버튼 클릭 시도...")
            agree_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//android.view.View[@text='필수 약관 및 안내사항 전체 동의']"))
            )
            agree_button.click()
            print("필수 약관 및 안내사항 전체 동의 버튼 클릭 완료!")

            # 🔹 스크롤 다운 버튼 클릭
            time.sleep(3)
            print("스크롤 다운 버튼 클릭 시도...")
            scroll_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@resource-id='scrollDown']"))
            )
            scroll_button.click()
            print("스크롤 다운 버튼 클릭 완료!")

            # 🔹 다음 단계 버튼 클릭
            time.sleep(3)  
            print("다음 단계 버튼 클릭 시도...")
            next_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@resource-id='goNext']"))
            )
            next_button.click()
            print("다음 단계 버튼 클릭 완료!")

            # 🔹 두 번째 "다음 버튼" 즉시 강제 클릭 (좌표: 246, 2270)
            time.sleep(3)
            print("두번째 다음 버튼 강제 클릭 실행 중...")
            self.driver.execute_script("mobile: shell", {
                "command": "input",
                "args": ["tap", str(x), str(y)]
            })
            print(f"두번째 다음 버튼 ADB 강제 클릭 완료! (좌표: {x}, {y})")

            # 🔹 첫 번째 확인 버튼 클릭
            time.sleep(3)
            print("첫 번째 확인 버튼 클릭 실행 중...")
            first_confirm_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@resource-id='com.kakaobank.channel:id/confirmButton']"))
            )
            first_confirm_button.click()
            print("첫 번째 확인 버튼 클릭 완료!")

            # 🔹 3초 대기 후 두 번째 확인 버튼 클릭
            time.sleep(3)
            print("두 번째 확인 버튼 클릭 실행 중...")
            second_confirm_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@resource-id='com.kakaobank.channel:id/confirmButton']"))
            )
            second_confirm_button.click()
            print("두 번째 확인 버튼 클릭 완료!")

        except Exception as e:
            print(f"버튼 클릭 실패: {e}")

    def tearDown(self):
        print("테스트 완료. 앱을 종료하지 않습니다.")  # self.driver.quit() 제거

if __name__ == "__main__":
    unittest.main()
