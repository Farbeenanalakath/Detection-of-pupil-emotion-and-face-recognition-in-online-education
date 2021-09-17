import os
import pymysql
from flask import *
from werkzeug.utils import secure_filename
app=Flask(__name__)
app.secret_key="99"
con=pymysql.connect(host='localhost',port=3306,user='farbi',password='password',db='pupil_emotion')
cmd=con.cursor()
@app.route('/')
def main():
    return render_template('index.html')
@app.route('/log')
def log():
    return render_template('login.html')
@app.route('/logout')
def logout():
    # session.clear()
    return render_template('login.html')
@app.route('/login',methods=['get','post'])
def login():
    un=request.form['textfield']
    pwd=request.form['textfield3']
    cmd.execute("select * from login where username='"+un+"' and password='"+pwd+"'")
    result=cmd.fetchone()
    if result is None:
        return '''<Script> alert ("invalid");window.location="/"</Script>'''
    elif result[3]=='admin':
        session['lid']=result[0]
        return '''<Script> alert ("successful");window.location="/adminhome" </Script>'''
    elif result[3]=='staff':
        session['lid']=result[0]
        return '''<Script> alert ("successful");window.location="/staffhome" </Script>'''
    else:
        return '''<Script> alert ("invalid");window.location="/" </Script>'''
@app.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')
@app.route('/staffhome')
def staffhome():
    return render_template('staffhome.html')
@app.route('/course')
def course():
    cmd.execute("select * from course")
    s=cmd.fetchall()
    return render_template('course.html',val=s)
@app.route('/course1',methods=['post'])
def course1():
    return render_template('course1.html')
@app.route('/course2',methods=['post'])
def course2():
    crs=request.form['textfield']
    cmd.execute("INSERT INTO `course` VALUES(NULL,'"+crs+"')")
    con.commit()
    return '''<Script> alert ("successful");window.location="/course" </Script>'''
@app.route('/dlt')
def dlt():
    id=request.args.get('id')
    cmd.execute("delete from course where id='"+str(id)+"'")
    con.commit()
    return '''<Script> alert ("deleted");window.location="/course" </Script>'''
@app.route('/staff')
def staff():
    cmd.execute("select * from staff")
    s=cmd.fetchall()
    return render_template('staff.html',val=s)
@app.route('/staffreg',methods=['post'])
def staffreg():
    return render_template('staffreg.html')
@app.route('/staffreg1',methods=['post'])
def staffreg1():
    fn=request.form['fn']
    ln=request.form['ln']
    gen=request.form['r']
    img=request.files['pic']
    pic=secure_filename(img.filename)
    path=r"./static/staffpic"
    img.save(os.path.join(path,pic))
    plc=request.form['plc']
    post=request.form['post']
    pin=request.form['pin']
    qualif=request.form['q']
    exp=request.form['exp']
    em=request.form['em']
    phn=request.form['phn']
    un=request.form['un']
    pd=request.form['pwd']
    cmd.execute("INSERT INTO login VALUES(NULL,'"+un+"','"+pd+"','staff')")
    id=con.insert_id()
    cmd.execute("INSERT INTO `staff` VALUES(NULL,'"+str(id)+"','"+fn+"','"+ln+"','"+gen+"','"+pic+"','"+plc+"','"+post+"','"+pin+"','"+qualif+"','"+exp+"','"+em+"','"+phn+"')")
    con.commit()
    return '''<Script> alert ("successful");window.location="/staff" </Script>'''
@app.route('/dltstaff')
def dltstaff():
    id=request.args.get('id')
    cmd.execute("delete from login where id='"+str(id)+"'")
    cmd.execute("delete from staff where lid='"+str(id)+"'")
    con.commit()
    return '''<Script> alert ("deleted");window.location="/course" </Script>'''
@app.route('/student')
def student():
    cmd.execute("select student.*,course.course from student join course on student.course_id=course.id")
    s=cmd.fetchall()
    return render_template('students.html',val=s)
@app.route('/studreg',methods=['post'])
def studreg():
    cmd.execute("select * from course")
    s=cmd.fetchall()
    return render_template('studreg.html',val=s)
@app.route('/studreg1',methods=['post'])
def studreg1():
    fn=request.form['fn']
    ln=request.form['ln']
    age=request.form['age']
    gen=request.form['r']
    img=request.files['pic']
    pic=secure_filename(img.filename)
    path=r"./static/staffpic"
    img.save(os.path.join(path,pic))
    plc=request.form['plc']
    post=request.form['post']
    pin=request.form['pin']
    crs=request.form['select']
    sem=request.form['select2']
    em=request.form['em']
    phn=request.form['phn']
    un=request.form['un']
    pd=request.form['pwd']
    cmd.execute("INSERT INTO login VALUES(NULL,'"+un+"','"+pd+"','student')")
    id=con.insert_id()
    cmd.execute("INSERT INTO `student` VALUES(NULL,'"+str(id)+"','"+fn+"','"+ln+"','"+age+"','"+gen+"','"+pic+"','"+plc+"','"+post+"','"+pin+"','"+str(crs)+"','"+sem+"','"+em+"','"+phn+"')")
    con.commit()
    return '''<Script> alert("successful");window.location="/student" </Script>'''
