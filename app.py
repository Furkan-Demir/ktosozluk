import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL,MySQLdb
from werkzeug.utils import secure_filename
import datetime
import bcrypt
import pytz
import random

UPLOAD_FOLDER = 'D:\Araclar\Py\PyProjects\ktosozluk\static\image\pp'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pykto'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mysql = MySQL(app)


## yardim sayfasi yap
## indexi degistir yeni bir fikir bul- okul haberleri olmasin



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
#######################################################################

@app.route("/ayarlar/upload", methods=['GET', 'POST'])
def index():
    liste = ['fu', 'rk', 'an', 'de', 'mir', 'fx',]
    if request.method == 'POST':

        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            isimrandom = random.choice(liste) +str(random.randrange(1,399))
            sonisim = isimrandom + filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], sonisim))
            
            degist = mysql.connection.cursor()
            degist.execute("""UPDATE users SET pp = %s WHERE id = %s """,(sonisim ,session['id'],))
            mysql.connection.commit()
            degist.close()

            return redirect(url_for('ayarlar'))
    return redirect(url_for('ayarlar'))
    

#######################################################################

@app.route('/denetle', methods = ['POST'])
def denetle():
    if 'id' in session:
        bildirim = mysql.connection.commit()
        bildirim.execute("SELECT * from mesajlar WHERE msj_okunma = 0 and msj_to = %s",(session['id'],))
        bildirimler = bildirim.fetchall()
        bildirim.close()
        return render_template("sistem.html", bildirimler = bildirimler)


## veritabanini ac
@app.route('/yardim')
def yardim():
    if 'id' in session:
        yardim = mysql.connection.commit()
        yardim.execute("SELECT * from yardim ORDER BY yardim_id DESC LIMIT 15")
        yardimlar = yardim.fetchall()
        yardim.close()
        return render_template("yardim.html", yardimlar = yardimlar)
    else:
        return redirect(url_for('home'))

@app.route('/')
def home():
    haber = mysql.connection.cursor()
    haber.execute("SELECT * from haber Order By haber_id DESC LIMIT 3")
    haberler = haber.fetchall()
    haber.close()
    return render_template("anasayfa.html", haberler = haberler)

@app.route('/panel/anonim')
def panel():
    if 'id' in session:
        itiraf = mysql.connection.cursor()
        itiraf.execute("SELECT * from anonim WHERE onay = 0 Order By itiraf_id")
        itiraflar = itiraf.fetchall()
        itiraf.close()    
        rank = mysql.connection.cursor()
        rank.execute("SELECT * from anonim_mod where mod_uye = %s",(session['id'],))
        rankcek = rank.fetchone()
        rank.close()
        return render_template("panel.html", rankcek = rankcek, itiraflar = itiraflar)
    else:
        return redirect(url_for('home'))

@app.route('/panel/onay/<itirafid>', methods=['GET','POST'])
def onaylamak(itirafid):
    if 'id' in session:
        rank = mysql.connection.cursor()
        rank.execute("SELECT * from anonim_mod where mod_uye = %s",(session['id'],))
        rankcek = rank.fetchone()
        rank.close()

        if rankcek['mod_uye'] == session['id']:

            if request.method == 'GET':
                return redirect(url_for('panel'))

            elif request.method == 'POST':
                degist = mysql.connection.cursor()
                degist.execute("""UPDATE anonim SET onay = onay+1 WHERE itiraf_id = %s """,(itirafid,))
                mysql.connection.commit()
                degist.close()  
                return redirect(url_for('panel'))
        else:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

@app.route('/panel/sil/<itirafid>', methods=['GET','POST']) ## YAPILACAK
def silmek(itirafid):
    if 'id' in session:
        rank = mysql.connection.cursor()
        rank.execute("SELECT * from anonim_mod where mod_uye = %s",(session['id'],))
        rankcek = rank.fetchone()
        rank.close()

        if rankcek['mod_uye'] == session['id']:

            if request.method == 'GET':
                return redirect(url_for('panel'))

            elif request.method == 'POST':
                degist = mysql.connection.cursor()
                degist.execute("""UPDATE anonim SET onay = onay-1 WHERE itiraf_id = %s """,(itirafid,))
                mysql.connection.commit()
                degist.close()  
                return redirect(url_for('panel'))
        else:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

