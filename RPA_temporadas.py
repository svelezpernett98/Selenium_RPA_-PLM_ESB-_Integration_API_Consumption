from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, base64, requests, json, os, random
from datetime import datetime, date, timedelta


class Master_temporadas(object):
    def __init__(self):
        pass
    @staticmethod
    def process_temporadas():
        numero_aleatorio = ""
    
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
        temporadas_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[12]/div[2]/ul/li[23]/a'))).click()
        
        init.switch_to.frame("formulario")
        
        add_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/table/thead/tr/td[1]/span[1]/a'))).click()
        
        url = "API_URL"

        myobj = {'access_token': 'TOKEN'}

        x = requests.post(url, myobj)

        response = json.dumps(x.json())

        object_response = json.loads(response)
        Θ = 1
        
        for z in object_response.keys():
            message_object = object_response.get("message")
            
            for y in message_object:
                    list_object = message_object.get("temporada")
                              
                    for l in list_object: 
                        
                        if(Θ == 1 or  Θ == 2):
                            codigo_alterno_value = l["codigo_alterno"]
                            codigo_alterno_input = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.ID, 'codigoAlternoTemporada')))
                            codigo_alterno_input.send_keys(str(codigo_alterno_value))
                            
                            click_validacion = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[2]/table/tbody/tr[4]/td[2]/spam/input'))).click()
                            print("valido codigo alterno P")
                            try:
                                WebDriverWait(init, 5).until(EC.alert_is_present(),
                                                'Timed out waiting for PA creation ' +
                                                'confirmation popup to appear.')
                                alert = init.switch_to.alert
                                alert.accept()
                                print("codigo alterno P repetido")
                                
                            except:
                                campana_value = l["campana"]
                                campana_input = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.ID, 'nombreTemporada')))
                                campana_input.send_keys(str(campana_value))
                                
                                try:
                                    inspiracion_value = l["inspiracion"]

                                    agregar_inspiracion_btn = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[2]/table/tbody/tr[7]/td/div/div/div/div[1]/div[3]/a'))).click()
                                    
                                    descripcion_inspiracion_input = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[2]/table/tbody/tr[7]/td/div/div/div/div[2]/div[2]/input[3]')))
                                    descripcion_inspiracion_input.send_keys(inspiracion_value)
                                    
                                    click_validacion = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[2]/table/tbody'))).click()
                                    print("valido NOMBRE INSPIRACION")
                                    
                                    try:
                                        WebDriverWait(init, 5).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')
                                        alert = init.switch_to.alert
                                        alert.accept()
                                        print("nombre de inspiracion repetido")
                                        time.sleep(1)
                                        # codigo_alterno_input.clear()
                                        # campana_input.clear()
                                        
                                        eliminar_inpiracion = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[2]/table/tbody/tr[7]/td/div/div/div/div[2]/div[2]/a'))).click()
                                        
                                        #BOTON PARA AGREGAR MAESTRO UNA VEZ LOS DATOS ESTEN CARGADOS (REVISAR RUTA HTML)
                                        #agregar_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[4]/table[2]/tbody/tr[2]/td/div[1]/span/input'))).click()
                                        
                                        #BOTON (+) PARA ABRIR EL MODAL O VENTANA EMERGENTE QUE PERMITE AGREGAR MAESTRO
                                        #add_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/table/thead/tr/td[1]/span[1]/a'))).click()
                                        print("cleared")
                                        
                                    except:
                                        print("siguio except")
                                        control_codigo_inpiracion = True
                                        while control_codigo_inpiracion == True:
                                            for i in range(0, 4):
                                                numero_aleatorio = numero_aleatorio + str(random.randint(0, 9))
                                            codigo_alterno_inspiracion = "CNI_" + numero_aleatorio
                                            
                                            codigo_inspiracion_input = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[2]/table/tbody/tr[7]/td/div/div/div/div[2]/div[2]/input[2]')))
                                            codigo_inspiracion_input.send_keys(codigo_alterno_inspiracion)
                                            
                                            click_validacion = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[2]/table/tbody'))).click()
                                            
                                            try:
                                                WebDriverWait(init, 5).until(EC.alert_is_present(),
                                                    'Timed out waiting for PA creation ' +
                                                    'confirmation popup to appear.')
                                                alert = init.switch_to.alert
                                                alert.accept()
                                                time.sleep(1)
                                                codigo_inspiracion_input.clear()
                                                numero_aleatorio = ""
                                                control_codigo_inpiracion = True

                                            except:
                                                control_codigo_inpiracion = False
                                                numero_aleatorio = ""

                                        #BOTON PARA AGREGAR MAESTRO UNA VEZ LOS DATOS ESTEN CARGADOS (REVISAR RUTA HTML)
                                        #agregar_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[4]/table[2]/tbody/tr[2]/td/div[1]/span/input'))).click()
                                        
                                        #BOTON (+) PARA ABRIR EL MODAL O VENTANA EMERGENTE QUE PERMITE AGREGAR MAESTRO
                                        #add_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/table/thead/tr/td[1]/span[1]/a'))).click()
                                        print("Maestro temporada añadido")
                                        
                                except:
                                    #BOTON PARA AGREGAR MAESTRO UNA VEZ LOS DATOS ESTEN CARGADOS (REVISAR RUTA HTML)
                                    #agregar_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[4]/table[2]/tbody/tr[2]/td/div[1]/span/input'))).click()
                                    
                                    #BOTON (+) PARA ABRIR EL MODAL O VENTANA EMERGENTE QUE PERMITE AGREGAR MAESTRO
                                    #add_button = WebDriverWait(init, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/table/thead/tr/td[1]/span[1]/a'))).click()
                                    print("Maestro temporada añadido")
                                        
                            time.sleep(1)
                            
                    print("Total de datos cargados exitosamente") 
                           
        time.sleep(2)      

def main():
        Master_temporadas.process_temporadas()

if __name__ == "__main__":
    main()