import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = os.environ['OO_USERNAME']
password = os.environ['OO_PASSWORD']


# browser = webdriver.Chrome()
# wait = WebDriverWait(browser, 30)


class Bot:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 30)

    def start(self):
        # Start Login
        self.browser.get('https://optionomega.com/login')

        self.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[1]/input').send_keys(username)
        self.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[2]/input').send_keys(password)
        self.browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[4]/button').click()
        # End Login

        time.sleep(5)

    def run(self, params):
        # Start Backtest
        new_backtest_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/button')))
        new_backtest_button.click()

        #

        new_backtest_form = self.wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'form')))

        ###


        toggles = new_backtest_form.find_elements(By.CLASS_NAME, 'toggle')

        # Round Strikes to Nearest

        #

        # Prune Oldest Trades

        #

        # Ignore Margin Requirements

        #

        # Use Floating Entry Time

        #

        # Use VIX

        #

        # Use Technical Indicators

        #

        # Use Gaps

        #

        # Use Intraday Movement

        #

        # Use SqueezeMetrics™ (Gamma / Dark Pool) Indicators

        #

        # Use Opening Range Breakout

        #

        # Use Profit Actions

        #

        # Use Early Exit

        #

        # Use VIX

        #

        # Use Technical Indicators

        #

        # Use Underlying Price Movement

        #

        # Use Delta

        #

        # Use Commissions & Fees

        #

        # Use Slippage

        #

        # Ignore Trades with Wide Bid-Ask Spread

        #

        # Close Open Trades on Test Completion

        #

        # Use Min/Max Entry Premium

        #

        # Use Blackout Days

        #

        # Re-Enter Trades After Exit

        #

        inputs = new_backtest_form.find_elements(By.TAG_NAME, 'input')
        for input_ in inputs:
            input_.click()
            time.sleep(5)

        # Start Date

        #

        # End Date

        #

        # Strikes

        #

        # Starting Funds

        #

        # Margin Allocation % Per Trade

        #

        # Max Open Trades

        #

        # Max Contracts Per Trade

        #

        # Max Allocation Amount Per Trade

        #

        # Entry Time

        #

        # Profit Target

        #

        # Stop Loss

        #

        select_inputs = new_backtest_form.find_elements(By.CLASS_NAME, 'selectInput')
        for select_input in select_inputs:
            print(select_input.text)

        # Ticker

        #

        # Strategy

        #

        # Delta

        #

        # Frequency

        #

        # PT

        #

        # SL

        #


        return


        start_date_field = self.browser.find_element(By.XPATH,
                                                     '//*[@id="headlessui-dialog-130"]/div/div[2]/div/form/div['
                                                     '1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/input')
        start_date_field.send_keys(params['start_date'])

        end_date_field = self.browser.find_element(By.XPATH,
                                                   '//*[@id="headlessui-dialog-130"]/div/div[2]/div/form/div[1]/div['
                                                   '2]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/input')

        end_date_field.send_keys(params['end_date'])

        # Ticker

        #

        # Common Strategies
        common_strategies_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="headlessui-listbox-button-13"]'))
        )
        #

        # End Backtest

# Close the WebDriver
# browser.quit()
