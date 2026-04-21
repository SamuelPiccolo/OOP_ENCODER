
"""
Encoder File 21/14/2026
Implementation of library and lists to be used
Class and function started
"""
# ============================================ #
# //             Module imports             // #
# ============================================ #

import sys
import os

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #

__author__ = "Samuel Piccolo", "Nicholas Constantin"
__copyright__ = "Copyright 2026, Samuel Piccolo & Nicholas Constantin"
__licence__ = "MIT"
__version__ = "1.2"


# ============================================ #
# //                Class                   // #
# ============================================ #

# -------------------------------------------- #
# //            class definitions           // #
# -------------------------------------------- #



class Encoder: 
    #Starting a list of characters
    Character = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Special_C = [" ", "1","2","3","4","5","6","7","8","9","0","!","?",">","<", ",", ".","@","£","$","%","^","~","&","*","(",")","_","-","+","=","/"]
    _char_index = {ch: i for i, ch in enumerate(Character)}
    images= (r"""
        A
                           AAAAABBBBBBBAAAAA
                      AAAAABBBBCCCCCCCCBBBBAAAAA
                 AAAAABBBCCCDDDEEEEEEEDDDCCBBBAAAAA
            AAAABBBCCCDDDEEEFFFFGGGGGGFFFFEEEDDDCCBBBAAA
        AAAABBBCCCDDDEEEFFFFGGGHHHHHHGGGFFFFEEEDDDCCBBBAAA
     AAABBBCCCDDDEEEFFFFGGGHHHIIIIIIIIHHHGGGFFFFEEEDDDCCBBBAA
   AABBBCCCDDDEEEFFFFGGGHHHIIJJJJJJJJJJIIHHHGGGFFFFEEEDDDCCBBAA
  ABBBCCCDDDEEEFFFFGGGHHHIIJJKKKKLLLLKKKKJJIIHHHGGGFFFFEEEDCCBBBA
 ABBCCCDDDEEEFFFFGGGHHHIIJJKKKLLLLMMMMLLLLKKKJJIIHHHGGGFFFFEEEDCCB
ABBCCCDDDEEEFFFFGGGHHHIIJJKKKLLLMMMMNNNNMMMMLLLKKKJJIIHHHGGGFFFFEE
BBCCCDDDEEEFFFFGGGHHHIIJJKKKLLLMMMNNNOOOONNNMMMKKKJJIIHHHGGGFFFFEE
BCCCDDDEEEFFFFGGGHHHIIJJKKKLLLMMMNNNNOOOOOONNNMMMKKKJJIIHHHGGGFFF
CCDDDEEEFFFFGGGHHHIIJJKKKLLLMMMNNNOOOOOOOOOONNNMMMKKKJJIIHHHGGGFF
DDDEEEFFFFGGGHHHIIJJKKKLLLMMMNNNOOOOPPPPPOOOONNNMMMKKKJJIIHHHGGG
EEEFFFFGGGHHHIIJJKKKLLLMMMNNNOOOOPPQQQQQQPPOOOONNNMMMKKKJJIIHHH
EEEFFFFGGGHHHIIJJKKKLLLMMMNNNOOOOPPQQQQQQQQPPPOOOONNNMMMKKKJJ
EEEFFFFGGGHHHIIJJKKKLLLMMMNNNOOOOPPQQQQRRQQQQPPPOOOONNNMMM
EEEFFFFGGGHHHIIJJKKKLLLMMMNNNOOOOPPQQQRRRRQQQPPPOOOONNN
EEEFFFFGGGHHHIIJJKKKLLLMMMNNNOOOOPPQQRRRRRRQQPPPOOOO
EEEFFFFGGGHHHIIJJKKKLLLMMMNNNOOOOPPQQRRRRRRQQPP
EEEFFFFGGGHHHIIJJKKKLLLMMMNNNOOOOPPQQQQRRQQQQ
EEEFFFFGGGHHHIIJJKKKLLLMMMNNNOOOOPPQQQQQQQQ
EEEFFFFGGGHHHIIJJKKKLLLMMMNNNOOOOPPQQQQQQ
EEEFFFFGGGHHHIIJJKKKLLLMMMNNNOOOO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~   ~~~      ~~~~      ~~~~~~        ~~~~      ~~~~     ~~~
~~         ~~~~~~~~~~         ~~~~~~~~~~~~~~         ~~~~~~~~
~~   ~~~~~~~~~~~~~~~~   ~~~~~~~~~~~~~~~~   ~~~~~~~~~~~~~~~~  ~
~~~~~~~~~~~~~   ~~~~~~~~~~~~~~~~   ~~~~~~~~~~~~~~~~   ~~~~~~~~
         AAAA      AAAA        AAAA        AAAA       AAAA
       AAAAAAAA  AAAAAAAA    AAAAAAAA    AAAAAAAA   AAAAAAAA
      AAABBBBBBAAABBBBBBAA  AAABBBBBBAA  AAABBBBBBAAABBBBBBAA
      AABCCCCCBBCCCCCBBCCA  AABCCCCCBBCCA AABCCCCCBBCCCCCBBCA
      AABCDDDDBBCDDDDBBCCA  AABCDDDDBBCCA AABCDDDDBBCDDDDBBCA
      AABCEEEEBBCEEEEBBCCA  AABCEEEEBBCCA AABCEEEEBBCEEEEBBCA
      AABCFGGGBBCFGGGBBCCA  AABCFGGGBBCCA AABCFGGGBBCFGGGBBCA
      AABCHHHHBBCHHHHBBCCA  AABCHHHHBBCCA AABCHHHHBBCHHHHBBCA
      AABCHIHHBBCHIHHBBCCA  AABCHIHHBBCCA AABCHIHHBBCHIHHBBCA
      AABCHIIBBCHIIBBCCA    AABCHIIBBCCA   AABCHIIBBCHIIBBCA
      AABCCBBCCBBCCBBCCA    AABCCBBCCBCCA  AABCCBBCCBBCCBBCA

                 DDDDDDDDD
              DDDDDDDDDDDDDDD
           DDDDDDDDDDDDDDDDDDDDD
          DDDDDDDDDDDDDDDDDDDDDDDD
             ||        ||        ||
             ||        ||        ||
             ||        ||        ||
         ____||____ ____||____ ____||____
        /____/____/\/____/____/\/____/____\
       /____/____/\/____/____/\/____/____/\
      /____/____/\/____/____/\/____/____/\
     /____/____/\/____/____/\/____/____/\
     """, r"""
B                              AAAA
                           AAAAABBAAAA
                        AAAAABBBBCCBBAAAA
                     AAAAABBBCCCCDDCCBBBAAAA
                  AAAAABBCCCCDDDDEEDDDCCCBBBAAAA
               AAAAABBCCCDDDDEEEEFFEEEEDDDCCCBBBAAAA
            AAAAABBCCCDDDDEEEEFFFFGGFFFFEEEEDDDCCCBBBAAAA
          AAAABBCCCDDDDEEEEFFFFGGGHHGGGFFFFEEEEDDDCCCBBBAAA
        AAABBCCCDDDDEEEEFFFFGGGHHHIIHHHGGGFFFFEEEEDDDCCCBBBAA
      AAABBCCCDDDDEEEEFFFFGGGHHHIIJJIIHHHGGGFFFFEEEEDDDCCCBBBAA
     AABBCCCDDDDEEEEFFFFGGGHHHIIJJKKJJIIHHHGGGFFFFEEEEDDDCCCBBBA
    AABBCCCDDDDEEEEFFFFGGGHHHIIJJKKLLKKJJIIHHHGGGFFFFEEEEDDDCCCBA
    ABBCCCDDDDEEEEFFFFGGGHHHIIJJKKLLMMLLKKJJIIHHHGGGFFFFEEEEDDDCCB
   ABBCCCDDDDEEEEFFFFGGGHHHIIJJKKLLMMMMLLKKJJIIHHHGGGFFFFEEEEDDDCCB
   BBCCCDDDDEEEEFFFFGGGHHHIIJJKKLLMMMMMMMLLKKJJIIHHHGGGFFFFEEEEDDDCC
   BBCCCDDDDEEEEFFFFGGGHHHIIJJKKLLMMMMMMMMLLKKJJIIHHHGGGFFFFEEEEDDDCC
   BBCCCDDDDEEEEFFFFGGGHHHIIJJKKLLMMMMMMMMLLKKJJIIHHHGGGFFFFEEEEDDDCC
   BBCCCDDDDEEEEFFFFGGGHHHIIJJKKLLMMMMMMMMLLKKJJIIHHHGGGFFFFEEEEDDDCC
   BBCCCDDDDEEEEFFFFGGGHHHIIJJKKLLMMMMMMMMLLKKJJIIHHHGGGFFFFEEEEDDDCC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~   ~~~~      ~~~~~~        ~~~~~~       ~~~~      ~~~~   ~~~
~~~        ~~~~~~~~~~~~    ~~~~~~~~~~~~~    ~~~~~~~~~~~~    ~~~~
~~~~   ~~~~~~~~~~~~~~~~    ~~~~~~~~~~~~~    ~~~~~~~~~~~~~   ~~~~
~~~~~~~~~~~~   ~~~~~~~~~~~~~   ~~~~~~~~~~~~~   ~~~~~~~~~~~~~~~~
                DDDD        DDDD        DDDD
              DDDDDDDD    DDDDDDDD    DDDDDDDD
            DDDDEEEEED  DDDDEEEEED  DDDDEEEEED
           DDDEFFFFEED DDDEFFFFEED DDDEFFFFEED
           DDEFGGGFEDD DDEFGGGFEDD DDEFGGGFEDD
           DDEFGHHGFDD DDEFGHHGFDD DDEFGHHGFDD
            DDFFHHFFDD  DDFFHHFFDD  DDFFHHFFDD
              DDFFFFDD    DDFFFFDD    DDFFFFDD
                 ||            ||            ||
                 ||            ||            ||
           _______||___________||___________||_______
          /_______/___________/__\_________/_______/\
         /_______/___________/____\_______/_______/  \
        /_______/___________/______\_____/_______/    \
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~ ~~~~~~~ ~~~~~~~~ ~~~~~ ~~ ~~~~~~~~ ~~~~~~~~ ~~~~~~~ ~~~~~""", r"""
        C
        
                 AAAA               BBBB                AAAA
                AAAAAA             BBBBBBB             AAAAAA
               AAAAABAA           BBBBCCCBBB           AAAAABAA
              AAAAACCBAAA       BBBCCDDDDCCBBB       AAAAACCBAAA
             AAAAADDDDAAAA     BBCCDDDEEDDDCCBB     AAAAADDDDAAAA
            AAAAEEEEAAA      BBCCDDDEFFFFEDDDCCBB      AAAAEEEEAAA
           AAAFFFAA        BBCCDDDEFFGGFFEDDDCCBB        AAAFFFAA
          AAAGGAA        BBCCDDDEFFGGHHGGFFEDDDCCBB        AAAGGAA
         AAHHAA        BBCCDDDEFFGGHHIIHHGGFFEDDDCCBB        AAHHAA
        AAIIAA         BBCCDDDEFFGGHHIIJJIIHHGGFFEDDDCCBB         AAIIAA
       AAJJAA          BBCCDDDEFFGGHHIIJJKKIIHHGGFFEDDDCCBB          AAJJAA
      AAKKAA           BBCCDDDEFFGGHHIIJJKKLLJJIIHHGGFFEDDDCCBB           AAKKAA
        """, r"""
        D
                                Q
                               QQQ
                              QQQQQ
                             QQQQQQQ
                            QQQQQQQQQ
                           QQQQQQQQQQQ
                          QQQQQQQQQQQQQ
                         QQQQQQQQQQQQQQQ
                        QQQQQQQQQQQQQQQQQ
                       QQQQQQQQQQQQQQQQQQQ
                      QQQQQQQQQQQQQQQQQQQQQ
                     QQQQQQQQQQQQQQQQQQQQQQQ
                    QQQQQQQQQQQQQQQQQQQQQQQQQ
                   QQQQQQQQQQQQQQQQQQQQQQQQQQQ
                  QQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
                 QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
                QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
               QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
              QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
             QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
            QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
           QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
          QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
         QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
        QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
       QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
      QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
     QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
    QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
   QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
  QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
 QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

                      HHHHHHHHHHHHHHHH
                   HHHHHHHHHIIIIIIIIHHHHHHHHH
                HHHHHHIIIIIIIIIIIIIIIIIIIIHHHHHH
             HHHHHIIIJJJJJJJJJJJJJJJJJJJJIIIHHHHH
          HHHHIIIJJJJKKKKKKKKKKKKKKKKKKJJJJIIIHHHH
       HHHIIIJJJKKKLLLLLLLLLLLLLLLLLLLLKKKJJJIIIHHH
    HHHIIIJJKKLLLLMMMMMMMMMMMMMMMMMMMMMMKKJJIIIHHH
 HHHIIJJKKLLLLNNNNNNNNNNNNNNNNNNNNNNNNNNLLKKJJIIHHH
HHIIJKKLLLLMMMMOOOOOOOOOOOOOOOOOOOOOOOOMMMMLLKKJIIH
        """, r"""
        E
                         /\
                        /  \
              /\       /EDIN\       /\
             /  \     /BURGH \     /  \
    /\      /CAST\    |EDINBU|    /EDIN\      /\
   /  \    /BURGH \   |RGHCAS|   /BURGH\     /  \
  /EDIN\   |EDINBU|   |TLEDIN|   |EDINBU|   /CAST\
 /BURGHE\  |RGHCAS|   |BURGHE|   |RGHCAS|  /BURGHE\
 |EDINBU|  |TLEDIN|   |DINBUR|   |TLEDIN|  |EDINBU|
 |RGHCAS|  |BURGHE|   |GHCAST|   |BURGHE|  |RGHCAS|
 |TLEDIN|  |EDINBU|   |LEDINB|   |EDINBU|  |TLEDIN|
 |BURGHE|  |RGHCAS|   |URGCAS|   |RGHCAS|  |BURGHE|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        """, r"""
        F
                              /\
                             /FI\
                            /FIJI\
                           /FIJIFI\
                          /FIJIFIJI\
              /\          /FIJIFIJIF\          /\
             /FI\        /IJIFIJIFIJI\        /FI\
            /FIJI\      /FIJIFIJIFIJIF\      /FIJI\
           /FIJIFI\    /IJIFIJIFIJIFIJI\    /FIJIFI\
          /FIJIFIJI\  /FIJIFIJIFIJIFIJIF\  /FIJIFIJI\
         /FIJIFIJIFI\/IJIFIJIFIJIFIJIFIJI\/FIJIFIJIFI\
        /____________\___________________/____________\
        |FIJIFIJIFIJI| |FIJIFIJIFIJIFIJI| |FIJIFIJIFIJ|
        |IJIFIJIFIJIF| |IJIFIJIFIJIFIJIF| |IJIFIJIFIJIF|
        |JIFIJIFIJIFI| |JIFIJIFIJIFIJIFI| |JIFIJIFIJIFI|
        |IFIJIFIJIFIJ| |IFIJIFIJIFIJIFIJ| |IFIJIFIJIFIJ|
        |FIJIFIJIFIJI| |FIJIFIJIFIJIFIJI| |FIJIFIJIFIJI|
        |IJIFIJIFIJIF| |IJIFIJIFIJIFIJIF| |IJIFIJIFIJIF|
        |JIFIJIFIJIFI| |JIFIJIFIJIFIJIFI| |JIFIJIFIJIFI|
        |IFIJIFIJIFIJ| |IFIJIFIJIFIJIFIJ| |IFIJIFIJIFIJ|
        |FIJIFIJIFIJI| |FIJIFIJIFIJIFIJI| |FIJIFIJIFIJI|
        |IJIFIJIFIJIF| |IJIFIJIFIJIFIJIF| |IJIFIJIFIJIF|
        |____________| |________________| |_____________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  \FIJI \FIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIF/ FIJI/
   \IJIF  \IJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJ/ IJIF/
    \JIFI   \JIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFI/ JIFI/
     \IFIJ    \IFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIF/ IFIJ/
      \FIJI     \FIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJI/ FIJI/
       \IJIF     \IJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJ/ IJIF/
        \JIFI     \JIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIFI/ JIFI/
         \IFIJ     \IFIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJIF/ IFIJ/
          \FIJI     \FIJIFIJIFIJIFIJIFIJIFIJIFIJIFIJI/ FIJI/
           \IJIF_____\IJIFIJIFIJIFIJIFIJIFIJIFIJIFIJ/_IJIF/
            \JIFIJIFIJ\JIFIJIFIJIFIJIFIJIFIJIFIJIFI/JIFIJ/
             \__________\________________________/__________/
        """, r"""
        G
                    /\          /\          /\
                   /AL\        /AL\        /AL\
                  /ALHА\      /ALHA\      /ALHA\
                 /ALHAMB\    /ALHAMB\    /ALHAMB\
                /ALHAMBRA\  /ALHAMBRA\  /ALHAMBRA\
               /ALHAMBRALH\/ALHAMBRALH\/ALHAMBRALH\
              /____________\____________\____________\
    /\        |ALHAMBRAALHА| |ALHAMBRALH| |ALHAMBRAALH|       /\
   /AL\       |HAMBRAALHАMB| |AMBRAALHАMB| |HAMBRAALHАMB|    /AL\
  /ALHA\      |AMBRAALHАMBR| |MBRAALHАMBRA| |AMBRAALHАMBR|  /ALHA\
 /ALHAMB\     |MBRAALHАMBRA| |BRAALHАMBRАЛ| |MBRAALHАMBRA| /ALHAMB\
/ALHAMBRA\    |BRAALHАMBRAL| |RAALHАMBRALH| |BRAALHАMBRAL|/ALHAMBRA\
|ALHAMBRАЛ|   |RAALHАMBRALH| |AALHАMBRALHA| |RAALHАMBRALH||ALHAMBRАЛ|
|HAMBRAALHА|  |AALHАMBRALHA| |ALHАMBRALHAM| |AALHАMBRALHA||HAMBRAALHА|
|AMBRAALHAM|  |____________| |____________| |____________||AMBRAALHAM|
|MBRAALHАMBR|   (  )  (  )      (  )  (  )     (  )  (  ) |MBRAALHАMBR|
|BRAALHАMBRA|  /    \/    \    /    \/    \    /    \/    \ |BRAALHАMBRA|
|RAALHАMBRAL| | ALHA  ALHA |  | ALHA  ALHA |  | ALHA  ALHA ||RAALHАMBRAL|
|AALHАMBRАLH| | MBRA  MBRA |  | MBRA  MBRA |  | MBRA  MBRA ||AALHАMBRАLH|
|ALHАMBRALHA| |  RA    RA  |  |  RA    RA  |  |  RA    RA  ||ALHАMBRALHA|
|HAMBRAALHAM| \____/\/\____/  \____/\/\____/  \____/\/\____/ |HAMBRAALHAM|
|AMBRAALHАMB|  |ALHAMBRALHA|  |ALHAMBRALHA|  |ALHAMBRALHA|  |AMBRAALHАMB|
|MBRAALHАMBR|  |HAMBRAALHАM|  |HAMBRAALHАM|  |HAMBRAALHАM|  |MBRAALHАMBR|
|BRAALHАMBRA|  |AMBRAALHАMB|  |AMBRAALHАMB|  |AMBRAALHАMB|  |BRAALHАMBRA|
|RAALHАMBRAL|  |MBRAALHАMBR|  |MBRAALHАMBR|  |MBRAALHАMBR|  |RAALHАMBRAL|
|___________|  |___________|  |___________|  |___________|  |___________|
|ALHAMBRALHA|__|ALHAMBRALHA|__|ALHAMBRALHA|__|ALHAMBRALHA|__|ALHAMBRALHA|
|HAMBRAALHАM|  |HAMBRAALHАM|  |HAMBRAALHАM|  |HAMBRAALHАM|  |HAMBRAALHАM|
|AMBRAALHАMB|  |AMBRAALHАMB|  |AMBRAALHАMB|  |AMBRAALHАMB|  |AMBRAALHАMB|
|MBRAALHАMBR|  |MBRAALHАMBR|  |MBRAALHАMBR|  |MBRAALHАMBR|  |MBRAALHАMBR|
|BRAALHАMBRA|  |BRAALHАMBRA|  |BRAALHАMBRA|  |BRAALHАMBRA|  |BRAALHАMBRA|
|RAALHАMBRAL|  |RAALHАMBRAL|  |RAALHАMBRAL|  |RAALHАMBRAL|  |RAALHАMBRAL|
|___________|  |___________|  |___________|  |___________|  |___________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  \ALHAMBRA \ALHAMBRAALHAMBRA/ \ALHAMBRA/ \ALHAMBRAALHAMBRA/ ALHAMBRA/
   \HAMBRAAL  \HAMBRAALHAMBR/   \HAMБRAL/   \HAMBRAALHAMBR/ HAMBRALH/
    \AMBRAАЛH   \AMBRAALHАMB/     \АMBRA/     \AMBRAALHАMB/ AMBRAALH/
     \MBRAALHА    \MBRAALHАM/       \МBR/        \MBRAALHАM/ MBRAALHA/
      \BRAALHАMB    \BRAALLHА/        \/            \BRAALLHА/ BRAАЛHАM/
       \RAALHАMBRA   \RAALHAM/                       \RAALHAM/ RAALHАMB/
        \AALHАMBRАLH   \AALHA/                         \AALHA/ AALHАMBR/
         \ALHАMBRALHA    \ALH/                           \ALH/ ALHАMBRA/
          \HAMBRAALHAM    \/                               \/ HAMBRAALH/
           \______________/                                 \__________/
              \ALHAMBRA /                                    \ALHAMBRA/
               \HAMBRAL/                                      \HAMBRAL/
                \AMBRA/                                        \AMBRA/
                 \MBR/                                          \MBR/
                  \A/                                            \A/
                   V                                              V        
        """, r"""
        H
                                  /\
                                 /HA\
                                /HAWA\
                               /HAWAII\
                              /HAWAIIHA\
                             /HAWAIIHAWA\
                            /HAWAIIHAWALL\
                           /HAWAIIHAWAIAH\
                          /HAWAIIHAWAIIHAW\
                         /HAWAIIHAWAIIHAWAI\
                        /HAWAIIHAWAIIHAWAIIH\
                       /HAWAIIHAWAIIHAWAIIHAW\
                      /HAWAIIHAWAIIHAWAIIHAWAI\
                     /HAWAIIHAWAIIHAWAIIHAWAIIH\
                    /HAWAIIHAWAIIHAWAIIHAWAIIHAWA\
                   /HAWAIIHAWAIIHAWAIIHAWAIIHAWAII\
                  /HAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHА\
                 /HAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWA\
                /HAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAII\
               /HAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHА\
              /HAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWA\
             /____________________________________________\
            |HAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAW|
            |AWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWA|
            |WAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAI|
            |AIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAII|
            |IIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIH|
            |IHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHА|
            |HAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAW|
            |AWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWA|
            |______________________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  \HAWAII  \HAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAII/  HAWAII/
   \HAWAI   \HAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWA/   HAWAI/
    \HAWA    \HAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAW/    HAWA/
     \HAW      \HAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAWAII/     HAW/
      \HAW       \HAWAIIHAWAIIHAWAIIHAWAIIHAWAIIHAW/      HAW/
       \HA         \HAWAIIHAWAIIHAWAIIHAWAIIHAWAII/        HA/
        \H           \HAWAIIHAWAIIHAWAIIHAWAIIHAW/          H/
         \              \HAWAIIHAWAIIHAWAIIHAWAI/             /
          \               \HAWAIIHAWAIIHAWAII/               /
           \                \HAWAIIHAWAIIHAW/               /
            \                 \HAWAIIHAWAII/               /
             \                  \HAWAIIHAW/               /
              \                   \HAWAII/               /
               \                   \HAWA/               /
                \                   \HA/               /
                 \___________________\/_______________/        
        """, r"""
        I
                              ***
                             *HOO*
                            *HOOKLI*
                           *HOOKLIGH*
                          *HOOKLIGHT*
                         *HOOKLIGHTH*
                        *HOOKLIGHTHO*
                       *HOOKLIGHOUSE*
                      *HOOKLIGHTHOUS*
                     *HOOKLIGHTHOUSE*
                    *HOOKLIGHTHOUSEE*
                   *___________________*
                   |HOOKLIGHTHOUSEHOOK|
                   |OOKLIGHTHOUSEHOOKL|
                   |OKLIGHTHOUSEHOOKLI|
                   |KLIGHTHOUSEHOOKLIG|
                   |LIGHTHOUSEHOOKLIGH|
                   |IGHTHOUSEHOOKLIGHT|
                   |GHTHOUSEHOOKLIGHTH|
                   |HTHOUSEHOOKLIGHTHO|
                   |THOUSEHOOKLIGHTHOU|
                   |HOUSEHOOKLIGHTHOUS|
                   |OUSEHOOKLIGHTHOUSE|
                   |USEHOOKLIGHTHOUSEH|
                   |__________________|
                   |HOOKLIGHTHOUSEHOOK|
                   |OOKLIGHTHOUSEHOOKL|
                   |OKLIGHTHOUSEHOOKLI|
                   |KLIGHTHOUSEHOOKLIG|
                   |LIGHTHOUSEHOOKLIGH|
                   |IGHTHOUSEHOOKLIGHT|
                   |GHTHOUSEHOOKLIGHTH|
                   |HTHOUSEHOOKLIGHTHO|
                   |__________________|
                   |HOOKLIGHTHOUSEHOOK|
                   |OOKLIGHTHOUSEHOOKL|
                   |OKLIGHTHOUSEHOOKLI|
                   |KLIGHTHOUSEHOOKLIG|
                   |LIGHTHOUSEHOOKLIGH|
                   |IGHTHOUSEHOOKLIGHT|
                   |GHTHOUSEHOOKLIGHTH|
                   |__________________|
                  /|HOOKLIGHTHOUSEHOOK|\
                 / |OOKLIGHTHOUSEHOOKL| \
                /  |OKLIGHTHOUSEHOOKLI|  \
               /   |KLIGHTHOUSEHOOKLIG|   \
              /    |LIGHTHOUSEHOOKLIGH|    \
             /     |__________________|     \
            /  []  |HOOKLIGHTHOUSEHOOK|  []  \
           /       |OOKLIGHTHOUSEHOOKL|       \
          /________| OKLIGHTHOUSE HOOK|________\
         |HOOKLIGHTHOUSEHOOKLIGHTHOUSEHOOKLIGHTH|
         |OOKLIGHTHOUSEHOOKLIGHTHOUSEHOOKLIGHTHO|
         |OKLIGHTHOUSEHOOKLIGHTHOUSEHOOKLIGHTHOU|
         |KLIGHTHOUSEHOOKLIGHTHOUSEHOOKLIGHTHOUS|
         |LIGHTHOUSEHOOKLIGHTHOUSEHOOKLIGHTHOUSE|
         |_______________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   \HOOK  \HOOKLIGHTHOUSEHOOKLIGHTHOUSEHOOKLIGHT/  HOOK/
    \HOOKL  \HOOKLIGHTHOUSEHOOKLIGHTHOUSEHOOKLI/  HOOKL/
     \HOOKLI  \HOOKLIGHTHOUSEHOOKLIGHTHOUSEHO/  HOOKLI/
      \HOOKLIG  \HOOKLIGHTHOUSEHOOKLIGHTHOUS/  HOOKLIG/
       \HOOKLIGT  \HOOKLIGHTHOUSEHOOKLIGHT/  HOOKLIGT/
        \__________\____________________/__________/
        """, r"""
        J
                                 *
                                *M*
                               *MON*
                              *MONAS*
                             *MONASM*
                            *MONASMONA*
                           *MONASMONAS*
                          *MONASMONASM*
                         *MONASMONA SMO*
                        *MONASMONASMONAS*
                       *___________________*
                       |MONASMONASMONASMON|
                       |ONASMONASMONASMON A|
                       |NASMONASMONASMONAS|
                       |ASMONASMONASMONAS M|
                       |SMONASMONASMONASMO|
                       |MONASMONASMONASMON|
                       |ONASMONASMONASMON A|
                       |NASMONASMONASMONAS|
                       |ASMONASMONASMONAS M|
                       |SMONASMONASMONASMO|
                       |MONASMONASMONASMON|
                       |__________________|
                       |MONASMONASMONASMON|
                       |ONASMONASMONASMON A|
                       |NASMONASMONASMONAS|
                       |ASMONASMONASMONAS M|
                       |SMONASMONASMONASMO|
                       |MONASMONASMONASMON|
                       |__________________|
                       |MONASMONASMONASMON|
                       |ONASMONASMONASMON A|
                       |NASMONASMONASMONAS|
                       |ASMONASMONASMONAS M|
                       |SMONASMONASMONASMO|
                       |MONASMONASMONASMON|
                       |__________________|
                      /|MONASMONASMONASMON|\
                     / |ONASMONASMONASMON A| \
                    /  |NASMONASMONASMONAS|  \
                   /   |ASMONASMONASMONAS M|   \
                  /    |SMONASMONASMONASMO|    \
                 /     |__________________|     \
                /      |MONASMONASMONASMON|      \
               /  []   |ONASMONASMONASMON |  []   \
              /________| NASMONASMONAS    |________\
             |MONASMONASMONASMONASMONASMONASMONASMON|
             |ONASMONASMONASMONASMONASMONASMONASMON A|
             |NASMONASMONASMONASMONASMONASMONASMONAS|
             |ASMONASMONASMONASMONASMONASMONASMONAS M|
             |SMONASMONASMONASMONASMONASMONASMONASMO|
             |__________________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   \MONAS  \MONASMONASMONASMONASMONASMONAS/  MONAS/
    \MONAS  \MONASMONASMONASMONASMONASMON/  MONAS/
     \MONA   \MONASMONASMONASMONASMONAS/   MONA/
      \MON    \MONASMONASMONASMONASMONA/    MON/
       \MO     \MONASMONASMONASMONAS/      MO/
        \M      \MONASMONASMONAS/          M/
         \       \MONASMONAS/              /
          \_______\MONAS/__________________/        
        """, r"""
        K
                    ___________________________________
                   /MELISSANIMELISSANIMELISSANIMELIS   \
                  /MELISSANIMELISSANIMELISSANIMELISSA   \
                 /MELISSANIMELISSANIMELISSANIMELISSANI   \
                /MELISSANIMELISSANIMELISSANIMELISSANIM   \
               /MELISSANIMELISSANIMELISSANIMELISSANIME   \
              /MELISSANIMELISSANIMELISSANIMELISSANIMEL   \
             /MELISSANIMELISSANIMELISSANIMELISSANIMELIS   \
            /___________________________________________  \
           |         *  *  *  *  *  *  *  *  *  *        |
           |       *                               *      |
           |      *   MELISSANIMELISSANIMELISSA     *     |
           |     *    NISSANIMELISSANIMELISSANI      *    |
           |    *     MELISSANIMELISSANIMELISSAN      *   |
           |   *      ISSANIMELISSANIMELISSANIM        *  |
           |  *       ELISSANIMELISSANIMELISSANI        * |
           | *        MELISSANIMELISSANIMELISSAN        * |
           |*         ISSANIMELISSANIMELISSANIM          *|
           |*         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  *|
           |*       ~~~MELISSANIMELISSANIMELISSANI~~~    *|
           |*      ~~MELISSANIMELISSANIMELISSANIM~~      *|
           |*     ~~MELISSANIMELISSANIMELISSANIME~~      *|
           | *   ~~MELISSANIMELISSANIMELISSANIMEL~~     * |
           |  *  ~~MELISSANIMELISSANIMELISSANIME~~~    *  |
           |   * ~~~MELISSANIMELISSANIMELISSANIM~~~   *   |
           |    *~~~~MELISSANIMELISSANIMELISSANI~~~~  *   |
           |     *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~* |
           |      *                                  *   |
           |       *                                *    |
           |        *                              *     |
           |         *                            *      |
           |          *                          *       |
           |     ______*________________________*______  |
           |    |MELIS  \MELISSANIMELISSANI/  SANIM    |  |
           |    |SANIMEL  \MELISSANIMELISS/  ISSANIME  |  |
           |    |ISSANIME  \MELISSANIMELIS/ LISSANIM   |  |
           |    |LISSANIM    \MELISSANIME/  ELISSANI   |  |
           |    |ELISSANI     \MELISSANI/   MELISSANI  |  |
           |    |_____________\/________\______________|  |
           |MELISSANIMELISSANIMELISSANIMELISSANIMELISSANI |
           |ELISSANIMELISSANIMELISSANIMELISSANIMELISSANIM |
           |LISSANIMELISSANIMELISSANIMELISSANIMELISSANIME |
           |ISSANIMELISSANIMELISSANIMELISSANIMELISSANIMEL |
           |_______________________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  \MELIS  \MELISSANIMELISSANIMELISSANIMELISSANIMELISSAN/  MELIS/
   \MELI   \MELISSANIMELISSANIMELISSANIMELISSANIMELIS/    MELI/
    \MEL    \MELISSANIMELISSANIMELISSANIMELISSANIME/      MEL/
     \ME     \MELISSANIMELISSANIMELISSANIMELISSAN/        ME/
      \M      \MELISSANIMELISSANIMELISSANIMELIS/           M/
               \MELISSANIMELISSANIMELISSANIM/
                \MELISSANIMELISSANIMELISSA/
                 \MELISSANIMELISSANIMEL/
                  \MELISSANIMELISSAN/
                   \MELISSANIMELIS/
                    \MELISSANIM/
                     \MELISSA/
                      \MELIS/
                       \MEL/
                        \M/
                         V        
        """, r"""
        L
                          |BB|
                         |BIGI|
                        |BIGBEN|
                       |BIGBENB|
                      |BIGBENBI|
                     |BIGBENBIG|
                    |BIGBENBIGB|
                   |____________|
                   |LONDONLONDO|
                   |ONDONLONDON|
                   |NDONLONDONL|
                   |DONLONDONLO|
                   |ONLONDONLON|
                   |NLONDONLOND|
                   |____________|
                  /|LONDONLONDO|\
                 / |ONDONLONDON| \
                /  |NDONLONDONL|  \
               /   |DONLONDONLO|   \
              /    |ONLONDONLON|    \
             /     |NLONDONLOND|     \
            /      |____________|     \
           /   ()  |LONDONLONDO|  ()   \
          /__________|ONDONLOND|_________\
         |LONDONLONDONLONDONLONDONLONDONLO|
         |ONDONLONDONLONDONLONDONLONDONLON|
         |NDONLONDONLONDONLONDONLONDONLOND|
         |DONLONDONLONDONLONDONLONDONLONDO|
         |ONLONDONLONDONLONDONLONDONLONDON|
         |________________________________|
         |LONDONLONDONLONDONLONDONLONDONLO|
         |ONDONLONDONLONDONLONDONLONDONLON|
         |NDONLONDONLONDONLONDONLONDONLOND|
         |DONLONDONLONDONLONDONLONDONLONDO|
         |ONLONDONLONDONLONDONLONDONLONDON|
         |________________________________|
         |LONDONLONDONLONDONLONDONLONDONLO|
         |ONDONLONDONLONDONLONDONLONDONLON|
         |NDONLONDONLONDONLONDONLONDONLOND|
         |DONLONDONLONDONLONDONLONDONLONDO|
         |ONLONDONLONDONLONDONLONDONLONDON|
         |________________________________|
        /|LONDONLONDONLONDONLONDONLONDONLO|\
       / |ONDONLONDONLONDONLONDONLONDONLON| \
      /  |NDONLONDONLONDONLONDONLONDONLOND|  \
     /   |DONLONDONLONDONLONDONLONDONLONDO|   \
    /    |ONLONDONLONDONLONDONLONDONLONDON|    \
   / []  |________________________________| []  \
  /      |LONDONLONDONLONDONLONDONLONDONLO|      \
 /  []   |ONDONLONDONLONDONLONDONLONDONLON|  []   \
/________|NDONLONDONLONDONLONDONLONDONLOND|________\
|LONDONLONDONLONDONLONDONLONDONLONDONLONDONLONDONLO|
|ONDONLONDONLONDONLONDONLONDONLONDONLONDONLONDONLON|
|NDONLONDONLONDONLONDONLONDONLONDONLONDONLONDONLOND|
|DONLONDONLONDONLONDONLONDONLONDONLONDONLONDONLONDO|
|ONLONDONLONDONLONDONLONDONLONDONLONDONLONDONLONDON|
|NLONDONLONDONLONDONLONDONLONDONLONDONLONDONLONDONL|
|LONDONLONDONLONDONLONDONLONDONLONDONLONDONLONDONLO|
|__________________________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  \LOND  \LONDONLONDONLONDONLONDONLONDON/  LOND/
   \LON   \LONDONLONDONLONDONLONDONLOND/   LON/
    \LO    \LONDONLONDONLONDONLONDONLO/    LO/
     \L     \LONDONLONDONLONDONLONDON/      L/
              \LONDONLONDONLONDONLON/
               \LONDONLONDONLONDONL/
                \LONDONLONDONLONDO/
                 \LONDONLONDONLON/
                  \LONDONLONDONL/
                   \LONDONLONDO/
                    \LONDONLON/
                     \LONDONL/
                      \LONDO/
                       \LON/
                        \LO/
                         \/        
        """, r"""
        M
                    /\        /\        /\
                   /MA\      /MA\      /MA\
                  /MACH\    /MACH\    /MACH\
                 /MACHU \  /MACHU \  /MACHU \
                /MACHUPI\/MACHUPI\/MACHUPI\/
               /MACHUPIC  MACHUPIC  MACHUPIC\
              /MACHUPICCH MACHUPICCH MACHUPICCH\
             /____________\________/____________\
            |MACHUPICCHUMA|        |MACHUPICCHUMA|
            |ACHUPICCHUMAS|        |ACHUPICCHUMAS|
            |CHUPICCHUMAS |        |CHUPICCHUMAS |
            |HUPICCHUMAS  |        |HUPICCHUMAS  |
            |UPICCHUMAS   |        |UPICCHUMAS   |
            |PICCHUMAS    |        |PICCHUMAS    |
            |_____________|        |_____________|
           /|MACHUPICCHUMA|        |MACHUPICCHUMA|\
          / |ACHUPICCHUMAS|        |ACHUPICCHUMAS| \
         /  |CHUPICCHUMAS |        |CHUPICCHUMAS |  \
        /   |_____________|        |_____________|   \
       / [] |MACHUPICCHUMA|        |MACHUPICCHUMA| [] \
      /_____|ACHUPICCHUMAS|________|ACHUPICCHUMAS|_____\
     |MACHUPICCHUMAS   MACHUPICCHU   SMACHUPICCHUMAS   |
     |ACHUPICCHUMAS    ACHUPICCHUMA   MACHUPICCHUMAS   |
     |CHUPICCHUMAS     CHUPICCHUMAS   ACHUPICCHUMAS    |
     |HUPICCHUMAS      HUPICCHUMAS    CHUPICCHUMAS     |
     |UPICCHUMAS       UPICCHUMAS     HUPICCHUMAS      |
     |PICCHUMAS        PICCHUMAS      UPICCHUMAS       |
     |_________________________________________________|
    /|MACHUPICCHUMAS  MACHUPICCHUMAS  MACHUPICCHUMAS   |\
   / |ACHUPICCHUMAS   ACHUPICCHUMAS   ACHUPICCHUMAS    | \
  /  |CHUPICCHUMAS    CHUPICCHUMAS    CHUPICCHUMAS     |  \
 /   |HUPICCHUMAS     HUPICCHUMAS     HUPICCHUMAS      |   \
/    |UPICCHUMAS      UPICCHUMAS      UPICCHUMAS       |    \
|    |_________________________________________________|    |
|MACHUPICCHUMAS  MACHUPICCHUMAS  MACHUPICCHUMAS  MACHUPICCHU|
|ACHUPICCHUMAS   ACHUPICCHUMAS   ACHUPICCHUMAS   ACHUPICCHUM|
|CHUPICCHUMAS    CHUPICCHUMAS    CHUPICCHUMAS    CHUPICCHUMA|
|HUPICCHUMAS     HUPICCHUMAS     HUPICCHUMAS     HUPICCHUMAS|
|___________________________________________________________|
        """, r"""
        N

                                             /\
                /\          /\              /NA\
               /NA\        /NA\            /NAIR\
              /NAIR\      /NAIR\          /NAIRO \
             /NAIRO \    /NAIRO \        /NAIROBI\
            /NAIROBI \  /NAIROBI \      /NAIROBINA\
           /NAIROBINA \/NAIROBINA \    /NAIROBINAIR\
          /____________\___________\__/_____________\
         |              |           |               |
    /\   |   /\    /\   |  /\   /\  |   /\    /\   |  /\
   /  \  |  /  \  /  \  | /  \ /  \ |  /  \  /  \  | /  \
  / NA \ | /NAIR\/NAIRO\ |/NAIR\/NAI\| /NAIRO\/NAIR\ |/NAIR\
 /NAIRO \|/NAIROBI    NA\|ROBI  ROBI |/ROBI    ROBI \|ROBI \
/NAIROBI\/NAIROBINAIROB  |INAIROBINAIROBI       NAIROBI\    \
|        |               |                              |    |
|  ~~~~  |    ~~~~~       |    ~~~~~~     ~~~~~~         |~~~~|
| ~NAIRO~|  ~~NAIRO~~     |  ~~NAIRO~~  ~~NAIRO~~        |~NA~|
|~~BINAIRO~~NAIROBI~~     | ~~BINAIRO~~~~BINAIRO~~       |~BI~|
| ~~NAIRO~~NAIROB~~       |  ~~NAIRO~~ ~~NAIRO~~         |~~~~|
|  ~~~~~  ~~~~~           |   ~~~~~     ~~~~~            |    |
|_________|_______________|______________________________|____|
|NAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROB      |
|AIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBIA     |
|IROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAI    |
|ROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROB  |
|OBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBIA |
|BINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINA |
|INAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIROBINAIRO|
|______________________________________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """, r"""
        O
                            /\
                           /OS\
                          /OSAK\
                         /OSAKA \
                        /OSAKAO  \
                       /OSAKAOSAKА\
                      /____________\
                      |OSAKAOSAKAO |
                      |SAKAOSAKAOS |
                      |AKAOSAKAOСА |
                      |KAOSAKAOSAKА|
                      |AOSAKAOSAKAO|
                      |OSAKAOSAKАOS|
                      |____________|
                     /|OSAKAOSAKAO |\
                    / |SAKAOSAKАOSA| \
                   /  |AKAOSAKAOSAKА| \
                  / * |KAOSAKAOSAKAO| * \
                 /______|AOSAKAOSAKА|______\
                |OSAKAOSAKAOSAKAOSAKAOSAKАOS|
                |SAKAOSAKAOSAKAOSAKAOSAKАOSA|
                |AKAOSAKAOSAKAOSAKAOSAKАOSAK|
                |KAOSAKAOSAKAOSAKAOSAKАOSAKA|
                |AOSAKAOSAKAOSAKAOSAKАOSAKAO|
                |___________________________|
               /|OSAKAOSAKAOSAKAOSAKAOSAKАOS|\
              / |SAKAOSAKAOSAKAOSAKAOSAKАOSA| \
             /  |AKAOSAKAOSAKAOSAKAOSAKАOSAK|  \
            / []|KAOSAKAOSAKAOSAKAOSAKАOSAKA|[] \
           /____|AOSAKAOSAKAOSAKAOSAKАOSAKAO|____\
          |OSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKА|
          |SAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKАO|
          |AKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOS|
          |KAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOSA|
          |AOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOSAK|
          |_________________________________________|
         /|OSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKА|\
        / |SAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKАO| \
       /  |AKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOS|  \
      / []|KAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOSA|[] \
     /____|AOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOSAK|____\
    |OSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKАO|
    |SAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOS|
    |AKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOSA|
    |KAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOSAK|
    |AOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOSAKA|
    |___________________________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  \OSAKA  \OSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOSAKA/  OSAKA/
   \OSAK   \OSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOSAK/  OSAK/
    \OSA    \OSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOSA/   OSA/
     \OS     \OSAKAOSAKAOSAKAOSAKAOSAKAOSAKАOS/    OS/
      \O      \OSAKAOSAKAOSAKAOSAKAOSAKAOSAKА/      O/
               \OSAKAOSAKAOSAKAOSAKAOSAKАOS/
                \OSAKAOSAKAOSAKAOSAKAOSAKА/
                 \OSAKAOSAKAOSAKAOSAKАOSA/
                  \OSAKAOSAKAOSAKАOSAK/
                   \OSAKAOSAKАOSAKA/
                    \OSAKAOSAKАOS/
                     \OSAKAOSAKА/
                      \OSAKАOSA/
                       \OSAKA/
                        \OSA/
                         \O/
                          V
        """, r"""
        P
                              /\
                             /PA\
                            /PAR\
                           /PARIS\
                          /PARISPO\
                         /PARISPAR\
                        /___________\
                        |PARISPARISO|
                        |ARISPARISPA|
                        |RISPARISPAR|
                        |ISPARISPAR I|
                        |___________|
                       /|PARISPARISO|\
                      / |ARISPARISPA| \
                     /  |RISPARISPAR|  \
                    /   |ISPARISPAR I|   \
                   /    |___________|    \
                  /  []  PARISPARISO  []  \
                 /________________________\
                /PARISPARISPARISPARISPARISO\
               /ARISPARISPARISPARISPARISPARIS\
              /________________________________\
             |PARISPARISPARISPARISPARISPARISPARI|
             |ARISPARISPARISPARISPARISPARISPARISO|
             |RISPARISPARISPARISPARISPARISPARISPAR|
             |___________________________________|
            /|PARISPARISPARISPARISPARISPARISPARI |\
           / |ARISPARISPARISPARISPARISPARISPARISO | \
          /  |RISPARISPARISPARISPARISPARISPARISPAR|  \
         /   |___________________________________|   \
        /  []|PARISPARISPARISPARISPARISPARISPARIS|[]  \
       /     |ARISPARISPARISPARISPARISPARISPARISO|     \
      /      |RISPARISPARISPARISPARISPARISPARISPA|      \
     /       |___________________________________|       \
    /   []   |PARISPARISPARISPARISPARISPARISPARIS|  []    \
   /         |ARISPARISPARISPARISPARISPARISPARISO|         \
  /__________|RISPARISPARISPARISPARISPARISPARISPA|__________\
 |PARISPARISPARISPARISPARISPARISPARISPARISPARISPARISPARISPARIS|
 |ARISPARISPARISPARISPARISPARISPARISPARISPARISPARISPARISPARISO|
 |RISPARISPARISPARISPARISPARISPARISPARISPARISPARISPARISPARISPA|
 |ISPARISPARISPARISPARISPARISPARISPARISPARISPARISPARISPARISPAR|
 |SPARISPARISPARISPARISPARISPARISPARISPARISPARISPARISPARISPAR I|
 |_____________________________________________________________|
        """, r"""
        Q
                              /=\
                             /===\
                            /=====\
                           /ZHANQIA\
                          /OZHANQIAO\
                         /ZHANQIAOZH\
                        /ANQIAOZHANQI\
                       /AOZHANQIAOZHA\
                      /_______________\
                      |ZHANQIAOZHANQIA|
                      |HANQIAOZHANQIAO|
                      |ANQIAOZHANQIAOZ|
                      |NQIAOZHANQIAOZE|
                      |QIAOZHANQIAOZHA|
                      |IAOZHANQIAOZHAN|
                      |AOZHANQIAOZHANG|
                      |_______________|
                     /|ZHANQIAOZHANQIA|\
                    / |HANQIAOZHANQIAO| \
                   /  |ANQIAOZHANQIAOZ|  \
                  / ()|NQIAOZHANQIAOZE|() \
                 /    |_______________|    \
                /     |ZHANQIAOZHANQIA|     \
               /  /\  |HANQIAOZHANQIAO|  /\  \
              /  /ZH\  |ANQIAOZHANQIAO| /AN\  \
             /__/ZHAN\__|_____________|/QIAO\___\
            |ZHANQIAOZHANQIAOZHANQIAOZHANQIAOZHAN|
            |HANQIAOZHANQIAOZHANQIAOZHANQIAOZHANQ|
            |ANQIAOZHANQIAOZHANQIAOZHANQIAOZHANQI|
            |___________________________________|
            |                                   |
            |  ZHANQIAOZHANQIAOZHANQIAOZHANQIAO  |
            |  HANQIAOZHANQIAOZHANQIAOZHANQIAOZ  |
            |  ANQIAOZHANQIAOZHANQIAOZHANQIAOZH  |
            |                                   |
            |  ZHANQIAOZHANQIAOZHANQIAOZHANQIAO  |
            |  HANQIAOZHANQIAOZHANQIAOZHANQIAOZ  |
            |  ANQIAOZHANQIAOZHANQIAOZHANQIAOZH  |
            |                                   |
            |  ZHANQIAOZHANQIAOZHANQIAOZHANQIAO  |
            |  HANQIAOZHANQIAOZHANQIAOZHANQIAOZ  |
            |  ANQIAOZHANQIAOZHANQIAOZHANQIAOZH  |
            |                                   |
            |  ZHANQIAOZHANQIAOZHANQIAOZHANQIAO  |
            |  HANQIAOZHANQIAOZHANQIAOZHANQIAOZ  |
            |  ANQIAOZHANQIAOZHANQIAOZHANQIAOZH  |
            |                                   |
            |  ZHANQIAOZHANQIAOZHANQIAOZHANQIAO  |
            |  HANQIAOZHANQIAOZHANQIAOZHANQIAOZ  |
            |  ANQIAOZHANQIAOZHANQIAOZHANQIAOZH  |
            |___________________________________|
~~~~~|ZHANQIAOZHANQIAOZHANQIAO|~~~~~~~~~~~~~~~~~~~~~
~~~~~|HANQIAOZHANQIAOZHANQIAOZ|~~~~~~~~~~~~~~~~~~~~
~~~~~|ANQIAOZHANQIAOZHANQIAOZH|~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   \ZHAN  \ZHANQIAOZHANQIAOZHANQIAOZHANQIAO/  ZHAN/
    \ZHANQ  \ZHANQIAOZHANQIAOZHANQIAOZHANQ/  ZHANQ/
     \ZHANQI  \ZHANQIAOZHANQIAOZHANQIAOZH/  ZHANQI/
      \ZHANQIA  \ZHANQIAOZHANQIAOZHANQIA/  ZHANQIA/
       \ZHANQIAO  \ZHANQIAOZHANQIAOZHAN/  ZHANQIAO/
        \__________\__________________/__________/
        """, r"""
        R
                    ___________________________________________
                   /ROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROMER\
                  /EROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMERO\
                 /ROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕR\
                /________________________________________________\
               /  ()    ()    ()    ()    ()    ()    ()    ()   \
              /  ROME  ROME  ROME  ROME  ROME  ROME  ROME  ROME  \
             /  ()    ()    ()    ()    ()    ()    ()    ()       \
            /______________________________________________________ \
           |  ()    ()    ()    ()    ()    ()    ()    ()    ()    |
           | ROME  ROME  ROME  ROME  ROME  ROME  ROME  ROME  ROME  |
           |  ()    ()    ()    ()    ()    ()    ()    ()    ()    |
           |ROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMERO|
           |EROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕR|
           |ROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕRO|
           |_______________________________________________________|
           |  ()    ()    ()    ()    ()    ()    ()    ()    ()   |
           | ROME  ROME  ROME  ROME  ROME  ROME  ROME  ROME  ROME |
           |  ()    ()    ()    ()    ()    ()    ()    ()    ()   |
           |ROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMERO|
           |EROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕR|
           |ROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕRO|
           |_______________________________________________________|
           |  ()    ()    ()    ()    ()    ()    ()    ()    ()   |
           | ROME  ROME  ROME  ROME  ROME  ROME  ROME  ROME  ROME |
           |  ()    ()    ()    ()    ()    ()    ()    ()    ()   |
           |ROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMERO|
           |EROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕR|
           |ROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕRO|
           |_______________________________________________________|
           |ROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMERO|
           |  []    []    []    []    []    []    []    []    []   |
           |EROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕR|
           |  []    []    []    []    []    []    []    []    []   |
           |ROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕRO|
           |_______________________________________________________|
          /  \ROME/  \ROME/  \ROME/  \ROME/  \ROME/  \ROME/  \  \
         /    \OM/    \OM/    \OM/    \OM/    \OM/    \OM/    \   \
        /      \/      \/      \/      \/      \/      \/      \   \
       /________\______/\______/\______/\______/\______/________\   \
      |ROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROME|
      |EROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMERОE|
      |ROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕROMEROМЕ|
      |_____________________________________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """, r"""
        S
                              *
                             *S*
                            *SHA*
                           *SHAN*
                          *SHANGH*
                         *SHANGHA*
                        *SHANGHAI*
                       *SHANGHAIS*
                      *____________*
                     |SHANGHAISHAN|
                     |HANGHAISHANG|
                     |ANGHAISHANGHAI|
                     |NGHAISHANGHAI|
                     |______________|
                      \SHANGHAISHA/
                       \SHANGHAIS/
                        \SHANGHA/
                         \SHANGH/
                          \SHANG/
                    ______/SHAN/______
                   /SHANGHAISHANGHAISH\
                  /HANGHAISHANGHAISHANG\
                 /ANGHAISHANGHAISHANGHAI\
                /NGHAISHANGHAISHANGHAISH\
               /SHAISHANGHAISHANGHAISHA  \
              /____________________________\
             |SHANGHAISHANGHAISHANGHAISHANG|
             |HANGHAISHANGHAISHANGHAISHANG H|
             |ANGHAISHANGHAISHANGHAISHANGHA|
             |NGHAISHANGHAISHANGHAISHANGHAI|
             |GHAISHANGHAISHANGHAISHANGHAISH|
             |_____________________________|
              \SHANGHAISHANGHAISHANGHAISH/
               \HANGHAISHANGHAISHANGHAI/
                \ANGHAISHANGHAISHANGHA/
                 \NGHAISHANGHAISHANG/
                  \GHAISHANGHAISHA/
                   \________________/
                   |SHANGHAISHANGHA|
                   |HANGHAISHANGHAI|
                   |ANGHAISHANGHAISH|
                   |NGHAISHANGHAISHA|
                   |GHAISHANGHAISHANG|
                   |HAISHANGHAISHANG|
                   |AISHANGHAISHANGHA|
                   |ISHANGHAISHANGHAI|
                   |SHANGHAISHANGHAISH|
                   |HANGHAISHANGHAISHA|
                   |___________________|
                  /|SHANGHAISHANGHAISH|\
                 / |HANGHAISHANGHAISHA| \
                /  |ANGHAISHANGHAISHANG|  \
               /   |NGHAISHANGHAISHANGHA|   \
              /    |GHAISHANGHAISHANGHAI|    \
             /     |____________________|     \
            / []   |SHANGHAISHANGHAISH  | []   \
           /       |HANGHAISHANGHAISHA  |       \
          /________|ANGHAISHANGHAISHANG |________\
         |SHANGHAISHANGHAISHANGHAISHANGHAISHANGHAI|
         |HANGHAISHANGHAISHANGHAISHANGHAISHANGHAISH|
         |ANGHAISHANGHAISHANGHAISHANGHAISHANGHAISHA|
         |NGHAISHANGHAISHANGHAISHANGHAISHANGHAISHANG|
         |GHAISHANGHAISHANGHAISHANGHAISHANGHAISHANGHA|
         |HAISHANGHAISHANGHAISHANGHAISHANGHAISHANGHAI|
         |___________________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """,  r"""
        T
                                   /\
                                  /KI\
                                 /KILI\
                                /KILIM\
                               /KILIMA\
                              /KILIMAN\
                             /KILIMANJ\
                            /KILIMANJA\
                           /KILIMANJAR\
                          /KILIMANJARO\
                         /KILIMANJAROK\
                        /KILIMANJARO  K\
                       /KILIMANJAROKILI\
                      /KILIMANJАРОKILIM\
                     /KILIMANJАROKILIMA\
                    /KILIMANJARОKILIMAN\
                   /KILIMANJАROKILIMANJ\
                  /KILIMANJAROKILIMANJA\
                 /KILIMANJAROKILIMANJАR\
                /KILIMANJAROKILIMANJARO\
               /KILIMANJAROKILIMANJАROK\
              /KILIMANJАROKILIMANJАROKI\
             /KILIMANJAROKILIMANJАROKIL\
            /KILIMANJAROKILIMANJАROKILI\
           /KILIMANJAROKILIMANJАROKILIM\
          /KILIMANJAROKILIMANJАROKILIMA\
         /KILIMANJAROKILIMANJАROKILIMAN\
        /KILIMANJAROKILIMANJАROKILIMANJ\
       /KILIMANJAROKILIMANJАROKILIMANJA\
      /KILIMANJAROKILIMANJАROKILIMANJАR\
     /KILIMANJAROKILIMANJАROKILIMANJARO\
    /KILIMANJAROKILIMANJАROKILIMANJАROK\
   /KILIMANJAROKILIMANJАROKILIMANJАROKI\
  /KILIMANJAROKILIMANJАROKILIMANJАROKIL\
 /KILIMANJAROKILIMANJАROKILIMANJАROKILI\
/KILIMANJAROKILIMANJАROKILIMANJАROKILIM\
|KILIMANJAROKILIMANJАROKILIMANJАROKILIMA|
|ILIMANJAROKILIMANJАROKILIMANJАROKILIMAN|
|LIMANJAROKILIMANJАROKILIMANJАROKILIMANJ|
|IMANJAROKILIMANJАROKILIMANJАROKILIMANJA|
|MANJAROKILIMANJАROKILIMANJАROKILIMANJАR|
|ANJAROKILIMANJАROKILIMANJАROKILIMANJARO|
|NJAROKILIMANJАROKILIMANJАROKILIMANJАROK|
|JAROKILIMANJАROKILIMANJАROKILIMANJАROKI|
|AROKILIMANJАROKILIMANJАROKILIMANJАROKIL|
|ROKILIMANJАROKILIMANJАROKILIMANJАROKILI|
|OKILIMANJАROKILIMANJАROKILIMANJАROKILIM|
|KILIMANJАROKILIMANJАROKILIMANJАROKILIMA|
|ILIMANJAROKILIMANJАROKILIMANJАROKILIMAN|
|____________________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
        """, r"""
        U
                    /\                    /\
                   /US\                  /US\
                  /USHУ\                /USHU\
                 /USHУAI\              /USHUAI\
                /USHUAIA \            /USHUAIA \
               /USHUAIAUSH\          /USHUAIAUSH\
              /USHUAIAUSHUA\        /USHUAIAUSHUA\
             /USHUAIAUSHUAI\       /USHUAIAUSHUAI\
            /USHUAIAUSHUAIA\      /USHUAIAUSHUAIA\
           /USHUAIAUSHUAIAU\     /USHUAIAUSHUAIAU\
          /__________________\  /______________________\
         |USHUAIAUSHUAIAUSHUА|  |USHUAIAUSHUAIAUSHUAIAU|
         |SHUAIAUSHUAIAUSHUAI|  |SHUAIAUSHUAIAUSHUAIAUS|
         |HUAIAUSHUAIAUSHUAIA|  |HUAIAUSHUAIAUSHUAIAUSH|
         |UAIAUSHUAIAUSHUAIAU|  |UAIAUSHUAIAUSHUAIAUSHU|
         |AIAUSHUAIAUSHUAIAUS|  |AIAUSHUAIAUSHUAIAUSHUA|
         |IAUSHUAIAUSHUAIAUSH|  |IAUSHUAIAUSHUAIAUSHУAI|
         |___________________|  |______________________|
        /|USHUAIAUSHUAIAUSHUА|  |USHUAIAUSHUAIAUSHUAIAU|\
       / |SHUAIAUSHUAIAUSHUAI|  |SHUAIAUSHUAIAUSHUAIAUS| \
      /  |HUAIAUSHUAIAUSHUAIA|  |HUAIAUSHUAIAUSHUAIAUSH|  \
     /   |___________________|  |______________________|   \
    / [] |USHUAIAUSHUAIAUSHUА|  |USHUAIAUSHUAIAUSHUAIAU| [] \
   /_____|___________________|__|______________________|_____\
  |USHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSH|
  |SHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHU|
  |HUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUA|
  |UAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAI|
  |AIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIA|
  |___________________________________________________________|
  |USHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSH|
  |SHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHU|
  |HUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUA|
  |UAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAI|
  |___________________________________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   \USHУ  \USHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIAUSH/  USHU/
    \USHУA  \USHUAIAUSHUAIAUSHUAIAUSHUAIAUSHUAIA/  USHUA/
     \USHУAI  \USHUAIAUSHUAIAUSHUAIAUSHUAIAUSH/  USHUAI/
      \USHUAIA  \USHUAIAUSHUAIAUSHUAIAUSHUAIA/  USHUAIA/
       \USHUAIAU  \USHUAIAUSHUAIAUSHUAIAUSH/  USHUAIAU/
        \USHUAIAUS  \USHUAIAUSHUAIAUSHUAIA/  USHUAIAUS/
         \USHUAIAUSH  \USHUAIAUSHUAIAUSH/  USHUAIAUSH/
          \USHUAIAUSHU  \USHUAIAUSHUAIA/  USHUAIAUSHU/
           \USHUAIAUSHUA  \USHUAIAUSH/  USHUAIAUSHUA/
            \USHUAIAUSHUAI  \USHUAIA/  USHUAIAUSHUAI/
             \USHUAIAUSHUAIA  \USHУ/  USHUAIAUSHUAIA/
              \________________\__/________________/
               \USHUAIAUSHUAIA/  \USHUAIAUSHUAIA/
                \USHUAIAUSHUА/    \USHUAIAUSHUА/
                 \USHUAIAUSH/      \USHUAIAUSH/
                  \USHUAIAU/                
        """, r"""
        V
                    /\      /\      /\      /\      /\
                   /VE\    /VE\    /VE\    /VE\    /VE\
                  /VENI\  /VENI\  /VENI\  /VENI\  /VENI\
                 /VENICE\/VENICE\/VENICE\/VENICE\/VENICE\
                /________\______/________\______/________\
               /VENICEVENICE\  /VENICEVENICE\  /VENICEVENICE\
              /ENICEVENICEV  \/ENICEVENICEV  \/ENICEVENICEV  \
             /_______________\/_______________\/_______________\
            |VENICEVENICEV () |VENICEVENICEV ()| VENICEVENICEV|
            |ENICEVENICEV     |ENICEVENICEV    | ENICEVENICEV |
            |NICEVENICEV  []  |NICEVENICEV []  | NICEVENICEV  |
            |ICEVENICEV       |ICEVENICEV      | ICEVENICEV   |
            |CEVENICEV   ()   |CEVENICEV  ()   | CEVENICEV    |
            |EVENICEV         |EVENICEV        | EVENICEV     |
            |VENICEV    []    |VENICEV   []    | VENICEV      |
            |VENICE           |VENICE          | VENICE       |
            |_________________|________________|______________|
           /|VENICEVENICEVENI | VENICEVENICEVEN|ICEVENICEVENICE|\
          / |ENICEVENICEV     | ENICEVENICEV   |VENICEVENICEVEN| \
         /  |NICEVENICEVEN    | NICEVENICEVEN  |ENICEVENICEV   |  \
        / ()|________________ |________________|_______________|()\
       /    |VENICEVENICEVENI | VENICEVENICEVEN|ICEVENICEVENICE|   \
      / []  |ENICEVENICEV     | ENICEVENICEV   |VENICEVENICEVE| []  \
     /      |NICEVENICEVEN    | NICEVENICEVEN  |ENICEVENICEV   |     \
    /  ()   |ICEVENICEV       | ICEVENICEV     |NICEVENICEVEN  | ()   \
   /________|_________________|________________|_______________|_______\
   |VENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICE|
   |ENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVE|
   |NICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENIV|
   |ICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICE|
   |CEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVE|
   |EVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENICEVENIV|
   |__________________________________________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      ~~~ ~~~~  ~(VENICE)~  ~~~~  ~(VENICE)~  ~~~~  ~(VENICE)~  ~~~
   ~~~  \VENICE/  ~~~  \VENICE/  ~~~  \VENICE/  ~~~  \VENICE/  ~~~
  ~~  ~~~\VENI/~~~ ~~~  \VENI/ ~~~  ~~~\VENI/~~~  ~~~\VENI/  ~~~  ~~
 ~~~       \VE/      ~~~  \VE/  ~~~      \VE/  ~~~     \VE/    ~~~
~~          \/         ~~~  \/  ~~~       \/    ~~~      \/      ~~~        
        """, r"""
        W
                    /\              /\
                   /WR\            /WR\
                  /WROC\          /WROC\
                 /WROCLA\        /WROCLA\
                /WROCLAW \      /WROCLAW \
               /WROCLAWWR\    /WROCLAWWR \
              /____________\  /____________\
             |WROCLAWWROCLA|  |WROCLAWWROCLA|
             |ROCLAWWROCLAW|  |ROCLAWWROCLAW|
             |OCLAWWROCLAWW|  |OCLAWWROCLAWW|
             |CLAWWROCLAWWR|  |CLAWWROCLAWWR|
             |LAWWROCLAWWRO|  |LAWWROCLAWWRO|
             |AWWROCLAWWROC|  |AWWROCLAWWROC|
             |_____________|  |_____________|
            /|WROCLAWWROCLA|  |WROCLAWWROCLA|\
           / |ROCLAWWROCLAW|  |ROCLAWWROCLAW| \
          /  |OCLAWWROCLAWW|  |OCLAWWROCLAWW|  \
         /   |_____________|  |_____________|   \
        / () |WROCLAWWROCLA|  |WROCLAWWROCLA| () \
       /     |ROCLAWWROCLAW|  |ROCLAWWROCLAW|     \
      / []   |OCLAWWROCLAWW|  |OCLAWWROCLAWW| []  \
     /       |_____________|__|_____________|      \
    /__________|WROCLAWWROCLAWWROCLAWWROCLAWW|______\
   |WROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLA|
   |ROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAW|
   |OCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWW|
   |CLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWR|
   |LAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWRO|
   |AWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROC|
   |WWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCL|
   |________________________________________________|
   |WROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLA|
   |ROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAW|
   |OCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWW|
   |CLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWR|
   |LAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWRO|
   |AWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROC|
   |________________________________________________|
   |WROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLA|
   |ROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAW|
   |OCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWW|
   |CLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWROCLAWWR|
   |________________________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """, r"""
        X
                    /\              /\              /\
                   /XI\            /XI\            /XI\
                  /XIAN\          /XIAN\          /XIAN\
                 /XIANXI\        /XIANXI\        /XIANXI\
                /XIANXIAN\      /XIANXIAN\      /XIANXIAN\
               /____________\  /____________\  /____________\
              |XIANXIANXIANX|  |XIANXIANXIANX|  |XIANXIANXIANX|
              |IANXIANXIANXI|  |IANXIANXIANXI|  |IANXIANXIANXI|
              |ANXIANXIANXIA|  |ANXIANXIANXIA|  |ANXIANXIANXIA|
              |NXIANXIANXIAN|  |NXIANXIANXIAN|  |NXIANXIANXIAN|
              |XIANXIANXIANX|  |XIANXIANXIANX|  |XIANXIANXIANX|
              |IANXIANXIANXI|  |IANXIANXIANXI|  |IANXIANXIANXI|
              |_____________|  |_____________|  |_____________|
              |  (o_o)  (o_o)  |  (o_o) (o_o) |  (o_o) (o_o) |
              |XIANXIANXIANX|  |XIANXIANXIANX|  |XIANXIANXIANX|
              |IANXIANXIANXI|  |IANXIANXIANXI|  |IANXIANXIANXI|
              |ANXIANXIANXIA|  |ANXIANXIANXIA|  |ANXIANXIANXIA|
              |NXIANXIANXIAN|  |NXIANXIANXIAN|  |NXIANXIANXIAN|
              |_____________|  |_____________|  |_____________|
         _____|XIANXIANXIANX|__|XIANXIANXIANX|__|XIANXIANXIANX|_____
        |XIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIA|
        |IANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIAN|
        |(o_o) (o_o) (o_o) (o_o) (o_o) (o_o) (o_o) (o_o) (o_o)    |
        |XIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIA|
        |IANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIAN|
        |(o_o) (o_o) (o_o) (o_o) (o_o) (o_o) (o_o) (o_o) (o_o)    |
        |XIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIA|
        |IANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIAN|
        |(o_o) (o_o) (o_o) (o_o) (o_o) (o_o) (o_o) (o_o) (o_o)    |
        |XIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIA|
        |IANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIAN|
        |(o_o) (o_o) (o_o) (o_o) (o_o) (o_o) (o_o) (o_o) (o_o)    |
        |XIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIA|
        |IANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIAN|
        |___________________________________________________________|
       /|XIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXI |\
      / |IANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIAN| \
     /  |ANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANX|  \
    /   |NXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXI|   \
   /    |___________________________________________________________|    \
  / []  |XIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXI | [] \
 /______|IANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIAN|_____\
|XIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANX|
|IANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXI|
|ANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIA|
|NXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIANXIAN|
|___________________________________________________________________________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      
        """, r"""
        Y
                              *
                             *S*
                            *SHW*
                           *SHWED*
                          *SHWEDAGO*
                         *SHWEDAGON*
                        *SHWEDAGONS*
                       *SHWEDAGONSH*
                      *SHWEDAGONSHW*
                     *SHWEDAGONSHWE*
                    *SHWEDAGONSHWED*
                   *SHWEDAGONSHWEDA*
                  *SHWEDAGONSHWEDAG*
                 *SHWEDAGONSHWEDAGO*
                *SHWEDAGONSHWEDAGON*
               *______________________*
              /|SHWEDAGONSHWEDAGONSSHW|\
             / |HWEDAGONSHWEDAGONSHWED| \
            /  |WEDAGONSHWEDAGONSHWEDA|  \
           /   |EDAGONSHWEDAGONSHWEDAGO|  \
          /    |DAGONSHWEDAGONSHWEDAGON|   \
         /     |________________________|   \
        /  ()  |SHWEDAGONSHWEDAGONSHWED| ()  \
       /       |HWEDAGONSHWEDAGONSHWEDA|      \
      /________| WEDAGONSHWEDAGONSHWED |_______\
     |SHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDA|
     |HWEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAG|
     |WEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGO|
     |EDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGON|
     |___________________________________________|
    /|SHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDA |\
   / |HWEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAG | \
  /  |WEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGO |  \
 / ()|EDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGON |() \
/    |___________________________________________|    \
|SHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGO|
|HWEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGON|
|WEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGONS|
|EDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSHWEDAGONSH|
|___________________________________________________|
    /\          /\                    /\          /\
   /SH\        /SH\                  /SH\        /SH\
  /SHWE\      /SHWE\                /SHWE\      /SHWE\
 /SHWED\     /SHWED\                /SHWED\    /SHWED\
/SHWEDА\    /SHWEDA\                /SHWEDA\  /SHWEDA\
|SHWEDAG|   |SHWEDAG|              |SHWEDAG|  |SHWEDAG|
|SHWEDAGO|  |SHWEDAGO|            |SHWEDAGO|  |SHWEDAGO|
|SHWEDAGON| |SHWEDAGON|          |SHWEDAGON|  |SHWEDAGON|
|_________|  |_________|          |_________|  |_________|
|SHWEDAGO|   |SHWEDAGO|          |SHWEDAGO|    |SHWEDAGO|
|SHWEDAGO|   |SHWEDAGO|          |SHWEDAGO|    |SHWEDAGO|
|_________|  |_________|          |_________|  |_________|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~         
        """, r"""
         Z
                    /\              /\
                   /SH\            /SH\
                  /SHAO\          /SHAO\
                 /SHAOLI\        /SHAOLI\
                /SHAOLIN \      /SHAOLIN \
               /SHAOLINSH\    /SHAOLINSH\
              /SHAOLINSHAO\  /SHAOLINSHAO\
             /______________\/____________\
            |SHAOLINSHAOLINSH|SHAOLINSHAO|
            |HAOLINSHAOLINSHA|OLINSHAOLING|
            |AOLINSHAOLINSHAO|LINSHAOLINSH|
            |OLINSHAOLINSHAO |INSHAOLINSHA|
            |LINSHAOLINSHAO  |NSHAOLINSHAO|
            |INSHAOLINSHAO   |SHAOLINSHAO |
            |________________|____________|
           /|\SHAOLINSHAOLINSH|SHAOLINSHA/|\
          / | \HAOLINSHAOLINSHA|OLINSHAO/ | \
         /  |  \AOLINSHAOLINSHA|LINSHAO/  |  \
        /   |   \______________|________/  |   \
       /  []|    |SHAOLINSHAOLINSHAOLINSH| |[]  \
      /     |    |HAOLINSHAOLINSHAOLINSHA| |     \
     /      |    |AOLINSHAOLINSHAOLINSHAO| |      \
    /       |    |OLINSHAOLINSHAOLINSHAO | |       \
   /   ()   |    |LINSHAOLINSHAOLINSHAO  | |   ()   \
  /         |    |________________________| |         \
 /__________|____|SHAOLINSHAOLINSHAOLINSH|__|__________\
|SHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAO|
|HAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAO |
|AOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAO  |
|OLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAO   |
|LINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAO    |
|INSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAO     |
|NSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAO      |
|SHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAO       |
|_____________________________________________________|
|SHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHA|
|HAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAO|
|AOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAO |
|OLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAO  |
|LINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAOLINSHAO   |
|____________________________________________________|
        """)
    def __init__(self, txt):
        self.txt = txt
        self.encoded_images = []        #Characters List creation

        for char in txt:
            c = char.lower()
            if c in Encoder._char_index:            #Selecting which character
                idx = Encoder._char_index[c]
                self.encoded_images.append(Encoder.images[idx])        #Selecting what img to use with what character
            elif c in self.Special_C:
                L_img = list(Encoder.images[0])
                A_count = 0
                i = 0
                while i < len(L_img):
                    if L_img[i] == "A":
                        A_count += 1
                        if A_count == 5:
                            L_img[i] = c
                            self.encoded_images.append("".join(L_img))
                            break
                    i += 1
                else:
                    self.encoded_images.append(None)
            else:
                # Non recognizable characters
                self.encoded_images.append(None)
        k = 0
        n = len(self.encoded_images)

        for j in range(n):
            if k == 0:
                if j + 3 < n:
                    self.encoded_images[j], self.encoded_images[j+3] = self.encoded_images[j+3], self.encoded_images[j]
            elif k == 1:
                if j + 1 < n:
                    self.encoded_images[j], self.encoded_images[j+1] = self.encoded_images[j+1], self.encoded_images[j]
            elif k == 4:
                if j - 3 >= 0:
                    self.encoded_images[j], self.encoded_images[j-3] = self.encoded_images[j-3], self.encoded_images[j]

            k = (k + 1) % 5

    def encode(self):
        result = []
        for char, img in zip(self.txt, self.encoded_images):
            if img is not None:
                result.append((char.lower(), img))
        return result

# ============================================ #
# //             main() Function            // #
# ============================================ #

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {__program__} <input_file> <output_file>")
        sys.exit(1)

    input_file  = sys.argv[1]
    output_file = sys.argv[2]

    # --- Read input file ---
    if not os.path.exists(input_file):
        print(f"Error: input file '{input_file}' not found.")
        sys.exit(1)

    with open(input_file, "r", encoding="utf-8") as f:
        message = f.read().strip()

    if not message:
        print("Error: input file is empty.")
        sys.exit(1)

    # --- Encode the message ---
    encoder = Encoder(message)
    encoded = encoder.encode()

    if not encoded:
        print("Error: no encodable characters found (letters only).")
        sys.exit(1)

    # --- Write output file ---
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Total encoded characters: {len(encoded)} Good Luck decoding!\n")
        f.write("=" * 100 + "\n\n")
        for char, img in encoded:
            f.write(img)
            f.write("\n" + "-" * 100 + "\n")

    print(f"File encoded successfully")
    print(f"  Input : {input_file}  ({len(message)} chars)")
    print(f"  Output: {output_file} ({len(encoded)} images written)")
