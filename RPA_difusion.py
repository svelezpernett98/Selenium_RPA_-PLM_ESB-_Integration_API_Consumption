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


class Master_diffusion(object):
    def __init__(self):
        pass
    @staticmethod
    def process_diffusion():

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
        difusion_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[12]/div[2]/ul/li[9]/a'))).click()
        
        init.switch_to.frame("formulario")
        add_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/table/thead/tr/td[1]/span[1]/a'))).click()
        
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
                    list_object = message_object.get("composicion")
                              
                    for l in list_object: 
                        print(l)
                        print(l["codigo_alterno"])
                        print(l["difucion"])
                        if(Θ == 1 or  Θ == 2):
                            codigo_alterno_value = l["codigo_alterno"]
                            codigo_alterno_input = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.ID, 'codigoAlternoDifusion')))
                            codigo_alterno_input.send_keys(str(codigo_alterno_value))
                            
                            click_validacion = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[2]/table/tbody/tr[5]/td[2]/span/input'))).click()
                            
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
                                    difucion_value = l["difucion"]
                                    difucion_input = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.ID, 'nombreDifusion')))
                                    difucion_input.send_keys(str(difucion_value))
                                    
                                    click_validacion = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body'))).click()
                                    time.sleep(0.5)
                                    
                                    try:
                                        WebDriverWait(init, 2.5).until(EC.alert_is_present(),
                                                        'Timed out waiting for PA creation ' +
                                                        'confirmation popup to appear.')
                                        alert = init.switch_to.alert
                                        alert.accept()
                                        codigo_alterno_input.clear()
                                    except:
                                        terceros_input = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[2]/table/tbody/tr[3]/td[2]/input')))
                                        terceros_input.send_keys(str("%" + "ART MODE S.A.S. BIC"))
                                        
                                        click_validacion = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[2]/table/tbody/tr[5]/td[2]/span/input'))).click()
                                        time.sleep(2.5)
                                        
                                        dd_list = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[2]/div/div/li[2]'))).text
                                        print(dd_list + "value list")
                                        if "ART MODE S.A.S. BIC" in str(dd_list):
                                            dd_list = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[2]/div/div/li[2]'))).click()
                                            time.sleep(4.5)
                                        
                                        else:
                                            terceros_input.clear()
                                            terceros_input.send_keys("ART MODE S.A.S. BIC")
                                            time.sleep(2.5)

                                        #BOTON PARA AGREGAR MAESTRO UNA VEZ LOS DATOS ESTEN CARGADOS (REVISAR RUTA HTML)
                                        #agregar_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[4]/table[2]/tbody/tr[2]/td/div[1]/span/input'))).click()
                                        
                                        #BOTON (+) PARA ABRIR EL MODAL O VENTANA EMERGENTE QUE PERMITE AGREGAR MAESTRO
                                        #add_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/table/thead/tr/td[1]/span[1]/a'))).click()
                                        print("Maestro difusion añadido")
                            time.sleep(1)
                            
                    print("Total de datos cargados exitosamente")        
                    
        time.sleep(2)          

def main():
        Master_diffusion.process_diffusion()

if __name__ == "__main__":
    main()