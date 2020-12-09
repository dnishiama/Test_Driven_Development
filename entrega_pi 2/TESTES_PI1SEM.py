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
  if elem2.is_displayed():
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[1]")
    not_found = False
  else:
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
  if elem2.is_displayed():
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[1]")
    not_found = False
  else:
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
  if elem2.is_displayed():
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[1]")
    not_found = False
  else:
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
  if elem2.is_displayed():
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[1]")
    not_found = False
  else:
    not_found = True

  assert not_found  
  driver.close_app()

  #####Teste de aceite de passageiro
def teste_aceite_de_passageiro():
  usuario = 'admin'
  senha = 'admin'
  driver = webdriver.Remote('http://localhost:4723/wd/hub', capability)

  #print('Preenchimento USUARIO')
  usuarioField = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[1]")
  usuarioField.send_keys(usuario)
  time.sleep(1)

  #print('Preenchimento SENHA')
  senhaField = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[2]")
  senhaField.send_keys(senha)
  time.sleep(1)

  #print('Tap em ENTRAR')
  elem= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button")
  action = TouchAction(driver)
  action.tap(elem).perform()
  time.sleep(1)

  #print('Tap em ACEITAR PASSAGEIRO')
  elem2= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[1]")
  action.tap(elem2).perform()
  time.sleep(1)

  #print('Aceite do 1º passageiro')
  elem3= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.TableLayout/android.widget.TableRow/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Switch")
  action.tap(elem3).perform()
  check1tela1 = elem3.get_attribute('checked')
  time.sleep(1)

  #print('Aceite do 2º passageiro')
  elem4= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.TableLayout/android.widget.TableRow/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Switch")
  action.tap(elem4).perform()
  check2tela1 = elem4.get_attribute('checked')
  time.sleep(1)

  print("Check 1 :", check1tela1)
  print("Check 2 :", check2tela1)

  #print('Tap em VOLTAR')
  elem5= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button")
  action.tap(elem5).perform()
  time.sleep(1)

  #print('Tap em ACEITAR PASSAGEIRO 2')
  elem2= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[1]")
  action.tap(elem2).perform()
  time.sleep(1)

  elem3= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[1]/android.widget.TableLayout/android.widget.TableRow/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Switch")
  check1tela2 = elem3.get_attribute('checked')
  time.sleep(1)

  elem4= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TableLayout/android.widget.TableRow[2]/android.widget.TableLayout/android.widget.TableRow/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Switch")
  check2tela2 = elem4.get_attribute('checked')
  time.sleep(1)

  print("Check 1 :", check1tela2)
  print("Check 2 :", check2tela2)

  if check1tela1 == check1tela2 and check2tela1 == check2tela2:
    teste = True
  else:
    teste = False
  
  assert teste
  print('Encerrado a aplicação')
  driver.close_app()
