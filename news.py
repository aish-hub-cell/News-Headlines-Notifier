import tkinter as tk
from tkinter import ttk
import requests
import json
from plyer import notification
import time
import winsound  

API_KEY = "b1f6a7510feb41d7b305fcf0a65c8cbe"
BASE_URL = "https://newsapi.org/v2/top-headlines?category={}&apiKey={}"

root = tk.Tk()
root.title("Live News Headlines")
root.geometry("600x400")  
root.configure(bg="#1E1E1E")  

title_label = tk.Label(root, text="📰 News Headlines", font=("Arial", 20, "bold"), fg="white", bg="#1E1E1E")
title_label.pack(pady=10)

# News Categories Dropdown
categories = ["general", "technology", "business", "entertainment", "sports", "health", "science"]
selected_category = tk.StringVar(value="general")

category_dropdown = ttk.Combobox(root, values=categories, textvariable=selected_category, state="readonly", font=("Arial", 12))
category_dropdown.pack(pady=5)

# News Display Box
news_display = tk.Text(root, wrap="word", font=("Arial", 12), bg="#282C34", fg="white", height=10, width=60)
news_display.pack(pady=10)
news_display.config(state="disabled")

# Scrollbar
scrollbar = ttk.Scrollbar(root, command=news_display.yview)
scrollbar.pack(side="right", fill="y")
news_display.config(yscrollcommand=scrollbar.set)

# Sound Alert Function
def play_sound():
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

# Fetch News Function
def get_news():
    category = selected_category.get()
    NEWS_URL = BASE_URL.format(category, API_KEY)

    try:
        response = requests.get(NEWS_URL)
        news_data = response.json()

        if news_data["status"] == "ok" and news_data["totalResults"] > 0:
            headlines = [f"🔹 {article['title']}" for article in news_data["articles"][:5]]
            news_text = "\n\n".join(headlines)

            # notification
            notification.notify(
                title=f"Latest {category.capitalize()} News",
                message=news_text,
                app_name="News Notifier",
                timeout=10
            )

            # sound alert
            play_sound()

            news_display.config(state="normal")
            news_display.delete("1.0", tk.END)
            news_display.insert(tk.END, news_text)
            news_display.config(state="disabled")

        else:
            news_display.config(state="normal")
            news_display.delete("1.0", tk.END)
            news_display.insert(tk.END, "⚠️ No news available.")
            news_display.config(state="disabled")

    except Exception as e:
        news_display.config(state="normal")
        news_display.delete("1.0", tk.END)
        news_display.insert(tk.END, f"❌ Error fetching news: {str(e)}")
        news_display.config(state="disabled")

    # Schedule the next update
    root.after(10800000, get_news)

# Refresh Button
refresh_button = ttk.Button(root, text="🔄 Refresh News", command=get_news)
refresh_button.pack(pady=10)

get_news()

root.mainloop()
