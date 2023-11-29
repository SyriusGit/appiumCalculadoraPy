#Esse código deve ser rodado no terminal através de "python testCalculadora.py"
from selenium.webdriver.common.by import By
from AppiumTest import driver

def testando (nTest):
    el1 = driver.find_element(By.ID, "com.android.calculator2:id/digit_6")
    el1.click()
    el2 = driver.find_element(By.ACCESSIBILITY_ID, "plus")
    el2.click()
    el3 = driver.find_element(By.ID, "com.android.calculator2:id/digit_9")
    el3.click()
    el4 = driver.find_element(By.ACCESSIBILITY_ID, "equals")
    el4.click()
    print("Teste nº ", nTest)
#Ao copiar o script de teste em Python do Appium, cuide com as atualizações
#No caso acima, graças à uma nova versão do Selenium, o "find_element_by_ID" mudou e não estava rodando o code

for nTest in range(1, 4):
    testando(nTest)

driver.quit()