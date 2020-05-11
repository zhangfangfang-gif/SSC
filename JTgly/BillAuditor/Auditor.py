# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# import re
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import os

# noinspection PyMethodMayBeStatic,PyUnusedLocal,SpellCheckingInspection,PyShadowingNames,PyUnresolvedReferences,PyPep8Naming
class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://dev.lanycee.com/login")
        time.sleep(8)
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("19817146896")
        time.sleep(5)
        # driver.find_element_by_xpath("//button[@type='button']").click()
        # time.sleep(3)
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        time.sleep(5)
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("0000")
        time.sleep(5)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(10)
        # 银行卡上传结算单并发放
        driver.find_element_by_xpath("//nz-select/div/div/div/div").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='cdk-overlay-2']/div/div/ul/li[3]").click()
        time.sleep(5)
        driver.find_element_by_link_text(u"提交结算单").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div/div/div[2]/div/div").click()

        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='cdk-overlay-4']/nz-modal/div/div[2]/div/div/div[2]/app-form/nz-form-item/nz-form-control/div/span/nz-upload/div/div").click()
        time.sleep(5)
        # 借助autoIT工具 创建脚本 生成exe文件   直接调用执行exe文件完成自动上传文件
        time.sleep(5)
        os.system(r"E:\Auto\UploadFile.exe")

        #文件上传直接获取windows窗口元素  无法满足上传文件功能 所以借助工具（如上描述）
        # driver.find_element_by_xpath("//input[@type='file']").clear()
        # time.sleep(3)
        # driver.find_element_by_xpath("//input[@type='file']").send_keys("")
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='cdk-overlay-4']/nz-modal/div/div[2]/div/div/div[2]/app-form/div[3]/button[3]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div/button").click()
        time.sleep(5)
        driver.find_element_by_link_text(u"开始结算").click()

        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='cdk-overlay-5']/nz-modal/div/div[2]/div/div/div/app-pay/app-confirmation/div/form/nz-form-item/nz-form-control/div/span/nz-select/div/div/div").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='cdk-overlay-6']/div/div/ul/li").click()
        time.sleep(5)
        driver.find_element_by_xpath(
            "//div[@id='cdk-overlay-5']/nz-modal/div/div[2]/div/div/div/app-pay/app-confirmation/div/form/nz-form-item[3]/nz-form-control/div/span/nz-select/div/div/div").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='cdk-overlay-7']/div/div/ul/li").click()
        driver.find_element_by_id("code").click()
        driver.find_element_by_id("code").clear()
        driver.find_element_by_id("code").send_keys("123456")
        time.sleep(5)
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        time.sleep(5)
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()

        # 调用同目录下的py文件验证码(最初想法的调用)
        # MSGcode = PYmysql.first
        # driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys()
        # time.sleep(5)
        # 先执行获取最新校验码的py
        #os.system('PYmysql.py') 效果同import PYmysql  如果两个都取消注释后，相当于执行了两次获取验证码操作
        time.sleep(10)
        # os.system('PYmysql.py')
        # driver.find_element_by_xpath("(//input[@type='text'])[2]").click()

        #调用获取验证码的py文件
        import PYmysql
        # os.system('PYmysql.py')
        time.sleep(3)
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(PYmysql.first)
        # driver.execute(self.vertify_code())
        time.sleep(5)

        driver.find_element_by_xpath("//div[@id='cdk-overlay-5']/nz-modal/div/div[2]/div/div/div/app-pay/app-captcha-input/div/div/div[3]/button").click()
        time.sleep(3)

        driver.find_element_by_xpath("//div[@id='cdk-overlay-5']/nz-modal/div/div[2]/div/div/div/app-pay/div/div/button").click()
        time.sleep(3)
        # 多次Fresh
        driver.find_element_by_xpath("//div/button").click()
        time.sleep(20)
        driver.find_element_by_xpath("//div/button").click()
        time.sleep(20)
        driver.find_element_by_xpath("//div/button").click()
        time.sleep(10)
        # driver.find_element_by_link_text(u"查看结算单明细").click()
        time.sleep(10)

        # 支付宝上传结算单并发放
        driver.find_element_by_link_text(u"提交结算单").click()
        time.sleep(10)

        driver.find_element_by_xpath("//div[3]/div/div").click()
        driver.find_element_by_xpath("//div[@id='cdk-overlay-6']/nz-modal/div/div[2]/div/div/div[2]/app-form/nz-form-item/nz-form-control/div/span/nz-upload/div/div").click()
        time.sleep(10)
        os.system(r"E:\Auto\UploadFilezfb.exe")
        # driver.find_element_by_xpath("//input[@type='file']").clear()
        # driver.find_element_by_xpath("//input[@type='file']").send_keys("")
        driver.find_element_by_xpath("//div[@id='cdk-overlay-4']/nz-modal/div/div[2]/div/div/div[2]/app-form/div[3]/button[3]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div/button").click()
        time.sleep(5)
        driver.find_element_by_link_text(u"开始结算").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='cdk-overlay-5']/nz-modal/div/div[2]/div/div/div/app-pay/app-confirmation/div/form/nz-form-item/nz-form-control/div/span/nz-select/div/div/div").click()
        driver.find_element_by_xpath("//div[@id='cdk-overlay-6']/div/div/ul/li").click()
        driver.find_element_by_xpath("//div[@id='cdk-overlay-5']/nz-modal/div/div[2]/div/div/div/app-pay/app-confirmation/div/form/nz-form-item[3]/nz-form-control/div/span/nz-select/div/div/div").\
            click()
        driver.find_element_by_xpath("//div[@id='cdk-overlay-7']/div/div/ul/li").click()
        driver.find_element_by_id("code").click()
        driver.find_element_by_id("code").clear()
        time.sleep(10)
        driver.find_element_by_id("code").send_keys("123456")
        time.sleep(10)
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        import PYmysql
        # os.system('PYmysql.py')
        time.sleep(5)
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(PYmysql.first)
        # driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("0978")
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='cdk-overlay-5']/nz-modal/div/div[2]/div/div/div/app-pay/app-captcha-input/div/div/div[3]/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='cdk-overlay-5']/nz-modal/div/div[2]/div/div/div/app-pay/div/div/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div/button").click()
        time.sleep(20)
        driver.find_element_by_xpath("//div/button").click()
        time.sleep(20)
        driver.find_element_by_xpath("//div/button").click()
        time.sleep(15)
        # driver.find_element_by_link_text(u"查看结算单明细").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    # noinspection PyMethodParameters,SpellCheckingInspection

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
