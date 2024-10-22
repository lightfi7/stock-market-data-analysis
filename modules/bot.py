import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

username = os.environ['OO_USERNAME']
password = os.environ['OO_PASSWORD']


# browser = webdriver.Chrome()
# wait = WebDriverWait(browser, 30)

class Bot:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 30)
        self.actions = ActionChains(self.browser)

    def start(self):
        # Start Login
        self.browser.get('https://optionomega.com/login')

        time.sleep(2)

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

        time.sleep(5)
        #

        new_backtest_form = self.wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'form')))
        ###

        leg_options = [
            {
                "opt": ["Sell", "Put"],
                "qty": 1,
                "v": 25,
                "dte": 6,
            },
            {
                "opt": ["Buy", "Put"],
                "qty": 1,
                "v": 0,
                "dte": 7,
            },
            {
                "opt": ["Sell", "Call"],
                "qty": 1,
                "v": 25,
                "dte": 6,
            },
            {
                "opt": ["Buy", "Call"],
                "qty": 1,
                "v": 0,
                "dte": 7,
            }
        ]


        toggles = new_backtest_form.find_elements(By.CSS_SELECTOR, 'button.toggle')

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

        # Use CSV Custom Signals File
        time.sleep(2)
        toggles[23].click()
        time.sleep(2)
        new_backtest_form = self.wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'form')))
        toggles = new_backtest_form.find_elements(By.CSS_SELECTOR, 'button.toggle')
        toggles[15].click()


        input_file = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type=file]')))
        input_file.send_keys(params['file'])

        time.sleep(2)

        #

        inputs = new_backtest_form.find_elements(By.TAG_NAME, 'input')
        # for input_ in inputs:
        #     input_.click()
        #     time.sleep(5)

        # Start Date
        inputs[0].send_keys(params['start_date'])
        #

        # End Date
        inputs[1].send_keys(params['end_date'])
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
        inputs[6].send_keys('1')
        toggles[2].click()
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
        # for select_input in select_inputs:
        #     print(select_input.text)

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


        # add_entry_time_button = self.wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[text()=' Add Entry Time ']"))
        # )
        #
        # times = generate_times('9:32', '15:59')
        # default_entry_time_input = self.browser.find_element(By.CSS_SELECTOR, 'input[type=time]')
        # default_entry_time_input.send_keys(times[0])
        #
        # for i in range(1, 19):
        #     add_entry_time_button.click()
        #     entry_time_inputs = self.browser.find_elements(By.CSS_SELECTOR, f'input[type=time]')
        #     entry_time_inputs[i].send_keys(times[i])

        add_leg_button = new_backtest_button.find_element(By.XPATH, "//button[text()='Add Leg']")
        add_leg_button.click()
        add_leg_button.click()

        table = new_backtest_button.find_element(By.XPATH, "//div/table")
        rows = table.find_elements(By.TAG_NAME, "td")
        for row in rows:
            buttons = row.find_elements(By.TAG_NAME, "button")
            buttons[5].click()

        rows = table.find_elements(By.TAG_NAME, "td")
        for i in range(len(rows)):
            row = rows[i]
            for opt in leg_options[i]['opt']:
                button = row.find_element(By.XPATH, f".//button[text()=' {opt} ']")
                button.click()
            inputs = row.find_elements(By.TAG_NAME, "input")
            inputs[0].send_keys(Keys.CONTROL + 'A')
            inputs[0].send_keys(leg_options[i]['qty'])
            inputs[1].send_keys(Keys.CONTROL + 'A')
            inputs[1].send_keys(leg_options[i]['v'])
            inputs[2].send_keys(Keys.CONTROL + 'A')
            inputs[2].send_keys(leg_options[i]['dte'])

        time.sleep(60*2)

        submit_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type=submit]')))
        submit_button.click()

        time.sleep(60*2) # Waiting 5 mins to get data

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Get result
        labels = self.browser.find_elements(By.CSS_SELECTOR, 'dl > div > dt')
        values = self.browser.find_elements(By.CSS_SELECTOR, 'dl > div > dd')

        for label, value in zip(labels, values):
            print(label.text, value.text)
        #

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Download
        trade_log_button = self.browser.execute_script(
            "return [...document.querySelectorAll('span')].find(e => e.textContent.includes('Trade Log'));"
        )
        print(trade_log_button.text)
        trade_log_button.click()

        download_button = self.browser.execute_script(
            "return [...document.querySelectorAll('.has-tooltip')].find(e => e.textContent.includes('Export to CSV'));"
        )
        print(download_button.text)
        download_button.click()

        #

        time.sleep(5)
        # End Backtest

# Close the WebDriver
# browser.quit()