@app.route('/dltstud')
def dltstud():
    id=request.args.get('id')
    cmd.execute("delete from login where id='"+str(id)+"'")
    cmd.execute("delete from student where lid='"+str(id)+"'")
    con.commit()
    return '''<Script> alert ("deleted");window.location="/student" </Script>'''
@app.route('/vvideo')
def vvideo():
    cmd.execute("select video.*,course.course from video join course on course.id=video.cid where video.staff_id='"+str(session['lid'])+"'")
    s=cmd.fetchall()
    return render_template('video.html',val=s)
@app.route('/viewstudemotion')
def viewstudemotion():
    cmd.execute("SELECT `student`.`fname`,`student`.`lname`,avg(emotion.rating) FROM `student` JOIN `emotion` ON `student`.`lid`=`emotion`.`userid` group by `student`.`fname`,`student`.`lname`,`student`.`lid`")
    s=cmd.fetchall()
    return render_template('viewemotion.html',val=s)


@app.route('/viewstudemotion1')
def viewstudemotion1():
    cmd.execute("SELECT `student`.`fname`,`student`.`lname`,avg(emotion.rating) FROM `student` JOIN `emotion` ON `student`.`lid`=`emotion`.`userid` group by `student`.`fname`,`student`.`lname`,`student`.`lid`")
    s=cmd.fetchall()
    return render_template('viewemotion1.html',val=s)

@app.route('/viewatt')
def viewatt():
    cmd.execute("select student.lid,student.fname,student.lname from student")
    s=cmd.fetchall()
    res=[]
    for i in s:
        row=[]
        print(i)
        row.append(i[1])
        row.append(i[2])
        cmd.execute("select distinct class_id from emotion where userid="+str(i[0]))
        ss=cmd.fetchall()
        cmd.execute("select distinct id from video")
        th=cmd.fetchall()
        att="No Attendance"
        if len(th)>0:
            att=(len(ss)/len(th))*100
        row.append(att)
        res.append(row)
    return render_template('viewettendance.html',val=res)

@app.route('/viewstudemotion2')
def viewstudemotion2():
    cmd.execute("SELECT `student`.`fname`,`student`.`lname`,avg(emotion.rating) FROM `student` JOIN `emotion` ON `student`.`lid`=`emotion`.`userid` group by `student`.`fname`,`student`.`lname`,`student`.`lid`")
    s=cmd.fetchall()
    return render_template('viewemotion2.html',val=s)
@app.route('/viewrating')
def viewrating():
    cmd.execute("SELECT `staff`.`fname`,`staff`.`lname`,AVG(`emotion`.`rating`) FROM `staff` JOIN `video` ON `staff`.`lid`=`video`.`staff_id` JOIN `emotion` ON `video`.`id`=`emotion`.`class_id` GROUP BY `staff`.`lid`,`staff`.`fname`,`staff`.`lname` ")
    s=cmd.fetchall()
    return render_template('vwrating.html',val=s)
@app.route('/viewrating1')
def viewrating1():
    cmd.execute("SELECT `staff`.`fname`,`staff`.`lname`,AVG(`emotion`.`rating`) FROM `staff` JOIN `video` ON `staff`.`lid`=`video`.`staff_id` JOIN `emotion` ON `video`.`id`=`emotion`.`class_id` GROUP BY `staff`.`lid`,`staff`.`fname`,`staff`.`lname` ")
    s=cmd.fetchall()
    return render_template('vwrating1.html',val=s)
@app.route('/video',methods=['post'])
def video():
    cmd.execute("select * from course")
    s=cmd.fetchall()
    return render_template('addvideo.html',val=s)
@app.route('/video1',methods=['post'])
def video1():
    cid=request.form['c']
    d=request.form['d']
    video=request.files['v']
    v=secure_filename(video.filename)
    vpath=r"./static/video"
    video.save(os.path.join(vpath,v))
    cmd.execute("INSERT INTO `video` VALUES(NULL,'"+str(session['lid'])+"','"+v+"',curdate(),'"+str(cid)+"','"+d+"')")
    con.commit()
    return '''<Script> alert ("success");window.location="/vvideo" </Script>'''
@app.route('/dltvd')
def dltvd():
    id=request.args.get('id')
    cmd.execute("delete from video where id='"+str(id)+"'")
    con.commit()
    return '''<Script> alert ("deleted");window.location="/vvideo" </Script>'''
def sent(rev,pid):
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    pstv=0
    ngtv=0
    ntl=0
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(rev)
    a = float(ss['pos'])
    b = float(ss['neg'])
    c = float(ss['neu'])
    rating = 2.5
    if (ss['neu'] > ss['pos'] and ss['neu'] > ss['neg']):
        pass
    if (ss['neg'] > ss['pos']):
        negva = 5 - (5 * ss['neg'])
        if negva > 2.5:
            negva = negva - 2.5
        rating = negva
    else:
        negva = 5 * ss['pos']
        if negva < 2.5:
            negva = negva + 2.5
        rating = negva
    cmd.execute("insert into `rating` VALUES(null,'"+pid+"','"+str(rating)+"')")
    con.commit()
    return "ol"

app.run(debug=True)