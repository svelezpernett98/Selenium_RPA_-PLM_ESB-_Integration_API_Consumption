from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, base64, requests, json, os
from datetime import datetime, date, timedelta
 

class Master_composition(object):
    def __init__(self):
        pass
    @staticmethod
    def process_composition():

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
        composicion_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[12]/div[2]/ul/li[8]/a'))).click()
        
        init.switch_to.frame("formulario")
        add_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/table/thead/tr/td[1]/span[1]/a'))).click()
        
        #URI ngrok + endpoint
        url = "API_URL"

        #parametros de envio (POST) porque es una peticion post
        myobj = {'access_token': 'TOKEN'}

        #peticion:
        x = requests.post(url, myobj)

        #respuesta en json
        response = json.dumps(x.json())

        #convierto respuesta a diccionario python
        object_response = json.loads(response)
        Θ = 1
        
        #por cada llave detnro de la respuesta
        for z in object_response.keys():
            message_object = object_response.get("message")
            
            for y in message_object:
                    list_object = message_object.get("composicion")
                              
                    for l in list_object: 
                        print(l)
                        print(l["codigo_alterno"])
                        print(l["descripcion"])
                        
                        # if(Θ == 1 or  Θ == 2):
                        codigo_alterno_value = l["codigo_alterno"]
                        codigo_alterno_input = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.ID, 'codigoAlternoComposicion')))
                        codigo_alterno_input.send_keys(str(codigo_alterno_value))
                        
                        #validar que no este repetido el codigo alterno
                        click_validacion = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[4]/table[1]/tbody/tr[3]/td[2]/span/input'))).click()
                        
                        try:
                            WebDriverWait(init, 5).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')
                            alert = init.switch_to.alert
                            alert.accept()
                            made = True
                        except:
                            made = False
                            
                            if made == False:
                                descripcion_value = l["descripcion"]
                                descripcion_input = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.ID, 'nombreComposicion')))
                                descripcion_input.send_keys(str(descripcion_value))

                                #BOTON PARA AGREGAR MAESTRO UNA VEZ LOS DATOS ESTEN CARGADOS (REVISAR RUTA HTML)
                                #agregar_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[4]/table[2]/tbody/tr[2]/td/div[1]/span/input'))).click()
                                
                                #BOTON (+) PARA ABRIR EL MODAL O VENTANA EMERGENTE QUE PERMITE AGREGAR MAESTRO
                                #add_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/table/thead/tr/td[1]/span[1]/a'))).click()
                                print("Maestro composicion añadido")
                        time.sleep(1)
                            
                    print("Total de datos cargados exitosamente")   
                             
        time.sleep(2)      

def main():
        Master_composition.process_composition()

if __name__ == "__main__":
    main()