@app.route('/anonim', methods=['GET', 'POST'])
def anonim():
    if 'id' in session:
        if request.method == 'POST':
            itiraf = request.form['itiraf'] 
            rumuz = request.form['rumuz']    
            cinsiyet = request.form['cinsiyet']  
            now = datetime.datetime.now()
            asd = pytz.timezone('Asia/Istanbul')
            zamanin = now.astimezone(asd) 
            tarih = zamanin.strftime("%d-%m-%y ")
            testttx = mysql.connection.cursor()

            testttx.execute("""INSERT INTO anonim 
            (itiraf, rumuz, cinsiyet, tarih, from_uye) 
            VALUES (%s,%s,%s,%s,%s)""",(itiraf, rumuz, cinsiyet, tarih, session['id']))

            mysql.connection.commit()
            return redirect(url_for('anonim'))

        elif request.method == 'GET':
            itiraf = mysql.connection.cursor()
            itiraf.execute("SELECT * from anonim WHERE onay = 1 Order By itiraf_id DESC LIMIT 30")
            itiraflar = itiraf.fetchall()
            itiraf.close()    
            return render_template("itiraf.html", itiraflar = itiraflar)
    else:
        return redirect(url_for('home'))

@app.route('/anonim/sikayet/<getir>', methods=["GET","POST"])
def sikayet_anonim(getir):
    if 'id' in session:
        if request.method == 'POST':
            sikayet = mysql.connection.cursor()
            sikayet.execute("""UPDATE anonim SET rapor = rapor+1 WHERE itiraf_id = %s """,(getir,))
            mysql.connection.commit()
            sikayet.close()
            return redirect(url_for('anonim'))
        else:
            return redirect(url_for('anonim'))
            

@app.route('/arama/baslik', methods=["GET","POST"])
def baslik_ara():
    if 'id' in session:
        if request.method == 'GET':
            return render_template("arama.html", kelime = "Başlık Arayın" , yontem = "baslikbulsana", urlbu = "/arama/baslik")

        elif request.method == 'POST':
            baslikara = request.form['baslikbulsana']
            aramabaslik = mysql.connection.cursor()
            aramabaslik.execute("SELECT * FROM baslik WHERE baslik_baslik LIKE %s",("%" + baslikara + "%",))
            cek = aramabaslik.fetchall()
            aramabaslik.close()

            return render_template("arama.html", cek = cek , kelime = "Başlık Arayın" , yontem = "baslikbulsana" , urlbu = "/arama/baslik" , baslikcek = "baslik_baslik")
    else:
        return redirect(url_for('home'))

@app.route('/arama/profil', methods=["GET","POST"])
def profilara():
    if 'id' in session:
        if request.method == 'GET':
        
            return render_template("arama.html", kelime = "Profil Arayın" , yontem = "nickara", urlbu = "/arama/profil")

        elif request.method == 'POST':
            nickara = request.form['nickara']
            nicaramalar = mysql.connection.cursor()
            nicaramalar.execute("SELECT * FROM users WHERE nick LIKE %s",("%" + nickara + "%",))
            cek = nicaramalar.fetchall()
            nicaramalar.close()

            return render_template("arama.html", cek = cek , kelime = "Profil Arayın" , yontem = "nickara", urlbu = "/arama/profil" , nick = "nick")
    else:
        return redirect(url_for('profilara'))

@app.route('/haber/<string:haber_id>')
def haber(haber_id):
    
    haber = mysql.connection.cursor()
    haber.execute("SELECT * from haber where haber_id = %s",(haber_id))
    habercek = haber.fetchone()
    haber.close()
    return render_template("haber.html", habercek = habercek)



