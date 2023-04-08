from faker.providers import DynamicProvider


brands_provider = DynamicProvider(
    provider_name="car_brands",
    elements=['Toyota', 'Mercedes-Benz', 'BMW', 'Honda', 'Volkswagen', 'Ford', 'Hyundai', 'Audi', 'Porsche', 'Nissan']
)


price_provider = DynamicProvider(
    provider_name="price",
    elements=['1000.00', '1100.00', '1200.00', '1250.00', '1300.00', '1400.00', '1500.00', '2000.00', '2100.00', '2500.00']
)