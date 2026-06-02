FOOD CALORIE TRACKER

Application Description

  The Food Calorie Tracker is a desktop application that helps users monitor their daily food intake and calorie consumption. Users can log meals, automatically calculate calories, view their daily meal records, track total calories consumed, and save data for future use through persistent storage.

The Application Allows Users To:

  Log meals and food items.
Automatically calculate calorie intake.
View daily meal records.
Calculate total calories consumed per day.
Save and load meal data using persistent storage.

OOP Concepts Used

  Class – Used to represent meal records and application components.
  Objects – Created from classes to manage meal data.
  Encapsulation – Data and methods are grouped within classes.
  Inheritance – Allows code reusability and extension of classes.
  Polymorphism – Enables methods to perform different functions when needed.

Technologies Used
  Python– Main programming language.
  Tkinter– Graphical User Interface (GUI) framework.
  JSON – Data storage format for saving meal records.
  Pytest– Automated testing framework.

Project Structure 

FoodCalorieTracker/
│
├── main.py
├── test_main.py
└── meals.json

How to Run

       1. Requirements Python 3.x
       2. Clone this repository
            git clone (https://github.com/madelyngueta/FOOD_CALORIE_TRACKER)


Navigate to the Project Folder

  cd FoodCalorieTracker

Run the Application:

  python main.py


Running Tests

  To run automated tests using Pytest:

   pytest

     Or:

   pytest -m pytest -v


Export Report

  The application can generate and display meal records and calorie summaries. Users can export or save reports based on the stored meal data for documentation and tracking purposes.

Author

Developed as a school project by:
    • Madelyn G. Gueta (https://github.com/madelyngueta)
    • Mar P. Grantos (https://github.com/margrantos591-tech)
    • Alvin G. Gipit (https://github.com/gipitalvin07-dot)

In Partial Fulfillment of the Requirements for the Subject CC103 Computer Programming 2 Under the Course of Bachelor of Science in Information Technology at Sorsogon State University Bulan Campus. With the Supervision of our Professor John Mark Gabrentina.

Notes
  • Basic input validation only (strip() checks)
  • Focus is on OOP structure, not advanced error handling
  • Designed for educational purposes