@app.route('/ayarlar', methods=["GET","POST"])
def ayarlar():
    if 'id' in session:
        profil = mysql.connection.cursor()
        profil.execute("SELECT * from users where nick= %s",(session['nick'],))
        gel = profil.fetchone()
        profil.close()

        if request.method == 'GET':
            return render_template("ayarlar.html", gel = gel)
        elif request.method == 'POST':
            degis = mysql.connection.cursor()
            yeniad = request.form['name']
            idbul = request.form['id']
            if len(yeniad) > 3:  
                degis.execute("""UPDATE users SET name = %s WHERE id = %s""",(yeniad,idbul))
                mysql.connection.commit()
                return redirect(url_for('ayarlar'))
            else:
                return render_template("ayarlar.html")
    else:
        return redirect(url_for('home'))

@app.route('/ayarlar/sosyal', methods=["GET","POST"])
def ayarlarsosyal():
    if request.method == 'GET':
        return render_template("ayarlar.html")
    elif request.method == 'POST':
        degist = mysql.connection.cursor()
        idgetir = request.form['id']
        face = request.form['face']
        insta = request.form['insta']
        twitter = request.form['twitter']
 
        degist.execute("""UPDATE users SET face = %s , twitter = %s , insta = %s WHERE id = %s """,(face,twitter,insta,idgetir))
        mysql.connection.commit()
        degist.close()
        return redirect(url_for('ayarlar'))

@app.route('/ayarlar/bio', methods=["GET","POST"])
def ayarlarbio():
    if request.method == 'GET':
        return render_template("ayarlar.html")
    elif request.method == 'POST':
        degiste = mysql.connection.cursor()
        idgetir = request.form['id']
        bio = request.form['bio']
        degiste.execute("""UPDATE users SET bio = %s WHERE id = %s """,(bio,idgetir))
        mysql.connection.commit()
        degiste.close()
        return redirect(url_for('ayarlar'))

@app.route('/ayarlar/bolum', methods=["GET","POST"])
def ayarlarbolum():
    if request.method == 'GET':
        return render_template("ayarlar.html")
    elif request.method == 'POST':
        degister = mysql.connection.cursor()
        idgetir = request.form['id']
        bolum = request.form['bolum']
        degister.execute("""UPDATE users SET bolum = %s WHERE id = %s """,(bolum,idgetir))
        mysql.connection.commit()
        degister.close()
        return redirect(url_for('ayarlar'))



@app.route('/profilim')
def profil():
    if 'id' in session:
        profil = mysql.connection.cursor()
        heasb = mysql.connection.cursor()
        profil.execute("SELECT * from users where nick= %s",(session['nick'],))
        profilim = profil.fetchone()

        profil.execute("SELECT * from entry,baslik where baslik_id = entry_from_baslik and entry_from_uye = %s  order by entry_id desc limit 20",(session['id'],))
        entrylerim = profil.fetchall()

        heasb.execute("SELECT * from baslik where baslik.baslik_acan = %s  order by baslik.baslik_id DESC limit 5",(session['id'],))
        basliklarimicek = heasb.fetchall() 
        profil.close() 
        heasb.close()
        return render_template("profil.html", profilim = profilim , entrylerim = entrylerim , textprofil = "Entry'lerim" , basliklarimicek = basliklarimicek)
    else:
        return redirect(url_for('home'))

@app.route('/profil/<string:nick>')
def bulprofil(nick):
    if 'id' in session:
        profil = mysql.connection.cursor()
        profil.execute("SELECT * from users where nick= %s",(nick,))
        profilim = profil.fetchone()

        profil.execute("SELECT * from entry,baslik where baslik_id = entry_from_baslik and entry_from_uye = %s  order by entry_id desc ",(profilim['id'],))
        entrylerim = profil.fetchall()

        profil.close() 

        profil.close()    
        return render_template("profil.html", profilim = profilim , entrylerim = entrylerim , textprofil = "Entry'leri")
    else:
        return redirect(url_for('home'))

