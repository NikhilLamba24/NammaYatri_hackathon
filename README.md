# NammaYatri_hackathon
<b>Main aim</b>:- <ins> booking a cab via just calling at a contact number</ins> , no need of opening their application or write down destination( but, just a simple call).  Can work well for firms like <b>Uber, Ola</b>, etc.
Submission in namma yatri hackathon, that includes:- <ins>Speech to text to database creation</ins> </br>
<b>Step1.)</b> Demonstration of voice call via <b><ins>twilio</ins></b> service that saves the voice( for demonstration purpose).</br>
<b>Step2.)</b> The voice so recorded passed to <b><ins>Whisper</ins></b>( OpenAI's model for speech to text).</br>
<b>Step3.)</b> Inside the output of text saved, it will search for 'to' keyword and saves the destination 'from' to 'to' in <b><ins>database</b></ins> for further processing of the task,i.e., to inform the nearest cab driver to reach that point.
