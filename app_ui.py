import streamlit as st
import pandas as pd
import todos 

st.set_page_config(page_title="Todos", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebarCollapseIcon"] {
        display: none !important;
    }
    .st-emotion-cache-1wh8as9 {
        display: none !important;
    }

    .stApp { background-color: #F4F9FF; }
    
    /* SIDEBAR STYLING */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 2px solid #E1EFFF;
    }
    
    .stRadio > label { display: none; } 
    
    /* METRIC CARDS (LIGHT BLUE GRADIENT) */
    .metric-card {
        background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
        border: 1px solid #90CAF9;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .metric-value { font-size: 34px; font-weight: 800; color: #1565C0; }
    .metric-label { font-size: 12px; color: #1976D2; font-weight: 700; text-transform: uppercase; }

    /* TASK ROWS */
    .task-row {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        border: 1px solid #E1EFFF;
    }
    .task-row:hover {
        border-color: #2196F3;
        background-color: #F0F7FF;
    }

    /* BADGES */
    .badge { padding: 4px 12px; border-radius: 15px; font-size: 10px; font-weight: 700; text-transform: uppercase; }
    .badge-high { background-color: #FFEBEE; color: #D32F2F; }
    .badge-medium { background-color: #FFFDE7; color: #FBC02D; }
    .badge-low { background-color: #E8F5E9; color: #388E3C; }
    .badge-status { background-color: #E3F2FD; color: #1976D2; }
</style>
""", unsafe_allow_html=True)

# SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='color: #1976D2;'>Todos</h2>", unsafe_allow_html=True)
    st.divider()
    
    st.markdown("**SELECT MODULE**")
    menu = st.radio(
        "Nav",
        ["Dashboard", "Add New Task", "Complete and Delete Task"],
        index=0
    )
    
    st.divider()
# Load data
tasks = todos.task_list

# --- DASHBOARD ---
if menu == "Dashboard":
    st.header("Task Overview")
    
    # Metrics
    total = len(tasks)
    done = sum(1 for t in tasks if t['status'].lower() == 'completed')
    pending = total - done

    m1, m2, m3 = st.columns(3)
    with m1: st.markdown(f'<div class="metric-card"><div class="metric-label">All Tasks</div><div class="metric-value">{total}</div></div>', unsafe_allow_html=True)
    with m2: st.markdown(f'<div class="metric-card"><div class="metric-label">Completed</div><div class="metric-value">{done}</div></div>', unsafe_allow_html=True)
    with m3: st.markdown(f'<div class="metric-card"><div class="metric-label">Pending</div><div class="metric-value">{pending}</div></div>', unsafe_allow_html=True)

    st.write("")
    st.divider()

    # SEARCH IN DASHBOARD
    st.subheader("🔍 Search tasks")
    search_q = st.text_input("Filter by task name...", placeholder="task's name", label_visibility="collapsed")
    
    filtered = [t for t in tasks if search_q.lower() in t['name'].lower()] if search_q else tasks

    if not filtered:
        st.info("No tasks matching your criteria.")
    else:
        # Table Header
        st.markdown("""
        <div style="display:flex; padding:0 15px; font-size:11px; font-weight:800; color:#90CAF9; text-transform:uppercase;">
            <div style="flex: 1;">ID</div>
            <div style="flex: 4;">Task Description</div>
            <div style="flex: 2;">Due Date</div>
            <div style="flex: 2;">Priority</div>
            <div style="flex: 2;">Status</div>
        </div>
        """, unsafe_allow_html=True)

        for t in filtered:
            p_class = f"badge-{t['priority'].lower()}"
            st.markdown(f"""
            <div class="task-row">
                <div style="flex: 1; font-weight:700; color:#BBDEFB;">#{t['id']}</div>
                <div style="flex: 4; font-weight:600; color:#0D47A1;">{t['name']}</div>
                <div style="flex: 2; color:#64B5F6; font-size:13px;">{t['due_date']}</div>
                <div style="flex: 2;"><span class="badge {p_class}">{t['priority']}</span></div>
                <div style="flex: 2;"><span class="badge badge-status">{t['status']}</span></div>
            </div>
            """, unsafe_allow_html=True)

# ADD NEW TASK
elif menu == "Add New Task":
    st.header("New Task")
    with st.container(border=True):
        with st.form("create_task", clear_on_submit=True):
            name = st.text_input("TASK TITLE")
            c1, c2 = st.columns(2)
            with c1:
                date = st.date_input("DUE DATE")
                status = st.selectbox("STATUS", ["Not started", "In progress", "Completed"])
            with c2:
                prio = st.selectbox("PRIORITY", ["Low", "Medium", "High"], index=1)
            
            if st.form_submit_button("🚀 CREATE", use_container_width=True):
                if name:
                    todos.add_task(name, str(date), prio, status)
                    todos.save_tasks_to_file() 
                    st.success("Task created and saved automatically!")
                else:
                    st.error("Please enter a task title.")

# --- COMPLETE AND DELETE TASK ---
elif menu == "Complete and Delete Task":
    st.header("Complete or Delete Task")

    if 'confirm_clear' not in st.session_state:
        st.session_state.confirm_clear = False

    def handle_complete():
        tid = st.session_state.task_id_input
        if tid is not None:
            todos.mask_task_completion(tid)
            todos.save_tasks_to_file()
            st.session_state.task_id_input = None

    def handle_delete():
        tid = st.session_state.task_id_input
        if tid is not None:
            todos.delete_task(tid)
            todos.save_tasks_to_file()
            st.session_state.task_id_input = None
            
    def trigger_clear_warning():
        st.session_state.confirm_clear = True
        
    def cancel_clear():
        st.session_state.confirm_clear = False
        
    def execute_clear_all():
        todos.clear_all_tasks()
        todos.save_tasks_to_file()
        st.session_state.confirm_clear = False
        st.session_state.task_id_input = None
            
    with st.container(border=True):
        st.subheader("Modify Task")
        
        ca, cb, cc, cd = st.columns([1.5, 1, 1, 1])
        
        with ca:
            st.number_input("TASK ID", min_value=1, step=1, value=None, key="task_id_input")
            
        with cb:
            st.write(""); st.write("")
            st.button("COMPLETE", use_container_width=True, on_click=handle_complete)
            
        with cc:
            st.write(""); st.write("")
            st.button("DELETE", use_container_width=True, on_click=handle_delete)
            
        with cd:
            st.write(""); st.write("")
            st.button("CLEAR ALL", type="primary", use_container_width=True, on_click=trigger_clear_warning)

        if st.session_state.confirm_clear:
            st.warning("⚠️ Are you sure you want to permanently delete ALL tasks? This action cannot be undone.")
            c_yes, c_no = st.columns([1, 1])
            with c_yes:
                st.button("Yes", type="primary", use_container_width=True, on_click=execute_clear_all)
            with c_no:
                st.button("Cancel", use_container_width=True, on_click=cancel_clear)

    st.write("")
    st.divider()
    
    st.dataframe(pd.DataFrame(tasks), use_container_width=True, hide_index=True)