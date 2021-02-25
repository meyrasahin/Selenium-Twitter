from githubUserInfo import username, password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Twitter:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)

    def signIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(4)

    def search(self, hashtag):
        searchInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
        searchInput.send_keys(hashtag)
        time.sleep(1)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(1)

        results = []

        list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")
        time.sleep(2)
        print("count: " + str(len(list)))

        for i in list:
            results.append(i.text)

        loopCounter = 0

        lastHeight = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 5:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)

            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if lastHeight == new_height:
                break
            lastHeight = new_height
            loopCounter += 1

            list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")
            time.sleep(2)
            print("count: " + str(len(list)))

            for i in list:
                results.append(i.text)

        count = 1
        with open("tweets.txt", "w", encoding="UTF-8") as file:
            for item in results:
                file.write(f"{count}-{item}'\n'")
                file.write(" "+"\n")
                count += 1

    def tweet(self, message):
        self.browser.get("https://twitter.com/home")
        time.sleep(2)

        button = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div")
        button.click()
        time.sleep(1)

        button.send_keys(message)

        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]').click()

    '''
    open to developing
    
    def likeTweet(self):
        self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[5]').click()
        submit_button = self.browser.find_element_by_xpath('/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[6]/a[1]')
        submit_button.click()
        time.sleep(5)
    '''


tw = Twitter(username, password)
tw.signIn()
#tw.search("python")
#tw.tweet("Hello World. This tweet is written by Selenium Twitter Bot.")
#tw.likeTweet()


'''


internetten veya hocadan bulduğum
from githubUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(4)

    def search(self, hashtag):
        searchInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        searchInput.send_keys(hashtag)
        time.sleep(3)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(3)

        results = []

        self.browser.implicitly_wait(5)

        for i in self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]"):
            results.append(i.text)
            print(i.text)
            #self.like(i)

        time.sleep(3)

        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 5:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(3)

            for i in self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]"):
                results.append(i.text)
                self.like(i)

            self.browser.implicitly_wait(5)

            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter += 1

        count = 1
        with open("tweets.txt", "w", encoding="UTF-8") as file:
            for item in results:
                file.write(f"{count}-{item}\n")
                count += 1

    def like(self, item):
        time.sleep(2)
        try:
            item.find_element_by_xpath("//div[@data-testid='like']").click()
            print("clicked")
        except:
            print("sorun")


twitter = Twitter(username, password)
# login
twitter.signIn()
twitter.search("reactjs")

'''


