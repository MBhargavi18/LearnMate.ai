# LearnMate.ai 🤖

**LearnMate.ai** is inspired by the challenges that students face while preparing for multiple exams across various subjects.
We recognized the need for a personalized, AI-driven solution that could help students to organize their study time efficiently,
taking into account their current knowledge level, preparation level and the time available before exams.
This also provides additional features like Resume Analysis and Quiz practices

## Demo
https://youtu.be/E4OwwxeHJ3Q

## Intro
**LearnMate.ai** is a revolutionary study planning tool that empowers students to achieve academic success. By inputting their subjects,
preparation levels, and exam dates, students can harness the power of Google's Gemini Al to receive personalized study resource
recommendations. The tool then generates a visually appealing and Interactive study schedule, complete with a variety of resources such
as videos, articles, and practice problems. To enhance engagement and understanding, study materials are presented in an engaging card format,
accompanied by informative Images and estimated completion times. Aso this integrates resume analyzer and quiz practice features.

## LearnMate.ai takes study planning to the next level. Here's how:
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
			
6) This provides Resume Analysis as an additional feature which is crucial to get
   shortlisted for the interviews. This also suggests **key skills lacking, resume
   improvement suggestions and learning resources.
			
7) In the Quiz Section, you can select the job role to practice the quiz and also select the difficulty level
	 With LearnMate.al, you get a study planning tool that's as powerful as it is user- friendly, empowering you to
   conquer your academic journey!

AWS Diagram:
![image](https://github.com/user-attachments/assets/bf5285c7-e13c-4ad5-93cb-e7ac2f2d786e)
The application has been deployed using Elastic BeansTalk using Docker image.
You can check out the link: learnmate-ai.us-east-1.elasticbeanstalk.com


## Getting Started
### Prerequisites
- Python 3.7+
- Streamlit
- Google Generative AI API access
- Docker
### API/Service Details
- Go to https://aistudio.google.com/app/apikey
- Create API key.
- Navigate to Google Cloud->Actvate your account->Under API & Services->Enable Generative Language API.
- Copy the API key in the application.


### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/anirudh-hegde/LearnMate.ai.git
   cd LearnMate.ai
   python3 -m venv venv
   pip install -r requirements.txt
2. Run the app:
   ```bash
   python3 -m streamlit run learnmate.py

 
Also you can checkout Docker image on DockeHub: [learnmate-ai](https://hub.docker.com/repository/docker/anirudh06/learnmate-ai/general)
## Conclusion
Congratulations! You have successfully run the application 🚀️.

To view the GolemAI app 👉 https://learnmate-ai.streamlit.app/
