# from playwright.sync_api import sync_playwright
# # https://playwright.dev/python/docs/api/class-playwright
# def run(playwright):
#     browser = playwright.chromium.launch()
#     page = browser.new_page()
#     page.goto('https://www.cotrisel.com/noticias')
#     # print(page.title())
#     # print(page.content())
    
#     #new__date.p4
#     #img
#     #
    
#     elements = page.query_selector_all('.new__title.p')
#     for element in elements:
#         # Obtém o texto de cada elemento e imprime
#         print(element.text_content())
#     browser.close()

# with sync_playwright() as playwright:
#     run(playwright)
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto('https://www.cotrisel.com/noticias')

    # Seleciona todos os elementos 'a' que contêm a classe 'new'
    
    paginator = page.query_selector_all('.pagination__item')
    print(paginator.text_content())
    news_items = page.query_selector_all('a.new')
    for item in news_items:
        # Para cada item, encontra a imagem e extrai a URL
        img_url = item.query_selector('img').get_attribute('src')
        
        # Encontra a data
        date = item.query_selector('.new__date').text_content()
        
        # Encontra o título
        title = item.query_selector('.new__title').text_content()
        more_info_link = item.get_attribute('href')
        print(f'URL da Imagem: {img_url}, Data: {date}, Título: {title}, Link Saiba Mais: https://www.cotrisel.com{more_info_link}')
    
        # print(f'URL da Imagem: {img_url}, Data: {date}, Título: {title}')
    
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
