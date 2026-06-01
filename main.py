import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime



class StorageManager:
    FILE_NAME = "meals.json"


    @staticmethod
    def load_data():
        if os.path.exists(StorageManager.FILE_NAME):
            try:
                with open(StorageManager.FILE_NAME, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []


    @staticmethod
    def save_data(data):
        with open(StorageManager.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)



class CalorieCalculator:
    food_db = {
        "rice": 200,
        "fried rice": 320,
        "burger": 350,
        "pizza": 285,
        "apple": 95,
        "banana": 105,
        "egg": 78,
        "chicken": 250,
        "fries": 365,
        "milk": 120,
        "coffee": 50,
        "noodles": 300
    }


    @staticmethod
    def calculate(food):
        return CalorieCalculator.food_db.get(food.lower(), 100)



class MealLogger:
    def __init__(self):
        self.meals = StorageManager.load_data()


    def add_meal(self, meal_type, food, calories):
        self.meals.append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "meal_type": meal_type,
            "food": food,
            "calories": calories
        })
        StorageManager.save_data(self.meals)


    def get_meals(self):
        return self.meals


    def clear_all(self):
        self.meals = []
        StorageManager.save_data(self.meals)



class FoodCalorieTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Calorie Tracker")
        self.root.geometry("600x450")
        self.root.config(bg="#7B2CBF")


        self.logger = MealLogger()


        tk.Label(
            root,
            text="Food Calorie Tracker",
            font=("Arial", 14, "bold"),
            bg="#7B2CBF",
            fg="white"
        ).pack(pady=5)



        frame = tk.Frame(root, bg="#9D4EDD")
        frame.pack(pady=5)


        tk.Label(frame, text="Meal Type:", bg="#9D4EDD", fg="white").grid(row=0, column=0)
        self.meal_var = tk.StringVar(value="Breakfast")


        tk.OptionMenu(
            frame,
            self.meal_var,
            "Breakfast", "Lunch", "Dinner", "Snack"
        ).grid(row=0, column=1)


        tk.Label(frame, text="Food:", bg="#9D4EDD", fg="white").grid(row=1, column=0)
        self.food_entry = tk.Entry(frame, width=20)
        self.food_entry.grid(row=1, column=1)


        btn_frame = tk.Frame(root, bg="#7B2CBF")
        btn_frame.pack(pady=5)


        tk.Button(btn_frame, text="ADD", width=8, bg="#FFAFCC", command=self.add_meal).grid(row=0, column=0, padx=3)
        tk.Button(btn_frame, text="CLEAR", width=8, bg="#FFAFCC", command=self.clear_all).grid(row=0, column=1, padx=3)
        tk.Button(btn_frame, text="EXIT", width=8, bg="#FFAFCC", command=root.destroy).grid(row=0, column=2, padx=3)



        self.listbox = tk.Listbox(root, width=60, height=15, bg="white")
        self.listbox.pack(pady=10)


    
        self.total_label = tk.Label(
            root,
            text="Total Calories: 0",
            bg="#7B2CBF",
            fg="yellow",
            font=("Arial", 11, "bold")
        )
        self.total_label.pack()


        self.update_display()


    def add_meal(self):
        food = self.food_entry.get().strip()


        if not food:
            messagebox.showerror("Error", "Enter food name")
            return


        calories = CalorieCalculator.calculate(food)


        self.logger.add_meal(self.meal_var.get(), food, calories)


        self.food_entry.delete(0, tk.END)
        self.update_display()


    def update_display(self):
        self.listbox.delete(0, tk.END)


        total = 0


        for meal in self.logger.get_meals():
            date = meal.get("date", "N/A")
            meal_type = meal.get("meal_type", "Unknown")
            food = meal.get("food", "Unknown")
            calories = meal.get("calories", 0)


            self.listbox.insert(
                tk.END,
                f"{date} | {meal_type} | {food} | {calories} cal"
            )


            total += calories


        self.total_label.config(text=f"Total Calories: {total}")


    def clear_all(self):
        self.logger.clear_all()
        self.update_display()




if __name__ == "__main__":
    root = tk.Tk()
    app = FoodCalorieTracker(root)
    root.mainloop()

