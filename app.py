from flask import Flask, render_template

app = Flask(__name__)

# Sample conference data
conference_data = {
    "name": "DevHorizon 2026",
    "date": "September 15, 2026",
    "location": "San Francisco, CA & Online",
    "description": "The premier 1-day technical conference for exploring the frontiers of software development, AI, and scalable architecture.",
    "speakers": [
        {
            "id": 1,
            "name": "Dr. Elena Rostova",
            "title": "Lead AI Researcher",
            "company": "DeepMind",
            "image": "speaker1.webp"
        },
        {
            "id": 2,
            "name": "Marcus Chen",
            "title": "Principal Architect",
            "company": "AWS",
            "image": "speaker2.webp"
        },
        {
            "id": 3,
            "name": "Sarah Jenkins",
            "title": "VP of Engineering",
            "company": "Vercel",
            "image": "speaker3.webp"
        },
        {
            "id": 4,
            "name": "David Kim",
            "title": "Open Source Maintainer",
            "company": "Linux Foundation",
            "image": "speaker4.webp"
        },
        {
            "id": 5,
            "name": "Alex Rivera",
            "title": "Cloud Architect",
            "company": "Google",
            "image": "speaker5.webp"
        },
        {
            "id": 6,
            "name": "Jordan Lee",
            "title": "Data Scientist",
            "company": "OpenAI",
            "image": "speaker6.webp"
        }
    ],
    "schedule": [
        {"time": "08:00 AM", "title": "Registration & Breakfast", "type": "break"},
        {"time": "09:00 AM", "title": "Keynote: The Future of Agentic AI", "speaker": "Dr. Elena Rostova", "type": "talk"},
        {"time": "10:00 AM", "title": "Building Resilient Distributed Systems", "speaker": "Marcus Chen", "type": "talk"},
        {"time": "11:00 AM", "title": "The Evolution of Cloud Native", "speaker": "Alex Rivera", "type": "talk"},
        {"time": "12:00 PM", "title": "Networking Lunch", "type": "break"},
        {"time": "01:00 PM", "title": "Next-Gen Frontend Architectures", "speaker": "Sarah Jenkins", "type": "talk"},
        {"time": "02:00 PM", "title": "Securing the Open Source Supply Chain", "speaker": "David Kim", "type": "talk"},
        {"time": "03:00 PM", "title": "Machine Learning in Production", "speaker": "Jordan Lee", "type": "talk"},
        {"time": "04:00 PM", "title": "Panel: The Next 10 Years in Tech", "type": "panel"},
        {"time": "05:00 PM", "title": "Closing Remarks & Happy Hour", "type": "break"}
    ],
    "pricing": [
        {"tier": "Virtual", "price": "$99", "features": ["Live Stream Access", "On-Demand Recordings", "Virtual Networking", "Digital Swag Bag"]},
        {"tier": "General", "price": "$299", "features": ["In-Person Access", "All Talks & Panels", "Breakfast & Lunch", "Conference Swag"], "featured": True},
        {"tier": "VIP", "price": "$599", "features": ["Everything in General", "VIP Lounge Access", "Exclusive Speaker Dinner", "1-on-1 Mentoring Session"]}
    ]
}

@app.route("/")
def index():
    return render_template("index.html", data=conference_data)


import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
