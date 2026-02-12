from fastapi import APIRouter, HTTPException
from fastapi import Request
router = APIRouter()

@router.get("/cars")
async def get_all_car(request: Request):
    try:
        cars = [
            {
                "id": 1,
                "brand_id" : 2,
                "name": "Х1",
                "price": 1,
                "image": "https://s.auto.drom.ru/d24313/foreignimport/1341540358/gen580x2_1481020259.jpg"
            },
            {
                "id": 2,
                "name": "Х6",
                "brand_id": 2,
                "price": 89999,
                "image": "https://avatars.mds.yandex.net/get-autoru-vos/2134119/d06da5eb3da7d77e36e4fc9295f95df7/1200x900"
            },
            {
                "id": 3,
                "brand_id": 2,
                "name": "Х7",
                "price": 149999,
                "image": "https://avatars.mds.yandex.net/get-autoru-vos/2154344/41df50b6c86f41093c8dab8ad2842a01/1200x900"
            },
            {
                "id": 4,
                "brand_id": 2,
                "name": "x7",
                "price": 59999,
                "image": "https://s.auto.drom.ru/d24313/foreignimport/1340819014/gen580_1480355994.jpg"
            },
            {
                "id": 5,
                "brand_id": 2,
                "name": "5",
                "price": 45999,
                "image": "https://s.auto.drom.ru/d24313/foreignimport/1340743163/gen580_1480273164.jpg"
            },
            {
                "id": 6,
                "brand_id": 2,
                "name": "Х6",
                "price": 89999,
                "image": "https://avatars.mds.yandex.net/get-autoru-vos/2134119/d06da5eb3da7d77e36e4fc9295f95df7/1200x900"
            }
        ]

        return cars

    except Exception as e:
        print(f"Ошибка обработки обновлений: {e}")
        return None


@router.get("/cars/brands/{brand_id}")
async def get_all_car_for_brand(brand_id: int):
    try:
        cars = [
            {
                "id": 1,
                "brand_id" : 2,
                "name": "Х1",
                "price": 1,
                "image": "https://s.auto.drom.ru/d24313/foreignimport/1341540358/gen580x2_1481020259.jpg"
            },
            {
                "id": 2,
                "name": "Х6",
                "brand_id": 3,
                "price": 89999,
                "image": "https://avatars.mds.yandex.net/get-autoru-vos/2134119/d06da5eb3da7d77e36e4fc9295f95df7/1200x900"
            },
            {
                "id": 3,
                "brand_id": 4,
                "name": "Х7",
                "price": 149999,
                "image": "https://avatars.mds.yandex.net/get-autoru-vos/2154344/41df50b6c86f41093c8dab8ad2842a01/1200x900"
            },
            {
                "id": 4,
                "brand_id": 2,
                "name": "x7",
                "price": 59999,
                "image": "https://s.auto.drom.ru/d24313/foreignimport/1340819014/gen580_1480355994.jpg"
            },
            {
                "id": 5,
                "brand_id": 2,
                "name": "5",
                "price": 45999,
                "image": "https://s.auto.drom.ru/d24313/foreignimport/1340743163/gen580_1480273164.jpg"
            },
            {
                "id": 6,
                "brand_id": 2,
                "name": "Х6",
                "price": 89999,
                "image": "https://avatars.mds.yandex.net/get-autoru-vos/2134119/d06da5eb3da7d77e36e4fc9295f95df7/1200x900"
            }
        ]
        car = [car for car in cars if car["brand_id"] == brand_id]

        if car is None:
            raise HTTPException(status_code=404, detail=f"Автомобили с бредом {brand_id} не найден")

        return car

    except Exception as e:
        print(f"Ошибка обработки обновлений: {e}")
        return None


@router.get("/cars/brand")
async def get_all_brand():
    try:
        cars = [
            {"id": 1,
             "brand": "Toyota"},
            {"id": 2,
             "brand": "BMW"},
            {"id": 3,
             "brand": "Mercedes"},
            {"id": 4,
             "brand": "Audi"},
            {"id": 5,
             "brand": "Ford"},
            {"id": 6,
             "brand": "Honda"},
            {"id": 7,
             "brand": "Hyundai"},
            {"id": 8,
             "brand": "Kia"},
            {"id": 9,
             "brand": "Lexus"},
            {"id": 10,
             "brand": "Mazda"},
            {"id": 11,
             "brand": "Nissan"},
            {"id": 12,
             "brand": "Volkswagen"},
            {"id": 13,
             "brand": "Volvo"},
            {"id": 14,
             "brand": "Porsche"},
            {"id": 15,
             "brand": "Tesla"}
        ]

        return cars




    except Exception as e:
        print(f"Ошибка в get_all_brand: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/cars/{car_id}")
async def get_car_by_id(car_id: int):
    try:
        cars = [
            {
                "id": 1,
                "name": "Х1",
                "price": 1,
                "image": "https://s.auto.drom.ru/d24313/foreignimport/1341540358/gen580x2_1481020259.jpg"
            },
            {
                "id": 2,
                "name": "Х6",
                "price": 89999,
                "image": "https://avatars.mds.yandex.net/get-autoru-vos/2134119/d06da5eb3da7d77e36e4fc9295f95df7/1200x900"
            },
            {
                "id": 3,
                "name": "Х7",
                "price": 149999,
                "image": "https://avatars.mds.yandex.net/get-autoru-vos/2154344/41df50b6c86f41093c8dab8ad2842a01/1200x900"
            },
            {
                "id": 4,
                "name": "x7",
                "price": 59999,
                "image": "https://s.auto.drom.ru/d24313/foreignimport/1340819014/gen580_1480355994.jpg"
            },
            {
                "id": 5,
                "name": "5",
                "price": 45999,
                "image": "https://s.auto.drom.ru/d24313/foreignimport/1340743163/gen580_1480273164.jpg"
            },
            {
                "id": 6,
                "name": "Х6",
                "price": 89999,
                "image": "https://avatars.mds.yandex.net/get-autoru-vos/2134119/d06da5eb3da7d77e36e4fc9295f95df7/1200x900"
            }
        ]

        car = next((car for car in cars if car["id"] == car_id), None)

        if car is None:
            raise HTTPException(status_code=404, detail=f"Автомобиль с ID {car_id} не найден")

        return car

    except Exception as e:
        print(f"Ошибка обработки обновлений: {e}")
        return None

