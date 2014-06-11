# TODO: Translation updated at 2014-04-18 09:28

# game/tutorial_atl.rpy:187
translate chinese tutorial_positions_a09a3fd1:

    # e "In this tutorial, I'll teach you how Ren'Py positions things on the screen. But before that, let's learn a little bit about how Python handles numbers."
    e ""

# game/tutorial_atl.rpy:189
translate chinese tutorial_positions_ba39aabc:

    # e "There are two main kinds of numbers in Python: integers and floating point numbers. An integer consists entirely of digits, while a floating point number has a decimal point."
    e ""

# game/tutorial_atl.rpy:191
translate chinese tutorial_positions_a60b775d:

    # e "For example, 100 is an integer, while 0.5 is a floating point number, or float for short. In this system, there are two zeros: 0 is an integer, and 0.0 is a float."
    e ""

# game/tutorial_atl.rpy:193
translate chinese tutorial_positions_7f1a560c:

    # e "Ren'Py uses integers to represent absolute coordinates, and floats to represent fractions of an area with known size."
    e ""

# game/tutorial_atl.rpy:195
translate chinese tutorial_positions_8e7d3e52:

    # e "When we're positioning something, the area is usually the entire screen."
    e ""

# game/tutorial_atl.rpy:197
translate chinese tutorial_positions_fdcf9d8b:

    # e "Let me get out of the way, and I'll show you where some positions are."
    e ""

# game/tutorial_atl.rpy:211
translate chinese tutorial_positions_76d7a5bf:

    # e "The origin is the upper-left corner of the screen. That's where the x position (xpos) and the y position (ypos) are both zero."
    e ""

# game/tutorial_atl.rpy:217
translate chinese tutorial_positions_be14c7c3:

    # e "When we increase xpos, we move to the right. So here's an xpos of .5, meaning half the width across the screen."
    e ""

# game/tutorial_atl.rpy:222
translate chinese tutorial_positions_9b91be6c:

    # e "Increasing xpos to 1.0 moves us to the right-hand border of the screen."
    e ""

# game/tutorial_atl.rpy:228
translate chinese tutorial_positions_80be064f:

    # e "We can also use an absolute xpos, which is given in an absolute number of pixels from the left side of the screen. For example, since this window is 800 pixels across, using an xpos of 400 will return the target to the center of the top row."
    e ""

# game/tutorial_atl.rpy:230
translate chinese tutorial_positions_c4d18c0a:

    # e "The y-axis position, or ypos works the same way. Right now, we have a ypos of 0.0."
    e ""

# game/tutorial_atl.rpy:236
translate chinese tutorial_positions_16933a61:

    # e "Here's a ypos of 0.5."
    e ""

# game/tutorial_atl.rpy:241
translate chinese tutorial_positions_6eb36777:

    # e "A ypos of 1.0 specifies a position at the bottom of the screen. If you look carefully, you can see the position indicator spinning below the text window."
    e ""

# game/tutorial_atl.rpy:243
translate chinese tutorial_positions_a423050f:

    # e "Like xpos, ypos can also be an integer. In this case, ypos would give the total number of pixels from the top of the screen."
    e ""

# game/tutorial_atl.rpy:249
translate chinese tutorial_positions_bc7a809a:

    # e "Can you guess where this position is, relative to the screen?" nointeract
    e "" nointeract

# game/tutorial_atl.rpy:255
translate chinese tutorial_positions_6f926e18:

    # e "Sorry, that's wrong. The xpos is .75, and the ypos is .25."
    e ""

# game/tutorial_atl.rpy:257
translate chinese tutorial_positions_5d5feb98:

    # e "In other words, it's 75%% of the way from the left side, and 25%% of the way from the top."
    e ""

# game/tutorial_atl.rpy:261
translate chinese tutorial_positions_77b45218:

    # e "Good job! You got that position right."
    e ""

# game/tutorial_atl.rpy:265
translate chinese tutorial_positions_6f926e18_1:

    # e "Sorry, that's wrong. The xpos is .75, and the ypos is .25."
    e ""

# game/tutorial_atl.rpy:267
translate chinese tutorial_positions_5d5feb98_1:

    # e "In other words, it's 75%% of the way from the left side, and 25%% of the way from the top."
    e ""

# game/tutorial_atl.rpy:281
translate chinese tutorial_positions_e4380a83:

    # e "The second position we care about is the anchor. The anchor is a spot on the thing being positioned."
    e ""

# game/tutorial_atl.rpy:283
translate chinese tutorial_positions_d1db1246:

    # e "For example, here we have an xanchor of 0.0 and a yanchor of 0.0. It's in the upper-left corner of the logo image."
    e ""

# game/tutorial_atl.rpy:288
translate chinese tutorial_positions_6056873f:

    # e "When we increase the xanchor to 1.0, the anchor moves to the right corner of the image."
    e ""

