from apps.home import blueprint

# Note you added session, redirect, url_for in purpose of the allquizes
from flask import render_template, request, flash, session, redirect, url_for   

from flask_login import login_required
from jinja2 import TemplateNotFound


import sqlite3



@blueprint.route('/index')
def index():
    return render_template('landing/landing.html', segment='index')

@blueprint.route('/dashboard')
@login_required
def dashboard():
    return render_template('home/home_page.html')

@blueprint.route('/admin')
@login_required
def admin():
    con = sqlite3.connect("apps/db.sqlite3")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Users")  
    rows = cur.fetchall()   
    return render_template('landing/admin_landing.html',rows = rows)

import pickle
@blueprint.route("/predict", methods = ['POST', 'GET'])
@login_required
def predict():
    output=""
    coursepredict =""
    id = current_user.username
    LR = "Logical_ReasoningScore"
    RC = "Reading_ComprehensionScore"
    NumA = "Numerical_AbilityScore"
    VA = "Verbal_AnalogyScore"
    LP = "Language_ProfeciencyScore"
    GI = "General_InformationScore"
    Math = "MathematicsScore"

    con = sqlite3.connect("apps/db.sqlite3")
    cur = con.cursor()
    query = "SELECT * FROM {} WHERE id = ?".format(LR)
    cur.execute(query, (id,))
    LRrow = cur.fetchone()
    query = "SELECT * FROM {} WHERE id = ?".format(RC)
    cur.execute(query, (id,))
    RCrow = cur.fetchone()
    query = "SELECT * FROM {} WHERE id = ?".format(NumA)
    cur.execute(query, (id,))
    NumArow = cur.fetchone()
    query = "SELECT * FROM {} WHERE id = ?".format(VA)
    cur.execute(query, (id,))
    VArow = cur.fetchone()
    query = "SELECT * FROM {} WHERE id = ?".format(LP)
    cur.execute(query, (id,))
    LProw = cur.fetchone()
    query = "SELECT * FROM {} WHERE id = ?".format(GI)
    cur.execute(query, (id,))
    GIrow = cur.fetchone()
    query = "SELECT * FROM {} WHERE id = ?".format(Math)
    cur.execute(query, (id,))
    Mathrow = cur.fetchone()
    if LRrow is None:
        return redirect(url_for("home_blueprint.allQuizes"))
    elif RCrow is None:
        return redirect(url_for("home_blueprint.allQuizes"))
    elif NumArow is None:
        return redirect(url_for("home_blueprint.allQuizes"))
    elif VArow is None:
        return redirect(url_for("home_blueprint.allQuizes"))
    elif LProw is None:
        return redirect(url_for("home_blueprint.allQuizes"))
    elif GIrow is None:
        return redirect(url_for("home_blueprint.allQuizes"))
    elif Mathrow is None:
        return redirect(url_for("home_blueprint.allQuizes"))
    else:
        Examscore = LRrow[1] + RCrow[1] + NumArow[1] + VArow[1] + LProw[1] + GIrow[1] + Mathrow[1]
        Compute = (((LRrow[1] + RCrow[1] + NumArow[1] + VArow[1] + LProw[1] + GIrow[1] + Mathrow[1])/155)*100)
        cur.close()
        model = pickle.load(open("mlinearmodel.pkl", "rb"))
            # Percentage = float(request.form["Percentage"])
        prediction = model.predict([[Compute]])
        output = round(prediction[0])
        
        if output<=1:
            coursepredict="Bachelor in Elementary Education Major in Special Education (BEED)"
        elif output==2:
            coursepredict="Bachelor in Secondary Education Major in Values Education (BSED)"
        elif output==3:
            coursepredict="Bachelor of Science in Sports Science"
        elif output==4:
            coursepredict="Bachelor of Science in Speech-Language Pathology"
        elif output==5:
            coursepredict="Bachelor of Science in Office Administration (BSOA)"
        elif output==6:
            coursepredict="Bachelor in Secondary Education Major in Technology and Livelihood Education (BSED)"
        elif output==7:
            coursepredict="Bachelor of Science in Social Work (BS Social Work)"
        elif output==8:
            coursepredict="Bachelor in Elementary Education (BEED)"
        elif output==9:
            coursepredict="Bachelor in Secondary Education (BSED)"
        elif output==10:
            coursepredict="Bachelor of Science in Food Technology (BS Food Tech)"
        elif output==11:
            coursepredict="Bachelor of Arts in Filipino (AB Filipino)"
        elif output==12:
            coursepredict="Bachelor of Physical Education (BPE)"
        elif output==13:
            coursepredict="Bachelor of Science in Public Safety (BSPS)"
        elif output==14:
            coursepredict="Bachelor in Secondary Education Major in Islamic Studies (BSED)"
        elif output==15:
            coursepredict="Bachelor in Secondary Education Major in Physical Sciences (BSED)"
        elif output==16:
            coursepredict="Bachelor in Secondary Education Major in Filipino (BSED)"
        elif output==17:
            coursepredict="Bachelor of Science in Entrepreneurship (BS Entrep)"
        elif output==18:
            coursepredict="Bachelor in Secondary Education Major in Music, Arts, Physical and Health Education (BSED)"
        elif output==19:
            coursepredict="Bachelor in Elementary Education Major in Preschool Education (BEED)"
        elif output==20:
            coursepredict="Bachelor of Science in Community Development(BS Community Development)"
        elif output==21:
            coursepredict="Bachelor in Elementary Education Major in Special Education (BEED)"
        elif output==22:
            coursepredict="Bachelor in Secondary Education Major in Values Education (BSED)"
        elif output==23:
            coursepredict="Bachelor of Science in Sports Science"
        elif output==24:
            coursepredict="Bachelor of Science in Speech-Language Pathology"
        elif output==25:
            coursepredict="Bachelor of Science in Office Administration (BSOA)"
        elif output==26:
            coursepredict="Bachelor in Secondary Education Major in Technology and Livelihood Education (BSED)"
        elif output==27:
            coursepredict="Bachelor of Science in Social Work (BS Social Work)"
        elif output==28:
            coursepredict="Bachelor in Elementary Education (BEED)"
        elif output==29:
            coursepredict="Bachelor in Secondary Education (BSED)"
        elif output==30:
            coursepredict="Bachelor of Library and Information Science in the Philippines (BLIS)"
        elif output==31:
            coursepredict="Bachelor of Science in Marine Transportation (BSMT)"
        elif output==32:
            coursepredict="Bachelor in Secondary Education Major in English (BSED)"
        elif output==33:
            coursepredict="Bachelor of Science in Hotel and Restaurant Management (BS HRM)"
        elif output==34:
            coursepredict="Bachelor of Science in Business Administration Major in Operations Management (BSBA major in OM)"
        elif output==35:
            coursepredict="Bachelor of Science in Business Administration Major in Marketing Management (BSBA major in MM)"
        elif output==36:
            coursepredict="Bachelor of Science in Business Administration Major in Human Resource Development (BSBA major in HRDM)"
        elif output==37:
            coursepredict="Bachelor of Science in Business Administration Major in Financial Management (BSBA major in FM)"
        elif output==38:
            coursepredict="Bachelor of Science in Business Administration Major in Business Economics (BSBA)"
        elif output==39:
            coursepredict="Bachelor in Secondary Education Major in Mathematics (BSED)"
        elif output==40:
            coursepredict="Bachelor in Secondary Education Major in Social Studies (BSED)"
        elif output==41:
            coursepredict="Bachelor of Science in Tourism Management (BSTM)"
        elif output==42:
            coursepredict="Bachelor of Science in Accounting Technology (BSAcT)"
        elif output==43:
            coursepredict="Bachelor of Science in Interior Design (BS Interior Design)"
        elif output==44:
            coursepredict="Bachelor in Landscape Architecture (BLA)"
        elif output==45:
            coursepredict="Bachelor of Science in Agroforestry (BS Agroforestry)"
        elif output==46:
            coursepredict="Bachelor of Science in Agribusiness (BS Agribusiness)"
        elif output==47:
            coursepredict="Bachelor of Science in Agriculture"
        elif output==48:
            coursepredict="Bachelor of Science in Occupational Therapy (BSOT)"
        elif output==49:
            coursepredict="Bachelor of Science in Midwifery (BS Midwifery)"
        elif output==50:
            coursepredict="Bachelor of Science in Medical Technology (BS Med Tech)"
        elif output==51:
            coursepredict="Bachelor of Science in Business Administration"
        elif output==52:
            coursepredict="Bachelor of Science in Real Estate Management (BS REM)"
        elif output==53:
            coursepredict="Bachelor of Science in Respiratory Therapy (BSRT)"
        elif output==54:
            coursepredict="Bachelor of Science in Radiologic Technology (BS Rad Tech)"
        elif output==55:
            coursepredict="Bachelor of Science in Physical Therapy (BSPT)"
        elif output==56:
            coursepredict="Bachelor of Arts in Literature (AB Literature)"
        elif output==57:
            coursepredict="Bachelor of Science in Information Systems (BSIS)"
        elif output==58:
            coursepredict="Bachelor of Science in Mathematics (BS Mathematics)"
        elif output==59:
            coursepredict="Bachelor of Science in Foreign Service (BS Foreign Service)"
        elif output==60:
            coursepredict="Bachelor of Science in Customs Administration (BSCA)"
        elif output==61:
            coursepredict="Bachelor of Science in Nutrition and Dietetics (BS Nutrition and Dietetics)"
        elif output==62:
            coursepredict="Bachelor of Science in Geology (BS Geology)"
        elif output==63:
            coursepredict="Bachelor of Arts in Sociology (AB Sociology)"
        elif output==64:
            coursepredict="Bachelor of Science in Biology (BS Biology)"
        elif output==65:
            coursepredict="Bachelor of Arts in Anthropology (AB Anthropology)"
        elif output==66:
            coursepredict="Bachelor of Fine Arts Major in Visual Communication (BFA)"
        elif output==67:
            coursepredict="Bachelor of Fine Arts Major in Sculpture (BFA)"
        elif output==68:
            coursepredict="Bachelor of Fine Arts Major in Painting (BFA)"
        elif output==69:
            coursepredict="Bachelor of Fine Arts Major in Industrial Design (BFA)"
        elif output==70:
            coursepredict="Bachelor of Arts in History (AB History)"
        elif output==71:
            coursepredict="Bachelor of Science in Information Technology"
        elif output==72:
            coursepredict="Bachelor of Arts in Psychology (AB Psychology)"
        elif output==73:
            coursepredict="BS in Business Administration major in Financial Management"
        elif output==74:
            coursepredict="Bachelor of Science in Economics (BS Economics)"
        elif output==75:
            coursepredict="Bachelor of Science in Nursing (BSN)"
        elif output==76:
            coursepredict="Bachelor of Arts in Mass Communication"
        elif output==77:
            coursepredict="Bachelor of Arts in Journalism (AB Journalism)"
        elif output==78:
            coursepredict="Bachelor of Science in Statistics (BS Stat)"
        elif output==79:
            coursepredict="Bachelor of Science in Criminology (BS Criminology)"
        elif output==80:
            coursepredict="Bachelor of Arts in Political Science (AB Political Science)"
        elif output==81:
            coursepredict="Bachelor of Science in Pharmacy (BS Pharmacy)"
        elif output==82:
            coursepredict="Bachelor of Science in Applied Mathematics (BS Applied Math)"
        elif output==83:
            coursepredict="Bachelor of Arts in Philosophy (AB Philosophy)"
        elif output==84:
            coursepredict="Bachelor of Science in Physics (BS Physics)"
        elif output==85:
            coursepredict="Bachelor of Science in Marine Engineering in (BSMarE)"
        elif output==86:
            coursepredict="Bachelor of Science in Industrial Engineering (BSIE)"
        elif output==87:
            coursepredict="Bachelor of Science in Materials Engineering (BSMatE)"
        elif output==88:
            coursepredict="Bachelor of Science in Sanitary Engineering (BSSE)"
        elif output==89:
            coursepredict="Master of Science in Bioethics"
        elif output==90:
            coursepredict="Master of Science in Clinical Medicine"
        elif output==91:
            coursepredict="Master of Science in Clinical Epidemiology"
        elif output==92:
            coursepredict="Bachelor of Science Basic Medical Sciences"
        elif output==93:
            coursepredict="Bachelor of Science in Mining Engineering (BSEM)"
        elif output==94:
            coursepredict="Bachelor of Science in Metallurgical Engineering (BSMetE)"
        elif output==95:
            coursepredict="Bachelor of Science in Applied Physics (BS Applied Physics)"
        elif output==96:
            coursepredict="Bachelor of Science in Architecture (BS Architecture)"
        elif output==97:
            coursepredict="Bachelor of Science in Petroleum Engineering (BSPetE)"
        elif output==98:
            coursepredict="Bachelor of Science in Mechanical Engineering (BSME)"
        elif output==99:
            coursepredict="Bachelor of Science in Geological Engineering (BSGeoE)"
        elif output==100:
            coursepredict="Bachelor of Science in Geodetic Engineering (BSGE)"
        elif output==101:
            coursepredict="Bachelor of Science in Electronics and Communications Engineering (BSECE)"
        elif output==102:
            coursepredict="Doctor of Medicine."
        elif output==103:
            coursepredict="Bachelor of Science in Computer Science"
        elif output==104:
            coursepredict="Bachelor of Science in Computer Engineering (BSCpE)"
        elif output==105:
            coursepredict="Bachelor of Science in Civil Engineering (BSCE)"
        elif output==106:
            coursepredict="Bachelor of Science in Accountancy (BSA)"
        elif output==107:
            coursepredict="Bachelor of Science in Electrical Engineering (BSEE)"
        elif output==108:
            coursepredict="Master of Science in Biochemistry."
        elif output==109:
            coursepredict="Bachelor of Science in Molecular Biology (BS Molecular Biology)"
        elif output==110:
            coursepredict="Bachelor of Science in Chemical Engineering (BSChE)"
        elif output==111:   
            coursepredict="Bachelor of Science in Management Engineering (BS ME)"
        elif output>=112:
            coursepredict="Bachelor of Science in Chemistry (BS Chemistry)"
        else:
            coursepredict = output
        return render_template("home/Exam/display_name.html",LRscore = LRrow[1], TheScore= Examscore, RCscore = RCrow[1], Average = Compute, prediction_text="{}" .format(coursepredict))

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None

