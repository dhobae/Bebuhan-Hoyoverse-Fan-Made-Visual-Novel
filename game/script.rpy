define chr_1 = Character("Ayaka")
define chr_2 = Character("Aether")
define chr_3 = Character("Paimon")
define chr_4 = Character("????")

# ganti namanya kena
# $ chr_4 = Character("HOV !")


# image sumi = "Sumi/Smile.png"
image ayaka = "chara/Ayaka.png"
image ayaka_yandere = "chara/AyakaYandere.png"
image ayaka_sad = "chara/AyakaSad.png"

image aether = "chara/Aether.png"
image aether_kaget = "chara/AetherKaget.png"
image aether_tertusuk = "chara/AetherTertusuk.png"
image aether_true_power = "chara/AetherTruePower.png"
image aether_true_power2 = "chara/AetherTruePower2.png"

image paimon = "chara/Paimon.png"
image paimon_pingsan = "chara/PaimonPingsan.png"
image paimon_kaget = "chara/PaimonKaget.png"
image paimon_hov = im.Scale("chara/PaimonHov.png", config.screen_width, config.screen_height)

image hov = "chara/KianaHov.png"
image hov_bayangan = "chara/HovBayangan.png"
image hov_marah = "chara/HovMarah.jpg"

image latar_1 = im.Scale("bg/Latar_1.jpg", config.screen_width, config.screen_height)
image latar_1_dark = im.Scale("bg/Latar_1_Gelap.jpg", config.screen_width, config.screen_height)
image latar_2 = im.Scale("bg/Latar_2.png", config.screen_width, config.screen_height)
image latar_2_dark = im.Scale("bg/Latar_2_Gelap.png", config.screen_width, config.screen_height)
image latar_3 = im.Scale("bg/Latar_3.png", config.screen_width, config.screen_height)
image latar_3_dark = im.Scale("bg/Latar_3_Gelap.png", config.screen_width, config.screen_height)
image latar_4 = im.Scale("bg/Latar_4.png", config.screen_width, config.screen_height)
image latar_4_dark = im.Scale("bg/Latar_4_Gelap.png", config.screen_width, config.screen_height)
image latar_5 = im.Scale("bg/Latar_5.jpg", config.screen_width, config.screen_height)
image latar_5_dark = im.Scale("bg/Latar_5_Gelap.jpg", config.screen_width, config.screen_height)

# Definisi variabel untuk nama pemain
# default player_name = "Pemain"

# Label start menu
# label splashscreen:
#     scene black
#     with Pause(2.0)
    
#     show text "Tekan untuk Mulai" at truecenter
#     with dissolve
#     pause
#     hide text
#     with dissolve
    
#     # jump nama_input
#     jump start

label start:
    scene black
    with Pause(2.0)
    
    show text "Tekan untuk Mulai" at truecenter
    with dissolve
    pause
    hide text
    with dissolve
    
    jump start_game

# Label untuk input nama
# label nama_input:
#     scene black
#     python:
#         player_name = renpy.input("Siapa nama kamu?", length=32)
#         player_name = player_name.strip()
        
#         if not player_name:
#             player_name = "Player"
    
#     jump start

