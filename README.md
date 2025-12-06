<h1>📘 Student Counseling Appointment System</h1>

<hr/>

<h2>🔹 Overview</h2>
<p>
This is a Python-based team project designed to streamline student counseling appointment management. 
The system runs through a command-line interface and allows students to book available session slots, 
while counselors can approve, cancel and monitor scheduled sessions. The goal is to simulate a real-world 
appointment workflow using modular Python structure.
</p>

<hr/>

<h2>🎯 Core Features</h2>
<ul>
  <li>📅 View available counseling time slots</li>
  <li>🟢 Students can book sessions with name + time selection</li>
  <li>💬 Built-in inspirational quote generator</li>
  <li>🧑‍💼 Counselor approval or cancellation of appointments</li>
  <li>🔄 Status updates — Completed / Cancelled / Rescheduled</li>
  <li>🗓 Weekly counseling calendar overview</li>
  <li>❌ Prevents double booking of time slots</li>
</ul>

<hr/>

<h2>🧠 Technology & Concepts Used</h2>
<ul>
  <li><strong>Language:</strong> Python</li>
  <li><strong>Architecture:</strong> Modular multi-file structure</li>
  <li><strong>Concepts:</strong> OOP Classes, Functions, Input Handling, State Management</li>
  <li><strong>Interface:</strong> CLI menu-driven workflow</li>
</ul>

<hr/>

<h2>📂 Project Structure</h2>
<pre>
student_counseling/
├── appointment.py
├── slots.py
├── quote.py
├── approval.py
├── status.py
├── calendar_view.py
└── main.py
</pre>

<hr/>

<h2>▶️ How to Run</h2>

<h3>1️⃣ Clone or Download</h3>
<pre>
git clone &lt;your-repo-url&gt;
cd student_counseling
</pre>

<h3>2️⃣ Execute the Main Program</h3>
<pre>
python main.py
</pre>

<hr/>

<h2>📍 Workflow Overview</h2>
<ol>
  <li>User selects an option from the menu (View → Book → Approve → Status → Calendar)</li>
  <li>Bookings are only successful when the requested slot is available</li>
  <li>Session ownership and approval is controlled by counselor actions</li>
  <li>The weekly calendar displays the entire session schedule</li>
</ol>

<hr/>

<h2>📄 Sample Menu Output</h2>
<pre><code>
1. View Available Slots
2. Book Session
3. Get Inspirational Quote
4. Approve/Cancel Session
5. Update Status
6. Weekly Calendar View
7. Exit
</code></pre>

<hr/>

<h2>🚀 Possible Future Enhancements</h2>
<ul>
  <li>Convert CLI model into Flask-based Web Application</li>
  <li>Integrate SQLite/MongoDB for persistent storage</li>
  <li>Email/SMS reminders for upcoming appointments</li>
  <li>User authentication system for students & counselors</li>
</ul>

<br/>

<h3 align="center">✨ Team Project — Demonstrating Python Modular Design & Workflow Automation</h3>
