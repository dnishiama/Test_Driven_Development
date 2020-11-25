import os
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
import time

capability = {
  'deviceName': '04b060c20405',
  'platformName': 'Android',
  'app': 'C:\\Users\\Douglas\\Desktop\\VAIdeVAN.apk'
}

#####Teste deveria passar, usuario e senha validos
def teste_login_correto():
  usuario = 'admin'
  senha = 'admin'
  driver = webdriver.Remote('http://localhost:4723/wd/hub', capability)

  print('Preenchimento USUARIO')
  usuarioField = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[1]")
  usuarioField.send_keys(usuario)
  time.sleep(1)
  
  print('Preenchimento SENHA')
  senhaField = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[2]")
  senhaField.send_keys(senha)
  time.sleep(1)

  print('Tap do botão')
  elem= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button")
  action = TouchAction(driver)
  action.tap(elem).perform()
  time.sleep(10)

  elem2= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[1]")
  assert elem2.is_displayed()
  
  driver.close_app()
  print('Encerrado a aplicação')

#####Teste deveria falhar, pois o login esta incorreto.
def teste_login_incorreto():
  usuario = 'usuariofalso'
  senha = 'senhafalsa'
  driver = webdriver.Remote('http://localhost:4723/wd/hub', capability)

  usuarioField = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[1]")
  usuarioField.send_keys(usuario)
  time.sleep(1)
  
  senhaField = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[2]")
  senhaField.send_keys(senha)
  time.sleep(1)

  elem= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button")
  action = TouchAction(driver)
  action.tap(elem).perform()
  time.sleep(10)

  #Variavel que recebe um valor booleano: se o login é efetuado, recebe False.
  try:
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[1]")
    not_found = False
  except:
    not_found = True

  assert not_found  
  driver.close_app()

#####Teste deveria falhar, pois o login é nulo.
def teste_usuario_nulo():
  usuario = ''
  senha = 'admin'
  driver = webdriver.Remote('http://localhost:4723/wd/hub', capability)

  usuarioField = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[1]")
  usuarioField.send_keys(usuario)
  time.sleep(1)
  
  senhaField = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[2]")
  senhaField.send_keys(senha)
  time.sleep(1)

  elem= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button")
  action = TouchAction(driver)
  action.tap(elem).perform()
  time.sleep(10)

  #Variavel que recebe um valor booleano: se o login é efetuado, recebe False.
  try:
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[1]")
    not_found = False
  except:
    not_found = True

  assert not_found
  driver.close_app()

#####Teste deveria falhar, pois a senha é nula.
def teste_senha_nula():
  usuario = 'admin'
  senha = ''
  driver = webdriver.Remote('http://localhost:4723/wd/hub', capability)

  usuarioField = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[1]")
  usuarioField.send_keys(usuario)
  time.sleep(1)
  
  senhaField = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[2]")
  senhaField.send_keys(senha)
  time.sleep(1)

  elem= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button")
  action = TouchAction(driver)
  action.tap(elem).perform()
  time.sleep(10)

  #Variavel que recebe um valor booleano: se o login é efetuado, recebe False.
  try:
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[1]")
    not_found = False
  except:
    not_found = True

  assert not_found
  driver.close_app()

#####Teste deveria falhar, pois o login e a senha são nulos.
def teste_login_e_senha_nulo():
  usuario = ''
  senha = ''
  driver = webdriver.Remote('http://localhost:4723/wd/hub', capability)

  usuarioField = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[1]")
  usuarioField.send_keys(usuario)
  time.sleep(1)
  
  senhaField = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[2]")
  senhaField.send_keys(senha)
  time.sleep(1)

  elem= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button")
  action = TouchAction(driver)
  action.tap(elem).perform()
  time.sleep(10)

  #Variavel que recebe um valor booleano: se o login é efetuado, recebe False.
  try:
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[1]")
    not_found = False
  except:
    not_found = True

  assert not_found
  driver.close_app()

