import streamlit as st
from streamlit_option_menu import option_menu

col1, col2, col3, col4 = st.columns(4)
with col1 :
    st.markdown('''
            <div class='AnggotaHome'>Asharina Nova Fitriani 2219040</div>
            ''', unsafe_allow_html=True)
with col2 :
    st.markdown('''
            <div class='AnggotaHome'>Aruna Irani 2219039</div>
            ''', unsafe_allow_html=True)
with col3 :
    st.markdown('''
            <div class='AnggotaHome'>Windi Rifani Aisyah 2219182</div>
            ''', unsafe_allow_html=True)
with col4 :
    st.markdown('''
            <div class='AnggotaHome'>Ilham Maulana 2219084</div>
            ''', unsafe_allow_html=True)

st.markdown('''
            <div class='HeaderHome'>SELAMAT DATANG DI PERHITUNGAN FISIKA DASAR KINEMATIKA</div>
            <div class='WriteHome'>• Kinematika merupakan cabang Ilmu fisika yang membahas mengenai bagaimana benda bergerak.\n
• Kinematika membahas gerak benda tanpa mempelajari penyebab gerak tersebut.\n
• Kinematika merupakan dasar bagi banyak cabang fisika lainnya, seperti fluida, kalor, gelombang,
cahaya, dsb.\n
• Dalam Analisis Kimia, Kinematika dapat diaplikasikan secara tidak langsung melalui cabang Fisika lainnya. Misalnya, gerak gelombang cahaya
merupakan dasar dari spektrofotometri.\n
            ''', unsafe_allow_html=True)

option = st.selectbox(
    'Silahkan Pilih',
    ['SILAHKAN PILIH', 'Kecepatan', 'Percepatan', 'Gerak Lurus Beraturan (GLB)', 'Gerak Lurus Berubah Beraturan (GLBB)'])

if option == 'Kecepatan':
    st.write ('Kecepatan adalah besaran vektor menunjukkan perpindahan yang dapat dilakukan dalam tiap satuan waktu.\n')
    from PIL import Image
    image = Image.open('WhatsApp Image 2023-05-05 at 17.22.24.jpeg')
    st.image(image, caption='Rumus Kecepatan', width=175)
    #input jarak
    jarak= st.number_input('Masukkan jarak (s)')
    st.write(f'Bilangan pertama adalah {jarak}')
    #input waktu
    waktu= st.number_input('Masukkan waktu (t)')
    st.write(f'Bilangan pertama adalah {waktu}')
    #hitung
    if st.button('hitung'):
        hasil= jarak/waktu
        st.write(f'hasil kecepatan yang diperoleh adalah {hasil}')
    else:
        st.write('silahkan pencet tombol hitung!')
    

if option == 'Percepatan':
    st.write ('Didefinisikan sebagai perubahan kecepatan per satuan waktu.')
    from PIL import Image
    image = Image.open('WhatsApp Image 2023-05-05 at 16.58.57.jpeg')
    st.image(image, caption='Rumus Percepatan', width=110)

    #input delta kecepatan
    deltakecepatan= st.number_input('Masukkan delta kecepatan')
    st.write(f'Bilangan pertama adalah {deltakecepatan}')
    #input delta waktu
    deltawaktu= st.number_input('Masukkan delta waktu')
    st.write(f'Bilangan pertama adalah {deltawaktu}')
    #hitung
    if st.button('hitung'):
        hasilpercepatan= deltakecepatan/deltawaktu
        st.write(f'hasil percepatan yang diperoleh adalah {hasilpercepatan}')
    else:
        st.write('silahkan pencet tombol hitung!')


if option == 'Gerak Lurus Beraturan (GLB)':
    st.write ('Suatu benda disebut mengalami gerak lurus beraturan ketika lintasan geraknya berupa garis lurus dan kecepatannya tetap setiap saat.')
    from PIL import Image
    image = Image.open('WhatsApp Image 2023-05-05 at 17.32.32.jpeg')
    st.image(image, caption='Rumus Gerak Lurus Beraturan', width=175)
   
    #input kecepatan
    kecepatan= st.number_input('Masukkan kecepatan (v)')
    st.write(f'Bilangan pertama adalah {kecepatan}')
    #input waktu
    waktu= st.number_input('Masukkan waktu')
    st.write(f'Bilangan pertama adalah {waktu}')
    #hitung
    if st.button('hitung'):
        hasilkecepatan= kecepatan*waktu
        st.write(f'hasil jarak yang diperoleh adalah {hasilkecepatan}')
    else:
        st.write('silahkan pencet tombol hitung!')


