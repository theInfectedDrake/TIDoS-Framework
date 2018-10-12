#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires TIDoS Framework
#https://github.com/theInfectedDrake/TIDoS-Framework

from core.Core.colors import *

auxilban_art = C+'''
\033[1;37m
      '      .      +          .    .       '       +           '         .       .
          .                    '               +          .         *          .
                +            '                                       .        +
        .             *        .     .       .          *        .        *
             .    \033[1;33m _\033[1;37m     .     .            .       .
      .    .  \033[1;33m _  / | \033[1;37m     .        .  *        \033[1;33m _ \033[1;37m .     .    +
              \033[1;33m| \_| | \033[1;37m           +          .   \033[1;33m| | __
           \033[1;33m _ |     |\033[1;37m       .           _       \033[1;33m| |/  |
       +   \033[1;33m| \      |     \033[1;36m _/\_        \033[1;33m| |     /  |    \  \033[1;37m +      /
           \033[1;33m|  |     \    \033[1;36m+/_\/_\+      \033[1;33m| |    /   |     \  \033[1;37m   .  |\033[1;34m
      ____\033[1;33m/____\--...\___ \033[1;36m\_||_/\033[1;34m ___...\033[1;33m|__\_\033[1;34m..\033[1;33m|____\____/\033[1;34m_______/_\033[1;34m
            .     .      \033[1;36m|_|__|_| \033[1;34m        .       .  .
         .    . .       \033[1;36m_/ /__\ \_\033[1;34m .          .            .   .
              .       .    .           .    .    .
         .      '                         '                    '      '
             '     \033[1;33m-=[\033[1;31m A U X I L L A R I E S \033[1;33m]=-\033[1;34m     .     '      .
       .             '       .          .       '       .
'''

scanenumban_art = """
                   \033[1;33m,-.        .      \033[1;37m   +           .                   +
\033[1;37m           *     \033[1;33m / \  `. \033[1;31m __..-,O \033[1;37m           +         *        .
\033[1;37m       +         \033[1;33m:   \ \033[1;31m--''_..-'.'
\033[1;37m                 \033[1;33m|    . \033[1;31m.-' `. '.\033[1;37m           +       .      .      +      +
\033[1;37m         .       \033[1;33m:     .     \033[1;31m.`.' \033[1;37m
\033[1;37m                 \033[1;33m \     `.  \033[1;31m/  ..  \033[1;37m     .          +            +      .
\033[1;37m           +      \033[1;33m \      `.   \033[1;31m' \033[1;33m.  \033[1;37m         *            .
\033[1;37m                   \033[1;33m `,       `.   \  \033[1;37m                +           +
\033[1;37m           .       \033[1;36m,|,\033[1;33m`.        `-.\  \033[1;37m     *      .
\033[1;37m       +          \033[1;36m'.|| \033[1;33m ``-...__..-`  \033[1;37m                            '
\033[1;37m               +   \033[1;36m|  |                      \033[1;37m  .          *           +
\033[1;37m          *        \033[1;36m|__|         \033[1;37m          +           *         .
\033[1;37m     .             \033[1;36m/||\      \033[1;37m     .
\033[1;37m               .  \033[1;36m//||\＼    \033[1;37m +    \033[1;33m-=[ \033[1;31mP R O B E  &  E N U M E R A T E \033[1;33m]=-\033[1;37m
\033[1;37m        +        \033[1;36m// || \＼    \033[1;37m               +
\033[1;37m             \033[1;36m __//__||__\＼_   \033[1;37m     .             .       *   .       +
\033[1;33m ____________\033[1;36m'--------------'\033[1;33m____________________________________________    """

exploitsban_art = '''
   \033[1;33m|\                      \033[1;33m/)
\033[1;37m /\_\033[1;33m\＼\033[1;37m__               \033[1;33m(_//
\033[1;37m|   `>＼-`    \033[1;36m_._        \033[1;33m//`)
\033[1;37m \ /` \033[1;33m\＼\033[1;36m  _.-\033[1;34m:::\033[1;36m`-._   \033[1;33m//
\033[1;37m  `    \033[1;33m\|\033[1;36m`    \033[1;34m:::   \033[1;36m `|\033[1;33m//     \033[1;37m[0x00] \033[1;31mE X P L O I T S
\033[1;36m        |    \033[1;34m :::     \033[1;36m|\033[1;33m/
\033[1;36m        |\033[1;34m.....:::.....\033[1;36m|                         \033[1;31mC A S T L E \033[1;37m[0x00]
\033[1;36m        |\033[1;34m:::::::::::::\033[1;36m|
\033[1;36m        |     \033[1;34m:::     \033[1;36m|
\033[1;36m        \    \033[1;34m :::     \033[1;36m/
\033[1;36m         \   \033[1;34m :::   \033[1;36m /   \033[1;37m" [0x00] \033[1;33mCode the Exploits
\033[1;36m          `-. \033[1;34m:::\033[1;36m .-'                   \033[1;33mand
           \033[1;33m//\033[1;36m`:::`\033[1;33m\＼             \033[1;33mExploit the Codes \033[1;37m[0x00] "
          \033[1;33m//   \033[1;36m'   \033[1;33m\＼
         |/         \033[1;33m\|        '''

