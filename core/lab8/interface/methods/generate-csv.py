import csv
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()


def calculate_age(birthdate):
    today = datetime.today()
    age = (
        today.year
        - birthdate.year
        - ((today.month, today.day) < (birthdate.month, birthdate.day))
    )
    return age


def generate_fake_data():
    name = fake.first_name()
    surname = fake.last_name()
    email = fake.email()
    sex = random.choice(["Male", "Female"])
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=70)
    job = fake.job()
    age = calculate_age(date_of_birth)

    return [name, surname, email, sex, date_of_birth, job, age]


def generate_csv(file_path, num_entries):
    with open(file_path, "w", newline="") as csv_file:
        fieldnames = ["name", "surname", "email", "sex", "date-of-birth", "job", "age"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(num_entries):
            fake_data = generate_fake_data()
            writer.writerow(dict(zip(fieldnames, fake_data)))


if __name__ == "__main__":
    generate_csv("data.csv", 60)