if option == 'Gerak Lurus Berubah Beraturan (GLBB)':
    st.write ('Jika suatu benda bergerak dengan lintasan garis lurus, dan kecepatannya selalu berubah beraturan (percepatan konstan).')
    from PIL import Image
    image = Image.open('WhatsApp Image 2023-05-05 at 16.59.29.jpeg')
    st.image(image, caption='Rumus Gerak Lurus Berubah Beraturan', width=175)
    st.markdown('''
            <div class='Header'>MENGHITUNG KECEPATAN</div>
            ''', unsafe_allow_html=True)
    #input kecepatan awal
    kecepatanawal= st.number_input('Masukkan kecepatan awal')
    st.write(f'Bilangan pertama adalah {kecepatanawal}')
    #input percepatan
    percepatangerak= st.number_input('Masukkan percepatan (a)')
    st.write(f'Bilangan pertama adalah {percepatangerak}')
    #input waktu
    waktutempuh= st.number_input('Masukkan waktu (t)')
    st.write(f'Bilangan pertama adalah {waktutempuh}')
    #hitung
    if st.button('hitung'):
        hasilkecepatanawal= kecepatanawal+percepatangerak*waktutempuh
        st.write(f'hasil kecepatan akhir yang diperoleh adalah {hasilkecepatanawal}')
    else:
        st.write('silahkan pencet tombol hitung!')

    st.markdown('''
            <div class='Header'>MENGHITUNG JARAK</div>
            ''', unsafe_allow_html=True)
     #input kecepatan awal
    kecepatanawalv0= st.number_input('Masukkan kecepatan awal (v0)')
    st.write(f'Bilangan pertama adalah {kecepatanawalv0}')
    #input waktu
    waktujarak= st.number_input('Masukkan waktu (t)1')
    st.write(f'Bilangan pertama adalah {waktujarak}')
    #input 1/2 percepatan
    setengahpercepatan= st.number_input('Masukkan percepatan (a)-')
    st.write(f'Bilangan pertama adalah {setengahpercepatan}')
    #input waktu
    waktukuadrat= st.number_input('Masukkan waktu (t)2')
    st.write(f'Bilangan pertama adalah {waktukuadrat}')
    #hitung
    if st.button('hasil hitung'):
        hasiljarak= kecepatanawalv0*waktujarak + ((setengahpercepatan*waktukuadrat)/2)
        st.write(f'hasil kecepatan akhir yang diperoleh adalah {hasiljarak}')
    else:
        st.write('silahkan pencet tombol hitung!')
    
    st.markdown('''
            <div class='Header'>MENGHITUNG KECEPATAN AKHIR</div>
            ''', unsafe_allow_html=True)
    #input kecepatan awal
    kecepatanawalkuadrat= st.number_input('Masukkan kecepatan awal kuadrat')
    st.write(f'Bilangan pertama adalah {kecepatanawalkuadrat}')
    #input percepatan
    percepatanglbb= st.number_input('Masukkan percepatan')
    st.write(f'Bilangan pertama adalah {percepatanglbb}')
    #input jarak
    jaraktempuh= st.number_input('Masukkan jarak (s)')
    st.write(f'Bilangan pertama adalah {jaraktempuh}')
    #hitung
    if st.button('hitung '):
        hasilkecepatanawalkuadrat= ((kecepatanawalkuadrat)**2+(2*percepatanglbb*jaraktempuh))
        st.write(f'hasil kecepatan akhir yang diperoleh adalah {hasilkecepatanawalkuadrat}')
    else:
        st.write('silahkan pencet tombol hitung!')

st.markdown('''
            <style>
            .HeaderHome{
                font-family: Helvetica;
                font-size: 35px;
                font-weight: bold;
                text-align: center;
                margin-top: 100px;
                margin-bottom: 100px
            }
            .AnggotaHome{
                text-align: center;
                font-family: Helvetica;
                margin-top: 10px;
            }

            .Header{
                font-family: Helvetica;
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                margin-top: 50px;
                margin-bottom: 50px
            }
            </style>
            ''', unsafe_allow_html=True)