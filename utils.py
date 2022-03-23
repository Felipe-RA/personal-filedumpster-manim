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

    try:
        for i in range(1):

            if student_answer.shape != h_teacher.shape:
                error = True
                msg += "</br><br><font color='red'>INCORRECT DIMENSIONS</font><br> expected " + str(h_teacher.shape) + " but got: " + str(student_answer.shape)
                break

            np.testing.assert_allclose(h_teacher,student_answer)

            if not error:
                msg += "<br><br><br><font color='green'><b>CORRECT! Congratulations</b></font>"

    except AssertionError as e_1:
        msg += "<br><font color='red'>INCORRECT ANSWER</font>: expected <br>" + str(h_teacher) + "<br><br>but got:<br><br>" + str(student_answer)
    except Exception as e:
        msg += "<br><br> The following error was detected! Check your code: "
        msg += "<br><br>" +  "<font color='red'INCORRECT!> " + repr(e) + "</font>"
  
    return HTML(msg)
  
  