@app.route('/topluluk/<string:tp_id>')
def bultopluluk(tp_id):
    tp = mysql.connection.cursor()
    tp.execute("SELECT * from topluluk where tp_id= %s",(tp_id,))
    tpp = tp.fetchone()
    tp.execute("SELECT * from tp_haber where tp_from = %s order by tphaber_id desc",(tp_id,))
    tphaber = tp.fetchall()
    tp.execute("SELECT * from users,yetkiler where yetkiler.yetki_from_tp = %s and yetkiler.yetki_from_uye = users.id  order by yetkiler.yetki_from_rank desc ",(tp_id,))
    yetkilerr = tp.fetchall()

    if 'id' in session:
        now = datetime.datetime.now()
        asd = pytz.timezone('Asia/Istanbul')
        zamanin = now.astimezone(asd) 
        zamanx = zamanin.strftime("%d-%m-%y ")
        tp.execute("SELECT * from yetkiler where yetki_from_uye = %s and yetki_from_tp = %s",(session['id'],tp_id,))
        yetkicek = tp.fetchone()
        tp.close()
        return render_template("topluluk.html", tphaber = tphaber, tpp = tpp, yetkilerr = yetkilerr, yetkicek = yetkicek, tphaber_date = zamanx)

    tp.close()
    return render_template("toplulukidsiz.html", tphaber = tphaber, tpp = tpp, yetkilerr = yetkilerr)


@app.route('/tpost', methods=["GET","POST"]) # YAPILACAK
def toplulukhaberpost():

    if request.method == 'GET':

        return redirect(url_for('topluluklar'))

    elif request.method == 'POST':

        tphaber_date = request.form['tphaber_date'] 
        tp_from = request.form['tp_from']    
        tphaber_baslik = request.form['tp_baslik']  
        tphaber_aciklama = request.form['tp_aciklama']

        cur = mysql.connection.cursor()

        cur.execute("""INSERT INTO tp_haber 
        (tp_from, tphaber_baslik, tphaber_aciklama, tphaber_date) 
        VALUES (%s,%s,%s,%s)""",(tp_from, tphaber_baslik, tphaber_aciklama, tphaber_date,))

        mysql.connection.commit()
        return redirect(url_for('bultopluluk', tp_id = tp_from ))


@app.route('/gundem')
def gundem():
    gundem = mysql.connection.cursor()
    gundem.execute("SELECT * from baslik Order By baslik_puan DESC LIMIT 11")
    gundemler = gundem.fetchall()
    gundem.close()
    return render_template("gundem.html", gundemler = gundemler)

@app.route('/yeni')
def yenibasliklar():
    yeni = mysql.connection.cursor()
    yeni.execute("SELECT * from baslik Order By baslik_id DESC LIMIT 20")
    yeniler = yeni.fetchall()
    yeni.close()
    return render_template("yeni.html", yeniler = yeniler)

@app.route('/topluluklar')
def topluluklar():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from topluluk")
    topluluklar = cur.fetchall()
    cur.close()
    return render_template("topluluklar.html", topluluklar = topluluklar)

@app.route('/entry/<entry_id>')
def entry(id):
    return render_template("entry.html")

@app.route('/etkinlikler')
def event():
    return render_template("etkinlikler.html")

