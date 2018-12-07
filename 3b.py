# input = """#1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2"""

input = """#1 @ 704,926: 5x4
#2 @ 272,413: 16x11
#3 @ 579,814: 26x29
#4 @ 526,479: 20x15
#5 @ 401,179: 15x11
#6 @ 916,565: 22x15
#7 @ 276,610: 28x29
#8 @ 235,942: 9x5
#9 @ 574,938: 15x26
#10 @ 768,180: 19x18
#11 @ 782,9: 26x17
#12 @ 579,718: 17x21
#13 @ 344,683: 13x22
#14 @ 212,343: 13x27
#15 @ 61,211: 22x10
#16 @ 184,929: 10x27
#17 @ 405,911: 27x28
#18 @ 333,433: 22x26
#19 @ 211,442: 25x29
#20 @ 346,516: 18x20
#21 @ 774,538: 12x12
#22 @ 122,486: 18x23
#23 @ 35,289: 16x23
#24 @ 963,538: 25x22
#25 @ 681,488: 15x27
#26 @ 199,207: 14x14
#27 @ 31,426: 28x14
#28 @ 253,717: 29x17
#29 @ 799,142: 12x12
#30 @ 614,209: 18x20
#31 @ 361,252: 26x19
#32 @ 832,730: 17x25
#33 @ 787,625: 11x12
#34 @ 862,760: 28x23
#35 @ 840,407: 15x19
#36 @ 836,410: 26x10
#37 @ 772,536: 20x21
#38 @ 169,391: 15x12
#39 @ 799,921: 23x16
#40 @ 163,398: 11x15
#41 @ 231,210: 18x10
#42 @ 638,289: 10x26
#43 @ 339,430: 21x27
#44 @ 303,88: 20x15
#45 @ 102,216: 26x21
#46 @ 496,577: 12x23
#47 @ 254,333: 14x28
#48 @ 763,544: 21x12
#49 @ 274,682: 19x26
#50 @ 748,231: 13x14
#51 @ 708,930: 12x14
#52 @ 594,627: 29x17
#53 @ 513,571: 24x21
#54 @ 353,181: 19x28
#55 @ 155,857: 27x26
#56 @ 729,277: 24x17
#57 @ 838,575: 15x12
#58 @ 202,9: 20x17
#59 @ 657,929: 13x14
#60 @ 835,405: 10x19
#61 @ 687,419: 22x22
#62 @ 392,85: 12x10
#63 @ 458,200: 19x15
#64 @ 684,478: 26x25
#65 @ 904,272: 26x10
#66 @ 778,291: 23x11
#67 @ 953,385: 27x29
#68 @ 788,536: 27x11
#69 @ 569,859: 26x21
#70 @ 242,123: 29x15
#71 @ 870,260: 13x17
#72 @ 721,739: 21x11
#73 @ 859,567: 23x19
#74 @ 904,810: 21x24
#75 @ 355,84: 29x24
#76 @ 458,137: 26x14
#77 @ 527,125: 15x29
#78 @ 100,259: 13x27
#79 @ 859,436: 16x28
#80 @ 640,700: 19x25
#81 @ 68,298: 21x11
#82 @ 939,728: 26x17
#83 @ 866,652: 19x17
#84 @ 142,165: 17x25
#85 @ 375,743: 18x20
#86 @ 105,210: 13x13
#87 @ 183,743: 17x17
#88 @ 203,690: 13x15
#89 @ 320,139: 22x22
#90 @ 815,950: 23x23
#91 @ 918,469: 16x28
#92 @ 55,890: 22x15
#93 @ 706,27: 26x11
#94 @ 606,839: 26x11
#95 @ 885,591: 19x22
#96 @ 532,510: 21x12
#97 @ 970,460: 19x15
#98 @ 368,133: 16x11
#99 @ 291,551: 22x28
#100 @ 591,329: 26x16
#101 @ 604,604: 25x22
#102 @ 270,971: 10x11
#103 @ 375,757: 27x22
#104 @ 907,703: 24x26
#105 @ 825,281: 27x15
#106 @ 710,101: 23x14
#107 @ 596,261: 26x26
#108 @ 160,432: 20x22
#109 @ 575,808: 15x11
#110 @ 669,109: 16x18
#111 @ 372,686: 20x16
#112 @ 1,144: 20x13
#113 @ 99,154: 12x14
#114 @ 586,33: 26x20
#115 @ 346,824: 27x14
#116 @ 541,939: 27x22
#117 @ 731,898: 21x20
#118 @ 352,660: 23x23
#119 @ 81,703: 13x20
#120 @ 405,401: 14x16
#121 @ 906,269: 12x17
#122 @ 902,544: 23x20
#123 @ 90,22: 28x28
#124 @ 718,17: 10x28
#125 @ 428,753: 11x21
#126 @ 683,743: 20x20
#127 @ 391,568: 12x29
#128 @ 944,800: 18x12
#129 @ 750,513: 14x13
#130 @ 73,202: 27x23
#131 @ 185,647: 19x19
#132 @ 168,173: 22x13
#133 @ 680,152: 11x22
#134 @ 360,53: 21x16
#135 @ 352,507: 12x20
#136 @ 165,494: 13x10
#137 @ 945,499: 7x3
#138 @ 914,300: 14x10
#139 @ 445,970: 20x18
#140 @ 630,66: 13x11
#141 @ 476,423: 24x22
#142 @ 860,898: 11x16
#143 @ 85,332: 21x20
#144 @ 198,686: 27x28
#145 @ 623,320: 16x26
#146 @ 872,927: 20x24
#147 @ 980,935: 14x19
#148 @ 699,599: 11x15
#149 @ 100,500: 19x27
#150 @ 903,496: 24x14
#151 @ 299,9: 13x10
#152 @ 33,47: 11x26
#153 @ 453,551: 18x27
#154 @ 77,454: 12x16
#155 @ 329,630: 19x10
#156 @ 305,341: 10x19
#157 @ 754,921: 11x15
#158 @ 137,600: 20x22
#159 @ 582,260: 21x19
#160 @ 638,538: 17x27
#161 @ 297,585: 21x12
#162 @ 303,459: 17x12
#163 @ 848,890: 15x19
#164 @ 76,479: 18x13
#165 @ 179,790: 24x22
#166 @ 642,941: 18x29
#167 @ 539,150: 6x7
#168 @ 927,64: 15x18
#169 @ 665,843: 12x18
#170 @ 409,940: 27x18
#171 @ 915,51: 12x28
#172 @ 956,142: 11x21
#173 @ 612,418: 12x28
#174 @ 281,889: 22x10
#175 @ 654,930: 22x22
#176 @ 932,577: 23x11
#177 @ 67,283: 26x20
#178 @ 856,135: 17x27
#179 @ 649,559: 15x24
#180 @ 51,14: 18x18
#181 @ 366,85: 20x21
#182 @ 666,695: 10x16
#183 @ 628,698: 16x15
#184 @ 379,765: 22x19
#185 @ 550,857: 22x25
#186 @ 822,660: 22x17
#187 @ 314,18: 28x19
#188 @ 675,210: 28x21
#189 @ 371,441: 19x19
#190 @ 331,16: 24x24
#191 @ 644,328: 5x3
#192 @ 17,426: 15x14
#193 @ 115,508: 22x10
#194 @ 652,312: 26x12
#195 @ 590,232: 15x25
#196 @ 332,367: 26x15
#197 @ 316,152: 22x24
#198 @ 298,608: 25x20
#199 @ 604,770: 18x13
#200 @ 697,875: 11x21
#201 @ 384,376: 16x23
#202 @ 307,341: 23x16
#203 @ 492,200: 18x11
#204 @ 971,4: 10x11
#205 @ 71,933: 10x21
#206 @ 769,185: 18x14
#207 @ 297,632: 23x18
#208 @ 665,921: 25x10
#209 @ 828,553: 16x24
#210 @ 338,857: 22x11
#211 @ 8,135: 17x18
#212 @ 526,481: 19x28
#213 @ 144,497: 16x26
#214 @ 583,362: 23x26
#215 @ 39,425: 13x21
#216 @ 333,244: 21x16
#217 @ 901,959: 17x29
#218 @ 765,424: 23x10
#219 @ 178,252: 15x19
#220 @ 131,785: 19x12
#221 @ 84,287: 12x11
#222 @ 215,958: 21x19
#223 @ 550,122: 19x26
#224 @ 847,554: 18x17
#225 @ 71,492: 21x25
#226 @ 542,649: 22x11
#227 @ 550,282: 24x11
#228 @ 685,115: 25x11
#229 @ 379,221: 27x12
#230 @ 363,732: 26x17
#231 @ 707,22: 18x12
#232 @ 542,371: 12x13
#233 @ 626,615: 16x21
#234 @ 191,733: 25x25
#235 @ 314,88: 16x29
#236 @ 113,254: 21x15
#237 @ 322,2: 22x20
#238 @ 672,43: 21x22
#239 @ 799,513: 15x27
#240 @ 84,31: 26x18
#241 @ 727,957: 12x26
#242 @ 551,874: 15x13
#243 @ 176,379: 18x23
#244 @ 649,121: 16x15
#245 @ 540,556: 27x15
#246 @ 802,148: 21x13
#247 @ 941,382: 25x15
#248 @ 611,620: 27x11
#249 @ 823,953: 14x14
#250 @ 638,407: 13x27
#251 @ 333,20: 16x11
#252 @ 152,819: 20x11
#253 @ 433,384: 25x29
#254 @ 224,939: 29x12
#255 @ 500,961: 18x18
#256 @ 348,562: 11x15
#257 @ 330,242: 22x27
#258 @ 734,279: 23x13
#259 @ 663,413: 22x20
#260 @ 75,881: 14x27
#261 @ 21,72: 26x21
#262 @ 56,247: 18x24
#263 @ 220,338: 16x13
#264 @ 801,933: 16x29
#265 @ 670,821: 27x29
#266 @ 672,733: 27x20
#267 @ 2,143: 14x10
#268 @ 583,957: 15x29
#269 @ 896,626: 7x12
#270 @ 422,972: 18x15
#271 @ 871,726: 23x14
#272 @ 68,52: 14x17
#273 @ 841,711: 28x24
#274 @ 424,314: 11x16
#275 @ 814,73: 13x27
#276 @ 305,106: 24x18
#277 @ 928,394: 18x27
#278 @ 94,532: 23x28
#279 @ 248,53: 17x24
#280 @ 164,516: 18x27
#281 @ 597,824: 28x26
#282 @ 931,307: 25x10
#283 @ 732,661: 19x20
#284 @ 179,560: 28x28
#285 @ 288,542: 18x10
#286 @ 206,229: 26x22
#287 @ 52,352: 28x15
#288 @ 400,221: 21x26
#289 @ 741,518: 27x10
#290 @ 917,746: 24x26
#291 @ 788,916: 15x22
#292 @ 639,311: 29x17
#293 @ 752,139: 23x29
#294 @ 431,740: 17x12
#295 @ 490,589: 10x20
#296 @ 255,930: 25x18
#297 @ 374,416: 10x27
#298 @ 398,850: 13x25
#299 @ 330,700: 21x15
#300 @ 562,407: 21x28
#301 @ 275,283: 14x20
#302 @ 583,771: 25x23
#303 @ 730,52: 16x18
#304 @ 321,80: 21x21
#305 @ 511,963: 11x28
#306 @ 682,729: 29x18
#307 @ 7,718: 13x24
#308 @ 791,111: 12x22
#309 @ 576,729: 16x24
#310 @ 541,131: 16x27
#311 @ 183,835: 24x25
#312 @ 142,144: 20x18
#313 @ 604,492: 23x20
#314 @ 510,479: 28x17
#315 @ 90,129: 20x24
#316 @ 95,289: 16x14
#317 @ 296,814: 29x29
#318 @ 545,162: 23x15
#319 @ 829,943: 16x16
#320 @ 686,876: 17x11
#321 @ 416,80: 23x25
#322 @ 681,112: 28x12
#323 @ 453,755: 21x16
#324 @ 892,455: 23x19
#325 @ 61,573: 13x28
#326 @ 443,555: 19x10
#327 @ 274,886: 13x24
#328 @ 972,341: 24x23
#329 @ 547,337: 24x15
#330 @ 657,731: 17x25
#331 @ 350,97: 27x10
#332 @ 86,457: 16x27
#333 @ 432,802: 14x18
#334 @ 318,255: 29x13
#335 @ 406,440: 24x11
#336 @ 969,363: 29x11
#337 @ 664,28: 25x10
#338 @ 889,199: 21x29
#339 @ 247,405: 27x12
#340 @ 476,509: 24x27
#341 @ 675,747: 19x26
#342 @ 826,633: 24x15
#343 @ 802,781: 11x28
#344 @ 977,488: 11x27
#345 @ 119,443: 18x27
#346 @ 372,455: 18x22
#347 @ 392,242: 20x28
#348 @ 587,805: 29x16
#349 @ 853,898: 20x15
#350 @ 928,707: 10x11
#351 @ 269,701: 11x12
#352 @ 619,323: 27x10
#353 @ 450,597: 18x12
#354 @ 721,858: 17x21
#355 @ 93,521: 22x15
#356 @ 113,664: 17x26
#357 @ 938,161: 10x26
#358 @ 601,503: 25x11
#359 @ 737,162: 11x15
#360 @ 132,497: 17x26
#361 @ 463,543: 23x28
#362 @ 648,608: 4x5
#363 @ 672,367: 10x13
#364 @ 5,906: 28x10
#365 @ 607,863: 23x28
#366 @ 896,320: 19x17
#367 @ 151,384: 11x14
#368 @ 364,740: 25x17
#369 @ 85,112: 21x22
#370 @ 391,872: 23x25
#371 @ 391,226: 25x18
#372 @ 131,673: 28x21
#373 @ 229,921: 28x24
#374 @ 325,523: 22x26
#375 @ 127,517: 23x24
#376 @ 556,607: 26x27
#377 @ 446,356: 29x28
#378 @ 441,604: 15x10
#379 @ 716,571: 26x15
#380 @ 388,752: 19x14
#381 @ 672,342: 17x16
#382 @ 155,316: 28x15
#383 @ 525,513: 15x16
#384 @ 882,828: 29x15
#385 @ 784,907: 10x23
#386 @ 419,419: 10x22
#387 @ 498,95: 13x19
#388 @ 613,461: 18x18
#389 @ 87,779: 24x16
#390 @ 689,927: 19x26
#391 @ 923,639: 17x10
#392 @ 163,500: 21x23
#393 @ 824,856: 27x21
#394 @ 337,467: 29x10
#395 @ 492,122: 29x12
#396 @ 426,832: 21x27
#397 @ 856,446: 29x26
#398 @ 405,195: 6x6
#399 @ 283,159: 25x26
#400 @ 219,314: 16x23
#401 @ 594,799: 12x25
#402 @ 898,297: 17x12
#403 @ 738,434: 16x24
#404 @ 395,842: 27x25
#405 @ 661,482: 29x13
#406 @ 650,235: 25x13
#407 @ 547,370: 26x29
#408 @ 395,665: 25x29
#409 @ 227,152: 28x22
#410 @ 873,327: 24x13
#411 @ 778,631: 17x12
#412 @ 228,833: 29x12
#413 @ 62,469: 23x20
#414 @ 702,920: 10x20
#415 @ 347,868: 18x25
#416 @ 21,436: 11x28
#417 @ 960,75: 14x14
#418 @ 292,732: 20x22
#419 @ 15,176: 20x23
#420 @ 358,87: 18x14
#421 @ 609,206: 22x29
#422 @ 384,151: 15x29
#423 @ 761,648: 25x24
#424 @ 368,949: 25x15
#425 @ 257,391: 14x19
#426 @ 324,33: 29x10
#427 @ 846,658: 29x19
#428 @ 332,363: 28x27
#429 @ 135,686: 27x13
#430 @ 94,505: 28x14
#431 @ 580,779: 25x27
#432 @ 130,856: 25x24
#433 @ 697,549: 24x20
#434 @ 685,872: 26x13
#435 @ 386,673: 16x23
#436 @ 2,110: 10x26
#437 @ 461,123: 29x29
#438 @ 319,248: 23x13
#439 @ 862,782: 18x18
#440 @ 84,366: 11x13
#441 @ 282,388: 16x29
#442 @ 723,66: 12x19
#443 @ 274,128: 12x21
#444 @ 532,140: 17x23
#445 @ 831,790: 24x25
#446 @ 457,375: 20x23
#447 @ 412,199: 20x24
#448 @ 42,955: 20x22
#449 @ 656,239: 13x5
#450 @ 110,479: 18x27
#451 @ 972,347: 27x23
#452 @ 374,670: 14x23
#453 @ 547,648: 11x23
#454 @ 359,842: 14x24
#455 @ 291,620: 17x23
#456 @ 246,742: 17x14
#457 @ 79,326: 21x21
#458 @ 516,132: 13x14
#459 @ 427,68: 18x11
#460 @ 550,834: 10x12
#461 @ 420,413: 22x10
#462 @ 905,375: 29x16
#463 @ 178,782: 16x27
#464 @ 904,805: 15x29
#465 @ 663,120: 27x24
#466 @ 742,331: 23x15
#467 @ 834,558: 23x22
#468 @ 219,764: 21x20
#469 @ 669,726: 29x27
#470 @ 608,845: 27x25
#471 @ 841,462: 29x18
#472 @ 793,808: 17x28
#473 @ 916,737: 16x27
#474 @ 958,845: 15x12
#475 @ 468,264: 25x18
#476 @ 134,984: 22x12
#477 @ 114,514: 10x13
#478 @ 753,189: 23x29
#479 @ 24,496: 21x27
#480 @ 375,731: 14x21
#481 @ 170,820: 18x16
#482 @ 243,53: 18x11
#483 @ 566,8: 10x29
#484 @ 160,741: 28x11
#485 @ 796,750: 20x10
#486 @ 949,32: 23x9
#487 @ 339,347: 25x13
#488 @ 369,107: 19x28
#489 @ 61,409: 26x13
#490 @ 756,923: 6x9
#491 @ 400,976: 18x10
#492 @ 573,648: 19x29
#493 @ 160,583: 26x25
#494 @ 493,94: 10x25
#495 @ 689,748: 13x23
#496 @ 752,441: 20x14
#497 @ 627,4: 27x29
#498 @ 745,435: 11x18
#499 @ 48,492: 17x21
#500 @ 753,363: 29x28
#501 @ 477,85: 15x17
#502 @ 159,777: 20x16
#503 @ 10,580: 12x29
#504 @ 646,900: 24x14
#505 @ 233,258: 20x25
#506 @ 973,284: 13x22
#507 @ 984,912: 10x24
#508 @ 422,209: 22x11
#509 @ 674,729: 27x20
#510 @ 564,223: 29x13
#511 @ 439,833: 15x24
#512 @ 409,407: 3x5
#513 @ 53,965: 21x21
#514 @ 384,39: 15x11
#515 @ 190,239: 18x18
#516 @ 48,441: 26x11
#517 @ 231,928: 13x27
#518 @ 326,630: 23x19
#519 @ 16,685: 16x17
#520 @ 295,739: 13x6
#521 @ 276,566: 20x14
#522 @ 288,532: 11x13
#523 @ 400,616: 11x11
#524 @ 593,45: 26x21
#525 @ 183,817: 19x28
#526 @ 42,658: 11x22
#527 @ 560,645: 20x24
#528 @ 259,320: 13x24
#529 @ 602,316: 21x23
#530 @ 426,723: 5x3
#531 @ 385,939: 13x14
#532 @ 717,766: 14x24
#533 @ 0,112: 14x14
#534 @ 114,46: 12x18
#535 @ 820,413: 10x25
#536 @ 517,131: 16x13
#537 @ 60,318: 16x28
#538 @ 61,333: 17x11
#539 @ 791,895: 14x23
#540 @ 49,241: 14x17
#541 @ 66,302: 17x15
#542 @ 843,477: 12x11
#543 @ 876,3: 21x15
#544 @ 686,733: 27x24
#545 @ 657,613: 29x16
#546 @ 470,615: 13x10
#547 @ 228,246: 25x19
#548 @ 697,750: 25x25
#549 @ 485,738: 24x16
#550 @ 70,890: 16x27
#551 @ 671,360: 12x10
#552 @ 760,58: 29x13
#553 @ 411,397: 19x21
#554 @ 403,188: 16x27
#555 @ 870,151: 23x25
#556 @ 490,582: 27x12
#557 @ 290,438: 19x22
#558 @ 87,358: 24x15
#559 @ 497,199: 19x27
#560 @ 788,634: 26x16
#561 @ 372,122: 7x9
#562 @ 890,946: 13x11
#563 @ 826,948: 23x20
#564 @ 320,179: 11x12
#565 @ 697,404: 26x24
#566 @ 477,727: 11x14
#567 @ 9,692: 15x21
#568 @ 282,959: 21x23
#569 @ 771,70: 10x13
#570 @ 566,224: 21x22
#571 @ 738,149: 10x18
#572 @ 140,942: 14x11
#573 @ 617,703: 18x18
#574 @ 569,793: 22x24
#575 @ 43,490: 15x10
#576 @ 57,67: 25x24
#577 @ 837,116: 20x11
#578 @ 949,61: 24x17
#579 @ 826,726: 26x16
#580 @ 249,252: 15x24
#581 @ 193,118: 17x18
#582 @ 889,309: 27x12
#583 @ 147,752: 23x15
#584 @ 20,71: 18x21
#585 @ 259,68: 25x12
#586 @ 477,197: 24x13
#587 @ 398,149: 24x28
#588 @ 216,338: 16x20
#589 @ 871,244: 16x17
#590 @ 356,20: 14x21
#591 @ 408,976: 15x24
#592 @ 890,575: 12x23
#593 @ 859,758: 13x19
#594 @ 388,196: 13x18
#595 @ 392,156: 10x20
#596 @ 401,903: 23x29
#597 @ 640,611: 12x28
#598 @ 149,679: 13x26
#599 @ 362,535: 18x24
#600 @ 814,60: 26x25
#601 @ 651,820: 11x17
#602 @ 613,459: 26x17
#603 @ 731,440: 19x26
#604 @ 582,126: 12x19
#605 @ 818,796: 28x28
#606 @ 434,910: 13x14
#607 @ 937,783: 16x20
#608 @ 293,172: 14x16
#609 @ 136,725: 17x28
#610 @ 204,85: 14x14
#611 @ 766,785: 18x28
#612 @ 46,588: 28x29
#613 @ 918,352: 21x26
#614 @ 826,956: 11x14
#615 @ 69,625: 17x10
#616 @ 572,823: 22x25
#617 @ 739,284: 15x15
#618 @ 244,932: 20x23
#619 @ 579,794: 11x17
#620 @ 508,411: 16x13
#621 @ 412,440: 20x18
#622 @ 919,326: 29x17
#623 @ 400,928: 14x19
#624 @ 263,677: 20x13
#625 @ 394,367: 15x17
#626 @ 26,161: 29x27
#627 @ 384,192: 15x13
#628 @ 464,536: 18x29
#629 @ 788,550: 29x10
#630 @ 146,776: 12x13
#631 @ 328,27: 14x13
#632 @ 100,217: 18x24
#633 @ 912,720: 14x12
#634 @ 890,190: 28x29
#635 @ 322,28: 19x14
#636 @ 276,688: 24x28
#637 @ 245,409: 29x25
#638 @ 232,252: 23x17
#639 @ 31,179: 10x15
#640 @ 701,688: 11x13
#641 @ 321,456: 27x19
#642 @ 468,541: 19x23
#643 @ 410,964: 23x28
#644 @ 107,201: 14x28
#645 @ 681,348: 17x16
#646 @ 642,326: 10x10
#647 @ 663,431: 27x14
#648 @ 650,281: 11x18
#649 @ 771,945: 25x28
#650 @ 957,879: 18x15
#651 @ 806,481: 13x10
#652 @ 4,668: 29x24
#653 @ 263,327: 23x27
#654 @ 603,807: 10x24
#655 @ 425,436: 17x11
#656 @ 97,648: 29x23
#657 @ 173,412: 17x28
#658 @ 569,807: 17x20
#659 @ 444,58: 28x24
#660 @ 740,320: 20x12
#661 @ 435,917: 20x14
#662 @ 642,918: 28x15
#663 @ 626,12: 21x21
#664 @ 888,11: 29x20
#665 @ 752,441: 20x22
#666 @ 446,911: 18x10
#667 @ 226,969: 12x27
#668 @ 79,617: 29x16
#669 @ 26,915: 15x23
#670 @ 162,366: 21x19
#671 @ 860,772: 19x26
#672 @ 111,242: 15x20
#673 @ 914,827: 15x16
#674 @ 388,185: 10x16
#675 @ 24,169: 16x19
#676 @ 892,615: 18x28
#677 @ 797,874: 10x23
#678 @ 903,535: 10x26
#679 @ 253,55: 4x5
#680 @ 428,292: 13x12
#681 @ 637,132: 16x27
#682 @ 725,871: 14x24
#683 @ 704,235: 28x12
#684 @ 52,9: 16x15
#685 @ 573,187: 29x24
#686 @ 621,809: 10x18
#687 @ 639,52: 29x28
#688 @ 315,352: 24x18
#689 @ 636,117: 27x24
#690 @ 851,418: 15x29
#691 @ 127,157: 28x15
#692 @ 350,128: 13x17
#693 @ 785,723: 15x26
#694 @ 685,32: 11x16
#695 @ 640,958: 25x19
#696 @ 414,556: 22x10
#697 @ 457,653: 29x13
#698 @ 385,444: 25x20
#699 @ 275,545: 21x13
#700 @ 700,875: 15x20
#701 @ 50,581: 14x24
#702 @ 622,881: 10x10
#703 @ 398,409: 25x15
#704 @ 205,688: 18x15
#705 @ 368,122: 14x26
#706 @ 319,470: 12x23
#707 @ 380,575: 11x23
#708 @ 721,563: 21x12
#709 @ 512,826: 13x26
#710 @ 505,795: 11x27
#711 @ 466,610: 21x24
#712 @ 570,549: 29x15
#713 @ 197,224: 28x17
#714 @ 6,573: 23x29
#715 @ 88,915: 18x28
#716 @ 744,223: 10x21
#717 @ 708,671: 19x18
#718 @ 852,905: 15x21
#719 @ 438,730: 15x24
#720 @ 537,957: 14x18
#721 @ 269,122: 20x11
#722 @ 908,320: 25x13
#723 @ 666,144: 21x26
#724 @ 377,694: 24x28
#725 @ 278,827: 18x22
#726 @ 451,368: 12x11
#727 @ 973,240: 16x14
#728 @ 786,533: 13x18
#729 @ 560,865: 16x10
#730 @ 381,411: 25x28
#731 @ 969,250: 25x21
#732 @ 739,435: 21x10
#733 @ 320,252: 18x24
#734 @ 769,617: 13x23
#735 @ 565,497: 24x10
#736 @ 572,418: 14x10
#737 @ 767,782: 11x12
#738 @ 683,756: 18x29
#739 @ 275,402: 28x26
#740 @ 288,413: 18x23
#741 @ 731,670: 28x13
#742 @ 328,532: 21x13
#743 @ 531,236: 23x22
#744 @ 733,866: 10x12
#745 @ 736,715: 18x12
#746 @ 95,227: 22x27
#747 @ 984,7: 5x13
#748 @ 632,122: 10x15
#749 @ 372,451: 14x15
#750 @ 64,553: 15x10
#751 @ 476,968: 26x24
#752 @ 328,926: 11x24
#753 @ 48,859: 20x16
#754 @ 736,261: 27x21
#755 @ 233,835: 15x24
#756 @ 180,390: 11x23
#757 @ 316,19: 17x9
#758 @ 513,735: 29x24
#759 @ 611,427: 27x12
#760 @ 222,702: 29x26
#761 @ 772,798: 18x25
#762 @ 329,337: 21x12
#763 @ 325,172: 27x17
#764 @ 279,970: 12x19
#765 @ 968,472: 28x18
#766 @ 274,974: 15x14
#767 @ 246,927: 19x21
#768 @ 573,545: 24x29
#769 @ 977,235: 13x12
#770 @ 193,810: 28x29
#771 @ 341,110: 22x28
#772 @ 651,904: 18x12
#773 @ 34,163: 14x29
#774 @ 753,492: 4x18
#775 @ 84,502: 28x15
#776 @ 871,445: 19x16
#777 @ 850,420: 17x19
#778 @ 27,401: 14x29
#779 @ 454,320: 24x14
#780 @ 544,497: 12x25
#781 @ 628,68: 20x18
#782 @ 373,39: 24x27
#783 @ 735,723: 19x13
#784 @ 786,430: 21x29
#785 @ 872,136: 14x20
#786 @ 345,599: 13x27
#787 @ 43,867: 10x15
#788 @ 290,613: 25x22
#789 @ 915,352: 22x26
#790 @ 384,742: 28x11
#791 @ 645,587: 25x27
#792 @ 371,29: 25x11
#793 @ 569,775: 23x20
#794 @ 404,185: 11x17
#795 @ 758,192: 5x3
#796 @ 261,311: 19x13
#797 @ 377,76: 26x12
#798 @ 390,209: 16x29
#799 @ 715,978: 28x10
#800 @ 313,12: 25x21
#801 @ 576,644: 26x21
#802 @ 133,583: 20x26
#803 @ 776,559: 28x14
#804 @ 76,824: 15x15
#805 @ 443,300: 14x21
#806 @ 939,302: 18x18
#807 @ 972,0: 16x11
#808 @ 468,970: 19x17
#809 @ 446,61: 26x26
#810 @ 369,154: 12x17
#811 @ 487,552: 23x23
#812 @ 793,730: 17x28
#813 @ 547,134: 10x21
#814 @ 874,902: 16x10
#815 @ 892,269: 29x12
#816 @ 692,684: 12x20
#817 @ 828,876: 21x19
#818 @ 571,789: 29x13
#819 @ 397,606: 28x10
#820 @ 187,240: 21x12
#821 @ 448,513: 20x23
#822 @ 818,279: 18x16
#823 @ 444,553: 12x16
#824 @ 861,74: 17x20
#825 @ 655,504: 10x15
#826 @ 142,494: 10x19
#827 @ 634,889: 23x16
#828 @ 777,414: 13x28
#829 @ 257,485: 20x27
#830 @ 281,418: 27x27
#831 @ 514,975: 13x16
#832 @ 131,932: 16x20
#833 @ 348,511: 28x28
#834 @ 646,604: 10x16
#835 @ 800,294: 11x22
#836 @ 709,860: 15x29
#837 @ 289,935: 24x25
#838 @ 202,218: 10x23
#839 @ 271,482: 28x12
#840 @ 241,856: 15x18
#841 @ 561,106: 25x15
#842 @ 927,717: 27x22
#843 @ 642,504: 16x16
#844 @ 636,539: 18x17
#845 @ 697,608: 14x19
#846 @ 332,829: 20x23
#847 @ 677,135: 19x23
#848 @ 557,759: 20x19
#849 @ 177,98: 17x26
#850 @ 522,603: 17x28
#851 @ 550,205: 28x21
#852 @ 396,377: 16x14
#853 @ 249,696: 22x14
#854 @ 17,92: 22x18
#855 @ 345,538: 10x28
#856 @ 364,166: 21x21
#857 @ 417,719: 24x12
#858 @ 510,787: 22x28
#859 @ 985,692: 11x18
#860 @ 789,442: 24x19
#861 @ 73,917: 11x21
#862 @ 290,452: 27x15
#863 @ 231,310: 16x12
#864 @ 484,681: 24x17
#865 @ 193,829: 10x27
#866 @ 569,107: 10x13
#867 @ 120,434: 11x15
#868 @ 349,475: 11x15
#869 @ 530,147: 19x15
#870 @ 359,186: 26x12
#871 @ 227,776: 16x29
#872 @ 519,40: 27x23
#873 @ 959,898: 28x22
#874 @ 785,484: 19x14
#875 @ 697,749: 16x24
#876 @ 154,171: 11x5
#877 @ 100,34: 14x26
#878 @ 382,604: 24x13
#879 @ 909,962: 19x12
#880 @ 902,827: 21x29
#881 @ 718,232: 22x13
#882 @ 627,819: 20x29
#883 @ 475,93: 19x10
#884 @ 848,426: 28x19
#885 @ 563,225: 29x28
#886 @ 14,575: 8x16
#887 @ 577,131: 22x27
#888 @ 296,518: 16x18
#889 @ 752,720: 26x13
#890 @ 226,829: 18x20
#891 @ 333,588: 18x17
#892 @ 214,347: 17x24
#893 @ 921,386: 12x15
#894 @ 29,603: 28x24
#895 @ 250,139: 10x23
#896 @ 267,705: 18x25
#897 @ 610,374: 12x20
#898 @ 478,879: 11x19
#899 @ 978,512: 14x29
#900 @ 307,739: 27x26
#901 @ 375,740: 12x18
#902 @ 284,17: 19x21
#903 @ 588,765: 22x27
#904 @ 47,604: 14x13
#905 @ 823,797: 14x22
#906 @ 311,116: 23x24
#907 @ 38,597: 28x24
#908 @ 449,981: 28x14
#909 @ 852,122: 15x15
#910 @ 957,745: 14x10
#911 @ 436,80: 27x15
#912 @ 280,619: 25x27
#913 @ 726,742: 14x11
#914 @ 422,240: 24x24
#915 @ 394,362: 22x20
#916 @ 324,13: 14x4
#917 @ 521,558: 19x11
#918 @ 743,909: 19x20
#919 @ 72,559: 16x19
#920 @ 718,129: 13x13
#921 @ 652,467: 19x22
#922 @ 418,462: 20x25
#923 @ 947,304: 29x11
#924 @ 815,155: 26x12
#925 @ 482,470: 28x10
#926 @ 188,624: 18x17
#927 @ 432,72: 18x13
#928 @ 760,928: 28x23
#929 @ 797,136: 18x25
#930 @ 872,572: 20x27
#931 @ 552,513: 28x22
#932 @ 794,3: 21x10
#933 @ 119,721: 17x14
#934 @ 273,924: 10x12
#935 @ 672,148: 10x18
#936 @ 239,725: 20x25
#937 @ 724,29: 18x27
#938 @ 574,885: 28x29
#939 @ 900,19: 11x14
#940 @ 632,503: 28x16
#941 @ 133,763: 29x24
#942 @ 546,227: 11x11
#943 @ 58,468: 26x22
#944 @ 176,566: 28x22
#945 @ 282,923: 20x17
#946 @ 403,439: 19x12
#947 @ 942,98: 18x18
#948 @ 746,920: 19x16
#949 @ 130,75: 13x27
#950 @ 338,959: 19x11
#951 @ 343,166: 16x17
#952 @ 745,931: 10x10
#953 @ 191,16: 17x21
#954 @ 821,729: 18x16
#955 @ 790,757: 29x14
#956 @ 613,301: 15x27
#957 @ 403,743: 19x23
#958 @ 972,50: 14x19
#959 @ 264,964: 14x24
#960 @ 129,59: 13x22
#961 @ 917,362: 17x6
#962 @ 162,152: 24x11
#963 @ 696,565: 29x18
#964 @ 420,222: 27x19
#965 @ 294,619: 27x15
#966 @ 51,459: 29x26
#967 @ 728,228: 19x15
#968 @ 155,129: 15x27
#969 @ 412,774: 29x15
#970 @ 63,338: 12x28
#971 @ 539,860: 26x22
#972 @ 730,866: 24x16
#973 @ 652,919: 18x21
#974 @ 930,390: 12x14
#975 @ 300,138: 26x19
#976 @ 632,827: 17x21
#977 @ 801,820: 18x14
#978 @ 754,341: 10x28
#979 @ 773,487: 27x16
#980 @ 635,405: 14x17
#981 @ 319,437: 25x13
#982 @ 687,852: 26x29
#983 @ 301,684: 16x12
#984 @ 523,445: 15x22
#985 @ 598,336: 20x27
#986 @ 562,228: 21x12
#987 @ 452,63: 16x17
#988 @ 371,549: 10x28
#989 @ 874,747: 15x14
#990 @ 180,158: 12x17
#991 @ 611,49: 27x22
#992 @ 491,101: 28x27
#993 @ 393,690: 13x15
#994 @ 809,281: 19x26
#995 @ 314,718: 28x29
#996 @ 601,375: 27x21
#997 @ 171,541: 16x26
#998 @ 983,897: 16x29
#999 @ 541,668: 11x14
#1000 @ 377,144: 17x23
#1001 @ 335,812: 18x24
#1002 @ 644,591: 18x14
#1003 @ 833,577: 26x22
#1004 @ 758,290: 26x15
#1005 @ 445,294: 12x17
#1006 @ 726,243: 13x25
#1007 @ 97,941: 23x11
#1008 @ 503,558: 23x24
#1009 @ 912,78: 21x10
#1010 @ 745,940: 23x19
#1011 @ 556,106: 20x29
#1012 @ 737,711: 14x13
#1013 @ 900,760: 27x13
#1014 @ 854,674: 10x16
#1015 @ 213,720: 16x28
#1016 @ 88,507: 19x17
#1017 @ 147,363: 16x29
#1018 @ 284,574: 16x22
#1019 @ 833,654: 29x10
#1020 @ 567,823: 15x21
#1021 @ 445,662: 13x12
#1022 @ 189,709: 16x27
#1023 @ 907,194: 29x24
#1024 @ 153,904: 12x17
#1025 @ 397,714: 17x11
#1026 @ 52,273: 15x29
#1027 @ 383,223: 23x24
#1028 @ 462,129: 14x12
#1029 @ 551,577: 17x25
#1030 @ 755,190: 16x10
#1031 @ 137,509: 7x10
#1032 @ 131,328: 12x25
#1033 @ 232,740: 12x20
#1034 @ 163,108: 28x15
#1035 @ 100,704: 22x28
#1036 @ 967,705: 26x25
#1037 @ 715,412: 24x29
#1038 @ 464,41: 10x18
#1039 @ 612,506: 8x3
#1040 @ 655,710: 23x24
#1041 @ 834,312: 26x28
#1042 @ 899,326: 20x11
#1043 @ 133,148: 19x27
#1044 @ 12,163: 16x17
#1045 @ 316,105: 26x13
#1046 @ 104,512: 28x15
#1047 @ 532,119: 10x18
#1048 @ 190,940: 26x17
#1049 @ 729,918: 20x17
#1050 @ 874,556: 19x26
#1051 @ 202,542: 20x21
#1052 @ 71,404: 23x11
#1053 @ 869,332: 10x13
#1054 @ 482,662: 24x27
#1055 @ 510,754: 21x10
#1056 @ 341,301: 27x18
#1057 @ 178,163: 29x16
#1058 @ 884,473: 20x21
#1059 @ 86,490: 10x27
#1060 @ 349,299: 11x15
#1061 @ 565,35: 17x12
#1062 @ 364,469: 18x11
#1063 @ 141,866: 24x14
#1064 @ 936,53: 25x29
#1065 @ 492,801: 16x10
#1066 @ 310,686: 18x19
#1067 @ 491,579: 15x10
#1068 @ 749,937: 18x21
#1069 @ 331,880: 20x19
#1070 @ 618,510: 10x10
#1071 @ 622,696: 18x23
#1072 @ 53,592: 21x21
#1073 @ 623,218: 29x14
#1074 @ 150,821: 11x16
#1075 @ 109,291: 23x27
#1076 @ 301,915: 24x12
#1077 @ 427,308: 29x14
#1078 @ 428,763: 27x12
#1079 @ 295,79: 17x13
#1080 @ 942,848: 21x10
#1081 @ 708,941: 28x15
#1082 @ 91,100: 29x26
#1083 @ 84,151: 24x21
#1084 @ 144,387: 25x12
#1085 @ 209,103: 11x20
#1086 @ 212,232: 27x11
#1087 @ 679,15: 12x24
#1088 @ 342,960: 25x22
#1089 @ 296,385: 26x14
#1090 @ 573,72: 23x19
#1091 @ 137,890: 19x23
#1092 @ 332,937: 24x19
#1093 @ 327,809: 13x27
#1094 @ 947,29: 29x20
#1095 @ 580,213: 13x18
#1096 @ 530,926: 17x21
#1097 @ 232,800: 26x18
#1098 @ 486,543: 26x24
#1099 @ 305,520: 24x27
#1100 @ 878,87: 20x29
#1101 @ 646,809: 11x28
#1102 @ 530,814: 24x22
#1103 @ 709,124: 18x24
#1104 @ 770,777: 13x22
#1105 @ 296,436: 12x18
#1106 @ 954,721: 22x27
#1107 @ 606,851: 21x15
#1108 @ 719,929: 18x19
#1109 @ 861,896: 16x21
#1110 @ 780,130: 16x10
#1111 @ 159,280: 25x25
#1112 @ 518,816: 26x21
#1113 @ 438,299: 26x25
#1114 @ 532,439: 20x24
#1115 @ 536,437: 26x28
#1116 @ 827,431: 29x29
#1117 @ 188,751: 27x10
#1118 @ 914,165: 28x25
#1119 @ 587,57: 17x22
#1120 @ 331,213: 17x29
#1121 @ 979,54: 11x26
#1122 @ 420,404: 13x23
#1123 @ 208,553: 17x27
#1124 @ 751,664: 11x16
#1125 @ 812,530: 28x22
#1126 @ 574,79: 19x10
#1127 @ 881,301: 16x22
#1128 @ 830,920: 26x24
#1129 @ 312,477: 12x16
#1130 @ 279,512: 15x22
#1131 @ 643,569: 22x26
#1132 @ 220,821: 25x24
#1133 @ 68,10: 20x29
#1134 @ 805,487: 28x17
#1135 @ 128,518: 29x18
#1136 @ 251,702: 11x15
#1137 @ 472,874: 20x12
#1138 @ 768,142: 23x20
#1139 @ 527,755: 21x24
#1140 @ 504,944: 29x23
#1141 @ 359,23: 7x14
#1142 @ 529,551: 15x22
#1143 @ 544,570: 19x12
#1144 @ 949,751: 18x19
#1145 @ 675,798: 22x16
#1146 @ 420,780: 14x13
#1147 @ 387,238: 14x17
#1148 @ 242,935: 25x26
#1149 @ 45,774: 20x10
#1150 @ 710,666: 28x19
#1151 @ 702,222: 18x18
#1152 @ 951,877: 12x13
#1153 @ 849,664: 10x21
#1154 @ 397,675: 18x27
#1155 @ 132,667: 21x23
#1156 @ 979,5: 15x20
#1157 @ 741,490: 25x25
#1158 @ 899,467: 16x11
#1159 @ 94,492: 29x10
#1160 @ 377,100: 20x11
#1161 @ 557,519: 24x21
#1162 @ 649,818: 17x24
#1163 @ 680,281: 23x18
#1164 @ 82,651: 12x21
#1165 @ 486,504: 19x22
#1166 @ 137,483: 25x22
#1167 @ 601,833: 27x29
#1168 @ 552,288: 16x14
#1169 @ 682,809: 26x11
#1170 @ 421,825: 27x27
#1171 @ 382,239: 10x25
#1172 @ 892,265: 20x29
#1173 @ 324,261: 8x3
#1174 @ 47,166: 12x23
#1175 @ 527,60: 13x12
#1176 @ 672,679: 24x25
#1177 @ 12,185: 16x16
#1178 @ 661,426: 18x16
#1179 @ 239,782: 17x24
#1180 @ 773,616: 23x11
#1181 @ 736,208: 29x28
#1182 @ 936,402: 21x12
#1183 @ 86,240: 17x23
#1184 @ 976,512: 21x19
#1185 @ 711,553: 17x10
#1186 @ 885,722: 10x14
#1187 @ 418,718: 27x26
#1188 @ 217,77: 13x29
#1189 @ 84,881: 11x13
#1190 @ 960,88: 14x21
#1191 @ 352,132: 24x23
#1192 @ 282,126: 27x28
#1193 @ 103,518: 16x11
#1194 @ 679,756: 23x17
#1195 @ 738,442: 19x13
#1196 @ 870,126: 13x29
#1197 @ 859,555: 16x14
#1198 @ 115,138: 21x14
#1199 @ 343,537: 16x19
#1200 @ 678,285: 28x16
#1201 @ 655,906: 22x22
#1202 @ 447,737: 20x24
#1203 @ 343,567: 17x21
#1204 @ 357,413: 10x18
#1205 @ 298,153: 23x22
#1206 @ 415,322: 21x26
#1207 @ 284,393: 21x29
#1208 @ 278,897: 23x26
#1209 @ 964,146: 11x12
#1210 @ 114,967: 23x28
#1211 @ 27,647: 25x28
#1212 @ 974,234: 17x28
#1213 @ 351,141: 20x14
#1214 @ 885,176: 26x19
#1215 @ 682,406: 16x20
#1216 @ 959,941: 11x21
#1217 @ 875,255: 13x22
#1218 @ 724,564: 17x21
#1219 @ 268,169: 19x27
#1220 @ 684,406: 25x21
#1221 @ 539,348: 22x28
#1222 @ 726,786: 12x11
#1223 @ 709,113: 17x20
#1224 @ 943,495: 14x12
#1225 @ 396,162: 18x19
#1226 @ 297,826: 12x16
#1227 @ 951,948: 20x17
#1228 @ 152,169: 19x11
#1229 @ 775,642: 21x10
#1230 @ 616,220: 21x11
#1231 @ 595,48: 13x13
#1232 @ 300,381: 17x29
#1233 @ 652,284: 18x13
#1234 @ 807,630: 22x11
#1235 @ 874,237: 24x15
#1236 @ 127,235: 15x21
#1237 @ 83,477: 29x23
#1238 @ 946,106: 12x16
#1239 @ 924,700: 29x25
#1240 @ 771,441: 12x10
#1241 @ 461,253: 15x25
#1242 @ 354,828: 24x12
#1243 @ 410,807: 25x20
#1244 @ 89,511: 10x15
#1245 @ 326,216: 11x23
#1246 @ 522,608: 23x13
#1247 @ 371,100: 10x14
#1248 @ 268,294: 11x20
#1249 @ 880,97: 21x13
#1250 @ 635,501: 10x14
#1251 @ 511,755: 15x12
#1252 @ 435,918: 13x20
#1253 @ 494,406: 20x24
#1254 @ 822,643: 29x24
#1255 @ 902,702: 29x11
#1256 @ 3,731: 23x10
#1257 @ 728,671: 19x20
#1258 @ 34,655: 25x21
#1259 @ 358,164: 16x26
#1260 @ 813,425: 29x19
#1261 @ 273,439: 22x21
#1262 @ 47,764: 10x11
#1263 @ 898,444: 24x12
#1264 @ 466,533: 26x24
#1265 @ 879,571: 16x28
#1266 @ 460,204: 14x4
#1267 @ 40,290: 14x10
#1268 @ 109,452: 25x28
#1269 @ 275,556: 16x27
#1270 @ 20,174: 29x25
#1271 @ 937,727: 11x20
#1272 @ 175,863: 19x28
#1273 @ 333,63: 13x28
#1274 @ 859,72: 27x16
#1275 @ 102,215: 13x29
#1276 @ 232,921: 22x15
#1277 @ 563,860: 28x24
#1278 @ 243,401: 16x22
#1279 @ 735,896: 14x28
#1280 @ 644,64: 24x15
#1281 @ 104,760: 24x29
#1282 @ 269,880: 13x23
#1283 @ 291,802: 13x26
#1284 @ 392,202: 11x13
#1285 @ 480,115: 15x26
#1286 @ 645,269: 18x24
#1287 @ 849,306: 21x17
#1288 @ 635,683: 24x22
#1289 @ 548,118: 17x22
#1290 @ 93,61: 25x11
#1291 @ 209,444: 11x28
#1292 @ 74,696: 25x27
#1293 @ 646,554: 15x24
#1294 @ 189,654: 13x14
#1295 @ 674,613: 25x25
#1296 @ 893,826: 13x28
#1297 @ 797,405: 24x17
#1298 @ 614,711: 10x27
#1299 @ 82,670: 22x23
#1300 @ 760,919: 26x29
#1301 @ 357,464: 10x23
#1302 @ 378,716: 24x16
#1303 @ 433,700: 24x22
#1304 @ 366,835: 22x12
#1305 @ 925,42: 24x14
#1306 @ 822,538: 12x26
#1307 @ 231,210: 19x11
#1308 @ 966,351: 14x22
#1309 @ 151,485: 29x29
#1310 @ 86,458: 27x12
#1311 @ 382,169: 26x29
#1312 @ 269,456: 19x18
#1313 @ 562,557: 23x25
#1314 @ 509,444: 17x23
#1315 @ 118,308: 20x26
#1316 @ 33,609: 11x22
#1317 @ 288,590: 22x14
#1318 @ 831,468: 22x15
#1319 @ 305,136: 25x26
#1320 @ 17,125: 18x21
#1321 @ 911,627: 18x25
#1322 @ 241,755: 16x18
#1323 @ 668,402: 15x16
#1324 @ 683,684: 28x19
#1325 @ 580,902: 16x14
#1326 @ 536,135: 24x23
#1327 @ 295,162: 29x18
#1328 @ 494,467: 21x20
#1329 @ 377,611: 29x23
#1330 @ 593,377: 22x13
#1331 @ 30,500: 4x17
#1332 @ 556,501: 15x18
#1333 @ 61,800: 23x29
#1334 @ 3,578: 15x23
#1335 @ 742,287: 19x15
#1336 @ 530,922: 11x27
#1337 @ 707,677: 12x28
#1338 @ 485,440: 24x16
#1339 @ 738,439: 19x16
#1340 @ 329,362: 24x27
#1341 @ 106,131: 25x28
#1342 @ 419,468: 27x14
#1343 @ 49,271: 28x23
#1344 @ 563,615: 24x13
#1345 @ 909,22: 20x22
#1346 @ 155,284: 12x29
#1347 @ 110,211: 23x17
#1348 @ 391,560: 28x24
#1349 @ 184,622: 21x15
#1350 @ 412,550: 29x24
#1351 @ 277,615: 24x27
#1352 @ 7,180: 28x13
#1353 @ 495,203: 10x23
#1354 @ 724,241: 10x15
#1355 @ 831,769: 29x16
#1356 @ 721,409: 12x15
#1357 @ 594,63: 27x13
#1358 @ 789,430: 23x28
#1359 @ 526,810: 18x15"""


