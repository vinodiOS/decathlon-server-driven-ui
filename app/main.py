from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/dashboard")
def read_root():
    return {
    "pageTitle": "Decathlon",
    "components": [

        {
            "type": "carousel",
            "data": {
                "items": [
                    {
                        "image_url": " https://user-images.githubusercontent.com/30258541/181459044-7d378f7f-ae83-4a02-a6b2-385e97d2843c.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181459088-ab8d7b00-af85-4aaf-9e80-7148aa853ffe.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181459100-ccf94a0a-772e-4962-91ac-8f1bd0c6c560.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181459120-61c67c46-567c-4d65-9c94-05a1f0c8b6ca.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181459134-7362d788-4444-4936-b11f-fac4af5f0ec3.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181459146-79d0ec51-d37a-453b-bab6-331d9354ecba.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181459163-9a0cfed2-c48e-444f-a1c3-0d3da1536b00.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181459178-e37841b8-835d-4fa0-a1ad-fa1dc0e37f70.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181459185-84fd4c31-1cae-4e53-bc3a-b677793b1766.png"
                    }
                ],
                "action": {
                    "type": "sheet",
                    "destination": "petDetail"
                }
            }
        },
        {
            "type": "featuredImage",
                "data": {
                    "image_url": "https://user-images.githubusercontent.com/30258541/181455822-f4fae7dc-b3ec-446c-9235-9cee1dac19fd.png"
                }
        },

        {
            "type": "list", 
            "data": {
                "subtitle": "Men",
                "title": "rain jackets and pants",
                "rows": [
                        {
                        "name": "Men's Hiking Raincoat Half Zip NH100 - Khaki",
                        "discounted_price": 599.0,
                        "mrp": 899.0,
                        "review": 4.4,
                        "image_url": "https://user-images.githubusercontent.com/30258541/181444339-7c537044-61d4-40f2-b7f7-41a2a67e4446.png"
                        },
                        {
                        "name": "Adult Hiking Rain Poncho 50 Blue",
                        "discounted_price": 499.0,
                        "mrp": 699.0,
                        "review": 4.2,
                        "tags":["price drop"],
                        "image_url": "https://user-images.githubusercontent.com/30258541/181444322-36ead874-0e91-4a52-9ee8-d27fabab4f00.png"
                        },
                        {
                        "name": "Men's Hiking Waterproof Jacket NH150 WP",
                        "discounted_price": 1599.0,
                        "mrp": 1999.0,
                        "review": 4.3,
                        "tags":["limited stock"],
                        "image_url": "https://user-images.githubusercontent.com/30258541/181444304-5036a305-e60c-4b2d-936f-cd361a045326.png"
                        },
                        {
                        "name": "Hiking Rain Poncho 40 Size S/M Grey",
                        "discounted_price": 1499.0,
                        "mrp": 1999.0,
                        "review": 4.4,
                        "image_url": "https://user-images.githubusercontent.com/30258541/181444278-7b029244-fb1a-44bf-9afe-4de4ef7e2c88.png"
                        },
                        {
                        "name": "Men's Hiking Lightweight Waterproof Jacket MH150 Blue",
                        "discounted_price": 3499.0,
                        "mrp": 4899.0,
                        "review": 4.4,
                        "tags":["Exclusive online"],
                        "image_url": "https://user-images.githubusercontent.com/30258541/181444250-f301de33-7b8f-4179-b7c7-8eff106a1ec5.png"
                        },
                        {
                        "name": "Men's Waterproof Hiking Over Trousers - NH500 Imper",
                        "discounted_price": 699.0,
                        "mrp": 1199.0,
                        "review": 4.3,
                        "tags":["Lowest Price","Best Value"],
                        "image_url": "https://user-images.githubusercontent.com/30258541/181444224-cb4ca66f-01e7-408c-bac0-62435570fa5c.png"
                        }
                ], 
                "action": {
                    "type": "push", 
                    "destination": "petDetail"
                } 
            }
        },
        {
            "type": "featuredImage",
            "data": {
                "image_url": "https://user-images.githubusercontent.com/30258541/181452749-2e9fac60-bbf8-44cc-ac43-438a85fb35e5.png"
            }
        },
        {
            "type": "featuredImage",
            "data": {
                "image_url": "https://user-images.githubusercontent.com/30258541/181445890-dc5d139a-0fa9-47be-aea6-754f6b9d057d.png)"
            }
        },
        {
            "type": "list", 
            "data": {
                "subtitle": "Trending",
                "title": "Near you",
                "rows": [
                    {
                        "name": "Men Gym Shorts Polyester With Zip Pockets FST 120 Black",
                        "discounted_price": 599.0,
                        "mrp": 1199.0,
                        "review": 4.6,
                        "tags": ["Eco Design"],
                        "image_url": "https://user-images.githubusercontent.com/30258541/181452385-ec5c8c21-f51d-4a33-ba29-0633b46eed09.png"
                        },
                        {
                        "name": "Men's Running Shoes Run 100 - GREY",
                        "discounted_price": 899.0,
                        "mrp": 1199.0,
                        "review": 4.6,
                        "tags":["Lowest Price", "Best Value"],
                        "image_url": "https://user-images.githubusercontent.com/30258541/181452374-e27b217d-90e7-4a3f-93cf-652bf1cb4405.png"
                        },
                        {
                        "name": "Men's Hiking Pant MH100 Black",
                        "discounted_price": 999.0,
                        "mrp": 1599.0,
                        "review": 4.4,
                        "image_url": "https://user-images.githubusercontent.com/30258541/181452360-fd0bdc94-f940-4f65-aff8-fbf57e5d6c82.png"
                        },
                        {
                        "Name": "Men Cotton Blend Gym Pants Regular fit 100 - Black",
                        "discounted_price": 599.0,
                        "mrp": 999.0,
                        "review": 4.3,
                        "image_url": "https://user-images.githubusercontent.com/30258541/181452317-83d1ff85-0082-4c6c-b335-3a5c81e29bbb.png"
                        }
                ], 
                "action": {
                    "type": "push", 
                    "destination": "petDetail"
                } 
            }
        },

        {
            "type": "carousel",
            "data": {
                "title": "Travel product",
                "items": [
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181453191-98de0c08-71ac-45b1-9c4a-a9530ffbc67a.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181453225-db14aa73-319b-471b-97b5-1ea36be078ca.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181453229-496e2054-c1ce-4c3a-a00d-53555f8e1ffe.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181453236-f470fc07-ba98-4a6b-8452-dfc5497ac2ed.png"
                    }
                ],
                "action": {
                    "type": "sheet",
                    "destination": "petDetail"
                }
            }
        },


        {
            "type": "carousel",
            "data": {
                "title": "Cardio & Hunting",
                "subtitle": "starting from 299",
                "items": [
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181453850-515846ef-cef8-4c7e-900c-3736e63c4e44.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181453862-5ce4b580-a412-4db3-ba87-1d442db22357.png"
                    }
                ],
                "action": {
                    "type": "sheet",
                    "destination": "petDetail"
                }
            }
        },

        {
            "type": "carousel",
            "data": {
                "title": "Offers",
                "items": [
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181454109-496dff57-5d51-4ed5-b197-4d06ee4476c5.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181454123-dc0afb9f-f0cd-42af-a48e-0e5dc060ccf4.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181454126-926bd5b0-22d1-4615-8a2c-0bfe9a209bfc.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181454131-630e309e-4612-4c77-9fa7-10c719926dc2.png"
                    }
                ],
                "action": {
                    "type": "sheet",
                    "destination": "petDetail"
                }
            }
        },

        {
            "type": "list", 
            "data": {
                "subtitle": "Inspired by your",
                "title": "Browsing History",
                "rows": [
                    {
                        "name": "Men's Running T-shirt Run Dry - Black",
                        "discounted_price": 349.0,
                        "mrp": 799.0,
                        "review": 4.5,
                        "image_url": "https://user-images.githubusercontent.com/30258541/181455395-0a9fd45b-95a4-4ed1-b65b-7a43c6e325de.png"
                        },
                        {
                        "name": "Men's Running T-shirt Run Dry - Prussian Blue",
                        "discounted_price": 349.0,
                        "mrp": 799.0,
                        "review": 4.5,
                        "image_url": "https://user-images.githubusercontent.com/30258541/181455387-c7c42a5a-0c7c-4476-9dd3-fd4b1c5e4ded.png"
                        },
                        {
                        "name": "Cycle Water Bottle 650ml - Red",
                        "discounted_price": 299.0,
                        "mrp": 499.0,
                        "review": 4.2,
                        "image_url": "https://user-images.githubusercontent.com/30258541/181455377-a7aa45a5-8fb5-4015-9042-f3cb68970cba.png"
                        
                        },
                        {
                        "name": "RUN COMFORT MEN'S JOGGING SHOES - BLUE",
                        "discounted_price": 3599.0,
                        "mrp": 5499.0,
                        "review": 4.1,
                        "image_url": "https://user-images.githubusercontent.com/30258541/181455345-87bf3f16-301c-4348-aaf2-42c957faa85d.png"
                        }
                ], 
                "action": {
                    "type": "push", 
                    "destination": "petDetail"
                } 
            }
        },
        {
            "type": "carousel",
            "data": {
                "title": "Offers",
                "items": [
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181456127-b60c8247-c229-4e6b-8600-8ca0ab40d484.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181456136-9fa9bc76-f6a0-45e1-82ea-6aa5e8651c50.png)"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181456143-f85c94c0-82c6-4248-a6d6-ce57c59e6f3e.png"
                    },
                    {
                        "image_url": "https://user-images.githubusercontent.com/30258541/181456151-21b66f30-be1e-46ce-b892-ebb473bc9205.png"
                    }
                ],
                "action": {
                    "type": "sheet",
                    "destination": "petDetail"
                }
            }
        },
        {
            "type": "list", 
            "data": {
                "subtitle": "Women",
                "rows": [
                    {
                        "name": "Women Cotton Blend Gym T-Shirt Regular-Fit 500 - Turquoise Marl",
                        "discounted_price": 399.0,
                        "mrp": 699.0,
                        "review": 4.6,
                        "tags":["best Seller"],
                        "image_url": "https://user-images.githubusercontent.com/30258541/181457724-24cec436-e80c-463c-84fd-a0ea0dc6b51b.png"
                        },
                        {
                        "name": "Women Gym Tshirt Polyester Loose Fit Bordeaux",
                        "discounted_price": 599.0,
                        "mrp": 999.0,
                        "review": 4.7,
                        "image_url": "https://user-images.githubusercontent.com/30258541/181457710-8d557dbb-260b-4d5f-bbed-4da0d17b3add.png"
                        },
                        {
                        "name": "Women's Cotton Gym T-shirt Regular fit Sportee - Red",
                        "discounted_price": 199.0,
                        "mrp": 299.0,
                        "review": 4.2,
                        "tags":["Lowest Price", "Best Value"],
                        "image_url": "https://user-images.githubusercontent.com/30258541/181457698-e7b64ac3-344a-4b27-bed8-1d3aa822e703.png"
                        },
                        {
                        "name": "Women's Gym Cotton Blend Loose fit printed tshirt-Purple Print",
                        "discounted_price": 599.0,
                        "mrp": 899.0,
                        "review": 4.4,
                        "image_url": "https://user-images.githubusercontent.com/30258541/181457678-3be0e2b2-4740-4b58-9e66-b45e0518b743.png"
                        }
                ], 
                "action": {
                    "type": "push", 
                    "destination": "petDetail"
                } 
            }
        }

        
    ]
}
