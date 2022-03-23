from IPython.display import HTML
from base64 import b64encode
import numpy as np
 
def show_video(video_path, video_width = 600):
   
  video_file = open(video_path, "r+b").read()
 
  video_url = f"data:video/mp4;base64,{b64encode(video_file).decode()}"
  return HTML(f"""<video width={video_width} controls><source src="{video_url}"></video>""")

def grader_01(X,y,theta,student_answer):
  error = False
  msg = "testing your answer..."
  
  sigm_teacher = lambda z: 1/(1+np.exp(-z))   
  h_teacher = sigm_teacher(np.dot(X,theta))
  
  for i in range(1):
  
   if student_answer.shape != h_teacher:
    error = True
    msg += "\n<font color='red'>INCORRECT DIMENSIONS<\font>: expected " + str(h_teacher.shape) + " but got: " + str(student_answer.shape)
    break
   
   if not np.allclose(h_teacher,student_answer):
    error = True
    msg += "\n<font color='red'>INCORRECT ANSWER<\font>: expected " + str(h_teacher) + "\n\nbut got:\n\n" + str(student_answer)
    
  if not error:
    msg += "\n\n\n<font color='green'><b>CORRECT! Congratulations</b><\font>"
  
  return HTML(msg)
   
  
  