@app.route('/baslik/<baslik_id>', methods=['POST','GET'])
def yazdir(baslik_id):
    if request.method == 'POST':      
        now = datetime.datetime.now()
        tz = pytz.timezone('Asia/Istanbul')
        your_now = now.astimezone(tz)
        zaman = your_now.strftime("%H:%M %d-%m-%y ")
        entry_entry = request.form['entry_entry']
        entry_from_uye = session['id']
        cursor = mysql.connection.cursor()
        veri="INSERT INTO entry (entry_entry,entry_from_baslik,entry_from_uye,entry_date) VALUES(%s,%s,%s,%s)"
        cursor.execute(veri,(entry_entry,baslik_id,entry_from_uye,zaman,))
        artibir="UPDATE baslik SET baslik_puan = baslik_puan + 1 WHERE baslik_id = %s"
        cursor.execute(artibir,(baslik_id,))

        entry = mysql.connection.cursor()
        entry.execute("""SELECT * from entry where entry_from_baslik = %s """,(baslik_id,))
        entrysayx = entry.fetchall()
        entrysay = len(entrysayx)
        bol = entrysay / 10
        if int(bol) == float(bol):
            sayfala = "UPDATE baslik SET sayfa = %s WHERE baslik_id = %s"
            cursor.execute(sayfala,(bol,baslik_id,))
        else:
            sayfalaxx = int(bol) + 1
            sayfalat = "UPDATE baslik SET sayfa = %s WHERE baslik_id = %s"
            cursor.execute(sayfalat,(sayfalaxx,baslik_id,))           


        mysql.connection.commit()
        sayfaid = 1
        cursor.close()
        return redirect(url_for('baslik', baslik_id = baslik_id, sayfaid = sayfaid))
    else: 
        return redirect(url_for('baslik', baslik_id = baslik_id, sayfaid = 1))


@app.route('/baslik/<string:baslik_id>/<int:sayfaid>', methods=["GET"])
def baslik(baslik_id, sayfaid):
    if request.method == 'GET':
        hersy=10              # her sayfa
        startat = int(sayfaid) * hersy
        kalan = startat - 10
        i = 0
        listem = []
        if startat == 10:
            baslik = mysql.connection.cursor()
            baslik.execute("SELECT * from baslik where baslik_id = %s",(baslik_id,))
            baslikcek = baslik.fetchone()

            entry = mysql.connection.cursor()
            entry.execute("""SELECT * from entry,users where entry_from_baslik = %s and
            entry_from_uye = id ORDER BY entry_id ASC limit 0, 10 """,(baslik_id,))
            entrycek = entry.fetchall()

            while i < baslikcek['sayfa']:
                i = i + 1
                listem.append(i)


        else:
            baslik = mysql.connection.cursor()
            baslik.execute("SELECT * from baslik where baslik_id = %s",(baslik_id,))
            baslikcek = baslik.fetchone()
            entry = mysql.connection.cursor()
            entry.execute("""SELECT * from entry,users where entry_from_baslik = %s and
            entry_from_uye = id ORDER BY entry_id ASC limit %s, %s """,(baslik_id,kalan,hersy,))
            entrycek = entry.fetchall()
            while i < baslikcek['sayfa']:
                i = i + 1
                listem.append(i)

        baslik.close()
        entry.close()
        return render_template("baslik.html", baslikcek = baslikcek , entrycek = entrycek, baslik_id = baslik_id , sayfaid = sayfaid, listem = listem)



@app.route('/baslikac', methods=["GET", "POST"])
def baslikac():
    if 'id' in session:
        if request.method == 'GET':
            return render_template("baslikac.html")
        else:
            baslik_baslik = request.form['baslik_baslik']
            if len(baslik_baslik) > 3:
                baslik_baslik = request.form['baslik_baslik']
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO baslik (baslik_baslik, baslik_acan) VALUES (%s,%s)",(baslik_baslik,session['id']))
                mysql.connection.commit()
            else:
                return redirect(url_for('yenibasliklar'))
        return redirect(url_for('yenibasliklar'))
    else:
        return redirect(url_for('home'))
## Alt Taraf Register-Login Kismidir
@app.route('/kayit', methods=["GET", "POST"])
def register():
    if 'id' in session:
        return redirect(url_for('home'))
    else:
        if request.method == 'GET':
            return render_template("kayit.html")
        else:
            name = request.form['name']
            nick = request.form['nick']
            email = request.form['email']
            pp = "noprofile.jpg"
            password = request.form['password'].encode('utf-8')
            hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

            curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            say = curl.execute("SELECT nick,email FROM users WHERE nick=%s OR email=%s ",(nick,email,))
            curl.close()

            if say == 0:
                if len(nick) < 2:
                    return render_template("kayit.html", hata = "Kullanıcı Adınız 2 Karakterden Fazla Olmalıdır")
                else:
                    cur = mysql.connection.cursor()
                    cur.execute("INSERT INTO users (name, email, password, nick, pp) VALUES (%s,%s,%s,%s,%s)",(name,email,hash_password,nick,pp,))
                    mysql.connection.commit()
                    return redirect(url_for('login'))
            else:
                return render_template("kayit.html", hata = "Eposta veya Kullanıcı Adı kullanılıyor.")
                