footprintban_art = """
\033[1;36m

\033[1;37m                .                                            .
     *   .                  .              .        .   *          .
  .         .                     .       .           . \033[1;35m ###
        \033[1;35mo     \033[1;33m-=[ \033[1;31mR E C O N N A I S S A N C E \033[1;33m]=- \033[1;35m     > ######-\033[1;37m   --0
    +    .              .                  .             \033[1;35m###
          \033[1;35m0\033[37m     .               .              .
                 .          .         +        ,                ,    ,
 .          \033[1;35m\ \033[37m          .                         .      + .
      .      \033[1;35m\ \033[36m   .             . \033[1;36m###\033[1;37m         .
   .          \033[1;35mo \033[36m    .         \033[1;33m> \033[1;36m###########-    --0\033[1;37m      .              +
     .         \033[36m\              \033[1;36m########\033[1;37m           .                .
               \033[34m#\##\##.       \033[1;33m> \033[1;36m###########-           --0\033[1;37m      .        .
        +    \033[34m#  #O##\###         \033[1;36m###\033[1;37m    .                 +       .
   .        \033[34m#*#  #\##\###\033[37m                       .  +                   .
        .   \033[34m##*#  #\##\##\033[37m     +          .
      .      \033[34m##*#  #o##\# \033[37m        .                       *      ,       .
          .    \033[34m**#  #\# \033[37m    .                    .             .
 +                    \          .     \033[33m/\^    \033[37m      \033[1;33m.".                 \033[1;33m/
\033[1;33m____^/\___^--____/\____\033[1;31mO\033[1;33m_____________/   \/\___________/\/   \______________
   /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                         --  __"""

vulnban_art = R+r"""
                     .....
               .:noONNNNNNNOon:.
            .:NNNNNNNmddddNNNNNNN:.
          :NNNNmy+:.   +   .:+ymNNNN:
         NNNNy:`       +       `:yNNNN
       NNNNy.                     -!NNNN
      NNNN/            +            \NNNN
     NNNm-         .:#####:.         -mNNN      \033[1;37m[0x00] \033[1;33mV U L N E R A B I L I T Y \033[1;31m
    :NNN+         #    +    #         +NNN:
    NNNm         #     +     #         mNNN                   \033[1;33mE N U M E R A T I O N\033[1;31m \033[1;37m[0x00]
    NNNh+++    ++#+++++++++++#++    +++hNNN
    NNNm         #     +     #         mNNN
    :NNN+         #    +    #         +NNN:
     NNNm-         *:#####:*         -mNNN
      NNNN\            +            /NNNN
       NNNNy.                     -yNNNN
         NNNNy:`       +       `:yNNNN"
          :NNNNmy+:.   +   .:+ymNNNN:
            *:NNNNNNNmddddNNNNNNNN*
               *:!NNNNNNNNNNN!:*
                    '''*'''

"""

bugsban_art = C+'''
\033[1;34m
  +------------------------------------------------------+
  |      \033[1;37mTIDoS Dialog                      \033[1;33m[-] [口] [×]  \033[1;34m|
  | ---------------------------------------------------- |
\033[1;36m  |                                                      |
  |  \033[1;33mTIDoS has detected that you want to hunt for bugs! \033[1;36m |
  |   \033[1;33mDo you wish to continue?                          \033[1;36m |
  |                                                      |
  |     \033[1;37m.----------.   .----------.    .----------.      \033[1;36m|
  |     \033[1;37m|    Yes   \033[1;37m|   |    No    \033[1;37m|    |   Maybe  \033[1;37m|      \033[1;36m|
  |     \033[1;37m'----------'   '----------'    '----------'     \033[1;36m |
  |______________________________________________________|

'''

tidosrules_art = """
                _nnnn_
               dGGGGMMb
              @p~qp~~qMb     {}TIDoS Rules!!!
              M(\033[37m@\033[96m)(\033[37m@\033[96m) M|   {}_;
              @\033[33m,----.\033[96mJM| {}-'
             JS^\033[33m\__/  \033[96mqKL
            dZP        qKRb
           dZP          qKKb
          fZP            SMMb
          HZM            MMMM
          FqM            MMMM
         \033[33m_| '.        |\033[96mdS'qML'
        \033[33m|    `.       | `' \_\033[96mZq'
       \033[33m_)      \.___.,|     .'
       \033[33m\________)\033[96mMMMMM\033[33m|   .'""".format(O, GR, GR)
