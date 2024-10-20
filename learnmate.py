import json
import re
from datetime import datetime
from io import BytesIO
from uuid import uuid4
from streamlit import button
from streamlit_card import card
import google.generativeai as genai
import requests
import streamlit as st
from PIL import Image
from streamlit_card import card
from streamlit_option_menu import option_menu

st.set_page_config(
	page_title="LearnMate.ai", page_icon="✧˖°📖🌐"
)

with st.sidebar:
	pages = option_menu("Navigate to",
						["Intro", "About", "Get started"])
API_KEY = st.sidebar.text_input(
	"Enter the Google Gemini api key (You can get or create gemini api key [here](https://makersuite.google.com/app/apikey)): ",
	type="password")

genai.configure(api_key=API_KEY)

def load_gemini_model():
	return genai.GenerativeModel('gemini-pro')


model = load_gemini_model()


def parse_duration(duration_str):
	match = re.search(r'\d+', duration_str)
	if match:
		return int(match.group())
	return 60



def get_gemini_ai_recommendations(subject, level, days_left):
	prompt = f"""
    Suggest 3 study resources for a student with the following criteria:
    - Subject: {subject}
    - Preparation level: {level}
    - Days left until exam: {days_left}

    Consider the time constraint and preparation level.
    If time is short, prioritize valid and available quick review materials.
    For longer time frames, suggest more available and accurate comprehensive resources.
    Please don't give unavailable resources appropriate (youtube videos, course, article)
    Use the following JSON format:
    [
        {{
            "title": "Resource Title",
            "type": "Resource Type (e.g., youtube video, course, article)",
            "duration": "Estimated study time in minutes (just the number)",
            "url": "URL of the resource",
            "image_url": "Url of an image representing the resource"
        }},
		{{
            // Second recommendation
        }},
        {{
            // Third recommendation
        }}
    ]
    """
	
	response = model.generate_content(prompt)
	
	try:
		recommendations = json.loads(response.text)
		for rec in recommendations:
			rec['duration'] = parse_duration(str(rec['duration']))
		return recommendations
	except json.JSONDecodeError:
		st.error("Failed to parse AI response. Please try again.")
		return []


def generate_study_schedule(subjects, levels, exam_dates):
	schedule = []
	start_date = datetime.now().date()
	
	for subject, level, exam_date in zip(subjects, levels, exam_dates):
		days_until_exam = (exam_date - start_date).days
		recommendations = get_gemini_ai_recommendations(subject, level, days_until_exam)
		for rec in recommendations:
			schedule.append({
				'subject': subject,
				'title': rec['title'],
				'duration': rec['duration'],
				'url': rec['url'],
				'image_url': rec['image_url'],
				'type': rec['type']
			})
			
	st.session_state['study_schedule'] = schedule
	return schedule
	
	# return schedule

def display_study_schedule(schedule):
    st.subheader("Your Study Schedule")
    cols = st.columns(3)
    for index, item in enumerate(schedule):
        with cols[index % 3]:
            icon = "📺" if item['type'].lower() == 'video' else "📄" if item['type'].lower() == 'article' else "🎓"
            card(
                title=f"{icon} {item['title']}",
                text=f"{item['duration']} minutes | {item['type']}",
                image=item['image_url'],
                url=item['url'],
                key=f"card_{index}_{item['title']}_{uuid4()}",  # Ensure the key is unique
                styles={"card": {"width": "100%", "height": "100%", "border-radius": "10px",
                                 "box-shadow": "0 0 10px rgba(0,0,0,0.1)"}}
            )
            with st.expander("More Info", expanded=False):
                st.write(f"Subject: {item['subject']}")
                st.write(f"Duration: {item['duration']} minutes")
                st.write(f"Type: {item['type']}")
                st.write(f"URL: {item['url']}")
				
# def get_image_from_url(url):
# 	try:
# 		response = requests.get(url)
# 		img = Image.open(BytesIO(response.content))
# 		# img = Image.open(BytesIO(response))
# 		return img
# 	except:
# 		return None


