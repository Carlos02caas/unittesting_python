def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total

def test_calculate_total_with_empty_list():
    print("Prueba")
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebook","price": 5
        }
    ]
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "book","price": 10
        },
        {
            "name": "pen","price": 2
        },
        {
            "name": "scisor","price": 20
        }
    ]
    assert calculate_total(products) == 32

if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()