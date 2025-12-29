"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
   "Chess Club": {
      "description": "Learn strategies and compete in chess tournaments",
      "schedule": "Fridays, 3:30 PM - 5:00 PM",
      "max_participants": 12,
      "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
   },
   "Programming Class": {
      "description": "Learn programming fundamentals and build software projects",
      "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
      "max_participants": 20,
      "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
   },
   "Gym Class": {
      "description": "Physical education and sports activities",
      "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
      "max_participants": 30,
      "participants": ["john@mergington.edu", "olivia@mergington.edu"]
   },
   "Basketball Team": {
      "description": "Competitive basketball training and games",
      "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
      "max_participants": 15,
      "participants": []
   },
   "Swimming Club": {
      "description": "Swimming training and water sports",
      "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
      "max_participants": 20,
      "participants": []
   },
   "Art Studio": {
      "description": "Express creativity through painting and drawing",
      "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
      "max_participants": 15,
      "participants": []
   },
   "Drama Club": {
      "description": "Theater arts and performance training",
      "schedule": "Tuesdays, 4:00 PM - 6:00 PM",
      "max_participants": 25,
      "participants": []
   },
   "Debate Team": {
      "description": "Learn public speaking and argumentation skills",
      "schedule": "Thursdays, 3:30 PM - 5:00 PM",
      "max_participants": 16,
      "participants": []
   },
   "Science Club": {
      "description": "Hands-on experiments and scientific exploration",
      "schedule": "Fridays, 3:30 PM - 5:00 PM",
      "max_participants": 20,
      "participants": []
   },
   "Soccer Team": {
      "description": "Competitive soccer training and matches",
      "schedule": "Mondays and Fridays, 3:30 PM - 5:00 PM",
      "max_participants": 18,
      "participants": []
   },
   "Volleyball Club": {
      "description": "Volleyball practice and friendly competitions",
      "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
      "max_participants": 16,
      "participants": []
   },
   "Music Club": {
      "description": "Learn instruments and perform in ensembles",
      "schedule": "Thursdays, 3:30 PM - 5:00 PM",
      "max_participants": 20,
      "participants": []
   },
   "Photography Club": {
      "description": "Learn photography techniques and digital editing",
      "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
      "max_participants": 18,
      "participants": []
   },
   "Robotics Club": {
      "description": "Build and program robots for competitions",
      "schedule": "Mondays and Wednesdays, 4:00 PM - 6:00 PM",
      "max_participants": 15,
      "participants": []
   },
   "Math Team": {
      "description": "Solve challenging math problems and compete in competitions",
      "schedule": "Thursdays, 4:00 PM - 5:30 PM",
      "max_participants": 14,
      "participants": []
   },
   "Tennis Team": {
      "description": "Tennis training and competitive matches",
      "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
      "max_participants": 12,
      "participants": []
   },
   "Track and Field": {
      "description": "Sprint, distance, and field events training",
      "schedule": "Tuesdays and Thursdays, 3:30 PM - 5:00 PM",
      "max_participants": 25,
      "participants": []
   },
   "Sculpture Club": {
      "description": "Create three-dimensional art with various materials",
      "schedule": "Fridays, 3:30 PM - 5:00 PM",
      "max_participants": 12,
      "participants": []
   },
   "Film Club": {
      "description": "Analyze and discuss films, create short video projects",
      "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
      "max_participants": 18,
      "participants": []
   },
   "History Club": {
      "description": "Explore historical events and complete research projects",
      "schedule": "Mondays, 3:30 PM - 5:00 PM",
      "max_participants": 20,
      "participants": []
   },
   "Literature Club": {
      "description": "Read and discuss classic and contemporary literature",
      "schedule": "Fridays, 4:00 PM - 5:30 PM",
      "max_participants": 15,
      "participants": []
   },
   "Baseball Team": {
      "description": "Competitive baseball training, practice, and games",
      "schedule": "Tuesdays, Thursdays, and Saturdays, 4:00 PM - 6:00 PM",
      "max_participants": 16,
      "participants": []
   },
   "Cross Country": {
      "description": "Long-distance running team and endurance training",
      "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
      "max_participants": 20,
      "participants": []
   },
   "Dance Club": {
      "description": "Learn various dance styles and perform in shows",
      "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
      "max_participants": 25,
      "participants": []
   },
   "Graphic Design Club": {
      "description": "Create digital art, logos, and visual designs",
      "schedule": "Mondays, 4:00 PM - 5:30 PM",
      "max_participants": 14,
      "participants": []
   },
   "Philosophy Club": {
      "description": "Explore philosophical ideas and ethical discussions",
      "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
      "max_participants": 16,
      "participants": []
   },
   "Coding Competition Team": {
      "description": "Prepare for programming contests and coding challenges",
      "schedule": "Thursdays, 4:00 PM - 5:30 PM",
      "max_participants": 12,
      "participants": []
   }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]
# Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str):
    """Unregister a student from an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]
    
    # Check if student is signed up
    if email not in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student not signed up for this activity")
    
    # Remove student
    activity["participants"].remove(email)
    return {"message": f"Unregistered {email} from {activity_name}"}
