import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

DYNAMIC_ID = (By.CSS_SELECTOR, "[class*='btn-primary']")
LINK = "http://uitestingplayground.com/dynamicid"


