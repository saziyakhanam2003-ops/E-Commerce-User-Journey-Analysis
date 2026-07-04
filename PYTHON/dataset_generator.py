import pandas as pd
import numpy as np
import random 
from faker import Faker
from datetime import datetime,timedelta

fake=Faker("en_IN")
random.seed(42)
np.random.seed(42)
num_records=100000

# Cities
cities = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Kolkata",
    "Ahmedabad",
    "Jaipur",
    "Lucknow"
]

# Devices
devices = ["Mobile", "Desktop", "Tablet"]

# Traffic Sources
traffic_sources = [
    "Google",
    "Facebook",
    "Instagram",
    "Direct",
    "Email",
    "Referral"
]

# Age Groups
age_groups = [
    "18-24",
    "25-34",
    "35-44",
    "45+"
]

# Genders
genders = ["Male", "Female"]

# Product Categories
categories = [
    "Electronics",
    "Fashion",
    "Beauty",
    "Home",
    "Grocery"
]

# Payment Methods
payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Wallet",
    "Cash on Delivery"
]

# Funnel Stages
funnel_stages = [
    "Visit",
    "Product View",
    "Add Cart",
    "Checkout",
    "Payment",
    "Purchase"
]

products = {
    "Electronics": [
        ("iPhone 15", 79999),
        ("Samsung S24", 74999),
        ("OnePlus 13", 54999),
        ("Boat Airdopes", 1999),
        ("Dell Laptop", 68999)
    ],

    "Fashion": [
        ("Men T-Shirt", 799),
        ("Women's Kurti", 1299),
        ("Jeans", 1999),
        ("Sneakers", 2999),
        ("Jacket", 3499)
    ],

    "Beauty": [
        ("Face Wash", 299),
        ("Lipstick", 699),
        ("Perfume", 1499),
        ("Moisturizer", 499),
        ("Sunscreen", 599)
    ],

    "Home": [
        ("Mixer Grinder", 3499),
        ("LED Bulb", 199),
        ("Bedsheet", 999),
        ("Water Bottle", 499),
        ("Chair", 2499)
    ],

    "Grocery": [
        ("Rice 5kg", 399),
        ("Cooking Oil", 249),
        ("Milk", 65),
        ("Biscuits", 40),
        ("Tea Powder", 220)
    ]
}
# -------------------------------
# Probability Weights
# -------------------------------

device_weights = [0.65, 0.25, 0.10]

traffic_weights = [0.35, 0.15, 0.15, 0.20, 0.10, 0.05]

category_weights = [0.20, 0.30, 0.15, 0.15, 0.20]

gender_weights = [0.55, 0.45]

age_weights = [0.25, 0.40, 0.20, 0.15]

# --------------------------------
# Store Final Dataset
# --------------------------------

data = []

for i in range(num_records):

    user_id = f"U{i+1:06d}"
    session_id = f"S{i+1:06d}"

    visit_date = fake.date_between(
        start_date="-180d",
        end_date="today"
    )

    visit_time = fake.time(pattern="%H:%M:%S")

    # Device
    device = np.random.choice(devices, p=device_weights)

    # Traffic Source
    traffic_source = np.random.choice(
        traffic_sources,
        p=traffic_weights
    )

    # City
    city = random.choice(cities)

    # Age Group
    age_group = np.random.choice(
        age_groups,
        p=age_weights
    )

    # Gender
    gender = np.random.choice(
        genders,
        p=gender_weights
    )

    # Product Category
    category = np.random.choice(
        categories,
        p=category_weights
    )

    # Product Name & Price
    product_name, product_price = random.choice(products[category])

    # Discount
    discount = random.choice([0, 5, 10, 15, 20, 25, 30])

    # Pages Viewed
    pages_viewed = random.randint(1, 15)

    # Session Duration (seconds)
    session_duration = random.randint(30, 1800)

    # Time Spent (minutes)
    time_spent = round(session_duration / 60, 2)

    # Cart Value
    cart_value = round(product_price * (1 - discount / 100), 2)

    # Funnel Stages
    product_view = np.random.choice([1, 0], p=[0.80, 0.20])

    if product_view:
        add_to_cart = np.random.choice([1, 0], p=[0.45, 0.55])
    else:
        add_to_cart = 0

    if add_to_cart:
        checkout = np.random.choice([1, 0], p=[0.65, 0.35])
    else:
        checkout = 0

    if checkout:
        payment = np.random.choice([1, 0], p=[0.85, 0.15])
    else:
        payment = 0

    if payment:
        purchase = np.random.choice([1, 0], p=[0.95, 0.05])
    else:
        purchase = 0

    # Order Status
    if purchase:
        order_status = random.choices(
            ["Delivered", "Cancelled", "Returned"],
            weights=[90, 5, 5]
        )[0]
    else:
        order_status = "No Purchase"

    # Customer Satisfaction
    if purchase:
        satisfaction = np.random.choice(
            [1, 2, 3, 4, 5],
            p=[0.03, 0.07, 0.15, 0.35, 0.40]
        )
    else:
        satisfaction = None

    # Payment Method
    payment_method = random.choice([
        "UPI",
        "Credit Card",
        "Debit Card",
        "Net Banking",
        "Cash on Delivery"
    ])

    data.append({
        "User_ID": user_id,
        "Session_ID": session_id,
        "Visit_Date": visit_date,
        "Visit_Time": visit_time,
        "Device": device,
        "Traffic_Source": traffic_source,
        "City": city,
        "Age_Group": age_group,
        "Gender": gender,
        "Product_Category": category,
        "Product_Name": product_name,
        "Product_Price": product_price,
        "Discount": discount,
        "Cart_Value": cart_value,
        "Pages_Viewed": pages_viewed,
        "Session_Duration": session_duration,
        "Time_Spent_Minutes": time_spent,
        "Product_View": product_view,
        "Add_To_Cart": add_to_cart,
        "Checkout": checkout,
        "Payment": payment,
        "Purchase": purchase,
        "Order_Status": order_status,
        "Payment_Method": payment_method,
        "Customer_Satisfaction": satisfaction
    })


df = pd.DataFrame(data)

df.to_csv("Dataset/user_journey_funnel_dataset.csv", index=False)

print("Dataset Generated Successfully!")
print(df.head())