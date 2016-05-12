# coding=utf-8
from selenium.webdriver.common.by import By

__author__ = 'Max'

from unittest import TestCase
from selenium import webdriver


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_loginProveedor(self):
        self.browser.get('http://localhost:8000/proveedor')

        usuario = self.browser.find_element_by_id('username')
        usuario.send_keys('productor1')

        clave = self.browser.find_element_by_id('password')
        clave.send_keys('goK-Rn7-83E-N32')

        ingresar = self.browser.find_element_by_id('ingresar')
        ingresar.click()
        self.browser.implicitly_wait(3)

        title = self.browser.find_element(By.CLASS_NAME, 'navbar-brand')
        self.assertIn('Proveedor', title.text)

    def test_proveedorLinkEditar(self):
        self.browser.get('http://localhost:8000/proveedor')

        usuario = self.browser.find_element_by_id('username')
        usuario.send_keys('productor1')

        clave = self.browser.find_element_by_id('password')
        clave.send_keys('goK-Rn7-83E-N32')

        ingresar = self.browser.find_element_by_id('ingresar')
        ingresar.click()
        self.browser.implicitly_wait(3)

        edit_link = self.browser.find_element(By.CLASS_NAME, 'editar_link')
        edit_link.click()
        self.browser.implicitly_wait(3)

        h2=self.browser.find_element(By.XPATH, '//h2[text()="Editar Oferta"]')
        self.assertIn('Editar Oferta', h2.text)

    def test_editarProveedor(self):
        self.browser.get('http://localhost:8000/proveedor')

        usuario = self.browser.find_element_by_id('username')
        usuario.send_keys('productor1')

        clave = self.browser.find_element_by_id('password')
        clave.send_keys('goK-Rn7-83E-N32')

        ingresar = self.browser.find_element_by_id('ingresar')
        ingresar.click()
        self.browser.implicitly_wait(3)

        edit_link = self.browser.find_element(By.CLASS_NAME, 'editar_link')
        edit_link.click()
        self.browser.implicitly_wait(3)

        cantidad = self.browser.find_element_by_id('producto')
        cantidad.get_attribute('Cebolla')

        cantidad = self.browser.find_element_by_id('cantidad')
        cantidad.clear()
        cantidad.send_keys('1')

        precio = self.browser.find_element_by_id('precio')
        precio.clear()
        precio.send_keys('1')

        editar = self.browser.find_element_by_id('editar')
        editar.click()
        self.browser.implicitly_wait(3)

        alert = self.browser.switch_to.alert
        print alert.text
        self.assertIn('Oferta editada exitosamente', alert.text)