# game/tutorial_atl.rpy:293
translate chinese tutorial_positions_7cdb8dcc:

    # e "Similarly, when both xanchor and yanchor are 1.0, the anchor is the bottom-right corner."
    e ""

# game/tutorial_atl.rpy:301
translate chinese tutorial_positions_03a07da8:

    # e "To place an image on the screen, we need both the position and the anchor."
    e ""

# game/tutorial_atl.rpy:309
translate chinese tutorial_positions_8945054f:

    # e "We then line them up, so that both the position and anchor are at the same point on the screen."
    e ""

# game/tutorial_atl.rpy:319
translate chinese tutorial_positions_2b184a93:

    # e "When we place both in the upper-left corner, the image moves to the upper-left corner of the screen."
    e ""

# game/tutorial_atl.rpy:328
translate chinese tutorial_positions_5aac4f3f:

    # e "With the right combination of position and anchor, any place on the screen can be specified, without even knowing the size of the image."
    e ""

# game/tutorial_atl.rpy:340
translate chinese tutorial_positions_3b59b797:

    # e "It's often useful to set xpos and xanchor to the same value. We call that xalign, and it gives a fractional position on the screen."
    e ""

# game/tutorial_atl.rpy:345
translate chinese tutorial_positions_b8ebf9fe:

    # e "For example, when we set xalign to 0.0, things are aligned to the left side of the screen."
    e ""

# game/tutorial_atl.rpy:350
translate chinese tutorial_positions_8ce35d52:

    # e "When we set it to 1.0, then we're aligned to the right side of the screen."
    e ""

# game/tutorial_atl.rpy:355
translate chinese tutorial_positions_6745825f:

    # e "And when we set it to 0.5, we're back to the center of the screen."
    e ""

# game/tutorial_atl.rpy:357
translate chinese tutorial_positions_64428a07:

    # e "Setting yalign is similar, except along the y-axis."
    e ""

# game/tutorial_atl.rpy:359
translate chinese tutorial_positions_cfb77d42:

    # e "Remember that xalign is just setting xpos and xanchor to the same value, and yalign is just setting ypos and yanchor to the same value."
    e ""

# game/tutorial_atl.rpy:366
translate chinese tutorial_positions_0f4ca2b6:

    # e "Once you understand positions, you can use transformations to move things around the Ren'Py screen."
    e ""

# game/tutorial_atl.rpy:373
translate chinese tutorial_atl_a1cc1bff:

    # e "While showing static images is often enough for most games, occasionally we'll want to change images, or move them around the screen."
    e ""

# game/tutorial_atl.rpy:375
translate chinese tutorial_atl_81dbb8f2:

    # e "We call this a Transform, and it's what ATL, Ren'Py's Animation and Transformation Language, is for."
    e ""

# game/tutorial_atl.rpy:383
translate chinese tutorial_atl_65badef3:

    # e "But first, let's have... a Gratuitous Rock Concert!"
    e ""

# game/tutorial_atl.rpy:391
translate chinese tutorial_atl_3ccfe2ac:

    # e "That was a lot of work, and before you can do that, we'll need to start with the basics of using ATL."
    e ""

# game/tutorial_atl.rpy:393
translate chinese tutorial_atl_1f22f875:

    # e "There are currently three places where ATL can be used in Ren'Py."
    e ""

# game/tutorial_atl.rpy:397
translate chinese tutorial_atl_fd036bdf:

    # e "The first place ATL can be used is as part of an image statement. Instead of a displayable, an image may be defined as a block of ATL code."
    e ""

# game/tutorial_atl.rpy:399
translate chinese tutorial_atl_7cad2ab9:

    # e "When used in this way, we have to be sure that ATL includes one or more displayables to actually show."
    e ""

# game/tutorial_atl.rpy:403
translate chinese tutorial_atl_c78b2a1e:

    # e "The second way is through the use of the transform statement. This assigns the ATL block to a python variable, allowing it to be used in at clauses and inside other transforms."
    e ""

# game/tutorial_atl.rpy:407
translate chinese tutorial_atl_da7a7759:

    # e "Finally, an ATL block can be used as part of a show statement, instead of the at clause."
    e ""

# game/tutorial_atl.rpy:411
translate chinese tutorial_atl_c21bc1d1:

    # e "The key to ATL is what we call composeability. ATL is made up of relatively simple commands, which can be combined together to create complicated transforms."
    e ""

# game/tutorial_atl.rpy:413
translate chinese tutorial_atl_ed82983f:

    # e "Before I explain how ATL works, let me explain what animation and transformation are."
    e ""

# game/tutorial_atl.rpy:418
translate chinese tutorial_atl_2807adff:

    # e "Animation is when the displayable being shown changes. For example, right now I am changing my expression."
    e ""