fabric = {}

def get_coords(coords_string):
    coords = coords_string.split(',')
    return (int(coords[0]), int(coords[1].replace(':', '')))

def get_size(string):
    sizes = string.split('x')
    return (int(sizes[0]), int(sizes[1]))

lines = input.split('\n')

for each in lines:
    words = each.split(' ')
    x_coord, y_coord = get_coords(words[2])
    x_size, y_size = get_size(words[3])
    x_index, y_index = 0, 0
    while x_index < x_size:
        while y_index < y_size:
            x_curr, y_curr = x_coord + x_index, y_coord + y_index
            coord_str = str(x_curr) + "," + str(y_curr)
            if coord_str in fabric:
                fabric[coord_str] = fabric[coord_str] + 1
            else:
                fabric[coord_str] = 1
            y_index = y_index + 1
        y_index = 0
        x_index = x_index + 1

not_overlaps_id = None

for each in lines:
    words = each.split(' ')
    x_coord, y_coord = get_coords(words[2])
    x_size, y_size = get_size(words[3])
    x_index, y_index = 0, 0
    overlaps = False
    while x_index < x_size:
        while y_index < y_size:
            x_curr, y_curr = x_coord + x_index, y_coord + y_index
            coord_str = str(x_curr) + "," + str(y_curr)
            if coord_str in fabric and fabric[coord_str] > 1:
                overlaps = True
            y_index = y_index + 1
        y_index = 0
        x_index = x_index + 1
    if not overlaps:
        not_overlaps_id = words[0]
    overlaps = False

print(not_overlaps_id)
