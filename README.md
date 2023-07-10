# SocialSpectrum
An AI-powered education platform helping individuals with Autism Spectrum Disorder (ASD) master social interaction.<br><br>
SocialSpectrum provides a personalized, immersive learning experience that equips users with essential social skills, emotional understanding, and effective communication techniques.<br><br>
Through visual lessons, AI chat mentor, and adaptive quizzes, SocialSpectrum empowers individuals with ASD to confidently navigate social situations, interpret social cues, and develop a deeper understanding of emotions, all within a private, inclusive environment.<br>


## Steps to run the project locally:
1. Download my files (you can git clone it but normal download works just fine)<br><br>
2. Put your google .json file with the name "google.json" in the directory<br>(this is in the email or Check this out:
https://developers.google.com/workspace/guides/create-credentials#:~:text=your%20service%20account%3A-,In%20the%20Google%20Cloud%20console%2C%20go%20to%20Menu%20menu,IAM%20%26%20Admin%20%3E%20Service%20Accounts.&text=Select%20your%20service%20account.,Select%20JSON%2C%20then%20click%20Create.)<br><br>
3. Go to /website/Creator.py and in the vertexai.init(project="ghc-022", location="us-central1") change project to the project written in your .json file (Important!)<br><br>
4. Go to .env file and add your openai api key.<br><br>
5. Run app.py! (You need packages google-cloud-aiplatform, openai, flask)<br><br>

#### By The Cyber Savvy Ninjas - Google Cloud Vertex AI Hackathon - Summer 2023

