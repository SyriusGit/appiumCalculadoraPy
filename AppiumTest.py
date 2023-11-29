from appium import webdriver
from appium.options.android import UiAutomator2Options

caps = {}
caps["platformName"] = "Android"
caps["automationName"]="uiautomator2"
caps["deviceName"] = "device-5554"
caps["avd"] = "Pixel_2_API_28"
caps["appPackage"] = "com.android.calculator2"
caps["appActivity"] = "com.android.calculator2.Calculator"

capabilities_options = UiAutomator2Options().load_capabilities(caps)

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=  capabilities_options)