# game/tutorial_atl.rpy:445
translate chinese tutorial_atl_3eec202b:

    # e "Transformation involves moving or distorting an image. This includes placing it on the screen, zooming it in and out, rotating it, and changing its opacity."
    e ""

# game/tutorial_atl.rpy:453
translate chinese tutorial_atl_fbc9bf83:

    # e "To introduce ATL, let's start by looking at at a simple animation. Here's one that consists of five lines of ATL code, contained within an image statement."
    e ""

# game/tutorial_atl.rpy:455
translate chinese tutorial_atl_12c839ee:

    # e "In ATL, to change a displayable, simply mention it on a line of ATL code. Here, we're switching back and forth between two images."
    e ""

# game/tutorial_atl.rpy:457
translate chinese tutorial_atl_c671ed7d:

    # e "Since we're defining an image, the first line of ATL has to name a displayable. Otherwise, there would be nothing to show."
    e ""

# game/tutorial_atl.rpy:459
translate chinese tutorial_atl_99386181:

    # e "The second and fourth lines are pause statements, which cause ATL to wait half of a second each before continuing. That's how we give the delay between images."
    e ""

# game/tutorial_atl.rpy:461
translate chinese tutorial_atl_60f2a5e8:

    # e "The final line is a repeat statement. This causes the current block of ATL to be restarted. You can only have one repeat statement per block."
    e ""

# game/tutorial_atl.rpy:466
translate chinese tutorial_atl_146cf4c4:

    # e "If we were to write repeat 2 instead, the animation would loop twice, then stop."
    e ""

# game/tutorial_atl.rpy:471
translate chinese tutorial_atl_d90b1838:

    # e "Omitting the repeat statement means that the animation stops once we reach the end of the block of ATL code."
    e ""

# game/tutorial_atl.rpy:476
translate chinese tutorial_atl_e5872360:

    # e "By default, displayables are replaced instantaneously. We can also use a with clause to give a transition between displayables."
    e ""

# game/tutorial_atl.rpy:483
translate chinese tutorial_atl_a7f8ed01:

    # e "Now, let's move on to see how we can use ATL to transform an image. We'll start off by seeing what we can do to position images on the screen."
    e ""

# game/tutorial_atl.rpy:492
translate chinese tutorial_atl_24501213:

    # e "Perhaps the simplest thing we can do is to position the images on the screen. This can be done by simply giving the names of the transform properties, each followed by the value."
    e ""

# game/tutorial_atl.rpy:497
translate chinese tutorial_atl_43516492:

    # e "With a few more statements, we can move things around on the screen."
    e ""

# game/tutorial_atl.rpy:499
translate chinese tutorial_atl_8b053b5a:

    # e "This code starts the image off at the top-right of the screen, and waits a second."
    e ""

# game/tutorial_atl.rpy:501
translate chinese tutorial_atl_d7fc5372:

    # e "It then moves it to the left side, waits another second, and repeats."
    e ""

# game/tutorial_atl.rpy:503
translate chinese tutorial_atl_7650ec09:

    # e "The pause and repeat statements are the same statements we used in our animations. They work throughout ATL code."
    e ""

# game/tutorial_atl.rpy:508
translate chinese tutorial_atl_d3416d4f:

    # e "Having the image jump around on the screen isn't all that useful. That's why ATL has the interpolation statement."
    e ""

# game/tutorial_atl.rpy:510
translate chinese tutorial_atl_4e7512ec:

    # e "The interpolation statement allows you to smoothly vary the value of a transform property, from an old to a new value."
    e ""

# game/tutorial_atl.rpy:512
translate chinese tutorial_atl_685eeeaa:

    # e "Here, we have an interpolation statement on the second ATL line. It starts off with the name of a time function, in this case linear."
    e ""

# game/tutorial_atl.rpy:514
translate chinese tutorial_atl_c5cb49de:

    # e "That's followed by an amount of time, in this case three seconds. It ends with a list of properties, each followed by its new value."
    e ""

# game/tutorial_atl.rpy:516
translate chinese tutorial_atl_72d47fb6:

    # e "The old value is the value of the transform property at the start of the statement. By interpolating the property over time, we can change things on the screen."
    e ""

# game/tutorial_atl.rpy:526
translate chinese tutorial_atl_2958f397:

    # e "ATL supports more complicated move types, like circle and spline motion. But I won't be showing those here."
    e ""

# game/tutorial_atl.rpy:528
translate chinese tutorial_atl_4a02c8d8:

    # e "Next, let's take a look at some of the transform properties that we can change using ATL."
    e ""

# game/tutorial_atl.rpy:543
translate chinese tutorial_atl_821fcb91:

    # e "We've already seen the position properties. Along with xalign and yalign, we support the xpos, ypos, xanchor, and yanchor properties."
    e ""

