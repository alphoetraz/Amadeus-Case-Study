import subprocess

# Playwright'ı yükle
subprocess.run(["pip", "install", "playwright"])

# Tarayıcıları indir ve ayarla
subprocess.run(["playwright", "install"])

from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        try:
            # Uygulama sayfasına gidilir
            page.goto('https://flights-app.pages.dev/')

            # "From" ve "To" input alanlarına aynı değer girildiğinde hata kontrolü
            page.fill('#from', 'Istanbul')
            page.fill('#to', 'Istanbul')
            page.click('text="Search"')
            page.wait_for_selector('text=Please select different cities.')

            # Uçuş listeleme testi
            page.fill('#from', 'Istanbul')
            page.fill('#to', 'Los Angeles')
            page.click('text="Search"')

            # "Found X items" yazısındaki X sayısı ile listelenen uçuş sayısının eşleşip eşleşmediğini kontrol etme
            found_items_text = page.inner_text('.results-summary')
            found_items = int(found_items_text.split()[1])
            flight_list_length = len(page.query_selector_all('.flight'))
            if found_items == flight_list_length:
                print("Listed flight count matches found items count.")
            else:
                print("Listed flight count does not match found items count.")
        except Exception as e:
            print("An error occurred:", e)
        finally:
            browser.close()

if __name__ == "__main__":
    main()