# Label utama game
label start_game:
    
    play music "audio/main/BaldrSkyOSTEasinessatTime.mp3" fadeout 1.0 fadein 3.0 loop

    scene latar_1_dark with dissolve
    pause(1.0)
    
    show text "Setelah berakhirnya pertarungan sengit Aether melawan Archon Inazuma yaitu Raiden Shogun, kedamaiannya akhirnya tiba" at truecenter with Dissolve(2.0)
    pause 6.0
    hide text with Dissolve(2.0)
    
    pause 1.0
    
    # Prolog bagian 2
    show text "Aether yang sedang berjalan-jalan di kota sambil bersiap menuju wilayah selanjutnya, ternyata menerima undangan untuk bertemu dengan Ayaka di kediamannya, Kamisato Yashiki" at truecenter with Dissolve(2.0)
    pause 8.0
    hide text with Dissolve(2.0)
    
    scene latar_2_dark with dissolve

    show text "Di Sore hari menjelang malam Aether menuju Kamisato Yashiki," at truecenter with Dissolve(2.0)
    pause 4.0
    hide text with Dissolve(2.0)
   
    show text "dan disambut hangat oleh ayaka di pintu depan" at truecenter with Dissolve(2.0)
    pause 4.0
    hide text with Dissolve(2.0)

    scene latar_3 with dissolve
 
    show ayaka:
        zoom 0.6
        yalign -1.0
        xalign 0.5 
    with dissolve
    
    pause 2.0  

    scene black with dissolve
    # 
    show text "Ayaka menyambut Aether yang datang bersama Paimon dengan senyum ceria" at truecenter with Dissolve(2.0)
    pause 5.0
    hide text with Dissolve(2.0)

    scene latar_3 with dissolve

    show ayaka at center:
        zoom 0.6
        yalign -1.0
        xalign 0.5 
    with dissolve

    chr_1 "Terima kasih sudah datang, Pengembara" with dissolve

    show ayaka at right:
        zoom 0.6
        yalign -1.0
        xalign 1.4
        xzoom -1
        ease 1.0
    with move

    show aether at left:
        zoom 0.3
        yalign -1.0
        xalign -0.3
    with dissolve

    show paimon at center: 
        zoom 0.3
        yalign 0.7
        xalign 0.3
    with dissolve

    chr_2 "Terima kasih telah mengundangku, Ayaka" with dissolve
    chr_3 "Ayaka, terima kasih telah mengundang kami." with dissolve

    pause(1.0)

    scene latar_3_dark with dissolve
    show text "Ayaka menyambut Aether yang datang bersama Paimon dengan senyum ceria" at truecenter with Dissolve(2.0)
    pause 3.0
    hide text with Dissolve(2.0)

    show text "Keduanya saling menyapa dan menatap satu sama lain. Lalu keduanya tersipu malu" at truecenter with Dissolve(2.0)
    pause 4.0
    hide text with Dissolve(2.0)

    show text "Paimon yang melihat hal ini merasa bingung dan akhirnya mengabaikan hal tersebut" at truecenter with Dissolve(2.0)
    pause 4.0
    hide text with Dissolve(2.0)

    scene latar_3 with dissolve

    show ayaka at right:
        zoom 0.6
        yalign -1.0
        xalign 1.4
        xzoom -1
        ease 1.0 

    show aether at left:
        zoom 0.3
        yalign -1.0
        xalign -0.3
    with dissolve

    show paimon at center: 
        zoom 0.3
        yalign 0.7
        xalign 0.3
    with dissolve

    pause(1.0)

    menu:
        "Kenapa kamu tiba-tiba mengundangku, Ayaka? Apa ada masalah?":
            jump rute_1
            
        "Kamu cuman sendirian saja saat ini, ayaka?":
            jump rute_2

label rute_1 :
    hide paimon
    hide aether 
    hide ayaka
    pause(0.5)

    show ayaka at center:
        zoom 0.6
        yalign -1.0
        xalign 0.5 
    with dissolve

    pause(1.0)
    hide ayaka

    show ayaka at center:
        zoom 0.6
        yalign -1.0
        xalign 0.5 
        xzoom -1
        ease 1.0
    with dissolve

    chr_1 "Aku cuman ingin mengobrol denganmu saja," with dissolve
    pause(0.5)

    chr_1 "terkait dengan masa depan Inazuma" with dissolve
    hide ayaka 

    pause(1.0)
    jump narator

label rute_2 :
    hide paimon
    hide aether 
    hide ayaka
    pause(0.5)

    show ayaka at center:
        zoom 0.6
        yalign -1.0
        xalign 0.5 
    with dissolve

    pause(1.0)
    hide ayaka

    show ayaka at center:
        zoom 0.6
        yalign -1.0
        xalign 0.5 
        xzoom -1
        ease 1.0
    with dissolve

    pause(0.5)

    chr_1 "Saat ini aku sedang sendirian saja," with dissolve
    pause(0.5)
    chr_1 "Kakak saat ini sedang sibuk dengan konflik-konflik yang tersisa dan tidak akan pulang dalam waktu yang lama" 
    with dissolve

    jump narator