@blueprint.route("/view")  
def view():  
    con = sqlite3.connect("apps/db.sqlite3")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Users")  
    rows = cur.fetchall()  
    return render_template("home/show_all.html",rows = rows)  

from flask_login import current_user
@blueprint.route('/allExam', methods = ["GET", "POST"])
@login_required
def allQuizes():
    id= current_user.username
    email=current_user.email
    return render_template('home/AllExam.html', name = id, mail=email)

@blueprint.route('/check')
@login_required
def check():  
    id = current_user.username
    quizName = request.args.get("type")
    session["quizName"] = quizName
    attemptTable = quizName + "Attempted"	# concat "Attempted" word, because thats how I have named the table
    con = sqlite3.connect("apps/db.sqlite3")
    cur = con.cursor()
    query = "SELECT id FROM {} WHERE id = ?".format(attemptTable)
    cur.execute(query, (id,))
    row = cur.fetchone()
    cur.close()
	#Quiz not attempted
    if row is None:
        return redirect(url_for("home_blueprint.instructions"))
    else:
    	return redirect(url_for("home_blueprint.display"))


@blueprint.route('/instructions')
@login_required
def instructions():
    id = current_user.username
    return render_template('/home/Exam/instructions.html', quiz = session["quizName"], name = id )

@blueprint.route('/questions', methods = ["POST"])
@login_required
def questions():
    quizName = session["quizName"]
    con = sqlite3.connect("apps/db.sqlite3")
    cur = con.cursor()
    query = "SELECT * FROM {}".format(quizName)
    cur.execute(query)
    ques_opts = cur.fetchall()
    cur.close()
    return render_template("/home/Exam/questions.html", questions = ques_opts, quizName = quizName)


