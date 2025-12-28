## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("City Dom")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "0.4"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "CityDom"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = None

default music_loop_fade = 1.0
default music_loop_volume_floor = 0.3
default music_loop_fading_out = False
default music_loop_last_pos = 0.0
default music_loop_track = None
default music_afternoon_hour = 8
default music_night_hour = 12

init python:
    MUSIC_TRACKS = {
        0: "audio/music_morning_looped.ogg",
        1: "audio/music_afternoon_looped.ogg",
        2: "audio/music_night_looped.ogg",
    }

    def _is_main_menu():
        try:
            if renpy.context()._main_menu:
                return True
        except Exception:
            pass
        try:
            return bool(store.main_menu)
        except Exception:
            return False

    def _get_time_music_track():
        if _is_main_menu():
            return None
        try:
            hour = store.calendar.Hours
        except Exception:
            hour = 0
        if hour < store.music_afternoon_hour:
            return MUSIC_TRACKS[0]
        if hour < store.music_night_hour:
            return MUSIC_TRACKS[1]
        return MUSIC_TRACKS[2]

    def _update_music_loop(track):
        if not track:
            return
        if renpy.music.get_playing("music") != track:
            return
        duration = renpy.music.get_duration("music")
        pos = renpy.music.get_pos("music")
        if not duration or pos is None:
            return
        if pos < store.music_loop_last_pos:
            store.music_loop_fading_out = False
            renpy.music.set_volume(1.0, delay=store.music_loop_fade, channel="music")
        store.music_loop_last_pos = pos
        remaining = duration - pos
        if (not store.music_loop_fading_out) and remaining <= store.music_loop_fade:
            store.music_loop_fading_out = True
            renpy.music.set_volume(store.music_loop_volume_floor, delay=remaining, channel="music")

    def _ensure_background_music():
        desired = _get_time_music_track()
        current = renpy.music.get_playing("music")
        tracked = store.music_loop_track
        if desired is None:
            if current:
                renpy.music.stop(channel="music", fadeout=1.0)
            store.music_loop_track = None
            store.music_loop_fading_out = False
            store.music_loop_last_pos = 0.0
            return
        if tracked != desired or current != desired:
            store.music_loop_track = desired
            store.music_loop_fading_out = False
            store.music_loop_last_pos = 0.0
            renpy.music.set_volume(1.0, delay=0, channel="music")
            renpy.music.play(desired, channel="music", loop=True, fadein=1.0, fadeout=1.0)
            return
        _update_music_loop(desired)

    if not hasattr(config, "after_load_callbacks"):
        config.after_load_callbacks = []
    if _ensure_background_music not in config.after_load_callbacks:
        config.after_load_callbacks.append(_ensure_background_music)

    if "music" not in config.main_menu_stop_channels:
        config.main_menu_stop_channels.append("music")


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "CityDom-1665840986"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Declare two archives.
    build.archive("scripts", "all")
    build.archive("images", "all")

    ## Put script files into the scripts archive.
    build.classify("game/**.rpy", "scripts")
    build.classify("game/**.rpyc", "scripts")

    ## Put images into the images archive.
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")

    ## Put videos into the images archive.
    build.classify("game/images/**.webm", "archive")

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

label after_load:
    $ _ensure_background_music()
    return