label narator : 
    scene latar_3_dark

    show text "Ayaka mempersilahkan Aether dan Paimon untuk masuk ke dalam kediamanya" at truecenter with Dissolve(2.0)
    pause 4.0
    hide text with Dissolve(2.0)
    show text "Namun Ayaka tampak gelisah dan menyembunyikan sesuatu" at truecenter with Dissolve(2.0)
    pause 3.0
    hide text with Dissolve(2.0)
    scene latar_4_dark with dissolve

    show text "Ayaka dan Aether mulai berbincang lebih dalam, sementara paimon sedang asik memakan makanan yang sudah disiapkan oleh Ayaka" at truecenter with Dissolve(2.0)
    pause 7.0
    hide text with Dissolve(2.0)

    jump lanjut

label lanjut :
    scene latar_4 with dissolve

    menu:
        "Kamu terlihat gelisah, apa ada sesuatu yang kamu sembunyikan?":
            jump rute_1_section_2
            
        "Aku merasa kamu menyembunyikan sesuatu dariku":
            jump rute_2_section_2

label rute_1_section_2 :
    hide paimon
    hide aether 
    hide ayaka
    pause(0.5)

    show ayaka at center:
        zoom 0.6
        yalign -1.0
        xalign 0.5 
    with dissolve

    pause(1.0)
    hide ayaka

    show ayaka at center:
        zoom 0.6
        yalign -1.0
        xalign 0.5 
        xzoom -1
        ease 1.0
    with dissolve

    chr_1 "Pengembara, ada sesuatu yang harus kau tahu keluargaku…" with dissolve

    pause(0.5)

    jump lanjut_section_2

label rute_2_section_2 :
    hide paimon
    hide aether 
    hide ayaka
    pause(0.5)

    show ayaka at center:
        zoom 0.6
        yalign -1.0
        xalign 0.5 
    with dissolve

    pause(1.0)
    hide ayaka

    show ayaka at center:
        zoom 0.6
        yalign -1.0
        xalign 0.5 
        xzoom -1
        ease 1.0
    with dissolve

    chr_1 "…" with dissolve

    pause(0.5)

    chr_1 "Mungkin lebih baik kau tidak tau, Aether" with dissolve

    jump lanjut_section_2