@blueprint.route('/calculate', methods = ["GET", "POST"])
def calculate():
    id = current_user.username
    attemptTable = session["quizName"] + "Attempted"
    scoreTable = session["quizName"] + "Score"
    userAnsTable = session["quizName"] + "UserAnswer"
    quiz = session["quizName"]
    con = sqlite3.connect("apps/db.sqlite3")
    cur = con.cursor()
    query = "SELECT answer FROM {}".format(quiz)
    cur.execute(query)
    rows = cur.fetchall()
    score = 0
    user = list()
        
    if quiz == "Aptitude":		#Apti has 10 questions 2 marks each
        score *= 2
    query = "INSERT INTO {} VALUES (?, ?)".format(attemptTable)
    cur.execute(query, (id, 1))

    Geninfo = "General_InformationUserAnswer"
    Math = "MathematicsUserAnswer"
    LangProf = "Language_ProfeciencyUserAnswer"
    NumAbility = "Numerical_AbilityUserAnswer"
    ReadCompre = "Reading_ComprehensionUserAnswer"
    verbAnal = "Verbal_AnalogyUserAnswer"
    Logreason = "Logical_ReasoningUserAnswer"

    if userAnsTable == Geninfo:
        for i in range(25):		# 25 questions
            user.append(request.form.get(str(i+1)))
            score += 1 if user[i] == rows[i][0] else 0
        query = "INSERT INTO {} VALUES (?, ?)".format(scoreTable)
        cur.execute(query, (id, score))
        query = "INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(userAnsTable)
        cur.execute(query, (id, user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9], user[10], user[11], user[12], user[13], user[14], user[15], user[16], user[17], user[18], user[19], user[20], user[21], user[22], user[23], user[24] ))
        con.commit()
        cur.close()

    elif userAnsTable == Math:
        for i in range(30):		# 30 questions
            user.append(request.form.get(str(i+1)))
            score += 1 if user[i] == rows[i][0] else 0
        query = "INSERT INTO {} VALUES (?, ?)".format(scoreTable)
        cur.execute(query, (id, score))
        query = "INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(userAnsTable)
        cur.execute(query, (id, user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9], user[10], user[11], user[12], user[13], user[14], user[15], user[16], user[17], user[18], user[19], user[20], user[21], user[22], user[23], user[24], user[25], user[26], user[27], user[28], user[29]))
        con.commit()
        cur.close()

    elif userAnsTable == LangProf:
        for i in range(30):		# 30 questions
            user.append(request.form.get(str(i+1)))
            score += 1 if user[i] == rows[i][0] else 0
        query = "INSERT INTO {} VALUES (?, ?)".format(scoreTable)
        cur.execute(query, (id, score))
        query = "INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(userAnsTable)
        cur.execute(query, (id, user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9], user[10], user[11], user[12], user[13], user[14], user[15], user[16], user[17], user[18], user[19], user[20], user[21], user[22], user[23], user[24], user[25], user[26], user[27], user[28], user[29]))
        con.commit()
        cur.close()

    elif userAnsTable == NumAbility:
        for i in range(20):		# 20 questions
            user.append(request.form.get(str(i+1)))
            score += 1 if user[i] == rows[i][0] else 0
        query = "INSERT INTO {} VALUES (?, ?)".format(scoreTable)
        cur.execute(query, (id, score))
        query = "INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(userAnsTable)
        cur.execute(query, (id, user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9], user[10], user[11], user[12], user[13], user[14], user[15], user[16], user[17], user[18], user[19]))
        con.commit()
        cur.close()

    elif userAnsTable == ReadCompre:
        for i in range(20):		# 20 questions
            user.append(request.form.get(str(i+1)))
            score += 1 if user[i] == rows[i][0] else 0
        query = "INSERT INTO {} VALUES (?, ?)".format(scoreTable)
        cur.execute(query, (id, score))
        query = "INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(userAnsTable)
        cur.execute(query, (id, user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9], user[10], user[11], user[12], user[13], user[14], user[15], user[16], user[17], user[18], user[19]))
        con.commit()
        cur.close()

    elif userAnsTable == verbAnal:
        for i in range(20):		# 20 questions
            user.append(request.form.get(str(i+1)))
            score += 1 if user[i] == rows[i][0] else 0
        query = "INSERT INTO {} VALUES (?, ?)".format(scoreTable)
        cur.execute(query, (id, score))
        query = "INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(userAnsTable)
        cur.execute(query, (id, user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9], user[10], user[11], user[12], user[13], user[14], user[15], user[16], user[17], user[18], user[19]))
        con.commit()
        cur.close()
    
    elif userAnsTable == Logreason:
        for i in range(10):		# 10 questions
            user.append(request.form.get(str(i+1)))
            score += 1 if user[i] == rows[i][0] else 0
        query = "INSERT INTO {} VALUES (?, ?)".format(scoreTable)
        cur.execute(query, (id, score))
        query = "INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(userAnsTable)
        cur.execute(query, (id, user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9]))
        con.commit()
        cur.close()

    return redirect(url_for("home_blueprint.display"))

