from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re

def search(query):
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--blink-settings=imagesEnabled=false'")  # Disable image loading
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    inputElems = driver.find_elements(By.XPATH, "//input[@type='search']")
    elem = inputElems[0]
    elem.send_keys(f"{query}")
    elem.send_keys(Keys.ENTER)
    validOptions = []
    page_source =driver.page_source
    beautifulSoup_source = BeautifulSoup(page_source, "html.parser")
    main_finder = beautifulSoup_source.find_all('span', class_='mw-headline')
    invalidSearchFinder = beautifulSoup_source.find('div', class_='mw-search-result-heading')

    paras = driver.find_elements(By.XPATH, "//p")
    for paragraph in paras:
        answer = paragraph.get_attribute("innerText")
        if answer.strip() != "":
            if "There were no results matching the query." == answer or "You can create a draft and submit it for review, but consider checking the search results below to see whether the topic is already covered." in answer:
                try:
                    suggested_result = invalidSearchFinder.find_next("a")
                except:
                    suggested_result = None
                if suggested_result:
                    answer_suggested = f"Showing results of {suggested_result.text} instead: \n"
                    suggested_link = "https://en.wikipedia.org"
                    suggested_link += suggested_result["href"]
                    driver.get(suggested_link)
                    paras_new = driver.find_elements(By.XPATH, "//p")
                    for paragraph in paras_new:
                        answer_new = paragraph.get_attribute("innerText")
                        if answer_new.strip() != "":
                            answer_suggested += answer_new
                            answer_suggested = re.sub(r'\[.*?\]', '', answer_suggested)
                            driver.quit()
                            return answer_suggested
                else:
                    driver.quit()
                    return f"Unable to find information on '{query}'. Recheck spellings"
            else:
                if "may refer to:" in answer or "can refer to:" in answer:
                    if not main_finder:
                        main_finder = beautifulSoup_source.find_all("div", class_='mw-parser-output')
                    for span in main_finder:
                        ul = span.find_next('ul')  # Find the nearest ul after the span
                        if ul:
                            li_items = ul.find_all('li')  # Find all li elements inside the ul
                            for li in li_items:
                                liText = li.text
                                liTextCleaned = re.sub(r',.*', '', liText)
                                if len(validOptions) <= 20:
                                    validOptions.append(liTextCleaned)
                                answer = validOptions
                try:
                    answer = re.sub(r'\[.*?\]', '', answer)
                except:
                    v1 = "W rizz"
                driver.quit()
                return answer
        else:
            continue


print(search("drugs"))
