from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, base64, requests, json, os, string, random
from datetime import datetime, date, timedelta 


class Master_category(object):
    def __init__(self):
        pass
    @staticmethod
    def process_category():
        numero_aleatorio = ""
        codigo_letras = ""
        
        #Ruta de chromedricer.exe
        dir = os.getcwd()
        PATH = str(dir)+"/chromedriver.exe"

        #declaramos variable de webdriver
        init = webdriver.Chrome(PATH)

        #voy a saya
        init.get("SITE_URL")

        #declaro variables de login input, password input, insertamos credenciales y click en ingresar
        login_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.ID, 'uname')))
        login_button.send_keys("USER")
        password_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.ID, 'pwd'))) 
        password_button.send_keys("PASS")
        enter_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div[1]/div/div/table/tbody/tr[5]/td[2]/input'))).click()

        general_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[12]/ul/li[2]'))).click()
        archivos_p_y_s_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[12]/div[1]/ul/li[11]'))).click()
        categoria_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[12]/div[2]/ul/li[3]/a'))).click()
        
        init.switch_to.frame("inferior")
        
        add_categoria_btn = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/table/tbody/tr[1]/td[1]/a[1]'))).click()
        
        url = "API_URL"

        myobj = {'access_token': 'TOKEN'}

        x = requests.post(url, myobj)

        response = json.dumps(x.json())

        object_response = json.loads(response)
        Θ = 1
        make = False
        for z in object_response.keys():
            message_object = object_response.get("message")
            
            for y in message_object:
                    list_object = message_object.get("categoria")
                              
                    for l in list_object: 
                        nombre_categoria = l["nombre"]

                        nombre_input = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/form/table/tbody/tr[2]/td[2]/input')))
                        nombre_input.send_keys(nombre_categoria)
                        
                        control_codigo_inpiracion = True
                        while control_codigo_inpiracion == True:
                            for i in range(0, 7):
                                # rand = random.choice(string.ascii_letters)
                                # print(rand)
                                def randletter(x, y):
                                    return chr(random.randint(ord(x), ord(y)))
                                R = randletter('A', 'Z')
                                numero_aleatorio = numero_aleatorio + str(random.randint(0, 9))
                                codigo_letras = codigo_letras + R
                            codigo_alterno_aleatorio_final = codigo_letras + numero_aleatorio
                            
                            codigo_alterno_input = nombre_input = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/form/table/tbody/tr[1]/td[2]/input[9]')))
                            codigo_alterno_input.send_keys(codigo_alterno_aleatorio_final)
                            
                            click_validacion = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body'))).click()
                            
                            try:
                                WebDriverWait(init, 5).until(EC.alert_is_present(),
                                    'Timed out waiting for PA creation ' +
                                    'confirmation popup to appear.')
                                alert = init.switch_to.alert
                                alert.accept()
                                time.sleep(1)
                                numero_aleatorio = ""
                                codigo_letras = ""
                                control_codigo_inpiracion = True

                            except:
                                control_codigo_inpiracion = False
                                numero_aleatorio = ""
                                codigo_letras = ""

                        
                        #BOTON PARA AGREGAR CATEGORIA, DESCOMENTAR EN PRODUCCION
                        #agregar_btn = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/form/div[2]/input'))).click()
                        #add_categoria_btn = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/table/tbody/tr[1]/td[1]/a[1]'))).click()
                        time.sleep(2.5)
                        print("Maestro categoria añadido")
                        
                    time.sleep(1)
                    
                    print("Total de datos cargados exitosamente")
        

def main():
        Master_category.process_category()

if __name__ == "__main__":
    main()