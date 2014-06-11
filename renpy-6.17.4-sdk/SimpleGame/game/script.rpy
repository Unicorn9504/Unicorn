define e = Character('Eileen', color="#c8ffc8")
image eileen concerned = "testData/eileen_concerned.png"
image eileen happy = "testData/eileen_happy.png"
image eileen side = "testData/eileen_side.png"
image eileen vhappy = "testData/eileen_vhappy.png"

image bg washington = "testData/washington.jpg"
image bg whitehouse = "testData/whitehouse.jpg"

init:
    python:
        import os
        import pygame
        import pyguts as spine
        
        class SkeDisModel(renpy.Displayable):
            def __init__(self, file, **kwargs):
                super(SkeDisModel, self).__init__(**kwargs)
                atlasfile = "data/"+file+".atlas"
                fullpath = renpy.loader.transfn(atlasfile);
                atlas = spine.Atlas(fullpath);
                jsonfile = "data/"+file+".json"
                fullpath = renpy.loader.transfn(jsonfile)
                skeletonJson = spine.SkeletonJson(spine.AtlasAttachmentLoader(atlas))
                
                self.skeletonData = skeletonJson.readSkeletonDataFile(fullpath)
 
                skeleton = spine.Skeleton(self.skeletonData)
                skeleton.debug = False
                skeleton.setToBindPose()
                skeleton.x = 0
                skeleton.y = 0
                skeleton.flipX = False
                skeleton.flipY = False
                skeleton.updateWorldTransform()
                
                self.skeleton = skeleton;
                self.animation = None;
                
            def set_animation(self, anim_name):
                self.animation = self.skeletonData.findAnimation(anim_name)
                if(self.animation is None):
                    raise("No Such animation")
                    
            def set_skin(skin_name):
                self.skeleton.setSkin(skin_name);
                
            def render(self, width, height, st, at):
                self.x = 0
                self.y = 0;
                renderobj = renpy.Render(0,0)

                if(self.animation):
                    self.animation.apply(self.skeleton, st, True);
                    self.skeleton.updateWorldTransform()
                    self.skeleton.draw(renderobj, 0)
                else:
                    raise("No Animation has been set")

                return renderobj

            def event(self, ev, x, y, st):
                return None;

            def visit(self):
                return [None];
        
        boy_model = SkeDisModel("dragon")
        def anim(st, at, model):
            return model,0.013
            
    image boy = DynamicDisplayable(anim,boy_model)
    
#Directly start
label main_menu:
    return

#####################
# Title Menu
#####################
define dissolveIn = Dissolve(2)
image titleMenuBackground = "data/Title_Background.png"
image titleMenuMainText = "data/Title_TextMain.png"
image titleMenuText2 = "data/Title_Text2.png"
image titleMenuRope = "data/Title_Rope.png"

label title_main:
    window hide None
    call title_menu_start
    call screen title
    if _return == "Start":
        jump story_start
    else:
        "Dead loop!"
        jump dead_loop
    return

label title_menu_start:
    scene titleMenuBackground
    show titleMenuMainText with dissolveIn
    pause 1.0
    show titleMenuRope
    pause 1.0
    show titleMenuText2 with moveintop
    return

#####################
# screen test
#####################
screen title:
    window id "window":
        vbox:
            xalign 0.5 yalign 0.5
            textbutton "新的里程" action Return("Start")
            textbutton "游戏回忆" action ShowMenu("load")
            textbutton "回头是岸" action Quit()

#####################
# HotMap Test
#####################
label hotspot_test:
    $ loop_cnt = 1
label hotspot_loop:
    call screen hotspot
    if _return == "end":
        return
    else:
        $ loop_cnt += 1
        e "This is [loop_cnt]"
        jump hotspot_loop
    
screen hotspot:
    fixed:
        imagebutton:
            xpadding 379 
            ypadding 46
            idle "data/00.png" 
            hover "data/00.png" 
            action Return()
        imagebutton:
            xpadding 264
            ypadding 116
            idle "data/01.png" 
            hover "data/01.png" 
            action Return()
        imagebutton:
            xpadding 267
            ypadding 238
            idle "data/02.png" 
            hover "data/02.png" 
            action Return()
        imagebutton:
            xpadding 0
            ypadding 275
            idle "data/03.png" 
            hover "data/03.png" 
            action Return()
#        imagebutton idle "data/hotspot_desk.png" action NullAction()
#        imagebutton idle "data/hotspot_window.png" action NullAction()


#####################
# GameS Start
#####################
label start:
#    call title_main
label story_start:
    scene bg washington
    call hotspot_test
    e "hotspot_test"
    $boy_model.set_animation("flying")
#    show boy:
#        xalign 0.5 yalign 0.5
    scene bg washington
    show eileen happy 
    e "你好，世界"
    e "Once you add a story, pictures, and music,you can release it to the world!
    Once you add a story, pictures, and music,you can release it to the world!"

    e "line 001"
    
    scene bg whitehouse
    "line 002"
    e "line 003"

    show eileen side with fade
    "line 004"
    e "line 005"

menu:
    "Yes":
        jump aaa
    "No":
        jump bbb
label aaa:
    show eileen vhappy
    e "line 006"
    e "line 007"
    jump ccc
label bbb:
    show eileen concerned at left with dissolve 
    e "line 008"
    jump ccc
label ccc:
    scene black with dissolve
    e "Once you add a story, pictures, and music, 
        you can release it to the world!"
    return