label lanjut_section_2 :
    scene latar_4_dark with dissolve

    play music "audio/main/MorphogeneticLamentationZeroEscapeSymphony.mp3" fadeout 1.0 fadein 1.0 loop

    pause 2.0

    show text "Setelah menjawab hal tersebut , Ayaka bangkit dari tempat duduknya, dia tiba-tiba menangis dan matanya dipenuhi air mata" at truecenter with Dissolve(2.0)
    pause 5.0
    hide text with Dissolve(2.0)

    
    hide ayaka
    scene latar_4 with dissolve
    
    show ayaka_sad at center:
        zoom 0.6
        yalign -1.0
        xalign 0.5 
    with dissolve

    pause 2.0

    scene latar_4_dark

    show text "Tiba-tiba Ayaka, mengeluarkan pedang yang ada disampingnya" at truecenter with Dissolve(2.0)
    pause 3.0
    hide text with Dissolve(2.0)

    hide ayaka_sad with dissolve

    scene latar_4

    show ayaka_yandere at center:
        zoom 0.75
        yalign -0.3
        xalign 0.5 
    with dissolve

    pause 1.0
    hide ayaka_yandere

    show aether_kaget at center:
        zoom 0.4
        yalign -0.3
        xalign 0.5 
    with dissolve

    pause 3.0

    hide aether_kaget

    scene latar_4_dark

    
    show text "Aether yang kaget dengan hal tersebut tidak bisa melakukan pertahanan apapun, dan akhirnya tertusuk di bagian dada" at truecenter with Dissolve(2.0)
    $ renpy.music.set_volume(0.4, channel='music')  
    play sound "audio/sfx/suaratusukayaka.mp3" 
    $ renpy.music.set_volume(1.0, channel='music')  
    pause 5.0
    hide text with Dissolve(2.0)

    show paimon_pingsan:
        zoom 0.4
        yalign 0.5
        xalign 0.5
    with dissolve

    show text "Paimon juga tiba-tiba berteriak kesakitan setelah memakan makannya, dan akhirnya tidak sadarkan diri dengan mulut berbusa." at center:
        yalign 0.7
    with Dissolve(2.0)
    pause 5.0
    hide text with Dissolve(2.0)

    hide paimon_pingsan with dissolve

    pause 1.0

    show aether_tertusuk at left:
        zoom 0.35
        yalign -0.7
        xalign -0.15
    with dissolve

    show ayaka_sad at center:
        zoom 0.65
        yalign -1.2
        xalign 0.6
        xzoom -1
    with dissolve
    pause 1.0

    show aether_tertusuk at left:
        ease 0.2 zoom 0.35 yalign -0.5 xalign -0.1
    chr_2 "Ayaka, kenapa kau melakukan semua ini?!"
    show aether_tertusuk at left:
        ease 0.2 zoom 0.35 yalign -0.7 xalign -0.15

    show ayaka_sad at center:
        ease 0.2 xalign 0.5 yalign -0.8 zoom 0.65 xzoom -1
    chr_1 "Maaf Pengembara, Aku terpaksa melakukan ini demi keselamatan Inazuma"
    show ayaka_sad at center:
        ease 0.2 xalign 0.6 yalign -1.2 zoom 0.65 xzoom -1
    
    show aether_tertusuk at left:
        ease 0.2 zoom 0.35 yalign -0.5 xalign -0.1
    chr_2 "Kenapa dengan membunuhku dan Paimon bisa menyelamatkan Inazuma"
    show aether_tertusuk at left:
        ease 0.2 zoom 0.35 yalign -0.7 xalign -0.15

    show ayaka_sad at center:
        ease 0.2 xalign 0.5 yalign -0.8 zoom 0.65 xzoom -1
    chr_1 "Kami diperintahkan oleh orang itu untuk membunuhmu dan paimon, jika kami menolak maka semua orang di Inazuma akan dihabisi dan dikutuk menjadi Abyss"
    show ayaka_sad at center:
        ease 0.2 xalign 0.6 yalign -1.2 zoom 0.65 xzoom -1
    
    show aether_tertusuk at left:
        ease 0.2 zoom 0.35 yalign -0.5 xalign -0.1
    chr_2 "Jadi begitu ya, aku tidak menyangka mereka akan melakukannya dengan cara seperti ini"
    chr_2 "Maafkan Aku Ayaka, Seandainya aku menyadari ini lebih awal"
    show aether_tertusuk at left:
        ease 0.2 zoom 0.35 yalign -0.7 xalign -0.15

    show ayaka_sad at center:
        ease 0.2 xalign 0.5 yalign -0.8 zoom 0.65 xzoom -1
    chr_1 "...."
    show ayaka_sad at center:
        ease 0.2 xalign 0.6 yalign -1.2 zoom 0.65 xzoom -1

    hide ayaka_yandere with dissolve
    scene latar_4_dark
    
    show text "Paimon yang mulai kembali sadar, kaget melihat Aether yang ditusuk oleh Ayaka dan tidak sadarkan diri" at truecenter with Dissolve(2.0)
    pause 4.0
    hide text with Dissolve(2.0)

    show paimon_kaget at truecenter:
        zoom 1.3

    chr_3 "Uuhh…Ayaka…apa yang kau lakukan terhadap pengembara?"

    show ayaka_sad at right:
        zoom 0.6
        yalign -1.0
        xalign 1.25
        xzoom -1
        ease 1.0
    with dissolve

    show paimon_kaget at left:
        zoom 1.3
        yalign 0.7
    with move

    chr_1 "…….Maafkan aku, Paimon… aku tidak punya pilihan…, aku…"

    show ayaka_sad at right:
        zoom 0.6
        yalign -1.9
        xalign 1.4
        xzoom -1
        ease 1.0

   
    show paimon_kaget at left:
        zoom 1.3
        yalign 0.5

    chr_3 "Pengembara… dia selalu percaya padamu… pada semua orang di sini…"

    scene latar_5_dark

    show text "Dalam sekejap, suara gemuruh terdengar di luar Kamisato Yashiki. Angin dingin menusuk menyusup ke dalam ruangan, diiringi dengan bayangan gelap yang memanjang ke segala arah" at truecenter with Dissolve(2.0)
    pause 7.0
    hide text with Dissolve(2.0)

    scene latar_4_dark with dissolve
    play music "audio/main/GATEOFSTEINERMaintheme.mp3" fadeout 1.0 fadein 3.0 loop

    show text "Ayaka terhenti sejenak, wajahnya pucat ketika melihat sosok yang kini berdiri di belakangnya" at truecenter with Dissolve(2.0)
    pause 5.0
    hide text with Dissolve(2.0)

    scene latar_4

    

    show ayaka_sad at center:
        zoom 0.7
        xzoom -1
        yalign -0.8
        xalign 0.9
    with dissolve

    show hov_bayangan at right:
        xalign 1.0 yalign 1.2
    with dissolve

    show ayaka_sad at left:
        xzoom 1
        zoom 0.7
        yalign -0.8
        xalign -0.8
    with move

    pause 2.0

    show hov_bayangan at right:
        ease 0.2 yalign 1.0 xalign 0.9

    chr_4 "Kau benar-benar melakukannya, Kamisato Ayaka. Aku tidak menyangka akan semudah ini membuatmu tunduk"

    show hov_bayangan at right:
        xalign 1.0 yalign 1.2
    with dissolve

    pause 1.0

    scene latar_4_dark with dissolve

    show text "Dari kegelapan, muncul sosok misterius. Suaranya dingin, penuh otoritas" at truecenter with Dissolve(2.0)
    pause 4.0
    hide text with Dissolve(2.0)

    show text "Ayaka tersentak dan menatap sosok itu dengan amarah" at truecenter with Dissolve(2.0)
    pause 3.0
    hide text with Dissolve(2.0)

    scene latar_4 with dissolve

    show ayaka_sad at center:
        xzoom 1
        zoom 0.7
        yalign -0.8
        xalign -0.8
    with dissolve

    show hov_bayangan at right:
        xalign 1.0 yalign 1.2
    with dissolve

    show ayaka_sad at center:
        ease 0.5 zoom 0.7 yalign -0.6 xalign -0.6

    chr_1 "Kau…! Kau sudah berjanji akan menyelamatkan rakyat Inazuma jika aku melakukan ini! Jangan menyakitinya lebih dari ini!"

    show ayaka_sad at center:
        ease 0.5 zoom 0.7 yalign -0.8  xalign -0.8
        
       
    show hov_bayangan at right:
        ease 0.2 yalign 1.0 xalign 0.9
    chr_4 "Janji? Ayaka, aku hanya memastikan kau menyingkirkan ancaman terbesar kami. Lihatlah, pengembara itu bahkan tidak bisa melindungi dirinya sendiri. Betapa lemahnya dia tanpa Vision"
    show hov_bayangan at right:
        ease 0.3 xalign 1.0 yalign 1.2
   
    scene latar_4_dark

    show text "Paimon tampaknya mencoba melawan, ekspresinya sangat menakutkan dan menunjukan rasa kebencian yang begitu besar" at truecenter with Dissolve(2.0)
    pause 6.0
    hide text with Dissolve(2.0)
    
    pause 1.0

    scene paimon_hov with dissolve

    pause 3.0

    chr_3 "Aether tidak lemah… dia… dia akan bangkit… dan menghentikanmu!"

    scene hov_marah with dissolve

    pause 3.0

    chr_4 "Kamu sendiri, makhluk kecil yang menyedihkan. Kau bahkan menyembunyikan rahasiamu sendiri, bukan?"

    scene latar_4_dark

    show text "Ayaka, dengan tangan yang gemetar, mengarahkan pedangnya kembali ke sosok misterius itu" at truecenter with Dissolve(2.0)
    pause 3.0
    hide text with Dissolve(2.0)

    scene latar_4

    show ayaka_yandere at left:
        xzoom -1
        zoom 0.65
        yalign -0.9
        xalign -0.5
    with dissolve

    chr_1 "Aku tidak akan membiarkanmu menguasai Inazuma! Pengorbanan ini cukup…!"

    hide ayaka_yandere with dissolve

    scene latar_4_dark with dissolve
    
    show text "Namun, sebelum Ayaka bisa bergerak, sosok itu mengangkat tangannya, mengeluarkan kekuatan gelap yang memaksa Ayaka berlutut" at truecenter with Dissolve(2.0)
    pause 7.0
    hide text with Dissolve(2.0)

    show text "Aether, yang sebelumnya terlihat tak sadarkan diri, mulai menunjukkan tanda-tanda kehidupan. Energi samar bercahaya dari tubuhnya" at truecenter with Dissolve(2.0)
    pause 7.0
    hide text with Dissolve(2.0)

    scene latar_4 with dissolve

    show aether_true_power at center:
        zoom 0.45
        yalign 0.011
    with dissolve

    pause 2.0

    hide aether_true_power with dissolve

    show aether_true_power2 at left:
        zoom 0.35
        yalign -0.9 # to -0.8
        xalign -0.4 # to -0.3
    with dissolve 

    show hov at right with dissolve

    chr_4 "Apa ini…? Tidak mungkin dia masih bisa bangkit setelah serangan itu!"

    scene latar_4_dark with dissolve

    show text "Aether perlahan membuka matanya, menatap Ayaka yang menangis di hadapannya dan sosok misterius di hadapannya" at truecenter with Dissolve(2.0)
    pause 6.0
    hide text with Dissolve(2.0)

    scene latar_4 with dissolve

    show aether_true_power2 at left:
        zoom 0.35
        yalign -0.9 # to -0.8
        xalign -0.2 # to -0.3
    with dissolve 

    show aether_true_power2 at left:
        ease 0.3 zoom 0.35 yalign -0.8 xalign -0.1

    chr_2 "Ayaka… aku tahu kau tidak ingin melakukan ini. Percayakanlah semuanya padaku…"

    show aether_true_power2 at left:
        ease 0.3 zoom 0.35 yalign -0.9 xalign -0.2
 
    show ayaka_yandere at right:
        zoom 0.7
        yalign -0.9
        xalign 1.5
        xzoom -1
    with dissolve

    show ayaka_yandere at right:
        ease 0.2 zoom 0.8 yalign -0.4 xalign 1.9 xzoom -1

    chr_1 "……Pengembara…aku…."

    pause 2.0

    hide ayaka_yandere with dissolve

    show hov at right with dissolve

    show aether_true_power2 at left:
        ease 0.3 zoom 0.35 yalign -0.8 xalign -0.1

    chr_2 "Kegelapanmu tidak akan menguasai Inazuma… atau siapa pun di sini"

    chr_2 "Kau telah memanipulasi cukup banyak orang. Ini akan berakhir sekarang"
    show aether_true_power2 at left:
        ease 0.3 zoom 0.35 yalign -0.9 xalign -0.2

    show hov at right:
        zoom 1.2
    with dissolve

    chr_4 "Kau ingin melawanku, Pengembara? Dunia ini akan menjadi kuburanmu!"

    pause 1.0

    $ renpy.music.set_volume(0.3, channel='music') 

    scene black with dissolve

    show text "TO BE CONTINUED" at truecenter with dissolve
    pause 4.0
    hide text with dissolve

label end:
    pause 1.0

    # Menampilkan kredit dengan fade
    # window hide
    # show screen credits_screen with fade
    # $ renpy.pause(6.0)  # Durasi kredit muncul
    # hide screen credits_screen with fade

    # Pesan penutup
    show text "Terimakasih telah Memainkan Game Kami" with dissolve
    pause 4.0
    hide text with dissolve

    show text "Develop By : Ridho | Sayed" with dissolve
    pause 4.0
    hide text with dissolve

    return

# screen credits_screen:
#     frame:
#         xalign 0.5
#         yalign 0.5
#         background None

#         vbox:
#             spacing 15
#             align (0.5, 0.5)  # Teks tetap di tengah layar
#             text "Kredit Game" size 30 bold True
#             text "Deve Ridho" size 25
#             text "Musik: Ridho" size 25
#             text "Desain Karakter: Sayed" size 25
#             text "Naskah: Sayed" size 25
#             text "Terima kasih kepada semua yang telah mendukung!" size 25