def main():
	if 'study_schedule' not in st.session_state:
		st.session_state['study_schedule'] = None
		
	if pages == "Intro":
		st.snow()
		st.title("LearnMate.ai: :rainbow[Study smarter with an AI study assistant]")
		
		st.subheader("Are you ready to elevate your "
					 "learning to the next level? Welcome to the "
					 "future of education with LearnMate.ai, your "
					 "personal AI learning buddy")
		
		st.write(
			"""
			**LearnMate.ai** is inspired by the challenges that students
			face while preparing for multiple exams across various subjects.
			We recognized the need for a personalized, AI-driven solution
			that could help students to organize their study time efficiently,
			taking into account their current knowledge level, preparation level
			and the time available before exams.
			"""
		)
	
	elif pages == "About":
		st.subheader("What it does?")
		st.write(
			"""
			**LearnMate.ai** is a revolutionary study planning tool that empowers
			students to achieve academic success. By inputting their subjects,
			preparation levels, and exam dates, students can harness the power
			of Google's Gemini Al to receive personalized study resource
			recommendations. The tool then generates a visually appealing and
			Interactive study schedule, complete with a variety of resources such
			as videos, articles, and practice problems. To enhance engagement and
			understanding, study materials are presented in an engaging card format,
			accompanied by informative Images and estimated completion times.
			Moreover, StudyAssistAl seamlessly Integrates with Google Calendar,
			providing students with a streamlined and efficient way to manage their
			academic commitments.
			"""
		)
		st.markdown(
			"""
			---
			"""
		)
		st.subheader("LearnMate.ai takes study planning to the next level. Here's how:")
		st.write(
			"""
			1) Seamless Al Integration: We leverage Google's powerful Gemini Al to analyze
			your inputs, creating a smooth and transparent bridge between user data and
			personalized recommendations.

			2) Intuitive Interface, Clear Information: Our user interface is designed with
			simplicity in mind. Even complex information is presented in a way that's easy
			to understand and navigate, keeping you focused on your goals.

			3) Relevant, Diverse Recommendations: LearnMate.al goes beyond the obvious.
			We ensure the Al recommendations are not only relevant to your learning style
			and needs but also diverse, offering a variety of resources to keep your studies engaging.

			4) Visually Appealing Cards: Forget boring text lists! LearnMate.al uses engaging card formats
			for study materials. These cards consistently display image URLS, providing a visually stimulating
			experience with estimated completion times for informed scheduling.

			5) Balance Is Key: We understand the importance of providing detailed information without overwhelming you.
			LearnMate.al offers a clean and uncluttered interface, striking the perfect balance between content richness
			and user experience.

			With LearnMate.al, you get a study planning tool that's as powerful as it is user- friendly, empowering you to
			conquer your academic journey!
			""")
	
	
	elif pages == "Get started":
		
		st.header("Get started")
		st.markdown(
			"""
			---
			"""
		)
		
		min_year = datetime(2021, 1, 1)
		max_year = datetime(2056, 12, 31)
		acdemic_year = st.date_input("Select the academic year", min_value=min_year, max_value=max_year)
		
		num_subjects = st.number_input("Number of subjects", min_value=1, max_value=10, value=3)
		subjects = []
		levels = []
		exam_dates = []
		
		for i in range(num_subjects):
			col1, col2, col3 = st.columns(3)
			with col1:
				subject = st.text_input(f"Subject {i + 1}")
				subjects.append(subject)
			with col2:
				level = st.selectbox(f"Preparation level for {subject}", ["bad", "good", "great"], key=f"level_{i}")
				levels.append(level)
			with col3:
				exam_date = st.date_input(f"Exam date for {subject}", key=f"exam_date_{i}")
				exam_dates.append(exam_date)
		
		if st.button("Find Study Resources"):
			if all(subjects) and all(exam_date > datetime.now().date() for exam_date in exam_dates):
				with st.spinner("Generating study schedule..."):
					schedule = generate_study_schedule(subjects, levels, exam_dates)
					# display_study_schedule(schedule)
			else:
				st.error("Please fill in all subjects and select future exam dates.")
		
		# Display the stored study schedule if it exists
		if st.session_state['study_schedule']:
			display_study_schedule(st.session_state['study_schedule'])
			
if __name__ == "__main__":
	main()
		# for i in range(num_subjects):
		# 	col1, col2, col3 = st.columns(3)
		# 	with col1:
		# 		subject = st.text_input(f"Subject {i + 1}")
		# 		subjects.append(subject)
		# 	with col2:
		# 		level = st.selectbox(f"Preparation level for {subject}", ["worst", "good", "great"], key=f"level_{i}")
		# 		prep_levels.append(level)
		# 	with col3:
		# 		exam_date = st.date_input(f"Exam date for {subject}", key=f"exam_date_{i}")
		# 		exam_dates.append(exam_date)
		#
		# if st.button("Find Resources to study"):
		# 	if all(subjects) and all(exam_date > datetime.now().date() for exam_date in exam_dates):
		# 		# if 'study_schedule' not in st.session_state:
		# 		# 	st.session_state.study_schedule = []
		# 		with st.spinner("Generating study schedule..."):
		# 			schedule = recommend_study_schedule(subjects, prep_levels, exam_dates)
		# 			display_study_schedule(schedule)
					# schedule = recommend_study_schedule(subjects, prep_levels, exam_dates)
					# st.session_state.study_schedule.extend(schedule)
					# recommend_study_schedule(schedule)
					
			# 		st.markdown(
			# 			"""
			# 			---
			# 			"""
			# 		)
			#
			# 		st.subheader("Your Study Schedule")
			#
			# 		cols = st.columns(3)
			#
			# 		for index, item in enumerate(schedule):
			#
			# 			with cols[index % 3]:
			# 				icon = "📺" if item['type'].lower() == 'video' else "📄" if item[
			# 																			  'type'].lower() == 'article' else "🎓"
			#
			# 				card(
			# 					title=f"{icon} {item['title']}",
			# 					text=f"{item['duration']} minutes | {item['type']}",
			# 					image=item['image_url'],
			# 					url=item['url'],
			# 					styles={
			# 						"card": {
			# 							"width": "100%",
			# 							"height": "100%",
			# 							"border-radius": "10px",
			# 							"box-shadow": "0 0 10px rgba(0,0,0,0.1)",
			# 						},
			# 						"filter": {
			# 							"background-color": "rgba(0,0,0,0.2)",
			# 						}
			# 					},
			# 					key=f"card_{index}"
			# 				)
			#
			# 				with st.expander("More Info"):
			# 					st.write(f"Subject: {item['subject']}")
			# 					st.write(f"Duration: {item['duration']} minutes")
			# 					st.write(f"Type: {item['type']}")
			# 					st.write(f"URL: {item['image']}")
			# else:
			# 	st.error("Please fill in all the subjects and also select future exam dates.")
		
		# if st.session_state['study_schedule']:
		# 	display_study_schedule(st.session_state['study_schedule'])
			


# AIzaSyCWUXHCAVRyuWsIAd338OZ6Q0ZplowFQG8
