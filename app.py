import streamlit as st

# -------------------------------------------------------
# LOAD CSS
# -------------------------------------------------------

def load_css():

    with open("styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Python ATM System",
    page_icon="🏧",
    layout="wide"
)

load_css()

# -------------------------------------------------------
# SESSION STATE
# -------------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "pin" not in st.session_state:
    st.session_state.pin = "1234"

if "balance" not in st.session_state:
    st.session_state.balance = 5000.0

if "mini_statement" not in st.session_state:
    st.session_state.mini_statement = []

if "page" not in st.session_state:
    st.session_state.page = "dashboard"

# -------------------------------------------------------
# LOGIN PAGE
# -------------------------------------------------------

if not st.session_state.logged_in:

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,1,2])

    with col2:
        st.image("assets/atm_logo.png", width=250)

    st.markdown(
        """
        <h1 style="text-align:center;">
        Python ATM System
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="text-align:center;
                  font-size:20px;
                  color:gray;">
        Secure Banking Simulation using Python & Streamlit
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    entered_pin = st.text_input(
        "Enter PIN",
        type="password"
    )

    if st.button(
        "🔐 Login",
        use_container_width=True
    ):

        if entered_pin == st.session_state.pin:

            st.session_state.logged_in = True

            st.rerun()

        else:

            st.error("Incorrect PIN")

# -------------------------------------------------------
# DASHBOARD
# -------------------------------------------------------

else:

    # ---------- LOGO ----------

    col1, col2, col3 = st.columns([2,1,2])

    with col2:
        st.image("assets/atm_logo.png", width=140)

    # ---------- TITLE ----------

    st.markdown("""
    <h1 style="text-align:center;">
        Python ATM System
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="
    text-align:center;
    font-size:22px;
    color:gray;
    ">
    Secure Banking Simulation using Python & Streamlit
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ---------- BALANCE CARD ----------

   
    st.markdown("---")

    st.markdown(
        """
        <h2 style="text-align:center;">
        Banking Services
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ---------- BUTTONS ----------

    col1, col2 = st.columns(
        [1,1],
        gap="large"
    )

    # LEFT SIDE

    with col1:

        if st.button(
            "💰 Check Balance",
            use_container_width=True
        ):
            st.session_state.page = "balance"

        st.write("")

        if st.button(
            "💸 Withdraw Money",
            use_container_width=True
        ):
            st.session_state.page = "withdraw"

        st.write("")

        if st.button(
            "📄 Mini Statement",
            use_container_width=True
        ):
            st.session_state.page = "statement"

    # RIGHT SIDE

    with col2:

        if st.button(
            "💵 Deposit Money",
            use_container_width=True
        ):
            st.session_state.page = "deposit"

        st.write("")

        if st.button(
            "🔐 Change PIN",
            use_container_width=True
        ):
            st.session_state.page = "change_pin"

        st.write("")

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):
            st.session_state.logged_in = False
            st.session_state.page = "dashboard"
            st.rerun()

    st.divider()

# =====================================================
# CHECK BALANCE
# =====================================================

if st.session_state.page == "balance":

    st.subheader("💰 Account Balance")

    st.metric(
        "Current Balance",
        f"₹ {st.session_state.balance:.2f}"
    )

# =====================================================
# DEPOSIT MONEY
# =====================================================

elif st.session_state.page == "deposit":

    st.subheader("💵 Deposit Money")

    st.info(f"Available Balance : ₹ {st.session_state.balance:.2f}")

    amount = st.number_input(
        "Enter Deposit Amount",
        min_value=0.0,
        step=100.0,
        key="deposit"
    )

    if st.button("Deposit", use_container_width=True):

        if amount > 0:

            st.session_state.balance += amount

            st.session_state.mini_statement.append(
                f"Deposited ₹{amount:.2f}"
            )

            st.success("Amount Deposited Successfully")

            st.metric(
                "Updated Balance",
                f"₹ {st.session_state.balance:.2f}"
            )

        else:

            st.error("Invalid Amount")

# =====================================================
# WITHDRAW MONEY
# =====================================================

elif st.session_state.page == "withdraw":

    st.subheader("💸 Withdraw Money")

    st.info(f"Available Balance : ₹ {st.session_state.balance:.2f}")

    amount = st.number_input(
        "Enter Withdraw Amount",
        min_value=0.0,
        step=100.0,
        key="withdraw"
    )

    if st.button("Withdraw", use_container_width=True):

        if amount <= 0:

            st.error("Invalid Amount")

        elif amount > st.session_state.balance:

            st.error("Insufficient Balance")

        else:

            st.session_state.balance -= amount

            st.session_state.mini_statement.append(
                f"Withdraw ₹{amount:.2f}"
            )

            st.success("Withdrawal Successful")

            st.metric(
                "Remaining Balance",
                f"₹ {st.session_state.balance:.2f}"
            )
# =====================================================
# CHANGE PIN
# =====================================================

elif st.session_state.page == "change_pin":

    st.subheader("🔐 Change PIN")

    old_pin = st.text_input(
        "Enter Old PIN",
        type="password"
    )

    new_pin = st.text_input(
        "Enter New PIN",
        type="password"
    )

    confirm_pin = st.text_input(
        "Confirm New PIN",
        type="password"
    )

    if st.button("Update PIN", use_container_width=True):

        if old_pin != st.session_state.pin:

            st.error("❌ Incorrect Old PIN")

        elif len(new_pin) != 4 or not new_pin.isdigit():

            st.error("PIN must be exactly 4 digits.")

        elif new_pin != confirm_pin:

            st.error("New PIN and Confirm PIN do not match.")

        else:

            st.session_state.pin = new_pin

            st.session_state.mini_statement.append(
                "PIN Changed Successfully"
            )

            st.success("✅ PIN Updated Successfully")

# =====================================================
# MINI STATEMENT
# =====================================================

elif st.session_state.page == "statement":

    st.subheader("📄 Mini Statement")

    if len(st.session_state.mini_statement) == 0:

        st.info("No Transactions Yet")

    else:

        st.write("### Recent Transactions")

        for transaction in reversed(st.session_state.mini_statement):

            st.success(transaction)



#Footer
st.markdown(
    """
    <div style="text-align:center; padding:15px; font-size:15px; color:gray;">
        👨‍💻 <b>Developed by Kathi Varshith</b> | 📧 <a href="mailto:kathivarshith14@gmail.com">kathivarshith14@gmail.com</a> | 💻 <a href="https://github.com/Kathivarshith" target="_blank">GitHub</a> | 💼 <a href="https://www.linkedin.com/in/kathi-varshith1114/" target="_blank">LinkedIn</a> | 🚀 <b>Open to Internship & Full-Time Opportunities</b>
    </div>
    """,
    unsafe_allow_html=True
)