# game/tutorial_atl.rpy:558
translate chinese tutorial_atl_cca5082b:

    # e "We can perform a pan by using xpos and ypos to position images off of the screen."
    e ""

# game/tutorial_atl.rpy:560
translate chinese tutorial_atl_0394dd50:

    # e "This usually means giving them negative positions."
    e ""

# game/tutorial_atl.rpy:577
translate chinese tutorial_atl_2624662e:

    # e "The zoom property lets us scale the displayable by a factor, making it bigger and smaller. For best results, zoom should always be greater than 0.5."
    e ""

# game/tutorial_atl.rpy:591
translate chinese tutorial_atl_b6527546:

    # e "The xzoom and yzoom properties allow the displayable to be scaled in the X and Y directions independently."
    e ""

# game/tutorial_atl.rpy:602
translate chinese tutorial_atl_9fe238de:

    # e "The size property can be used to set a size, in pixels, that the displayable is scaled to."
    e ""

# game/tutorial_atl.rpy:617
translate chinese tutorial_atl_6b982a23:

    # e "The alpha property allows us to vary the opacity of a displayable. This can make it appear and disappear."
    e ""

# game/tutorial_atl.rpy:631
translate chinese tutorial_atl_60d6d9f3:

    # e "The rotate property lets us rotate a displayable."
    e ""

# game/tutorial_atl.rpy:633
translate chinese tutorial_atl_898a138a:

    # e "Since rotation can change the size, usually you'll want to set xanchor and yanchor to 0.5 when positioning a rotated displayable."
    e ""

# game/tutorial_atl.rpy:644
translate chinese tutorial_atl_207b7fc8:

    # e "The crop property crops a rectangle out of a displayable, showing only part of it."
    e ""

# game/tutorial_atl.rpy:658
translate chinese tutorial_atl_ebb84988:

    # e "When used together, they can be used to focus in on specific parts of an image."
    e ""

# game/tutorial_atl.rpy:664
translate chinese tutorial_atl_d08fe8d9:

    # e "Apart from displayables, pause, interpolation, and repeat, there are a few other statements we can use as part of ATL."
    e ""

# game/tutorial_atl.rpy:678
translate chinese tutorial_atl_db6302bd:

    # e "When we create an ATL transform using the transform statement, we can use that transform as an ATL statement."
    e ""

# game/tutorial_atl.rpy:680
translate chinese tutorial_atl_785911cf:

    # e "Since the default positions are also transforms, this means that we can use left, right, and center inside of an ATL block."
    e ""

# game/tutorial_atl.rpy:698
translate chinese tutorial_atl_331126c1:

    # e "Here, we have two new statements. The block statement allows you to include a block of ATL code. Since the repeat statement applies to blocks, this lets you repeat only part of an ATL transform."
    e ""

# game/tutorial_atl.rpy:700
translate chinese tutorial_atl_24f67b67:

    # e "We also have the time statement, which runs after the given number of seconds have elapsed from the start of the block. It will run even if another statement is running, stopping the other statement."
    e ""

# game/tutorial_atl.rpy:702
translate chinese tutorial_atl_30dc0008:

    # e "So this code will bounce the image back and forth for eleven and a half seconds, and then move back to the right side of the screen."
    e ""

# game/tutorial_atl.rpy:718
translate chinese tutorial_atl_f903bc3b:

    # e "The parallel statement lets us run two blocks of ATL code at the same time."
    e ""

# game/tutorial_atl.rpy:720
translate chinese tutorial_atl_5d0f8f9d:

    # e "Here, the top block move the image in the horizontal direction, and the bottom block moves it in the vertical direction. Since they're moving at different speeds, it looks like the image is bouncing on the screen."
    e ""

# game/tutorial_atl.rpy:737
translate chinese tutorial_atl_28a7d27e:

    # e "Finally, the choice statement makes Ren'Py randomly pick a block of ATL code. This allows you to add some variation as to what Ren'Py shows."
    e ""

# game/tutorial_atl.rpy:743
translate chinese tutorial_atl_5fc8c0df:

    # e "This tutorial game has only scratched the surface of what you can do with ATL. For example, we haven't even covered the on and event statements. For more information, you might want to check out the ATL chapter in the reference manual."
    e ""

# game/tutorial_atl.rpy:747
translate chinese tutorial_atl_1358c6b4:

    # e "But for now, just remember that when it comes to animating and transforming, ATL is the hot new thing."
    e ""

translate chinese strings:

    # game/tutorial_atl.rpy:249
    old "xpos 1.0 ypos .5"
    new ""

    # game/tutorial_atl.rpy:249
    old "xpos .75 ypos .25"
    new ""

    # game/tutorial_atl.rpy:249
    old "xpos .25 ypos .33"
    new ""

