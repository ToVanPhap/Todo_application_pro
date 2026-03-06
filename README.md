# 🚀 Todo application
A sleek, modern, and efficient task management application built with **Python** and **Streamlit**. This app features a clean UI/UX and a robust backend designed to help you organize your daily workflow seamlessly.

---

## ✨ Key Features

* **📊 Smart Dashboard:** Real-time metrics showing total tasks, pending items, and completion rates.
* **➕ Quick Task Creation:** Easily add tasks with specific due dates, priority levels (High, Medium, Low), and statuses.
* **🛠️ Centralized Action Center:** Complete or delete tasks by ID and clear all records with a single click (includes a safety confirmation).
* **💾 Auto-Persistence:** All data is automatically saved to a local `task.json` file, ensuring your data is never lost when you close the app.
* **🎨 Professional UI:** A custom light-blue theme with a scannable layout designed for productivity.



## 🛠 Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (Data-flow oriented UI)
* **Data Handling:** [Pandas](https://pandas.pydata.org/) (DataFrames & Analysis)
* **Backend Logic:** Python 3.x
* **Storage:** JSON (Persistent file-based storage)

---

## 📥 Installation & Setup

Follow these steps to run the application on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/todo-streamlit-app.git](https://github.com/your-username/todo-streamlit-app.git)
    cd todo-streamlit-app
    ```

2.  **Set Up a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the App:**
    ```bash
    streamlit run app_ui.py
    ```

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `app_ui.py` | Main entry point; handles the Streamlit UI and page routing. |
| `todos.py` | Core logic; manages task operations and JSON I/O. |
| `task.json` | Local database storing all task records. |
| `requirements.txt` | List of required Python libraries for deployment. |
| `.gitignore` | Ensures `venv/` and cache files are not pushed to GitHub. |

---

## 🚀 Roadmap

- [ ] **Dark Mode Support:** Toggle between light and dark themes.
- [ ] **Data Visualization:** Advanced charts showing productivity trends.
- [ ] **User Authentication:** Allow multiple users to have private task lists.
- [ ] **Notifications:** Browser alerts for upcoming due dates.


---
⭐ **If you find this project helpful, please give it a Star!**
