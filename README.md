# News Headlines Notifier

## Description

This Python project provides live news headlines from various categories and shows them in a desktop application. The app uses `Tkinter` for the GUI, `NewsAPI` for fetching the latest news, and `plyer` for desktop notifications and sound alerts.

- Fetches news from multiple categories like general, technology, business, and more.
- Displays top 5 news headlines in a clean and readable format.
- Provides sound alerts when new headlines are fetched.
- Auto-refreshes every 3 hours to show the latest news.

## Features

- **Categories**: Choose from general, technology, business, entertainment, sports, health, or science.
- **Notification**: Desktop notifications show the latest headlines.
- **Sound Alerts**: A system sound plays when new headlines are fetched.
- **Auto Refresh**: The news refreshes every 3 hours to keep you updated.

## Requirements

- Python 3.x
- Tkinter (`pip install tk`)
- Requests (`pip install requests`)
- Plyer (`pip install plyer`)

## How to Use

1. Install the required dependencies:
   ```bash
   pip install requests plyer tk
   ```
2. Download or clone the repository to your local machine.
3. Open the `news.py` file in your preferred Python IDE or editor (like VS Code).
4. Replace `API_KEY = "your_api_key"` with your actual NewsAPI key, which you can get by signing up at [NewsAPI](https://newsapi.org/).
5. Run the `news.py` file:
   ```bash
   python news.py
   ```
6. The app will show a window with a dropdown to select the category, a button to refresh the news, and display the latest headlines.

## License

This project is licensed under the MIT License.