@app.route('/giris',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        nick = request.form['nick']
        password = request.form['password'].encode('utf-8')

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        saydir = curl.execute("SELECT * FROM users WHERE nick=%s",(nick,))
        user = curl.fetchone()
        curl.close()
        if saydir == 1:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['nick'] = user['nick']
                session['email'] = user['email']
                session['name'] = user['name']
                session['id'] = user['id']
                return redirect(url_for('home'))
            else:
                bildirim = "Kullanıcı adı veya Şifre yanlış"
                return render_template("giris.html",bildirim = bildirim)
        else:
            return render_template("giris.html",bildirim = "Giriş Bilgileri Hatalı!")
    else:
            return render_template('giris.html')


@app.route('/admin')
def admin():
    return render_template("admin-index.html")

@app.route('/cikis')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(host='0.0.0.0',debug=False)


# @app.route('/baslik/<baslik_id>', methods=['POST','GET'])
# def yazdir(baslik_id):
#     if request.method == 'POST':      
#         now = datetime.datetime.now()
#         tz = pytz.timezone('Asia/Istanbul')
#         your_now = now.astimezone(tz)
#         zaman = your_now.strftime("%H:%M %d-%m-%y ")
#         entry_entry = request.form['entry_entry']
#         entry_from_uye = session['id']
#         cursor = mysql.connection.cursor()
#         veri="INSERT INTO entry (entry_entry,entry_from_baslik,entry_from_uye,entry_date) VALUES(%s,%s,%s,%s)"
#         cursor.execute(veri,(entry_entry,baslik_id,entry_from_uye,zaman,))
#         artibir="UPDATE baslik SET baslik_puan = baslik_puan + 1 WHERE baslik_id = %s"
#         cursor.execute(artibir,(baslik_id,))
#         mysql.connection.commit()
#         sayfaid = 1
#         return redirect(url_for('baslik', baslik_id = baslik_id, sayfaid = sayfaid))

#     else: 
#         return redirect(url_for('baslik', baslik_id = baslik_id, sayfaid = 1))


# @app.route('/baslik/<string:baslik_id>/<int:sayfaid>', methods=["GET"])
# def baslik(baslik_id, sayfaid):
#     if request.method == 'GET':
#         hersy=5              # her sayfa
#         startat=sayfaid*hersy
#         if startat == 5:
#             baslik = mysql.connection.cursor()
#             baslik.execute("SELECT * from baslik where baslik_id = %s",(baslik_id,))
#             baslikcek = baslik.fetchone()

#             entry = mysql.connection.cursor()
#             entry.execute("""SELECT * from entry,users where entry_from_baslik = %s and
#             entry_from_uye = id ORDER BY entry_id DESC limit 0, 10 """,(baslik_id,))
#             entrycek = entry.fetchall()

#         else:
#             baslik = mysql.connection.cursor()
#             baslik.execute("SELECT * from baslik where baslik_id = %s",(baslik_id,))
#             baslikcek = baslik.fetchone()
#             entry = mysql.connection.cursor()
#             entry.execute("""SELECT * from entry,users where entry_from_baslik = %s and
#             entry_from_uye = id ORDER BY entry_id DESC limit %s, %s """,(baslik_id,startat,hersy,))
#             entrycek = entry.fetchall()

#         baslik.close()
#         entry.close()
#         return render_template("baslik.html", baslikcek = baslikcek , entrycek = entrycek, baslik_id = baslik_id , sayfaid = sayfaid)
