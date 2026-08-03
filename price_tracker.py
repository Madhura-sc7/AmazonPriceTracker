import requests
from bs4 import BeautifulSoup
65674547574545475745


products_to_track = [
    {
        "product_url": "https://www.amazon.in/Redmi-11-SE-Cosmic-White/dp/B0BHZN4NQ4/ref=sr_1_1?crid=8QSEZM5SM26X&dib=eyJ2IjoiMSJ9.WaEzFhnx6S6Cs2FOmhADP-yp102o28O5_HbeJcGm8dSM_jO4bbuR6dW4YjCsPuwANNtyDyB-OfJaaW_dMwVw8qghKcnQNOTW5zGqWZw9N26gideNHbQ50WmFB8dseFygelb3kEhV9kXojqvj70ziKWJsLNlwhePPAb76uziB0_RLEF9Crhq_3VFj9P0h40T72s3mF7uLAJwpPYg8A2dK37hlR5o7mSSamO70fJ5ISFk.h3U2hj3imbnt7CdrtWA4pROq1FnuTL6sYZrD6FZVbFY&dib_tag=se&keywords=redmi+11+to+20+k&qid=1746952515&sprefix=redmi+11+to+20+k+%2Caps%2C236&sr=8-1",
        "name": "REDMI Note 11 SE (Cosmic White, 64 GB) (6 GB RAM)",
        "target_price":9500
    },

    {

        "product_url":"https://www.amazon.in/Redmi-11-SE-Space-Black/dp/B0BHZLZ1NZ/ref=sr_1_4?crid=1PYCMJMKHP8UQ&dib=eyJ2IjoiMSJ9.WaEzFhnx6S6Cs2FOmhADP-yp102o28O5_HbeJcGm8dSM_jO4bbuR6dW4YjCsPuwANNtyDyB-OfJaaW_dMwVw8qghKcnQNOTW5zGqWZw9N26gideNHbQ50WmFB8dseFygelb3kEhV9kXojqvj70ziKWJsLNlwhePPAb76uziB0_RLEF9Crhq_3VFj9P0h40T72s3mF7uLAJwpPYg8A2dK37hlR5o7mSSamO70fJ5ISFk.h3U2hj3imbnt7CdrtWA4pROq1FnuTL6sYZrD6FZVbFY&dib_tag=se&keywords=redmi+11+to+20+k&qid=1746952543&sprefix=redmi+11+to+20+k%2Caps%2C206&sr=8-4",
        "name":"REDMI Note 11 SE (Space Black, 64 GB) (6 GB RAM)",
        "target_price":9000
    },

    {
       "product_url":"https://www.amazon.in/Redmi-Purple-Design-Performance-Triple/dp/B0BBH4C5KT/ref=sr_1_3?crid=1PYCMJMKHP8UQ&dib=eyJ2IjoiMSJ9.WaEzFhnx6S6Cs2FOmhADP-yp102o28O5_HbeJcGm8dSM_jO4bbuR6dW4YjCsPuwANNtyDyB-OfJaaW_dMwVw8qghKcnQNOTW5zGqWZw9N26gideNHbQ50WmFB8dseFygelb3kEhV9kXojqvj70ziKWJsLNlwhePPAb76uziB0_RLEF9Crhq_3VFj9P0h40T72s3mF7uLAJwpPYg8A2dK37hlR5o7mSSamO70fJ5ISFk.h3U2hj3imbnt7CdrtWA4pROq1FnuTL6sYZrD6FZVbFY&dib_tag=se&keywords=redmi%2B11%2Bto%2B20%2Bk&qid=1746952543&sprefix=redmi%2B11%2Bto%2B20%2Bk%2Caps%2C206&sr=8-3&th=1",
        "name":"Redmi 11 Prime",
        "target_price":8999
    },

    {

         "product_url":"https://www.amazon.in/Redmi-Orchid-128GB-Without-Offer/dp/B0F2MLLPQB/ref=sr_1_4?dib=eyJ2IjoiMSJ9.ag6AqJ5xYs5Cm5qRJdE1g6_wni8UCT7nZHaA_dfk_oHuZnPnvf6PyBGY1xoSLaZHX3bMMWSJZohT88lZViPy94UKo9OjyqKosmzsxz239oLjJXUT_p9tH7xC-RbHPJciuSlfnxcDR-vvDdBfXm1xzWj3_MNsd2AzvggQ0mUdxbU9jCIAKqHx8v0jMq52K8K1n03VO4B0BCEKYhxY7Dmf1tND5VeYwt5-36aoZOYhW2-Ho-dFancKZyO57D86etgkNiBhRHcsz3xm8VZWSRaxeDgKFxEaxxSEXpgxGl57q_I.4mf5S0YsUeK3byXweeYKv2LB8b4BM4L_O3sPs9TZj_4&dib_tag=se&keywords=redmi&qid=1747320658&s=electronics&sr=1-4&th=1",
         "name": "Redmi 13 5G  Orchid Pink",
         "target_price": 12400

    },

    {

         "product_url": "https://www.amazon.in/Redmi-Hawaiian-Largest-Display-Segment/dp/B0D78X544X/ref=sr_1_9?dib=eyJ2IjoiMSJ9.ag6AqJ5xYs5Cm5qRJdE1g6_wni8UCT7nZHaA_dfk_oHuZnPnvf6PyBGY1xoSLaZHX3bMMWSJZohT88lZViPy94UKo9OjyqKosmzsxz239oLjJXUT_p9tH7xC-RbHPJciuSlfnxcDR-vvDdBfXm1xzWj3_MNsd2AzvggQ0mUdxbU9jCIAKqHx8v0jMq52K8K1n03VO4B0BCEKYhxY7Dmf1tND5VeYwt5-36aoZOYhW2-Ho-dFancKZyO57D86etgkNiBhRHcsz3xm8VZWSRaxeDgKFxEaxxSEXpgxGl57q_I.4mf5S0YsUeK3byXweeYKv2LB8b4BM4L_O3sPs9TZj_4&dib_tag=se&keywords=redmi&qid=1747320658&s=electronics&sr=1-9&th=1",
         "name": "Redmi 13 5G Hawaiian Blue",
         "target_price": 13500

    }
]

def give_product_price(URL):
    headers = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find("span", class_="a-price-whole")

    return product_price.get_text()


result_file = open('my_result_file.text','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)

        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                "name") + '-\t' +' Available at target price ' + ' current price - ' + str(my_product_price) + '\n')
        else:   
            print("still at current price")

finally:
    result_file.close()