@blueprint.route('/display', methods = ["GET", "POST"])
def display():
    id = current_user.username
    scoreTable = session["quizName"] + "Score"	# concat "Score" word because thats how I have named the table
    con = sqlite3.connect("apps/db.sqlite3")
    cur = con.cursor()
    query = "SELECT * FROM {} WHERE id = ?".format(scoreTable)
    cur.execute(query, (id,))
    row = cur.fetchone()
    query = "SELECT * FROM {} ORDER BY Score DESC, id".format(scoreTable)
    cur.execute(query)
    scores = cur.fetchall()
    cur.close()
    return render_template('/home/Exam/display.html', score = row[1], scores = scores)

@blueprint.route('/answers', methods = ["GET", "POST"])
def answers():
    id = current_user.username
    quiz = session["quizName"]
    userAnsTable = quiz + "UserAnswer"
    con = sqlite3.connect("apps/db.sqlite3")
    cur = con.cursor()
    query = "SELECT * FROM {}".format(quiz)
    cur.execute(query)
    ques_opts = cur.fetchall()
    query = "SELECT * FROM {} WHERE id = ?".format(userAnsTable)
    cur.execute(query, (id, ))
    userAns = cur.fetchone()
    cur.close()
    print(userAns)
    return render_template("/home/Exam/answers.html", quizName = quiz, questions = ques_opts, user_ans = userAns)

@blueprint.route('/display_score', methods = ["GET", "POST"])
def display_score():
    id = current_user.username
    LR = "Logical_ReasoningScore"
    RC = "Reading_ComprehensionScore"
    con = sqlite3.connect("apps/db.sqlite3")
    cur = con.cursor()
    query = "SELECT * FROM {} WHERE id = ?".format(LR)
    cur.execute(query, (id,))
    LRrow = cur.fetchone()
    query = "SELECT * FROM {} WHERE id = ?".format(RC)
    cur.execute(query, (id,))
    RCrow = cur.fetchone()
    query = "SELECT * FROM {} ORDER BY Score DESC, id".format(LR)
    Compute = LRrow[1] + RCrow[1] + 60
    cur.execute(query)
    scores = cur.fetchall()
    cur.close()
    return render_template('/home/prediction.html', Average = Compute, LRscore = LRrow[1], RCscore = RCrow[1], scores = scores)