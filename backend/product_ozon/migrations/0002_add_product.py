from django.db import migrations
import json
from product_ozon.models import Product

def load_products_from_json(apps, schema_editor):
    Product = apps.get_model('product_ozon', 'Product')  # Укажите имя вашего приложения

    json_file_path = "product_ozon/migrations/json_items/all_products.json" 

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    products = data.get('product', [])

    for product_data in products:
        print(product_data)
        print(product_data["code_product"])
        Product.objects.create(
            name=product_data["name"],
            price=product_data['price'],
            discount=product_data['discount'],
            image_url=product_data['image_url'],
            code_product=int(product_data['code_product'])
        )

class Migration(migrations.Migration):

    dependencies = [
        ('product_ozon', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_products_from_json),
    ]
